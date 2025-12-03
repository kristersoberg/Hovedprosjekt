# Switch Configuration Documentation: 1-aksess-sw01-9.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: This switch appears to be a network access layer device, managing user traffic and providing management interfaces for administrators. It has multiple VLANs configured, with at least three access ports (FastEthernet0/1, FastEthernet0/2, and FastEthernet0/3) assigned to different VLANs.
- **Last Modified**: Not specified in the configuration
- **Domain Name**: krister.local

## Device Information
- **Model**: Not specified in the configuration (check hardware details or serial number for more information)
- **System Image**: The boot image is unknown due to the missing IOS version
- **Serial Number**: Not available in the provided configuration

## Management & Access

### Management Interfaces
The switch has a management VLAN and IP addressing configured on interface Vlan90:
- **Management VLAN and IP addressing**:
  - Interface: Vlan90
  - Description: Management SVI
  - IP Address: 10.90.0.11/255.255.255.0
  - Access Group: MGMT-MGMT (inbound)
- **Default gateway configuration**: The default gateway is set to 10.90.0.254

### Access Control & Security
- **Console Access**:
  - Console line configured, using authentication method "console"
  - Enable password is set with a secret level of 15
- **VTY Access**:
  - VTY lines (0 through 4) are configured for SSH only
  - Authentication default group is set to "tacacs+" followed by local
- **Enable Password**: The enable secret password is encrypted with a strength level of 15
- **AAA Configuration**: AAA configuration includes conditional fallback, with TACACS+ as the primary method and local authentication as the secondary method.
- **Login Banners**: A banner prohibiting unauthorized access is configured.

### Management Access Lists
The MGMT-MGMT ACL is applied to inbound traffic on interface Vlan90. Here's a breakdown of its rules:
| Rule # | Action | Protocol | Source | Destination | Port Range |
| --- | --- | --- | --- | --- | --- |
| 1    | Permit | IP        | 10.90.0.0/255.255.255.0 | Any          | -           |
| 2    | Permit | IP        | 10.91.0.0/255.255.255.0 | Any          | -           |
| 3    | Deny   | Any      | Any              | Any          | - |

## VLANs

### VLAN Database
Here's a table summarizing the VLAN database:

| VLAN ID | Name            | Purpose/Description        |
|---------|-----------------|----------------------------|
| 11      | Usergroup1-1    | User traffic, VLAN 11       |
| 12      | Usergroup1-2    | User traffic, VLAN 12       |
| 90      | Admin-Mgmt-LEFT | Management VLAN            |
| 666     | native-trunk    | Native trunk VLAN           |

### VLAN Interfaces (SVIs)
Here's a breakdown of the SVI configurations:

#### Vlan11 Interface
- **VLAN ID**: 11
- **IP Address**: Not configured directly in this configuration; however, it should be used for accessing devices on VLAN 11.
- **Description**: Usergroup1-1
- **DHCP Helper**: Not configured
- **HSRP/VRRP**: Not configured

#### Vlan12 Interface
- **VLAN ID**: 12
- **IP Address**: Not configured directly in this configuration; however, it should be used for accessing devices on VLAN 12.
- **Description**: Usergroup1-2
- **DHCP Helper**: Not configured
- **HSRP/VRRP**: Not configured

#### Vlan90 Interface
- **VLAN ID**: 90
- **IP Address**: 10.90.0.11/255.255.255.0
- **Description**: Management SVI
- **DHCP Helper**: Not configured
- **HSRP/VRRP**: Not configured

### VTP Configuration
The switch appears to be in a different VTP mode, but we can't determine the exact mode due to missing information.

## Physical Interfaces

### Interface Summary
Here's an interface summary table:

| Interface | Description     | Mode | VLAN/Trunk | Speed/Duplex | Status   | Special Features |
|-----------|-----------------|------|------------|--------------|----------|------------------|
| Gig0/1    | dis-venstre-sw01| Trunk| 11,12,90   | -            | Up       | STP, PortFast     |
| Fa0/1     | PC4-Access port | Access| 11         | -            | Up       | STP, PortFast     |
| Fa0/2     | PC5-Access port | Access| 12         | -            | Up       | STP, PortFast     |
| Fa0/3     | Mgmt-PC Access | Access| 90         | -            | Up       | STP, PortFast     |

### Detailed Interface Configurations
Here are detailed explanations of the interface configurations:

#### GigabitEthernet0/1
- **Description**: dis-venstre-sw01 gig0/1
- **Mode**: Trunk
- **Configuration Details**:
  - Switchport trunk encapsulation: dot1q
  - Switchport mode trunk
  - Switchport nonegotiate (enables DTP to be disabled)
  - Switchport trunk native vlan 666
  - Switchport trunk allowed vlans 11,12,90

#### FastEthernet0/1
- **Description**: PC4-Access port
- **Mode**: Access
- **Configuration Details**:
  - Switchport mode access
  - Switchport access vlan 11
  - Port-security enabled (max mac addresses: 1, violation action restrict)

#### FastEthernet0/2
- **Description**: PC5-Access port
- **Mode**: Access
- **Configuration Details**:
  - Switchport mode access
  - Switchport access vlan 12
  - Port-security enabled (max mac addresses: 1, violation action restrict)

#### FastEthernet0/3
- **Description**: Management-PC Access port
- **Mode**: Access
- **Configuration Details**:
  - Switchport mode access
  - Switchport access vlan 90
  - Port-security enabled (max mac addresses: 1, violation action restrict)

## Routing Configuration

### Routing Protocol
No routing protocol is configured in this configuration.

### Static Routes
There are no static routes configured.

### Default Route
The default route is not explicitly configured.

### Inter-VLAN Routing
Inter-VLAN routing appears to be disabled.

## Spanning Tree Protocol

### STP Configuration
- **Mode**: PVST+
- **Root Bridge**: Not specified in the configuration (this switch may or may not be the root bridge)
- **Priority**: 61440 (configured priority value for VLANs 11,12,90)

### STP Features
- **PortFast**: Enabled on Fa0/1, Fa0/2, and Fa0/3 interfaces
- **BPDU Guard**: Not explicitly configured; however, it is possible that the global BPDU guard setting applies to these interfaces.
- **Root Guard**: Not explicitly configured
- **Loop Guard**: Not explicitly configured
- **UDLD**: Not explicitly configured

### Per-VLAN STP Status
The per-VLAN STP status is not specified in this configuration.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
No FHRP configuration is present in the provided switch configuration.

### Stack Configuration
This switch appears to be a standalone device; there's no indication that it's part of a stack.

### Redundant Links
No redundant link configurations are specified in this configuration.

## Quality of Service (QoS)

No QoS configuration has been found in the provided switch configuration.

## Security Features

### Port Security
Port security is enabled on Fa0/1, Fa0/2, and Fa0/3 interfaces. Here's a summary:

| Interface | Max MAC addresses allowed | Violation action |
|-----------|-----------------------------|------------------|
| Fa0/1     | 1                           | Restrict        |
| Fa0/2     | 1                           | Restrict        |
| Fa0/3     | 1                           | Restrict        |

### DHCP Security
- **DHCP Snooping**: Enabled (trusted ports: Gig0/1)
- **DHCP Snooping Database**: Not explicitly configured

### Dynamic ARP Inspection (DAI)
- **Status**: Disabled
- **Trusted interfaces**: None
- **VLANs protected**: None

### IP Source Guard
No configuration has been found for IP source guard.

### Storm Control
Storm control is enabled on Fa0/1, Fa0/2, and Fa0/3 interfaces:

| Interface | Threshold (broadcast/multicast/unicast) |
|-----------|------------------------------------------|
| Fa0/1     | 1.00 (broadcast)                         |
| Fa0/2     | 1.00 (broadcast)                         |
| Fa0/3     | 1.00 (broadcast)                         |

### Access Control Lists (ACLs)
There are no ACLs in the provided switch configuration.

## Network Services

### DHCP Server/Relay
- **DHCP Server**: Not configured as a server; however, it may be configured to act as a relay.
- **DHCP Relay**: Not explicitly configured as a relay helper address.

### NTP (Network Time Protocol)
- **NTP Server(s)**: 10.91.0.123
- **NTP Authentication**: Yes (using MD5 with key number 15 and password "KomplekstPassord")
- **Timezone**: Not explicitly configured

### SNMP (Simple Network Management Protocol)
No configuration has been found for SNMP.

### Syslog
Syslog is enabled, but the logging level and remote syslog servers are not specified in this configuration:
- **Logging Level**: Not specified
- **Logging Hosts**: None
- **Logging Buffer**: The buffer size is set to 4096

### DNS Configuration
No DNS server has been configured on this switch.

### CDP/LLDP
CDP and LLDP appear to be globally disabled, but there's no per-interface configuration provided:

## Best Practices Analysis

### Good Practices Identified
- Port security enabled (Fa0/1, Fa0/2, and Fa0/3)
- STP portfast enabled (Fa0/1, Fa0/2, and Fa0/3)
- DHCP snooping is enabled globally, but there are no trusted ports specified.

### Potential Issues or Concerns
- No FHRP configuration has been found in this switch configuration.
- There's an unused interface (GigabitEthernet0/2).
- Port security settings could be made more specific to limit the number of MAC addresses allowed per port.
- The default route is not configured; ensure a suitable default gateway is set.

### Recommendations for Improvement
1. Configure FHRP (HSRP or VRRP) on at least one interface for redundancy and failover capabilities.
2. Document all interfaces, including their purposes, descriptions, and security settings.
3. Consider implementing VLAN trunking to carry multiple VLANs over a single link.
4. Verify the port-security settings are suitable for the environment.

## Configuration Summary

* **Total VLANs**: 5
* **Total Configured Interfaces**: 10 (active)
* **Routing**: Disabled
* **Spanning Tree**: PVST+ mode, configured priority value 61440
* **Key Features Enabled**: Port security, STP portfast, DHCP snooping
* **Security Posture**: The switch appears to have some basic security features enabled; however, further analysis is required for a more comprehensive assessment.
* **Overall Assessment**: This configuration has potential issues and can be improved with specific recommendations.

## Appendix

### Uncommon or Complex Configurations
No uncommon or complex configurations are documented here.