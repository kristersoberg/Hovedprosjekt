# Switch Configuration Documentation: 1-aksess-sw01-10.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: This switch is likely a network core or aggregation device with multiple access and uplink interfaces.
- **Last Modified**: Not specified in the config
- **Domain Name**: krister.local

## Device Information
- **Model**: Not specified in the config (need more information to extract)
- **System Image**: Not available from this configuration
- **Serial Number**: Not available from this configuration
- **Hardware Details**: This switch has multiple Gigabit Ethernet and FastEthernet interfaces.

## Management & Access

### Management Interfaces
The management VLAN is configured as VLAN 90 with the IP address 10.90.0.11/24.
- Management VLAN and IP addressing: VLAN 90, IP address: 10.90.0.11/24
- Default gateway configuration: Not specified in the config (but found at 10.90.0.254)
- Management protocols enabled:
  - SSH version 2 is configured with a timeout of 60 seconds.
  - TACACS+ is configured, but there's no evidence it's being used for authentication.

### Access Control & Security
- **Console Access**: Console line configuration: `line con 0 login authentication console exec-timeout 10 0 logging synchronous`
- **VTY Access**: Telnet/SSH configuration:
  - Line configuration: `line vty 0 4 login authentication default transport input ssh access-class MGMT-MGMT in`
  - Access class restrictions: `access-class MGMT-MGMT in` (MGMT-MGMT is a standard IP ACL)
- **Enable Password**: Enable secret password is configured with the command `enable secret 3NA8le$cret!=1`
- **AAA Configuration**: Authentication, Authorization, and Accounting configuration:
  - TACACS+ is configured as the primary AAA source.
  - Local authentication is used when TACACS+ fails.
  - Exec authorization uses group TACACS+ and local.
  - Accounting is enabled for exec sessions using group TACACS+.
- **Login Banners**: An unauthorized access banner is displayed at login: `banner login ^CUnauthorized access prohibited.^C`

### Management Access Lists
There's a standard IP ACL (MGMT-MGMT) configured to restrict management access:
- `ip access-list standard MGMT-MGMT permit 10.90.0.0 0.0.0.255` and `permit 10.91.0.0 0.0.0.255` are defined as permitted sources.
- `deny any` is used to block all other traffic.

## VLANs

### VLAN Database
| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      | Usergroup1-1 | Access for user group 1 |
| 12      | Usergroup1-2 | Access for user group 2 |
| 90      | Admin-Mgmt-LEFT | Management VLAN for admins and left-side access |
| 666     | native-trunk | Native VLAN for trunk links |

### VLAN Interfaces (SVIs)
**VLAN 11 Interface**
- IP Address: Not specified
- Description: Not configured
- DHCP Helper: Not configured
- HSRP/VRRP: Not configured

**VLAN 12 Interface**
- IP Address: Not specified
- Description: Not configured
- DHCP Helper: Not configured
- HSRP/VRRP: Not configured

**VLAN 90 Interface**
- IP Address: 10.90.0.11/24
- Description: Management SVI
- DHCP Helper: Not configured
- HSRP/VRRP: Not configured

## Physical Interfaces

### Interface Summary
| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| Gi0/1    | dis-venstre-sw01 gig0/1 | Trunk | 11,12,90   | Not specified | Up        | None            |
| Fa0/1    | PC4-Access port      | Access | 11         | Not specified | Up        | Port Security   |
| Fa0/2    | PC5-Access port      | Access | 12         | Not specified | Up        | Port Security   |
| Fa0/3    | Management-PC Access port | Access | 90         | Not specified | Up        | Port Security   |
| Gi0/2    | (shutdown)             | -      | -          | -            | Down     | None            |
| Fa0/4-24 | (shutdown)             | -      | -          | -            | Down     | None            |

### Detailed Interface Configurations
#### Gi0/1
- **Description**: dis-venstre-sw01 gig0/1
- **Mode**: Trunk
- **Configuration Details**:
  - `switchport trunk encapsulation dot1q` and `switchport mode trunk` are used to enable trunking.
  - `switchport nonegotiate` disables DTP negotiation, forcing the link to always be in trunk mode.
  - `switchport trunk native vlan 666` sets the native VLAN for this trunk interface.

#### Fa0/1
- **Description**: PC4-Access port
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 11` assigns this port to VLAN 11.
  - Port security is enabled with a maximum of one MAC address allowed and a violation action of restrict.

#### Fa0/2
- **Description**: PC5-Access port
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 12` assigns this port to VLAN 12.
  - Port security is enabled with a maximum of one MAC address allowed and a violation action of restrict.

#### Fa0/3
- **Description**: Management-PC Access port
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 90` assigns this port to VLAN 90.
  - Port security is enabled with a maximum of one MAC address allowed and a violation action of restrict.

## Other Sections

### Routing Configuration
The switch does not appear to be configured as a router; there are no routing protocols or static routes defined in the configuration.

### Spanning Tree Protocol (STP)
- **Mode**: Rapid-PVST (configured with `spanning-tree mode rapid-pvst`)
- **Root Bridge**: Not specified, but this switch appears to be part of an STP domain.
- **Priority**: The priority for VLANs 11,12 and 90 is set to 61440.

### Port Security
Port security is enabled on access ports Fa0/1, Fa0/2, and Fa0/3 with a maximum of one MAC address allowed per port and a violation action of restrict.

## Best Practices Analysis

This configuration mostly adheres to Cisco best practices:
-   The switch has a meaningful hostname.
-   A management VLAN (VLAN 90) is defined and used for management access.
-   Port security is enabled on access ports, restricting the number of MAC addresses allowed per port.
-   STP is configured with Rapid-PVST mode.

However, there are some potential issues or concerns:
-   SSH version 2 should be upgraded to version 2.0 as soon as possible for better security.
-   The switch has several unused interfaces that should be either shut down or removed from the configuration.
-   There's no evidence of NTP (Network Time Protocol) being used; it would be beneficial to configure an NTP server for accurate timekeeping.

### Recommendations
1.  Upgrade SSH version to 2.0 as soon as possible for better security.
2.  Remove unused interfaces or shut them down in the configuration.
3.  Configure an NTP (Network Time Protocol) server for accurate timekeeping.

## Configuration Summary

-   **Total VLANs**: 4
-   **Total Configured Interfaces**: 9 active interfaces
-   **Routing**: Not enabled
-   **Spanning Tree**: Rapid-PVST mode with a priority of 61440 for VLANs 11,12 and 90.
-   **Key Features Enabled**:
    -   Port security on access ports.
    -   STP (Rapid-PVST) for network redundancy.
    -   SSH version 2 for secure remote access.
-   **Security Posture**: This switch has a good security posture, but it should be upgraded to the latest SSH version and consider implementing NTP.

## Appendix

There are no uncommon or complex configurations that need additional explanation in this configuration.