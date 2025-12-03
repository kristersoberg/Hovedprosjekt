# Switch Configuration Documentation: 1-aksess-sw01-10.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: This switch likely serves as a network access layer device, providing connectivity to various networks and devices.
- **Last Modified**: Not available in the configuration file
- **Domain Name**: krister.local

## Device Information
- **Model**: Not available (unknown)
- **System Image**: The boot image is not explicitly mentioned, but it's likely a Cisco IOS version that supports this feature set.
- **Serial Number**: Not available
- **Hardware Details**: This device has multiple Gigabit Ethernet interfaces and FastEthernet interfaces.

## Management & Access

### Management Interfaces
The management VLAN is 90 with the IP address 10.90.0.11/24, which is also the default gateway for this switch (10.90.0.254).

- **Management VLAN and IP addressing**: VLAN 90
  - Description: Management SVI
  - IP Address: 10.90.0.11/24
- **Default Gateway Configuration**: The default gateway is set to 10.90.0.254.
- **Management Protocols Enabled**: SSH (version 2), and TACACS+ are enabled.

### Access Control & Security

#### Console Access
- **Console Line Configuration**:
  - Login Authentication: local console
  - Exec Timeout: 10 minutes

#### VTY Access
- **Line Configuration**:
  - Login Authentication: default group tacacs+ local
  - Transport Input: SSH
- **Access Class Restrictions**: MGMT-MGMT is applied to restrict access.
- **Transport Protocols Allowed**: Only SSH is enabled.

#### Enable Password
- **Enable Secret**: The enable secret password is set, but it's not explicitly mentioned in the configuration.

#### AAA Configuration
- **Authentication Method**: This switch uses TACACS+ for authentication and authorization. Local authentication is also configured as a fallback.
- **Authorization Method**: Authorization is done using TACACS+ with local as a fallback.
- **Accounting Method**: Accounting is done using TACACS+.

#### Login Banners
- **Login Banner**: A banner login is set, prohibiting unauthorized access.

### Management Access Lists
The ACL MGMT-MGMT is applied to restrict management access.

| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      | Usergroup1-1 | Network for user group 1 |
| 12      | Usergroup1-2 | Network for user group 2 |
| 90      | Admin-Mgmt-LEFT | Management VLAN |
| 666     | native-trunk | Native VLAN for trunk links |

### VLAN Interfaces (SVIs)
The following SVIs are configured:

#### VLAN 11 Interface
- **IP Address**: Not explicitly mentioned, but it's likely on the 10.0.0.0/24 network.

#### VLAN 12 Interface
- **IP Address**: Not explicitly mentioned, but it's likely on the 10.0.0.0/24 network.

#### VLAN 90 Interface
- **IP Address**: 10.90.0.11/24

### VTP Configuration
This switch is not configured as a VTP server or client; therefore, VTP is disabled.

## Physical Interfaces

### Interface Summary
| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| GigabitEthernet0/1  | dis-venstre-sw01 gig0/1 | Trunk | VLANs 11,12,90 | Auto/Medium | Up | None |
| FastEthernet0/1    | PC4-Access port   | Access  | VLAN 11     | Auto/Medium | Up | Port Security, Storm Control |
| FastEthernet0/2    | PC5-Access port   | Access  | VLAN 12     | Auto/Medium | Up | Port Security, Storm Control |
| FastEthernet0/3    | Management-PC Access port | Access  | VLAN 90     | Auto/Medium | Up | None |
| GigabitEthernet0/2 | unused interface | - | - | Auto/Medium | Down | None |

### Detailed Interface Configurations
#### GigabitEthernet0/1

- **Description**: dis-venstre-sw01 gig0/1
- **Mode**: Trunk
- **Configuration Details**:
  - switchport trunk encapsulation dot1q
  - switchport mode trunk
  - switchport nonegotiate
  - switchport trunk native vlan 666
  - switchport trunk allowed vlan 11,12,90
- **Security Features Enabled**: None

#### FastEthernet0/1

- **Description**: PC4-Access port
- **Mode**: Access
- **Configuration Details**:
  - switchport mode access 
  - switchport access vlan 11
  - switchport port-security
  - switchport port-security maximum 1 
  - switchport port-security violation restrict
  - switchport port-security aging time 3
  - switchport port-security mac-address sticky
- **Security Features Enabled**: Port Security, Storm Control

#### FastEthernet0/2

- **Description**: PC5-Access port
- **Mode**: Access
- **Configuration Details**:
  - switchport mode access 
  - switchport access vlan 12
  - switchport port-security
  - switchport port-security maximum 1 
  - switchport port-security violation restrict
  - switchport port-security aging time 3
  - switchport port-security mac-address sticky
- **Security Features Enabled**: Port Security, Storm Control

#### FastEthernet0/3

- **Description**: Management-PC Access port
- **Mode**: Access
- **Configuration Details**:
  - switchport mode access 
  - switchport access vlan 90
  - switchport port-security
  - switchport port-security maximum 1 
  - switchport port-security violation restrict
  - switchport port-security aging time 3
  - switchport port-security mac-address sticky
- **Security Features Enabled**: None

### Unused Interfaces
There are two unused interfaces: GigabitEthernet0/2 is shut down, and FastEthernet0/4 through 24 are also in shutdown state. The default configuration for these ports would include the "shutdown" command.

## Port-Channel / EtherChannel
No port-channel configurations were found.

## Routing Configuration

### Routing Protocol
This device does not have any routing protocols configured (OSPF, EIGRP, RIP, BGP).

### Static Routes
There are no static routes configured in this configuration file. However, the default route is set to 10.90.0.254 for all traffic.

### Default Route
- **Configuration**: The default route points to 10.90.0.254.
- **Next-hop**: This would depend on whether a static route exists for that network segment.

### Inter-VLAN Routing
This device does not have inter-vlan routing enabled.

## Spanning Tree Protocol

### STP Configuration
- **Mode**: The spanning tree mode is not explicitly set, but it's likely using the default PVST+ (Per VLAN Spanning Tree Plus) mode.
- **Root Bridge**: This switch may be configured as a root bridge for specific VLANs.
- **Priority**: Not available.

### STP Features
- **PortFast**: Some interfaces have portfast enabled; however, there is no comprehensive list of all PortFast-enabled ports.
- **BPDU Guard**: BPDU guard is not explicitly set but might be inherited from the global settings or VTP domain.
- **Root Guard**: Not configured.
- **Loop Guard**: Not configured.
- **UDLD**: Not configured.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
No HSRP, VRRP, or GLBP configurations were found in the provided configuration.

### Stack Configuration
This device does not appear to be part of a stack.

### Redundant Links
There are no redundant link configurations explicitly mentioned.