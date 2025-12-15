# Switch Configuration Documentation: aksess-sw01.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: 12.2(37)SE1
- **Configuration Purpose**: This switch appears to be a core layer device, acting as a management station and providing access to VLANs.
- **Last Modified**: Not explicitly stated in the configuration file
- **Domain Name**: krister.local

## Device Information
- **Model**: Not explicitly stated in the configuration file
- **System Image**: The system image is 12.2(37)SE1, which is a standard Cisco IOS release.
- **Serial Number**: Not available
- **Hardware Details**: The switch has multiple FastEthernet and GigabitEthernet interfaces.

## Management & Access

### Management Interfaces
The management VLAN (VLAN 90) has an IP address of 10.90.0.11/24, which is the default gateway for this network segment.

- **Management VLAN and IP addressing**:
  - VLAN 90: Management SVI with IP address 10.90.0.11/24
  - Default gateway configuration: `ip default-gateway 10.90.0.254`
  - Management protocols enabled: SSH version 2 is supported (`ip ssh version 2`)

### Access Control & Security

#### Console Access
- **Console Access**: The console line has authentication set to the local database (`login authentication console`).

#### VTY Access
- **VTY Access**:
  - Line configuration: `line vty 0 4`
  - Access class restrictions: `access-class MGMT-MGMT in`
  - Transport protocols allowed: SSH is enabled (`transport input ssh`)
  - Enable password status and encryption level: Not explicitly stated in the configuration file

#### AAA Configuration
- **AAA Configuration**: TACACS+ is configured for authentication, authorization, and accounting. The server host is set to `10.91.0.10` with a key of `KompleksNoekkel`.

### Login Banners
- **Login Banners**: A login banner is configured (`banner login ^CUnauthorized access prohibited.^C`).

#### Management Access Lists
- **Management Access Lists**:
  - The management ACL (MGMT-MGMT) allows IP addresses within the ranges `10.90.0.0/24` and `10.91.0.0/24`.

## VLANs

### VLAN Database

| VLAN ID | Name        | Purpose/Description |
|---------|-------------|---------------------|
| 11      |             |                     |
| 12      |             |                     |
| 90      | Management  | Management SVI     |

### VLAN Interfaces (SVIs)

#### VLAN 11 Interface
- **VLAN 11 Interface**:
  - IP Address: Not configured
  - Description: Not provided
  - DHCP Helper: Not configured
  - HSRP/VRRP: Not configured

#### VLAN 12 Interface
- **VLAN 12 Interface**:
  - IP Address: Not configured
  - Description: Not provided
  - DHCP Helper: Not configured
  - HSRP/VRRP: Not configured

#### VLAN 90 Interface
- **VLAN 90 Interface**:
  - IP Address: `10.90.0.11/24`
  - Description: Management SVI
  - DHCP Helper: Not configured
  - HSRP/VRRP: Not configured

### VTP Configuration
- **VTP Mode**: This switch is not participating in VTP, as there are no VTP-related configuration statements.
- **VTP Domain**: Not configured
- **VTP Version**: Not configured
- **Analysis**: Since this switch is not participating in VTP, it's recommended to configure a domain name and enable VTP for centralized management.

## Physical Interfaces

### Interface Summary

| Interface | Description      | Mode     | VLAN/Trunk | Speed/Duplex | Status    | Special Features       |
|-----------|------------------|----------|------------|--------------|-----------|------------------------|
| F0/1     | PC4-Access port  | Access   | 11         |             | Up        | Port Security, STP    |
| F0/2     | PC5-Access port  | Access   | 12         |             | Up        | Port Security, STP    |
| F0/3     | Management-PC   | Access   | 90         |             | Up        |                        |
| G0/1     | dis-venstre-sw01 | Trunk    | 666 (Native) | Gigabit     | Up        | PortFast, BPDUGuard    |
| F0/4-F0/23| Unused Ports    | Access   | Shutdown   |             | Down      |                        |

### Detailed Interface Configurations

#### FastEthernet0/1
- **Description**: PC4-Access port
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 11`
  - `ip dhcp snooping limit rate 15`

#### FastEthernet0/2
- **Description**: PC5-Access port
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 12`
  - `ip dhcp snooping limit rate 15`

#### FastEthernet0/3
- **Description**: Management-PC Access port
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 90`

## Port-Channel / EtherChannel

Not configured.

## Routing Configuration

### Routing Protocol
No routing protocol is enabled on this switch.

### Static Routes
No static routes are defined.

### Default Route
- **Default Route**: The default route points to the next hop at `10.90.0.254`.

### Inter-VLAN Routing
- **Status**: This switch does not appear to be configured for inter-VLAN routing, as no router-on-a-stick configuration is present.
- **Method**: Not applicable

## Spanning Tree Protocol

### STP Configuration
- **Mode**: PVST+ (default)
- **Root Bridge**: The root bridge is locally calculated based on the priority and MAC address of this switch.

### STP Features
- **PortFast**: Enabled (`spanning-tree portfast`) on all interfaces except trunk ports.
- **BPDU Guard**: Enabled (`spanning-tree bpduguard enable`) for all access ports.
- **Root Guard**: Not configured.
- **Loop Guard**: Not configured.
- **UDLD**: Not configured.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
Not configured.

### Stack Configuration
This switch does not appear to be part of a stack configuration.

### Redundant Links
No redundant link configurations are present in the provided output.

## Quality of Service (QoS)

Not configured.

## Security Features

### Port Security
- **Port Security**: Enabled on FastEthernet0/1, FastEthernet0/2, and FastEthernet0/3.
  - Maximum MAC addresses allowed: 16
  - Violation actions configured: Restrict (`switchport port-security violation restrict`)
  - Static MAC addresses: Two entries are specified for each interface.

### DHCP Security
- **DHCP Snooping**: Enabled on VLANs 11, 12, and 90.
  - Trusted ports: None

## Storm Control
- **Storm Control**: Broadcast threshold is set to level 1 (`storm-control broadcast level 1`) for all interfaces except the trunk port.

### Access Control Lists (ACLs)
Two ACLs are configured:

#### Standard ACL MGMT-MGMT
- **Purpose**: Filter management access based on IP address.
- **Rules**:
  - `permit 10.90.0.0/24`
  - `permit 10.91.0.0/24`
  - `deny any`

## Network Services

### DHCP Server/Relay
Not configured.

### NTP (Network Time Protocol)
- **NTP Server**: An NTP server at `10.91.0.123` is configured with authentication key 15 (`ntp authenticate`).
- **NTP Authentication**: Enabled (`ntp authentication-key 15 md5`).

### SNMP (Simple Network Management Protocol)
Not configured.

### Syslog
- **Syslog Level**: Not explicitly stated in the configuration file
- **Logging Hosts**: One syslog host at `10.91.0.10`
- **Logging Buffer**: Not configured

## Best Practices Analysis

### Good Practices Identified
- PortFast and BPDU Guard are enabled to prevent loops on access ports.
- DHCP snooping is enabled for VLANs 11, 12, and 90.

### Potential Issues or Concerns
- There are no VTP-related configuration statements; it's recommended to configure a domain name and enable VTP for centralized management.
- No routing protocol is configured; consider enabling an IGP (Interior Gateway Protocol) for intra-VLAN routing.
- The switch has multiple unused ports in shutdown state.

### Recommendations for Improvement
1. **Configure VTP**: Enable VTP, set a domain name, and configure the version for centralized VLAN management.
2. **Implement Routing**: Configure a routing protocol to enable intra-VLAN routing.
3. **Secure Unused Ports**: Remove any unnecessary interfaces from service.

## Configuration Summary

- **Total VLANs**: 4
- **Total Configured Interfaces**: 23 (active) + 1 (trunk)
- **Routing**: Disabled (no routing protocol configured)
- **Spanning Tree**: PVST+ with local root bridge calculation
- **Key Features Enabled**:
  - PortFast on access ports
  - BPDU Guard for access ports
  - DHCP snooping for VLANs 11, 12, and 90
  - Storm control with broadcast threshold level 1
- **Security Posture**: Good practices identified; consider implementing additional security features.
- **Overall Assessment**: The configuration is generally well-maintained but lacks VTP and routing configurations.