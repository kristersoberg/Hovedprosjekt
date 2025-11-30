# Switch Configuration Documentation: 1-aksess-sw01-2.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown (not specified)
- **Configuration Purpose**: This switch is likely a network access layer device, providing access to various VLANs and management interfaces.
- **Last Modified**: Not available in the configuration file.
- **Domain Name**: krister.local

## Device Information
- **Model**: Not explicitly stated; based on the features enabled, this could be a Cisco Catalyst 3850 or similar.
- **System Image**: Unknown (not specified)
- **Serial Number**: Not available in the configuration file.
- **Hardware Details**: The switch has multiple Gigabit Ethernet and Fast Ethernet ports.

## Management & Access

### Management Interfaces
The management VLAN is configured as VLAN 90 with IP address 10.90.0.11/24.

- **Management VLAN and IP addressing**:
    - VLAN 90: name "Admin-Mgmt-LEFT", IP address 10.90.0.11/24, access-group MGMT-MGMT in
    - Default gateway configuration: ip default-gateway 10.90.0.254

- **Default gateway configuration**: The default gateway is set to 10.90.0.254.
- **Management protocols enabled**:
    - SSH version 2 (ip ssh version 2)
    - SSH authentication retries limited to 3 (ip ssh authentication-retries 3)

### Access Control & Security
- **Console Access**: Console access is configured with local authentication.
    - Console line configuration: line con 0, login authentication console, exec-timeout 10 0
- **VTY Access**: Telnet/SSH access is enabled on VTY lines 0 through 4.
    - Line configuration: line vty 0 4, login authentication default, transport input ssh
    - Access class restrictions: access-class MGMT-MGMT in
- **Enable Password**: The enable secret password is set to "3NA8le$cret!=1".
- **AAA Configuration**: TACACS+ server is configured for authentication and accounting.
    - AAA configuration: aaa new-model, tacacs-server host 10.91.0.10 key KompleksNoekkel
    - Authentication methods:
        + Default method group: aaa authentication login default group tacacs+ local
        + Console authentication method: aaa authentication login console local
        + Authorization method for exec sessions: aaa authorization exec default group tacacs+ local
- **Login Banners**: Unauthorized access is prohibited.
    - Login banner configuration: banner login ^CUnauthorized access prohibited.^C

### Management Access Lists
- **Management ACLs**:
    + MGMT-MGMT ACL is configured to permit only specific IP addresses for management access.
        * Permit 10.90.0.0/24 and 10.91.0.0/24 in the MGMT-MGMT ACL.

## VLANs

### VLAN Database
| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      | Usergroup1-1 | Access port for PC4 |
| 12      | Usergroup1-2 | Access port for PC5 |
| 90      | Admin-Mgmt-LEFT | Management SVI VLAN |
| 666     | native-trunk | Native VLAN for trunk ports |

### VLAN Interfaces (SVIs)
#### Vlan90 Interface
- **VLAN ID**: 90
- **IP Address**: 10.90.0.11/24
- **Description**: Management SVI
- **DHCP Helper**: Not configured
- **HSRP/VRRP**: Not configured
- Additional settings:
    + IP access-group MGMT-MGMT in

## Physical Interfaces

### Interface Summary
| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status |
|-----------|-------------|------|------------|--------------|--------|
| GigabitEthernet0/1  | dis-venstre-sw01 gig0/1   | Trunk    | 11,12,90     | Unknown        | Up     |
| FastEthernet0/1    | PC4-Access port       | Access   | 11           | Unknown        | Up     |
| FastEthernet0/2    | PC5-Access port       | Access   | 12           | Unknown        | Up     |
| FastEthernet0/3    | Management-PC Access port    | Access   | 90           | Unknown        | Up     |

### Detailed Interface Configurations

#### GigabitEthernet0/1
- **Mode**: Trunk
- **Configuration Details**:
    - switchport trunk encapsulation dot1q
    - switchport mode trunk
    - switchport nonegotiate
    - switchport trunk native vlan 666
    - switchport trunk allowed vlan 11,12,90
    + ip dhcp snooping trust
    + ip arp inspection trust

#### FastEthernet0/1
- **Mode**: Access
- **Configuration Details**:
    - switchport mode access
    - switchport access vlan 11
    - switchport port-security
    - switchport port-security maximum 1 
    - switchport port-security violation restrict
    - switchport port-security aging time 3
    - switchport port-security mac-address sticky
    + ip dhcp snooping limit rate 15
    + spanning-tree portfast
    + spanning-tree bpduguard enable
    + storm-control broadcast level 1.00

#### FastEthernet0/2
- **Mode**: Access
- **Configuration Details**:
    - switchport mode access 
    - switchport access vlan 12
    - switchport port-security
    - switchport port-security maximum 1 
    - switchport port-security violation restrict
    - switchport port-security aging time 3
    - switchport port-security mac-address sticky
    + ip dhcp snooping limit rate 15
    + spanning-tree portfast
    + spanning-tree bpduguard enable
    + storm-control broadcast level 1.00

#### FastEthernet0/3
- **Mode**: Access
- **Configuration Details**:
    - switchport mode access 
    - switchport access vlan 90
    - switchport port-security
    - switchport port-security maximum 1 
    - switchport port-security violation restrict
    - switchport port-security aging time 3
    - switchport port-security mac-address sticky
    + spanning-tree portfast
    + spanning-tree bpduguard enable
    + storm-control broadcast level 1.00

## Device Information

### Hostname
- **Hostname**: aksess-sw01

### IOS Version
- **IOS Version**: Unknown (running-config is required for accurate version detection)

### Configuration Purpose
- **Configuration Purpose**: The switch appears to be a core or aggregation layer device, handling multiple VLANs and providing connectivity to various devices and networks.

## Management & Access

### Management Interfaces
- **Management VLAN and IP addressing**:
  - `interface Vlan90`: This is the management VLAN (VLAN 90) with an IP address of `10.90.0.11/24`.
- **Default gateway configuration**:
  - `ip default-gateway 10.90.0.254`: The default gateway for this switch is set to `10.90.0.254`.

### Access Control & Security
- **Console Access**:
  - The console line (`line con 0`) is configured with authentication using the `console` AAA group.
- **VTY Access**:
  - VTY access is enabled on lines 0 through 4, and SSH version 2 is specified as the transport protocol.
  - `login authentication default`: Authentication for VTY access uses the `default` AAA group.
- **Enable Password**:
  - The enable secret password (`enable secret`) is set to `3NA8le$cret!=1`, which is encrypted.

### AAA Configuration
- The switch is configured with a TACACS+ server (`tacacs-server host 10.91.0.10 key KompleksNoekkel`), and authentication/authorization/accounting settings are defined for various contexts.
- **AAA Authentication**:
  - `aaa authentication login default group tacacs+ local`: The default AAA authentication method is set to use TACACS+ as the primary source, with local authentication as a fallback.
- **AAA Authorization**:
  - `aaa authorization exec default group tacacs+ local`: AAA authorization for EXEC commands uses TACACS+ and local sources.
- **AAA Accounting**:
  - `aaa accounting exec default start-stop group tacacs+`: AAA accounting for EXEC commands is enabled.

### Login Banners
- A login banner has been configured: `banner login ^CUnauthorized access prohibited.^C`

## VLAN Database

| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      | Usergroup1-1 | User group VLAN |
| 12      | Usergroup1-2 | User group VLAN |
| 90      | Admin-Mgmt-LEFT | Management VLAN for left admin network |
| 666     | native-trunk | Native trunk VLAN |

### VLAN Interfaces (SVIs)

#### Vlan90 Interface
- **VLAN 90 Interface**: `interface Vlan90`
- IP Address: `10.90.0.11/255.255.255.0`
- Description: `Management SVI`
- DHCP Helper: Not configured
- HSRP/VRRP: Not configured

## Physical Interfaces

### Interface Summary

| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| GigabitEthernet0/1    | dis-venstre-sw01 gig0/1        | trunk     | 11,12,90   | auto       | up          | DSCP, STP, Port Security |
| FastEthernet0/1      | PC4-Access port            | access   | 11         | auto       | up          | Port Security, Storm Control |
| FastEthernet0/2      | PC5-Access port            | access   | 12         | auto       | up          | Port Security, Storm Control |
| FastEthernet0/3      | Management-PC Access port        | access   | 90         | auto       | up          | Port Security, Storm Control |

### Detailed Interface Configurations

#### GigabitEthernet0/1
- **Description**: `dis-venstre-sw01 gig0/1`
- **Mode**: Trunk
- **Configuration Details**:
  - `switchport trunk encapsulation dot1q`
  - `switchport mode trunk`
  - `switchport nonegotiate`
  - `switchport trunk native vlan 666`
  - `switchport trunk allowed vlan 11,12,90`
  - `ip dhcp snooping trust`
  - `ip arp inspection trust`

#### FastEthernet0/1
- **Description**: `PC4-Access port`
- **Mode**: Access
- **Configuration Details**:
  - `switchport mode access`
  - `switchport access vlan 11`
  - `switchport port-security`
  - `switchport port-security maximum 1 `
  - `switchport port-security violation restrict`
  - `switchport port-security aging time 3`
  - `switchport port-security mac-address sticky`
  - `ip dhcp snooping limit rate 15`
  - `spanning-tree portfast`
  - `spanning-tree bpduguard enable`
  - `storm-control broadcast level 1.00`

#### FastEthernet0/2
- **Description**: `PC5-Access port`
- **Mode**: Access
- **Configuration Details**:
  - `switchport mode access`
  - `switchport access vlan 12`
  - `switchport port-security`
  - `switchport port-security maximum 1 `
  - `switchport port-security violation restrict`
  - `switchport port-security aging time 3`
  - `switchport port-security mac-address sticky`
  - `ip dhcp snooping limit rate 15`
  - `spanning-tree portfast`
  - `spanning-tree bpduguard enable`
  - `storm-control broadcast level 1.00`

#### FastEthernet0/3
- **Description**: `Management-PC Access port`
- **Mode**: Access
- **Configuration Details**:
  - `switchport mode access`
  - `switchport access vlan 90`
  - `switchport port-security`
  - `switchport port-security maximum 1 `
  - `switchport port-security violation restrict`
  - `switchport port-security aging time 3`
  - `switchport port-security mac-address sticky`
  - `spanning-tree portfast`
  - `spanning-tree bpduguard enable`
  - `storm-control broadcast level 1.00`

## Switch Configuration Documentation: 1-aksess-sw01-2.txt

## Overview
### Hostname
 aksess-sw01
### IOS Version
 Unknown
### Configuration Purpose
This switch is likely a core or distribution layer switch, providing connectivity and services to various network segments.
### Last Modified
2025-11-30T20:29:04.502461 (automatically generated timestamp)
### Domain Name
 krister.local

## Device Information
### Model
Not specified in the configuration, but based on the features and commands used, it is likely a Cisco Catalyst switch series.
### System Image
 Boot image information not available.
### Serial Number
Not provided in the configuration.
### Hardware Details
 Not specified.

## Management & Access

### Management Interfaces
#### Management VLAN and IP Addressing
- **VLAN 90**: Management SVI with IP address 10.90.0.11/24.
- Default gateway is set to 10.90.0.254.
- No DHCP helper configuration is found.

#### VTY (Telnet/SSH) Access
- **VTY Line Configuration**:
    - Login authentication uses the default group "tacacs+" followed by local authentication.
    - Transport input is limited to SSH only.
    - An access class restriction using ACL MGMT-MGMT is applied.
- **Console Access**: Console line configuration allows authentication using the "console" group, which is set to use local authentication.

#### Enable Password
The enable secret password is set to 3NA8le$cret!=1 and is encrypted.

### AAA Configuration
Authentication, Authorization, and Accounting (AAA) services are enabled with TACACS+ as the primary method. Local authentication is used as a fallback.

- **TACACS+ Server**:
    - Host: 10.91.0.10
    - Key: KompleksNoekkel

### Login Banners
A login banner is configured, stating "Unauthorized access prohibited."

## Management Access Lists
#### MGMT-MGMT ACL
This standard ACL permits traffic from the networks 10.90.0.0/24 and 10.91.0.0/24.

```
ip access-list standard MGMT-MGMT
 permit 10.90.0.0 0.0.0.255
 permit 10.91.0.0 0.0.0.255
 deny   any
```

## VLANs

### VLAN Database

| VLAN ID | Name        | Purpose/Description          |
|---------|-------------|------------------------------|
| 11      | Usergroup1-1| User group 1, VLAN 1         |
| 12      | Usergroup1-2| User group 1, VLAN 2         |
| 90      | Admin-Mgmt-LEFT | Management SVI             |
| 666     | native-trunk| Native VLAN for trunk ports |

### VLAN Interfaces (SVIs)

#### Vlan90 Interface
- **VLAN 90 Interface**:
    - IP Address: 10.90.0.11/24
    - Description: Management SVI
    - DHCP Helper: Not configured
    - HSRP/VRRP: Not configured

## Physical Interfaces

### Interface Summary

| Interface | Description         | Mode   | VLAN/Trunk | Speed/Duplex | Status  | Special Features          |
|-----------|---------------------|--------|------------|--------------|---------|---------------------------|
| Gi0/1    | dis-venstre-sw01 gig0/1 | trunk  | 11,12,90   | Auto/Auto    | Up      | Switchport trunk encapsulation dot1q |
| Fa0/1    | PC4-Access port     | access | 11         | Auto/Auto    | Up      | Port-security enabled       |
| Fa0/2    | PC5-Access port     | access | 12         | Auto/Auto    | Up      | Port-security enabled       |
| Fa0/3    | Management-PC Access port | access | 90         | Auto/Auto    | Up      | Spanning-tree portfast enabled |

### Detailed Interface Configurations

#### Gi0/1
- **Description**: Uplink trunk to distribusjon-venstre-sw01
- **Mode**: Trunk
- **Configuration Details**:
  - Switchport trunk encapsulation dot1q
  - Switchport mode trunk
  - Switchport nonegotiate
  - Switchport trunk native vlan 666
  - Switchport trunk allowed vlan 11,12,90

#### Fa0/1
- **Description**: PC4-Access port
- **Mode**: Access
- **Configuration Details**:
  - Switchport access vlan 11
  - Port-security enabled (maximum 1 mac-address)
  - Spanning-tree portfast enabled

#### Fa0/2
- **Description**: PC5-Access port
- **Mode**: Access
- **Configuration Details**:
  - Switchport access vlan 12
  - Port-security enabled (maximum 1 mac-address)
  - Spanning-tree portfast enabled

## Routing Configuration

### Static Routes
List all static routes:

| Destination | Next-hop |
|-------------|----------|
| 0.0.0.0/24  | 10.90.0.254 |

### Default Route
- **Configuration**: ip default-gateway 10.90.0.254
- **Next-hop**: 10.90.0.254

## Spanning Tree Protocol

### STP Configuration
- **Mode**: PVST+
- **Root Bridge**: No
- **Priority**: Priority values not specified

### STP Features
- **PortFast**: Enabled on several interfaces (e.g., Fa0/1, Fa0/2)
- **BPDU Guard**: Disabled
- **Root Guard**: Not configured
- **Loop Guard**: Not configured
- **UDLD