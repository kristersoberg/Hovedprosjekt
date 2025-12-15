# Switch Configuration Documentation: 1-aksess-sw01-14.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown (no version information provided)
- **Configuration Purpose**: This switch appears to be a core access layer device, providing management and user access for the network.
- **Last Modified**: Not available in the configuration file
- **Domain Name**: krister.local

## Device Information
- **Model**: Not available in the configuration file
- **System Image**: Not available in the configuration file
- **Serial Number**: Not available in the configuration file
- **Hardware Details**: Not available in the configuration file

## Management & Access

### Management Interfaces
The switch has a management VLAN (VLAN 90) with IP address 10.90.0.11/24.

#### Management SVI
- **Management VLAN and IP addressing**: The interface Vlan90 is configured as the management SVI with an IP address of 10.90.0.11/24.
- **Default gateway configuration**: The default gateway for this subnet is set to 10.90.0.254.
- **Management protocols enabled**: SSH version 2 and TACACS+ are enabled.

### Access Control & Security
The switch has a console line configured with authentication, enable secret password, and access class restrictions.

#### Console Access
- **Console line configuration**: The console line is configured for local authentication.
- **Enable Password**: The enable secret password is set to 3NA8le$cret!=1.

#### VTY Access
The switch has VTY lines 0 through 4 configured with authentication and access class restrictions.

#### AAA Configuration
AAA (Authentication, Authorization, Accounting) is enabled on the switch with a TACACS+ server at IP address 10.91.0.10.

### Login Banners
There is a login banner set to display "Unauthorized access prohibited."

## VLANs

### VLAN Database
| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      | Usergroup1-1 | Access VLAN for user group 1.1 |
| 12      | Usergroup1-2 | Access VLAN for user group 1.2 |
| 90      | Admin-Mgmt-LEFT | Management SVI VLAN |
| 666     | native-trunk | Native VLAN for trunk interfaces |

### VLAN Interfaces (SVIs)
For each VLAN interface, the following configurations are applied:

#### Vlan11 Interface
- **VLAN ID**: 11
- **Name**: Usergroup1-1

#### Vlan12 Interface
- **VLAN ID**: 12
- **Name**: Usergroup1-2

#### Vlan90 Interface
- **VLAN ID**: 90
- **Name**: Admin-Mgmt-LEFT
- **IP Address**: 10.90.0.11/24
- **Access Group**: MGMT-MGMT is applied to this interface.

## Physical Interfaces

### Interface Summary
| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| GigabitEthernet0/1 | dis-venstre-sw01 gig0/1 | Trunk | 11,12,90 | 1000 Full | Up | None |
| FastEthernet0/1 | PC4-Access port | Access | 11 | Auto Auto | Up | Port Security |
| FastEthernet0/2 | PC5-Access port | Access | 12 | Auto Auto | Up | Port Security |
| FastEthernet0/3 | Management-PC Access port | Access | 90 | Auto Auto | Up | Port Security |

### Detailed Interface Configurations
Each interface has the following configurations:

#### GigabitEthernet0/1
- **Mode**: Trunk
- **VLANs Allowed**: 11, 12, 90
- **Native VLAN**: 666

#### FastEthernet0/1
- **Mode**: Access
- **Access VLAN**: 11
- **Port Security**: Enabled with maximum MAC addresses set to 1 and violation action restricted.

## Port-Channel / EtherChannel

No port-channel configurations are found in the switch configuration.

## Routing Configuration

### Routing Protocol
No routing protocols are configured on this switch, as it appears to be operating in a Layer 2 environment.

### Static Routes
No static routes are configured on this switch.

### Default Route
There is no default route configured on this switch.

### Inter-VLAN Routing
Inter-VLAN routing is not enabled on this switch.

## Spanning Tree Protocol

### STP Configuration
Spanning Tree Protocol (STP) is enabled with the following configurations:

- **Mode**: Rapid-PVST+
- **Priority**: 61440 for VLANs 11, 12, and 90

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
No HSRP or VRRP configurations are found in the switch configuration.

## Quality of Service (QoS)

No QoS configurations are found in the switch configuration.

## Security Features

### Port Security
Port security is enabled on FastEthernet0/1, 0/2, and 0/3 interfaces with a maximum MAC address limit set to 1 and violation action restricted.

### DHCP Snooping
DHCP snooping is configured on VLANs 11, 12, and 90.

## Access Control Lists (ACLs)

The following ACLs are defined:

- **MGMT-MGMT**: An access list named MGMT-MGMT is applied to the Vlan90 interface.

## Network Services

### DHCP Server/Relay
No DHCP server or relay configurations are found in the switch configuration.

### NTP (Network Time Protocol)
NTP is configured with a single server at IP address 10.91.0.123, authentication key set to MD5 KomplekstPassord.

## Best Practices Analysis

- **Good practices identified**: The switch has TACACS+ enabled for AAA and SSH version 2 enabled for secure remote access.
- **Potential issues or concerns**:
  - Port security is not configured on all interfaces; it's recommended to enable port security globally to prevent unauthorized device connections.
  - There are no ACLs applied to the VLAN interfaces, which could be used for traffic filtering and management.
  - STP priority values should be set consistently across all switches in the network to ensure proper root bridge election.
- **Recommendations for improvement**:
  1. Enable port security globally on the switch.
  2. Apply ACLs to VLAN interfaces as needed.
  3. Review and configure consistent STP priority settings.

## Configuration Summary

- **Total VLANs**: 4
- **Total Configured Interfaces**: 7
- **Routing**: Not enabled
- **Spanning Tree**: Rapid-PVST+
- **Key Features Enabled**: TACACS+, SSH version 2, Port Security on selected interfaces
- **Security Posture**: The switch has a good security posture with TACACS+ and SSH version 2 enabled. However, there are potential issues regarding port security configuration.
- **Overall Assessment**: This switch appears to be a well-configured access layer device with good security practices in place.