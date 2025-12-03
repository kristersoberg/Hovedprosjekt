# Switch Configuration Documentation: 1-aksess-sw01-5.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown (extracted from the configuration)
- **Configuration Purpose**: The switch appears to be a management and access layer switch for a network, given its VLAN configurations and interface settings.
- **Last Modified**: Not available in the provided configuration file.
- **Domain Name**: krister.local

## Device Information
- **Model**: Not available in the provided configuration file.
- **System Image**: Unknown (extracted from the configuration)
- **Serial Number**: Not available in the provided configuration file.
- **Hardware Details**: The switch has multiple Gigabit Ethernet and Fast Ethernet interfaces.

## Management & Access

### Management Interfaces
The management VLAN is configured as VLAN 90 with IP address 10.90.0.11/24, which is used for management access.

#### Management VLAN (VLAN 90)
- **VLAN ID**: 90
- **Name**: Admin-Mgmt-LEFT
- **IP Address**: 10.90.0.11/24
- **Description**: Management SVI

### Access Control & Security
The switch has a variety of access control and security configurations in place.

#### Console Access
- The console line is configured for local authentication with no timeout.

#### VTY Access
- Telnet and SSH are allowed on the VTY lines, which use the default authentication method.
- An access class restriction is applied using ACL MGMT-MGMT.

#### Enable Password
- The enable secret password is set to 3NA8le$cret!=1.

#### AAA Configuration
- The switch uses TACACS+ for authentication and authorization.
- Local users are also configured, including an emergency-admin user with high privilege level.

### Login Banners
- A login banner is configured warning unauthorized access.

### Management Access Lists
The MGMT-MGMT ACL allows traffic from 10.90.0.0/24 and 10.91.0.0/24.

#### MGMT-MGMT ACL (Standard)
- **Name**: MGMT-MGMT
- **Rules**:
  - permit 10.90.0.0 0.0.0.255
  - permit 10.91.0.0 0.0.0.255
  - deny   any

## VLANs

### VLAN Database
The switch has multiple VLANs configured, including VLANs for user access and management.

#### VLAN Summary Table
| VLAN ID | Name         | Purpose/Description          |
|---------|--------------|------------------------------|
| 11      | Usergroup1-1 | User access VLAN            |
| 12      | Usergroup1-2 | User access VLAN            |
| 90      | Admin-Mgmt-LEFT | Management VLAN              |
| 666     | native-trunk | Native trunk VLAN          |

### VLAN Interfaces (SVIs)
The switch has multiple SVIs configured.

#### VLAN 11 Interface
- **VLAN ID**: 11
- **Name**: Usergroup1-1
- **IP Address**: Not configured

#### VLAN 12 Interface
- **VLAN ID**: 12
- **Name**: Usergroup1-2
- **IP Address**: Not configured

#### VLAN 90 Interface
- **VLAN ID**: 90
- **Name**: Admin-Mgmt-LEFT
- **IP Address**: 10.90.0.11/24 (management IP)

## Physical Interfaces

### Interface Summary Table
| Interface | Description        | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features          |
|-----------|--------------------|------|------------|--------------|--------|---------------------------|
| Gi0/1    | dis-venstre-sw01   | trunk| 666        | auto         | up     | nonegotiate               |
| Fx0/1    | PC4-Access port   | access| 11         | auto         | up     | storm-control, port-security|
| Fx0/2    | PC5-Access port   | access| 12         | auto         | up     | storm-control, port-security|
| Fx0/3    | Management-PC Access port| access| 90        | auto         | up     |                            |
| Gi0/2    | dis-venstre-sw01   | trunk|             | auto         | down   | nonegotiate               |
| Fx0/4-24| Unused ports      | access|             | auto         | shutdown|                          |

### Detailed Interface Configurations
Multiple interfaces are configured for specific purposes.

#### Gi0/1 (Trunk)
- **Description**: dis-venstre-sw01 gig0/1
- **Mode**: trunk
- **Configuration Details**:
  - switchport trunk encapsulation dot1q
  - switchport mode trunk
  - switchport nonegotiate
  - switchport trunk native vlan 666
  - switchport trunk allowed vlan 11,12,90

#### Fx0/1 (Access)
- **Description**: PC4-Access port
- **Mode**: access
- **Configuration Details**:
  - switchport mode access 
  - switchport access vlan 11
  - switchport port-security
  - switchport port-security maximum 1 
  - switchport port-security violation restrict
  - switchport port-security aging time 3
  - switchport port-security mac-address sticky

## Port-Channel / EtherChannel
Not configured.

## Routing Configuration

### Routing Protocol
No routing protocol is configured on this switch.

### Static Routes
None are configured.

### Default Route
The default gateway is set to 10.90.0.254.

#### Default Gateway Configuration
- **IP Address**: 10.90.0.254
- **Gateway Name**: Not available

## Spanning Tree Protocol

### STP Configuration
- **Mode**: PVST+
- **Root Bridge**: This switch is not the root bridge for any VLANs.
- **Priority**: The priority value is set to 61440.

### STP Features
- **PortFast**: Enabled on multiple interfaces, including Fx0/1 and Fx0/2.
- **BPDU Guard**: Not configured.
- **Root Guard**: Not configured.
- **Loop Guard**: Not configured.
- **UDLD**: Not configured.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
Not configured.

### Stack Configuration
This switch is not part of a stack.

## Quality of Service (QoS)

No QoS configuration is present.

## Security Features

### Port Security
- Interfaces with port security enabled: Fx0/1, Fx0/2, and Fx0/3.
- **Maximum MAC addresses allowed**: 1 per port.
- **Violation actions configured**: restrict.

### DHCP Security
- **DHCP Snooping**: Enabled on VLANs 11, 12, and ip dhcp snooping trust is configured on Gi0/1.
- **DHCP Snooping Database**: Not configured.

### Dynamic ARP Inspection (DAI)
- Status: Enabled on VLANs 11, 12.
- **Trusted interfaces**: Gi0/1.

### IP Source Guard
Not configured.

### Storm Control
- **Configuration**: broadcast level 1.00 is set for Fx0/1 and Fx0/2.

## Access Control Lists (ACLs)

Multiple ACLs are configured, including MGMT-MGMT.

#### MGMT-MGMT ACL (Standard)
- **Name**: MGMT-MGMT
- **Rules**:
  - permit 10.90.0.0 0.0.0.255
  - permit 10.91.0.0 0.0.0.255
  - deny   any

## Network Services

### DHCP Server/Relay
No DHCP server or relay is configured on this switch.

### NTP (Network Time Protocol)
- **NTP Server**: 10.91.0.123.
- **NTP Authentication**: Enabled with a key of 15 and MD5 authentication.

### SNMP (Simple Network Management Protocol)
- **SNMP Version**: Not available in the configuration.
- **Community Strings**: Not configured or exposed.
- **SNMP Traps**: Not configured.
- **SNMP Hosts**: Not configured.

### Syslog
- **Logging Level**: Not configured.
- **Logging Hosts**: 10.91.0.10.
- **Logging Buffer**: Size and settings not available.

## Best Practices Analysis

The configuration appears to follow many best practices, including:

- Using meaningful VLAN names
- Documenting VLAN assignments
- Avoiding using VLAN 1 for user traffic
- Planning VLAN numbering scheme

However, some potential issues or concerns were identified:

- The switch has a mix of enabled and disabled security features.
- No QoS configuration is present.
- There are unused ports that should be configured with default settings.

The following recommendations for improvement were suggested:

- Enable QoS configuration to prioritize traffic based on business needs.
- Configure port security and MAC address limiting on all access ports.
- Consider implementing a unified threat management (UTM) solution to improve network security.
- Review and adjust the VLAN numbering scheme to ensure it aligns with organizational policies.

## Configuration Summary

- **Total VLANs**: 4
- **Total Configured Interfaces**: Multiple interfaces are configured for specific purposes.
- **Routing**: Not enabled.
- **Spanning Tree**: PVST+ mode is used, but this switch is not the root bridge for any VLANs.
- **Key Features Enabled**: Port security, DHCP snooping, and DAI are enabled on certain VLANs and interfaces.
- **Security Posture**: The configuration has a mix of enabled and disabled security features, indicating room for improvement.

## Appendix

### Uncommon or Complex Configurations
Multiple configurations could be considered uncommon or complex due to their specific use cases. However, these can be documented as needed in the future.

### Configuration Snippets
No additional configuration snippets are available for this analysis.