# Switch Configuration Documentation: 1-aksess-sw01.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: This switch appears to be a management switch for a network, providing access to the native VLAN and user groups. It also serves as an uplink trunk to another switch.
- **Last Modified**: Not specified in the configuration.
- **Domain Name**: krister.local

## Device Information
- **Model**: Not specified in the configuration.
- **System Image**: Boot image information is not available.
- **Serial Number**: Not specified in the configuration.
- **Hardware Details**: Not available.

## Management & Access

### Management Interfaces
#### Vlan90 Interface
- **Management VLAN and IP addressing**:
  - `ip address 10.90.0.11 255.255.255.0` on VLAN 90
  - `description Management SVI` on Vlan90 interface
- **Default gateway configuration**: Not available.
- **Management protocols enabled**: SSH version 2.

### Access Control & Security

#### Console Access
- **Console line configuration**: The console is enabled with a timeout of 10 minutes and logging synchronized.

#### VTY Access
- **Telnet/SSH configuration**:
  - `login authentication default` on all VTY lines.
  - `transport input ssh` allows only SSH connections to the switch.

#### Enable Password
- **Enable password**: The enable secret is set to `3NA8le$cret!=1`, encrypted.

#### AAA Configuration
- **Authentication/authorization/accounting setup**: This switch uses TACACS+ for authentication with a conditional fallback to local users. Authorization and accounting are also enabled for exec sessions.

#### Login Banners
- **Login banners**: A login banner is set to display "Unauthorized access prohibited."

### Management Access Lists

#### MGMT-MGMT ACL
- **ACL applied to management access**:
  - `ip access-list standard MGMT-MGMT` defines the ACL.
  - `permit 10.90.0.0 0.0.0.255` and `permit 10.91.0.0 0.0.0.255` allow traffic from these networks.

## Device Information

### Model
- **Model**: This information is not provided in the configuration file.

### System Image
- **System image**: The system image is unknown since the IOS version is not specified.

### Serial Number
- **Serial number**: This information is not available in the configuration file.

### Hardware Details
- **Hardware details**: There are no specific hardware-related configurations mentioned in this switch configuration.

## Management & Access

### Management Interfaces

#### Management VLAN and IP Addressing
- **Management VLAN and IP addressing**:
  - `interface Vlan90` defines a management VLAN.
  - `ip address 10.90.0.11 255.255.255.0` assigns an IP address to the interface.

#### Default Gateway Configuration
- **Default gateway configuration**: The default gateway is set to `10.90.0.254`.

#### Management Protocols Enabled
- **Management protocols enabled**:
  - SSH version 2 is enabled.
  - NTP authentication and timezone are configured, but no specific details are available.

### Access Control & Security

#### Console Access
- **Console access**: The console line configuration includes `login authentication console` for local login.

#### VTY Access
- **VTY access**:
  - `line vty 0 4` defines the VTY lines.
  - `login authentication default` specifies the authentication method.

#### Enable Password
- **Enable password**: The enable secret is set to a strong password (`3NA8le$cret!=1`).

#### AAA Configuration
- **AAA configuration**:
  - TACACS+ server is configured with host `10.91.0.10` and key `KompleksNoekkel`.
  - Authentication for login, exec, and accounting are specified using the TACACS+ group.

#### Login Banners
- **Login banners**: A login banner (`^CUnauthorized access prohibited.^C`) is configured to prevent unauthorized access.

### Management Access Lists

#### MGMT-MGMT ACL
- **MGMT-MGMT ACL**:
  - `ip access-list standard MGMT-MGMT` defines a standard ACL.
  - `permit 10.90.0.0 0.0.0.255` and `permit 10.91.0.0 0.0.0.255` allow specific IP addresses.

## Device Information

### Model
Unknown (not specified in the configuration)

### System Image
Unknown (not specified in the configuration)

### Serial Number
Unknown (not specified in the configuration)

### Hardware Details
No hardware details are provided in the configuration.

## Management & Access

### Management Interfaces

#### Management VLAN and IP Addressing
- **Management VLAN**: The management VLAN is configured on interface `Vlan90`.
- **IP Addressing**: The IP address for `Vlan90` is set to `10.90.0.11/24`.

#### Default Gateway Configuration
- **Default Gateway**: The default gateway is specified as `10.90.0.254`.

### Access Control & Security

#### AAA Configuration (continued)
- **AAA Authorization and Accounting**: Authorization for exec access and accounting are specified using the TACACS+ group.

## VLANs

### VLAN Database

| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      | Usergroup1-1 | User VLAN         |
| 12      | Usergroup1-2 | User VLAN         |
| 90      | Admin-Mgmt-LEFT | Management VLAN    |
| 666     | native-trunk | Native VLAN        |

### VLAN Interfaces (SVIs)

#### Vlan90 Interface
- **VLAN ID**: 90
- **IP Address**: `10.90.0.11/24`
- **Description**: "Management SVI"
- **DHCP Helper**: Not configured

## Physical Interfaces

### Interface Summary

| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| GigabitEthernet0/1 | dis-venstre-sw01 gig0/1 | Trunk | 11,12,90 | full-duplex | up |   |
| FastEthernet0/1 | PC4-Access port | Access | 11 | auto-negotiate | up | Port Security, STP |
| FastEthernet0/2 | PC5-Access port | Access | 12 | auto-negotiate | up | Port Security, STP |
| FastEthernet0/3 | Management-PC Access port | Access | 90 | auto-negotiate | up | Port Security, STP |

### Detailed Interface Configurations

#### GigabitEthernet0/1
- **Description**: "dis-venstre-sw01 gig0/1"
- **Mode**: Trunk
- **Configuration Details**:
  - `switchport trunk encapsulation dot1q`
  - `switchport mode trunk`
  - `switchport nonegotiate`
  - `switchport trunk native vlan 666`
  - `switchport trunk allowed vlan 11,12,90`

#### FastEthernet0/1
- **Description**: "PC4-Access port"
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 11`
  - `switchport port-security`
  - `switchport port-security maximum 1`
  - `switchport port-security violation restrict`

#### FastEthernet0/2
- **Description**: "PC5-Access port"
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 12`
  - `switchport port-security`
  - `switchport port-security maximum 1`
  - `switchport port-security violation restrict`

#### FastEthernet0/3
- **Description**: "Management-PC Access port"
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 90`
  - `switchport port-security`
  - `switchport port-security maximum 1`
  - `switchport port-security violation restrict`

## Best Practices Analysis

### ✅ Good Practices Identified

* The switch uses a meaningful VLAN naming convention.
* Port Security is enabled on all access ports to prevent unauthorized devices from connecting.
* STP (Spanning Tree Protocol) is enabled on all interfaces for network redundancy and loop prevention.

### ⚠️ Potential Issues or Concerns

* The `ip address` command is used without specifying a subnet mask. It's recommended to use the full IP address with a subnet mask, such as "ip address 10.90.0.11 255.255.255.0".
* There are multiple interfaces configured for DHCP Snooping and DAI (Dynamic ARP Inspection) without any specific VLANs mentioned. Make sure these settings are correctly applied to the corresponding VLANs.
* The switch is configured with a management interface (Vlan90) but there's no clear indication of its purpose or how it's being used.

### 💡 Recommendations for Improvement

1. **Verify the `ip address` command syntax** by checking if the subnet mask is correctly specified and applied across all interfaces.
2. **Review DHCP Snooping and DAI configurations** to ensure these settings are accurately applied to their respective VLANs.
3. **Document management interface (Vlan90) purpose** to improve overall clarity and maintainability.

## Configuration Summary

* **Total VLANs**: 6
* **Total Configured Interfaces**: 8
* **Routing**: Enabled using OSPF (Open Shortest Path First)
* **Spanning Tree**: PVST+ mode with root bridge status for certain VLANs.
* **Key Features Enabled**:
	+ DHCP Snooping and DAI on multiple VLANs
	+ Port Security enabled on various interfaces
	+ Storm Control configured with broadcast/multicast/unicast thresholds
* **Security Posture**: Good security posture overall, but potential issues mentioned above.

## Appendix

### Uncommon or Complex Configurations

The configuration includes some uncommon settings such as:

* `crypto key generate rsa general-keys modulus 2048` - Generates an RSA key pair with a 2048-bit modulus for secure SSH connections.
* `ip dhcp snooping verify mac-address` - Enables the verification of MAC addresses in DHCP packets to prevent spoofing attacks.

These configurations are documented here for clarity and reference purposes.