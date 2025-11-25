# Switch Configuration Documentation: 1-aksess-sw01.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: This switch is likely a core switch in the network, responsible for providing connectivity and management services.
- **Last Modified**: Not available from the configuration
- **Domain Name**: krister.local

## Device Information
- **Model**: Not available
- **System Image**: Boot image information not available
- **Serial Number**: Not available
- **Hardware Details**: No hardware-related info is available in the configuration.

## Management & Access

### Management Interfaces
- **Management VLAN and IP addressing**:
  - Interface Vlan90 (SVI) has an IP address of 10.90.0.11/24.
  - This interface also applies the management ACL MGMT-MGMT.
- **Default gateway configuration**: The default gateway is set to 10.90.0.254.
- **Management protocols enabled**: SSH version 2 is enabled, and there is no indication of any other management protocols.

### Access Control & Security
- **Console Access**:
  - Console access is configured for local authentication only.
  - The console timeout is set to 10 seconds with a maximum session time of 0 seconds.
- **VTY Access**:
  - VTY access (lines vty 0-4) uses the default authentication method.
  - Only SSH transport input is allowed on these lines.
  - The MGMT-MGMT ACL restricts access from specific IP addresses.
- **Enable Password**: The enable secret password is set to 3NA8le$cret!=1, which is encrypted.
- **AAA Configuration**:
  - TACACS+ is used as the default authentication method for login and exec sessions.
  - Local users are allowed for fallback purposes only.
- **Login Banners**: An unauthorized access banner is configured.

### Management Access Lists
- **MGMT-MGMT ACL**: This standard ACL permits access from IP addresses in the 10.90.0.0/24 and 10.91.0.0/24 networks while denying all other traffic.

## VLANs

### VLAN Database
| VLAN ID | Name        | Purpose/Description          |
|---------|-------------|------------------------------|
| 11      | Usergroup1-1 |                            |
| 12      | Usergroup1-2 |                            |
| 90      | Admin-Mgmt-LEFT | Management VLAN             |
| 666     | native-trunk | Native VLAN for trunk ports |

### VLAN Interfaces (SVIs)
- **VLAN 11 Interface**: No SVI is explicitly configured for VLAN 11. This implies that the switch is not providing a management IP address for this VLAN.
- **VLAN 12 Interface**: Same as above for VLAN 12.
- **VLAN 90 Interface**:
  - SVI Vlan90 has an IP address of 10.90.0.11/24.
  - This interface also applies the MGMT-MGMT ACL.

### VTP Configuration
- **VTP Mode**: Not explicitly configured, implying default operation (Client).
- **VTP Domain**: Not configured.
- **VTP Version**: Not configured.
- **Analysis**: The switch is in client mode by default. It does not have a specific VTP domain or version configured.

## Physical Interfaces

### Interface Summary
| Interface | Description                  | Mode      | VLAN/Trunk | Speed/Duplex | Status    | Special Features        |
|-----------|-------------------------------|-----------|------------|--------------|-----------|--------------------------|
| Gi0/1     | dis-venstre-sw01 gig0/1       | Trunk     | 11,12,90   | No config    | Up        | None                    |
| Fa0/1     | PC4-Access port              | Access    | 11         | No config    | Up        | Port-security enabled    |
| Fa0/2     | PC5-Access port              | Access    | 12         | No config    | Up        | Port-security enabled    |
| Fa0/3     | Management-PC Access port   | Access    | 90         | No config    | Up        | Port-security enabled    |

### Detailed Interface Configurations
#### GigabitEthernet0/1
- **Description**: dis-venstre-sw01 gig0/1
- **Mode**: Trunk
- **Configuration Details**:
  - Set to trunk mode with DTP disabled.
  - Native VLAN is set to 666 (native-trunk).
  - Allowed VLANs are set to 11, 12, and 90.

#### FastEthernet0/1
- **Description**: PC4-Access port
- **Mode**: Access
- **Configuration Details**:
  - Set to access mode with VLAN 11 assigned.
  - Port-security is enabled with a maximum of 1 MAC address allowed.