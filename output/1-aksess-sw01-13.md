# Switch Configuration Documentation: 1-aksess-sw01-13.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: This switch is likely a management switch for the network, given its configuration and interfaces.
- **Last Modified**: Not specified in the config
- **Domain Name**: krister.local

## Device Information
- **Model**: Not available in this config snippet (refer to actual device documentation)
- **System Image**: Unknown (refer to actual device documentation)
- **Serial Number**: Not available in this config snippet (refer to actual device documentation)
- **Hardware Details**: Not specified in the config

## Management & Access

### Management Interfaces
The switch has a management VLAN (Vlan 90) with an IP address of 10.90.0.11/24 and is configured for SSH access.

#### Management VLAN Interface: Vlan90
- **IP Address**: 10.90.0.11/24
- **Description**: Management SVI
- **DHCP Helper**: Not configured
- **HSRP/VRRP**: Not configured

### Access Control & Security
The switch has an enable secret password, and there is a conditional fallback AAA configuration with TACACS+ as the primary method.

#### Enable Password
- **Status**: Enabled
- **Encryption Level**: 3 (AES/DES encryption)

#### AAA Configuration
- **TACACS+ Server**: Host 10.91.0.10 with key KompleksNoekkel
- **Local Users**: emergency-admin with privilege level 15

#### Console Access
- **Authentication Method**: Local users only (console line configured for local authentication)
- **Exec Timeout**: 10 minutes

#### VTY Access
- **Line Configuration**: vty lines 0 through 4 are enabled for SSH access, and the default authentication method is used.
- **Access Class Restrictions**: MGMT-MGMT ACL is applied to all vty lines.

### Management Access Lists
There is a standard management ACL (MGMT-MGMT) configured on this switch:

#### MGMT-MGMT ACL
| Sequence Number | Action | Source IP Address |
|-----------------|--------|--------------------|
| 10              | Permit | 10.90.0.0/24       |
| 20              | Permit | 10.91.0.0/24       |
| 30              | Deny   | Any                |

## VLANs

### VLAN Database
Here is the list of configured VLANs:

| VLAN ID | Name            | Purpose/Description           |
|---------|-----------------|-------------------------------|
| 11      | Usergroup1-1    | Users in group 1, VLAN 1       |
| 12      | Usergroup1-2    | Users in group 1, VLAN 2       |
| 90      | Admin-Mgmt-LEFT | Management VLAN for admin     |
| 666     | native-trunk   | Native trunk VLAN             |

### VLAN Interfaces (SVIs)
There is only one SVI configured on this switch:

#### Vlan90 Interface
- **IP Address**: 10.90.0.11/24
- **Description**: Management SVI
- **DHCP Helper**: Not configured
- **HSRP/VRRP**: Not configured

## Physical Interfaces

### Interface Summary
Here is the summary of all interfaces:

| Interface    | Description       | Mode          | VLAN/Trunk  | Speed/Duplex | Status        | Special Features                |
|--------------|-------------------|---------------|-------------|--------------|---------------|-------------------------------|
| Gig0/1       | dis-venstre-sw01   | Trunk         | Dot1Q       | auto         | Up            | None                            |
| Fa0/1        | PC4-Access port  | Access        | VLAN 11     | auto         | Up            | Port Security, STP, Storm Ctrl |
| Fa0/2        | PC5-Access port  | Access        | VLAN 12     | auto         | Up            | Port Security, STP, Storm Ctrl |
| Fa0/3        | Management-PC    | Access        | VLAN 90     | auto         | Up            | Port Security, STP             |
| Fa0/4-24     | Unused Ports      | Shutdown      | None        | auto         | Down          | None                            |
| Gi0/2        | Unused Gigabit   | Shutdown      | None        | auto         | Down          | None                            |

### Detailed Interface Configurations
Here are the detailed configurations for each interface:

#### GigabitEthernet0/1
- **Description**: dis-venstre-sw01 gig0/1
- **Mode**: Trunk (Dot1Q encapsulation)
- **VLAN Configuration**:
  - Native VLAN: 666
  - Allowed VLANs: 11, 12, 90

#### FastEthernet0/1
- **Description**: PC4-Access port
- **Mode**: Access (VLAN 11)
- **Port Security**:
  - Maximum MAC addresses allowed: 1
  - Violation action: Restrict
- **Storm Control**:
  - Broadcast threshold: 1.00

#### FastEthernet0/2
- **Description**: PC5-Access port
- **Mode**: Access (VLAN 12)
- **Port Security**:
  - Maximum MAC addresses allowed: 1
  - Violation action: Restrict
- **Storm Control**:
  - Broadcast threshold: 1.00

#### FastEthernet0/3
- **Description**: Management-PC Access port
- **Mode**: Access (VLAN 90)
- **Port Security**:
  - Maximum MAC addresses allowed: 1
  - Violation action: Restrict

## Port-Channel / EtherChannel
No Port-Channel or EtherChannel configurations were found in the config.

## Routing Configuration
There is no routing protocol configuration on this switch, but there are some static routes and a default route:

### Static Routes
| Destination | Next-hop |
|-------------|----------|
| 10.90.0.0/24| 10.90.0.254|

### Default Route
- **Configuration**: ip default-gateway 10.90.0.254

## Spanning Tree Protocol

### STP Configuration
- **Mode**: PVST+
- **Root Bridge**: Not configured as root for any VLANs
- **Priority**: Not specified in the config (default is 32768)

### STP Features
- **PortFast**: Enabled on Fa0/1, Fa0/2, and Fa0/3
- **BPDU Guard**: Not configured
- **Root Guard**: Not configured
- **Loop Guard**: Not configured
- **UDLD**: Not configured

## High Availability & Redundancy
No FHRP or Stack configurations were found in the config.

## Quality of Service (QoS)
There is no QoS configuration on this switch.

## Security Features

### Port Security
- **Interfaces with port security enabled**:
  - Fa0/1, Fa0/2, and Fa0/3 have port security configured
- **Maximum MAC addresses allowed**: 1 for all interfaces with port security enabled
- **Violation actions configured**: Restrict on all interfaces with port security enabled

### DHCP Security
- **DHCP Snooping**: Enabled (with ip dhcp snooping trust on Gig0/1 and ip arp inspection trust)
- **Trusted ports**: Gig0/1 is trusted for DHCP snooping

## Miscellaneous
The switch has a banner login message prohibiting unauthorized access.

---

This documentation was generated automatically from running-config, and it may not be complete or entirely accurate.