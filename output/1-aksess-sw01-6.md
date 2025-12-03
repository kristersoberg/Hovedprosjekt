# Switch Configuration Documentation: 1-aksess-sw01-6.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: This is a management switch, likely configured for administrative purposes with access control and security features enabled.
- **Last Modified**: Not specified in the configuration file.
- **Domain Name**: krister.local

## Device Information
- **Model**: Not specified in the configuration file.
- **System Image**: Unknown due to lack of information about the IOS version.
- **Serial Number**: Not available.
- **Hardware Details**: The switch has GigabitEthernet0/1 and FastEthernet0/1-3 interfaces.

## Management & Access

### Management Interfaces
Document all management-related interface configurations:
- **Management VLAN and IP addressing**:
  - Vlan90 is the management VLAN, configured with IP address 10.90.0.11.
  - Default gateway is set to 10.90.0.254.
- **Default gateway configuration**: The default gateway for the switch is 10.90.0.254.
- **Management protocols enabled**:
  - SSH version 2 is enabled with a timeout of 60 seconds and authentication retries limited to 3.

### Access Control & Security
- **Console Access**:
  - Console line is configured with login authentication set to console and an exec-timeout of 10 minutes.
- **VTY Access**:
  - Line configuration for VTY access is set with login authentication default and transport input SSH enabled.
  - Access-class MGMT-MGMT is applied in for inbound traffic.
- **Enable Password**: The enable secret password is set to 3NA8le$cret!=1, which is encrypted.
- **AAA Configuration**:
  - AAA is enabled using the new-model command.
  - TACACS+ server is configured with IP address 10.91.0.10 and a key of KompleksNoekkel.
  - Local authentication is also configured for console access.
  - Authentication, authorization, and accounting are all set to use TACACS+ as the primary source.
- **Login Banners**: A login banner is configured with the message "Unauthorized access prohibited."

### Management Access Lists
- **MGMT-MGMT**:
  - This standard ACL permits IP addresses from networks 10.90.0.0/24 and 10.91.0.0/24, and denies all other traffic.

## VLANs

### VLAN Database
| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      | Usergroup1-1        | Access VLAN for users in group 1 |
| 12      | Usergroup1-2        | Access VLAN for users in group 2 |
| 90      | Admin-Mgmt-LEFT     | Management VLAN              |
| 666     | native-trunk        | Native VLAN for trunk ports   |

### VLAN Interfaces (SVIs)
#### Vlan90 Interface
- **IP Address**: 10.90.0.11/24
- **Description**: Management SVI
- **DHCP Helper**: None configured.
- **HSRP/VRRP**: Not configured.

## Physical Interfaces

### Interface Summary
| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| GigabitEthernet0/1  | dis-venstre-sw01 gig0/1 | Trunk   | 11,12,90    | Full-duplex | Up      | CDP and LLDP disabled, Port security enabled |
| FastEthernet0/1     | PC4-Access port      | Access | 11          | Auto        | Up      | Port security enabled, Spanning Tree enabled |
| FastEthernet0/2     | PC5-Access port      | Access | 12          | Auto        | Up      | Port security enabled, Spanning Tree enabled |
| FastEthernet0/3     | Management-PC Access port | Access | 90          | Auto        | Up      | Port security enabled, Spanning Tree enabled |

### Detailed Interface Configurations

#### GigabitEthernet0/1
- **Description**: dis-venstre-sw01 gig0/1
- **Mode**: Trunk
- **Configuration Details**:
  - switchport trunk encapsulation dot1q is set.
  - switchport mode trunk is enabled.
  - Switchport nonegotiate is enabled, which means the interface will not engage in DTP (Dynamic Trunking Protocol) negotiation with its peer.
  - switchport trunk native vlan 666 is configured to set the native VLAN for this trunk port to VLAN 666.
  - switchport trunk allowed vlan 11,12,90 is configured to allow traffic from these three VLANs on this trunk interface.
  - ip dhcp snooping trust and ip arp inspection trust are enabled.

#### FastEthernet0/1
- **Description**: PC4-Access port
- **Mode**: Access
- **Configuration Details**:
  - switchport access vlan 11 is configured to assign the interface to VLAN 11 for user group 1.
  - Port security is enabled with maximum number of MAC addresses set to 1 and violation action restricted.
  - Aging time for MAC address entries is set to 3 minutes.

#### FastEthernet0/2
- **Description**: PC5-Access port
- **Mode**: Access
- **Configuration Details**:
  - switchport access vlan 12 is configured to assign the interface to VLAN 12 for user group 2.
  - Port security is enabled with maximum number of MAC addresses set to 1 and violation action restricted.
  - Aging time for MAC address entries is set to 3 minutes.

#### FastEthernet0/3
- **Description**: Management-PC Access port
- **Mode**: Access
- **Configuration Details**:
  - switchport access vlan 90 is configured to assign the interface to VLAN 90 for management.
  - Port security is enabled with maximum number of MAC addresses set to 1 and violation action restricted.
  - Spanning Tree is enabled.

### Unused Interfaces
There are two unused interfaces: FastEthernet0/4-24 and GigabitEthernet0/2. They are both in a shutdown state, which means they can be used for future expansion or modifications.

## Port-Channel / EtherChannel

There is no port-channel configuration on the switch.

## Routing Configuration

### Routing Protocol
No routing protocol is configured.

### Static Routes
There are no static routes configured.

### Default Route
The default route is set to 10.90.0.254, which is likely a gateway of last resort.

### Inter-VLAN Routing
Inter-vlan routing is not enabled on this switch because the VLANs are not associated with any router interface.

## Spanning Tree Protocol

### STP Configuration
- **Mode**: PVST+
- **Root Bridge**: This switch is configured as a root bridge for all VLANs.
- **Priority**: The priority of the root bridge is 61440, which is set for VLANs 11, 12, and 90.

### STP Features
- **PortFast**: Portfast is enabled on interfaces FastEthernet0/1, FastEthernet0/2, and FastEthernet0/3.
- **BPDU Guard**: Bpdu guard is not configured on any interface.
- **Root Guard**: Root guard is not configured on any interface.
- **Loop Guard**: Loop guard is not configured on any interface.
- **UDLD**: UDLD is not enabled.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
No HSRP or VRRP configuration is present in the provided switch configuration.

### Stack Configuration
The switch is not part of a stack because there is no information about other switches being connected to it.

## Quality of Service (QoS)

There are no QoS configurations on this switch.

## Security Features

### Port Security
Port security is enabled with maximum number of MAC addresses set to 1 and violation action restricted on interfaces FastEthernet0/1, FastEthernet0/2, and FastEthernet0/3.

### DHCP Security
- **DHCP Snooping**: DHCP snooping is enabled with the trusted interface GigabitEthernet0/1.
- **DHCP Snooping Database**: The configuration for the DHCP snooping database is not provided in the given output.

## Storm Control

Storm control is configured on interfaces FastEthernet0/1, FastEthernet0/2, and FastEthernet0/3 to prevent broadcast storms.