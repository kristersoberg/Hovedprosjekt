# Switch Configuration Documentation: SAMPLE-SWITCH.txt

## Overview
- **Hostname**: CORE-SWITCH-01
- **IOS Version**: 15.2
- **Configuration Purpose**: Core switch for the network, likely providing connectivity between various parts of the infrastructure.
- **Last Modified**: Mon Nov 25 2024 10:30:45 UTC
- **Domain Name**: example.local

## Device Information
- **Model**: Not specified in the configuration file. To determine the model, you would need access to the actual device or its documentation.
- **System Image**: Not specified in the configuration file. However, based on the IOS version (15.2), it is likely that the switch runs on a standard Cisco 3750 series or similar hardware.
- **Serial Number**: Not available from the configuration file.
- **Hardware Details**: Not specified.

## Management & Access

### Management Interfaces
The management VLAN and IP addressing are configured as follows:

- **Management VLAN (VLAN 10)**:
  - **Name**: MANAGEMENT
  - **IP Address**: 192.168.10.1/24
  - **Description**: MANAGEMENT VLAN

- **Default Gateway**:
  - **Gateway IP**: 192.168.10.254

- **Management Protocols Enabled**:
  - SSH (version 2)
  - HTTP server and secure-server enabled

### Access Control & Security
- **Console Access**: 
  - Configuration of console line: `line con 0`
    - Exec-timeout set to 5 minutes with no idle timeout (`exec-timeout 5 0`)
    - Logging synchronous enabled for console output (`logging synchronous`)

- **VTY Access**:
  - Line configuration: `line vty 0 4` and `line vty 5 15`
    - Exec-timeout set to 10 minutes with no idle timeout (`exec-timeout 10 0`)
    - Logging synchronous enabled for VTY output (`logging synchronous`)
    - Access-class restriction applied (`access-class 10 in`)
    - SSH transport input allowed (`transport input ssh`)

- **Enable Password**:
  - Configuration of enable password: `enable secret`
    - Encryption level set to strong encryption (`5 $1$mERr$hx5rVt7rPNoS4wqbXKX7m0`)
  - Status and encryption level: Strongly encrypted

- **AAA Configuration**: Not configured.

- **Login Banners**: None configured.

## Management Access Lists
### ACL 10:
- **Purpose**: Restrict access to the management VLAN
- **Type**: Standard/Extended: Standard
- **Rules**:
  - `permit 192.168.10.0 0.0.255` (allow traffic on the management VLAN)
  - `deny   any log` (deny all other traffic and log attempts)

### Applied to: VTY lines

## VLANs
### VLAN Database

| VLAN ID | Name          | Purpose/Description                                  |
|---------|---------------|------------------------------------------------------|
| 10      | MANAGEMENT    | Management VLAN for network administrators          |
| 20      | SERVERS       | VLAN for production servers                           |
| 30      | WORKSTATIONS  | VLAN for office users                                 |
| 40      | GUEST         | Guest VLAN                                             |
| 99      | NATIVE_VLAN   | Native VLAN for trunking                             |

### VLAN Interfaces (SVIs)
#### VLAN 10 Interface
- **IP Address**: `192.168.10.1/24`
- **Description**: Management VLAN interface
- **DHCP Helper**: Not configured

#### VLAN 20 Interface
- **IP Address**: `192.168.20.1/24`
- **Description**: Server VLAN interface
- **DHCP Helper**: `192.168.10.50`

#### VLAN 30 Interface
- **IP Address**: `192.168.30.1/24`
- **Description**: Workstation VLAN interface
- **DHCP Helper**: `192.168.10.50`

#### VLAN 40 Interface
- **IP Address**: `192.168.40.1/24`
- **Description**: Guest VLAN interface
- **DHCP Helper**: `192.168.10.50`

### VTP Configuration
- **VTP Mode**: Transparent
- **VTP Domain**: Not configured (default domain name is used)
- **VTP Version**: 3 (latest supported version)

## Physical Interfaces

### Interface Summary

| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| Gi0/1    | Uplink to core router | Trunk | 99,10-40   | Auto          | Up     | STP enabled      |
| Gi0/2    | Server VLAN - Production server | Access | 20         | 1000         | Up     | PortFast enabled  |
| Gi0/3    | Workstation VLAN - Office users | Access | 30         | 1000         | Up     | Port security, BPDU guard |
| Gi0/4    | Guest network          | Access | 40         | 1000         | Up     |                    |
| Gi0/5    | Etherchannel to distribution switch | Trunk | 10-30      | Auto          | Up     | STP enabled, Etherchannel member|
| Gi0/6    | Etherchannel to distribution switch | Trunk | 10-30      | Auto          | Up     | STP enabled, Etherchannel member|
| Gi0/7    | Shutdown                         | Access | -         |               | Down   |
| Gi0/8    | Shutdown                         | Access | -         |               | Down   |
| Port-channel1 | LACP bundle to distribution switch | Trunk | 10-30      | Auto          | Up     |

## Physical Interfaces

### Interface Summary
| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| Gi0/1    | Uplink to core router  | Trunk | -         | Auto          | Up     |                    |
| Gi0/2    | Server VLAN - Production server   | Access | 20        | 1000         | Up     | PortFast enabled, BPDU guard|
| Gi0/3    | Workstation VLAN - Office Users  | Access | 30       | 1000          | Up     | Port-security max 3, restrict mode, port-security |
| Gi0/4    | Guest Network             | Access | 40      | 1000         | Up     |                    |
| Gi0/5    | Etherchannel to distribution switch   | Trunk | -        | Auto          | Up     | Channel-group 1 active|
| Gi0/6    | Etherchannel to distribution switch  | Trunk | -       | Auto            | Up     | Channel-group 1 active|
| Gi0/7    | Shutdown                          | Access | -      |               | Down   |
| Gi0/8    | Shutdown                          | Access | -        |              | Down   |
| Port-channel1 | LACP bundle to distribution       | Trunk | -          | Auto           | Up     |

## Switch Configuration Documentation: SAMPLE-SWITCH.txt

### Overview
- **Hostname**: CORE-SWITCH-01
- **IOS Version**: 15.2
- **Configuration Purpose**: This configuration is likely for a core switch in a network infrastructure, handling management VLANs and server traffic.
- **Last Modified**: Last configuration change was at 10:30:45 UTC Mon Nov 25 2024
- **Domain Name**: example.local

### Device Information
- **Model**: Not explicitly mentioned but based on the IOS version, it could be a Cisco Catalyst switch (e.g., 6500 or 4500 series).
- **System Image**: Boot image information not provided in the configuration.
- **Serial Number**: Not available in this configuration.
- **Hardware Details**: The configuration mentions Gigabit Ethernet ports and Port-channel interfaces, suggesting a modern hardware setup with multiple interfaces.

### Management & Access

#### Management Interfaces
The management VLAN and IP addressing are configured as follows:

*   Management VLAN (VLAN 10):
    *   Description: MANAGEMENT VLAN
    *   IP Address: 192.168.10.1/24
*   Default Gateway Configuration:
    *   IP default-gateway 192.168.10.254

Management protocols enabled:

*   SSH version 2 is configured for secure management access.

#### Access Control & Security

##### Console Access

The console line configuration is set to enable password encryption and restrict access with an exec-timeout of 5 minutes.

```bash
line con 0
exec-timeout 5 0
```

The enable secret password is encrypted, but its value cannot be retrieved directly from the provided configuration. The enable secret command is used to encrypt the password.

#### VTY Access

Telnet/SSH access is restricted by configuring an access class (ACL) on VTY lines and enabling SSH version 2:

```bash
line vty 0 4
access-class 10 in
exec-timeout 10 0
login local
transport input ssh
```

Line configuration, including the access class restrictions, is documented below.

##### Access Class

The access class (ACL) is configured as follows:

*   ACL 10:
    *   Permit IP address range: 192.168.10.0/24
    *   Deny all other traffic with a log message

```bash
access-list 10 permit 192.168.10.0 0.0.0.255
access-list 10 deny any log
```

#### AAA Configuration

No AAA (Authentication, Authorization, and Accounting) configuration is present in the provided switch configuration.

### Login Banners

No login banners are configured on the device.

## VLANs

### VLAN Database

| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 10      | MANAGEMENT | Management VLAN for network management |
| 20      | SERVERS    | Server VLAN for production servers |
| 30      | WORKSTATIONS | Workstation VLAN for office users |
| 40      | GUEST      | Guest VLAN for guest network access |
| 99      | NATIVE_VLAN | Native VLAN (default) |

### VLAN Interfaces (SVIs)

#### VLAN 10 Interface
- **VLAN ID**: 10
- **IP Address**: 192.168.10.1/24
- **Description**: Management VLAN for network management
- **DHCP Helper**: Not configured
- **HSRP/VRRP**: Not configured

#### VLAN 20 Interface
- **VLAN ID**: 20
- **IP Address**: 192.168.20.1/24
- **Description**: Server VLAN for production servers
- **DHCP Helper**: Yes, with address 192.168.10.50
- **HSRP/VRRP**: Not configured

#### VLAN 30 Interface
- **VLAN ID**: 30
- **IP Address**: 192.168.30.1/24
- **Description**: Workstation VLAN for office users
- **DHCP Helper**: Yes, with address 192.168.10.50
- **HSRP/VRRP**: Not configured

#### VLAN 40 Interface
- **VLAN ID**: 40
- **IP Address**: 192.168.40.1/24
- **Description**: Guest VLAN for guest network users
- **DHCP Helper**: Yes, with address 192.168.10.50
- **HSRP/VRRP**: Not configured

#### VLAN 99 Interface
- **VLAN ID**: 99
- **IP Address**: N/A (Native VLAN)
- **Description**: Native VLAN for trunking
- **DHCP Helper**: Not applicable
- **HSRP/VRRP**: Not configured

## Physical Interfaces

### Interface Summary

| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| GigabitEthernet0/1    | UPLINK TO CORE ROUTER | Trunk | 99,10-40   | Not Specified | Up     | 802.1Q trunking |
| GigabitEthernet0/2    | SERVER VLAN - Production Server | Access | 20          | Not Specified | Up     | PortFast enabled |
| GigabitEthernet0/3    | WORKSTATION VLAN - Office Users | Access | 30          | Not Specified | Up     | PortSecurity enabled |
| GigabitEthernet0/4    | GUEST NETWORK        | Access | 40          | Not Specified | Up     | PortFast enabled |
| GigabitEthernet0/5    | ETHERCHANNEL TO DISTRIBUTION SWITCH | Trunk | 10-30       | Not Specified | Up     | EtherChannel member |
| GigabitEthernet0/6    | ETHERCHANNEL TO DISTRIBUTION SWITCH | Trunk | 10-30       | Not Specified | Up     | EtherChannel member |
| GigabitEthernet0/7    | Shutdown                | -      | -           | Not Specified | Down   | -                  |
| GigabitEthernet0/8    | Shutdown                | -      | -           | Not Specified | Down   | -                  |

## Physical Interfaces

### Detailed Interface Configurations

#### GigabitEthernet0/1
- **Description**: UPLINK TO CORE ROUTER
- **Mode**: Trunk
- **Configuration Details**:
  - `switchport trunk encapsulation dot1q`
  - `switchport trunk allowed vlan 10,20,30,40`
  - `channel-group 1 mode active`

#### GigabitEthernet0/2
- **Description**: SERVER VLAN - Production Server
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 20`
  - `spanning-tree portfast`
  - `spanning-tree bpduguard enable`

#### GigabitEthernet0/3
- **Description**: WORKSTATION VLAN - Office Users
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 30`
  - `switchport port-security maximum 3`
  - `switchport port-security violation restrict`
  - `spanning-tree portfast`
  - `spanning-tree bpduguard enable`

#### GigabitEthernet0/4
- **Description**: GUEST NETWORK
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 40`
  - `spanning-tree portfast`

#### GigabitEthernet0/5, GigabitEthernet0/6
- **Description**: ETHERCHANNEL TO DISTRIBUTION SWITCH
- **Mode**: Trunk
- **Configuration Details**:
  - `switchport trunk encapsulation dot1q`
  - `channel-group 1 mode active`

## VLAN Database

| VLAN ID | Name         | Purpose/Description          |
|---------|--------------|------------------------------|
| 10      | MANAGEMENT   | Management network           |
| 20      | SERVERS      | Server VLAN                  |
| 30      | WORKSTATIONS | Workstation VLAN             |
| 40      | GUEST        | Guest VLAN                   |
| 99      | NATIVE_VLAN | Native VLAN for trunking     |

## VLAN Interfaces (SVIs)

### VLAN 10 Interface

* IP Address: `192.168.10.1/24`
* Description: MANAGEMENT VLAN
* DHCP Helper: Not configured
* HSRP/VRRP: Not configured

### VLAN 20 Interface

* IP Address: `192.168.20.1/24`
* Description: SERVER VLAN
* DHCP Helper: Yes, helper address is `192.168.10.50`

### VLAN 30 Interface

* IP Address: `192.168.30.1/24`
* Description: WORKSTATION VLAN
* DHCP Helper: Yes, helper address is `192.168.10.50`

### VLAN 40 Interface

* IP Address: `192.168.40.1/24`
* Description: GUEST VLAN
* DHCP Helper: Yes, helper address is `192.168.10.50`

## Physical Interfaces

### Interface Summary Table

| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| GigE0/1   | UPLINK TO CORE ROUTER | Trunk | 99,10-40    | Auto          | Up     | Dot1q trunking   |
| GigE0/2   | SERVER VLAN - Production Server | Access | 20           | Auto          | Up     | PortFast        |
| GigE0/3   | WORKSTATION VLAN - Office Users | Access | 30           | Auto          | Up     | Port Security   |
| GigE0/4   | GUEST NETWORK | Access | 40           | Auto          | Up     |                  |
| GigE0/5   | ETHERCHANNEL TO DISTRIBUTION SWITCH | Trunk | 10-30        | Auto          | Up     | LACP            |
| GigE0/6   | ETHERCHANNEL TO DISTRIBUTION SWITCH | Trunk | 10-30        | Auto          | Up     | LACP            |
| GigE0/7   | Shutdown | -      |              | -             | Down   |                  |
| GigE0/8   | Shutdown | -      |              | -             | Down   |                  |

## VLANs

### VLAN Database

| VLAN ID | Name         | Purpose/Description            |
|---------|--------------|-------------------------------|
| 10      | MANAGEMENT   | Management VLAN               |
| 20      | SERVERS      | Servers VLAN                   |
| 30      | WORKSTATIONS | Workstations VLAN              |
| 40      | GUEST        | Guest Network VLAN             |
| 99      | NATIVE_VLAN  | Native VLAN for trunk ports    |

### VLAN Interfaces (SVIs)

#### Vlan10 Interface
- **VLAN ID**: 10
- **IP Address**: 192.168.10.1/24
- **Description**: MANAGEMENT VLAN
- **DHCP Helper**: Not configured

#### Vlan20 Interface
- **VLAN ID**: 20
- **IP Address**: 192.168.20.1/24
- **Description**: SERVERS VLAN
- **DHCP Helper**: Enabled with address 192.168.10.50

#### Vlan30 Interface