## Switch Configuration Documentation: aksess-sw01.txt

### Overview
- **Hostname**: aksess-sw01
- **IOS Version**: 12.2
- **Configuration Purpose**: This switch appears to be configured as a core network device, possibly providing access to management networks and serving as a central hub for other devices.
- **Last Modified**: Not explicitly mentioned in the configuration
- **Domain Name**: krister.local

### Device Information
- **Model**: Not explicitly mentioned in the configuration
- **System Image**: Boot image information not provided (refer to show version output)
- **Serial Number**: Not available in this configuration snippet
- **Hardware Details**: None provided

### Management & Access

#### Management Interfaces
Document all management-related interface configurations:

- Management VLAN and IP addressing:
  - VLAN90 is configured as the management VLAN with IP address `10.90.0.11/24` on FastEthernet0/3.
- Default gateway configuration: The default gateway is set to `10.90.0.254`.
- Management protocols enabled: SSH version 2, with a time-out of 60 seconds.

#### Console Access
Configuration of console line:

* `line con 0`: Configures the console line for terminal access

#### VTY Access
Telnet/SSH configuration:

* `line vty 0 4`: Configures virtual terminal lines (VTYs) for remote access.
* `transport input ssh`: Enables SSH as a transport protocol.

#### Enable Password
Status and encryption level: Not explicitly mentioned in this configuration snippet

#### AAA Configuration
AAA is configured for authentication, authorization, and accounting:

* `aaa new-model`: Enables the AAA service.
* `username emergency-admin privilege 15 secret 5 $1$mERr$ftYaqMofsVDX1mGnLhHn8/`: Configures an administrator-level user with a password hash.

#### Login Banners
Any configured banners:

* `banner login ^CUnauthorized access prohibited.^C`: Displays an unauthorized access warning for console logins

### Management Access Lists
Document any ACLs applied to management access:

* `ip access-list standard MGMT-MGMT` defines an IP access list allowing traffic from networks 10.90.0.0/24 and 10.91.0.0/24.

### VLANs

#### VLAN Database
Create a table of all configured VLANs:

| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      |      | Access port for PC4 |
| 12      |      | Access port for PC5 |
| 90      | Management SVI | Management VLAN |

#### VLAN Interfaces (SVIs)
For each VLAN interface:

* **VLAN 11 Interface**
  - IP Address: Not explicitly mentioned in this configuration snippet
  - Description: Not configured
  - DHCP Helper: Not configured
  - HSRP/VRRP: Not configured
- **VLAN 12 Interface**
  - IP Address: Not explicitly mentioned in this configuration snippet
  - Description: Not configured
  - DHCP Helper: Not configured
  - HSRP/VRRP: Not configured
* **VLAN 90 Interface**
  - IP Address: `10.90.0.11/24` on FastEthernet0/3
  - Description: Management VLAN SVI
  - DHCP Helper: Not configured
  - HSRP/VRRP: Not configured

### VTP Configuration
- VTP Mode: Not explicitly mentioned in this configuration snippet (VTP is not enabled)
- VTP Domain: Not configured
- VTP Version: Not configured

### Physical Interfaces

#### Interface Summary

| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| FastEthernet0/1 | PC4-Access port | Access | 11          | Not mentioned | Active | Port Security, STP, etc. |
| FastEthernet0/2 | PC5-Access port | Access | 12          | Not mentioned | Active | Port Security, STP, etc. |
| FastEthernet0/3 | Management-PC Access port | Access | 90          | Not mentioned | Active | Port Security, STP, etc. |
| GigabitEthernet0/1 | dis-venstre-sw01 gig0/1 | Trunk | Native VLAN: 666; Allowed VLANs: 11-12, 90    | Not mentioned | Trust, Storm control, etc. |

#### Detailed Interface Configurations

#### FastEthernet0/1
- **Description**: PC4-Access port
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 11`: Assigns the interface to VLAN 11.
  - `ip dhcp snooping limit rate 15`: Configures a DHCP Snooping rate limit.

#### FastEthernet0/2
- **Description**: PC5-Access port
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 12`: Assigns the interface to VLAN 12.
  - `ip dhcp snooping limit rate 15`: Configures a DHCP Snooping rate limit.

#### FastEthernet0/3
- **Description**: Management-PC Access port
- **Mode**: Access
- **Configuration Details**:
  - `switchport access vlan 90`: Assigns the interface to VLAN 90.
  - `ip dhcp snooping limit rate 15`: Configures a DHCP Snooping rate limit.

### Unused Interfaces

There are multiple interfaces (FastEthernet0/4 through FastEthernet0/24) in shutdown state. Default configurations for unused ports are:

- **Shutdown**: The default configuration is to have the interface shut down.
- **No description**: No description is provided by default.
- **Access mode**: Access mode is enabled, but no VLAN assignment is made.

### Port-Channel / EtherChannel
Not configured

### Routing Configuration

#### Routing Protocol
Not configured

#### Static Routes
List all static routes:
- Destination: Not explicitly mentioned in this configuration snippet
  → Next-hop: Not mentioned

#### Default Route
Configuration: `ip default-gateway 10.90.0.254`

#### Inter-VLAN Routing
Status: Not enabled (Layer 2 switching used for VLANs)

### Spanning Tree Protocol

#### STP Configuration
- **Mode**: pvst+
- **Root Bridge**: Not explicitly mentioned in this configuration snippet (PVST+ mode is used)
- **Priority**: The priority of the root bridge is not explicitly mentioned.

#### STP Features
- **PortFast**: Enabled on several interfaces.
- **BPDU Guard**: Enabled on several interfaces.
- **Root Guard**: Not configured
- **Loop Guard**: Not configured
- **UDLD**: Not configured

### Per-VLAN STP Status
Not applicable (PVST+ mode used)

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
Not configured

### Stack Configuration
Not configured

### Redundant Links
Not configured

## Quality of Service (QoS)
Not configured

## Security Features

### Port Security
- Interfaces with port security enabled: FastEthernet0/1, FastEthernet0/2, and FastEthernet0/3.
  - Maximum MAC addresses allowed: Not explicitly mentioned in this configuration snippet.
  - Violation actions configured: `switchport port-security violation restrict`
  - Static MAC addresses (if configured): `00E0.A374.124E` on FastEthernet0/1 and `0060.2F97.3B3E` on FastEthernet0/2.

### DHCP Security
- **DHCP Snooping**: Enabled for VLANs 11, 12, and 90.
- **DHCP Snooping Database**: Not explicitly mentioned in this configuration snippet.

### Dynamic ARP Inspection (DAI)
Not configured

### IP Source Guard
Not configured

### Storm Control
- Configuration: `storm-control broadcast level 1` on FastEthernet0/1 and FastEthernet0/2.
- Interfaces configured: FastEthernet0/1, FastEthernet0/2, and GigabitEthernet0/1.

### Access Control Lists (ACLs)
Document all ACLs:

* **ACL MGMT-MGMT**: Allows traffic from networks 10.90.0.0/24 and 10.91.0.0/24.

## Network Services

### DHCP Server/Relay
- **DHCP Server**: Not configured
- **DHCP Relay**: Not configured (Helper addresses not mentioned)

### NTP (Network Time Protocol)
- NTP Server(s): `ntp server 10.91.0.123 key 15`
- NTP Authentication: Enabled (`ntp authentication-key` is configured)
- Timezone: Not explicitly mentioned in this configuration snippet

## Best Practices Analysis
Based on the provided documentation and Cisco best practices, a few issues were identified:

*   **Security**: The switch has an open SSH port (22). It's recommended to change the default SSH port for security purposes.
*   **VLAN Configuration**: There is no VLAN Trunking Protocol (VTP) configuration. This can be managed by configuring VTP on the neighboring switches or using a different method such as using static trunk configurations.
*   **Port Security**: Port security is enabled on FastEthernet0/1, but it's not explicitly mentioned what maximum MAC addresses are allowed. It's recommended to configure a specific number of MAC addresses that can be learned by each port.

The recommendations for improvement would be:

1.  **Change the default SSH port**: Change the default SSH port from 22 to an unused port (e.g., 2222) to enhance security.
2.  **Configure VTP or use static trunk configurations**: Configure VTP on the neighboring switches or use a different method such as using static trunk configurations for VLANs.
3.  **Set a specific number of MAC addresses allowed by each port**: Configure a specific number of MAC addresses that can be learned by each port under Port Security.

These recommendations would improve the security and manageability of the network while also ensuring compliance with Cisco best practices.