# Switch Configuration Documentation: 1-aksess-sw01-7.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: The configuration suggests that the switch is a managed switch for a small to medium-sized network, possibly with a focus on security and management access.
- **Last Modified**: Not available in the provided configuration.
- **Domain Name**: krister.local

## Device Information
- **Model**: Not specified in the configuration.
- **System Image**: The boot image information is not provided.
- **Serial Number**: Not available in the configuration.
- **Hardware Details**: Not specified.

## Management & Access

### Management Interfaces
The management VLAN and IP addressing are configured on VLAN 90 (Management SVI).

*   Management VLAN: VLAN 90 (Admin-Mgmt-LEFT)
*   IP Addressing: `10.90.0.11/24`
*   Default Gateway Configuration: The default gateway is set to `10.90.0.254`.
*   Management Protocols Enabled:
    *   SSH version 2
    *   Telnet (disabled by not allowing transport input telnet)

### Access Control & Security

#### Console Access
The console line is configured for local authentication.

*   Authentication Method: Local
*   Login Banner: None

#### VTY Access
VTY access is enabled, and the default authentication method is set to group tacacs+ followed by local. This suggests that TACACS+ server 10.91.0.10 is used as the primary source for authentication.

*   Authentication Method: Group tacacs+ followed by local
*   VTY Timeout: Not specified.
*   Transport Protocols Allowed:
    *   SSH

#### Enable Password
The enable password is set, but it's encrypted with a secret level of 5. This suggests that the password is not easily readable.

*   Enable Secret Level: 5
*   Enable Secret Password: Encrypted (`3NA8le$cret!=1`)

#### AAA Configuration
AAA (Authentication, Authorization, and Accounting) is enabled with TACACS+ as the primary source for authentication. The configuration includes:

*   Authentication Methods:
    *   Login: Group tacacs+ followed by local
    *   Exec: Group tacacs+ followed by local
*   Authorization Method:
    *   Exec: Group tacacs+ followed by local

#### Login Banners
A login banner is set with the message "Unauthorized access prohibited."

### Management Access Lists
The management ACL (MGMT-MGMT) allows traffic from `10.90.0.0/255.255.255.255` and `10.91.0.0/255.255.255.255`, while denying all other traffic.

*   ACL Name: MGMT-MGMT
*   Permit Rules:
    *   `permit 10.90.0.0 0.0.0.255`
    *   `permit 10.91.0.0 0.0.0.255`
*   Deny Rule:
    *   `deny any`

## VLANs

### VLAN Database
The following table shows the configured VLANs:

| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11     | Usergroup1-1 | For client traffic (PC Access) |
| 12     | Usergroup1-2 | For client traffic (PC Access) |
| 90     | Admin-Mgmt-LEFT | Management VLAN |
| 666    | native-trunk | Native VLAN for trunk ports |

### VLAN Interfaces (SVIs)
The management SVI is configured on VLAN 90.

*   **VLAN 90 Interface**
    *   IP Address: `10.90.0.11/24`
    *   Description: Management SVI
    *   DHCP Helper: Not configured.
    *   HSRP/VRRP: Not configured.
    *   Additional Settings:
        +   No shutdown state.

## Physical Interfaces

### Interface Summary
The following table shows the interface summary:

| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| Gig 0/1   | dis-venstre-sw01 gig0/1 | trunk | 11,12,90    | Not specified | Up       | Switchport trunk encapsulation dot1q, switchport mode trunk |
| Fast Eth 0/1 | PC4-Access port     | access| 11          | Not specified | Up       | Port security enabled, storm control broadcast level 1.00 |
| Fast Eth 0/2 | PC5-Access port     | access| 12          | Not specified | Up       | Port security enabled, storm control broadcast level 1.00 |
| Fast Eth 0/3 | Management-PC Access port  | access| 90          | Not specified | Up       | Port security enabled |

### Detailed Interface Configurations
The detailed interface configurations are:

#### GigabitEthernet0/1
*   **Description**: dis-venstre-sw01 gig0/1
*   **Mode**: trunk
*   **Configuration Details**:
    *   `switchport trunk encapsulation dot1q`
    *   `switchport mode trunk`
    *   `ip dhcp snooping trust` (enables DHCP snooping on the port)
    *   `ip arp inspection trust` (enables ARP inspection on the port)

#### FastEthernet0/1
*   **Description**: PC4-Access port
*   **Mode**: access
*   **Configuration Details**:
    *   `switchport mode access`
    *   `switchport access vlan 11`
    *   Port security enabled (`switchport port-security`)
    *   `ip dhcp snooping limit rate 15` (configures DHCP snooping rate limit)
    *   Spanning Tree Protocol settings (`spanning-tree portfast`, `spanning-tree bpduguard enable`)

#### FastEthernet0/2
*   **Description**: PC5-Access port
*   **Mode**: access
*   **Configuration Details**:
    *   `switchport mode access`
    *   `switchport access vlan 12`
    *   Port security enabled (`switchport port-security`)
    *   `ip dhcp snooping limit rate 15` (configures DHCP snooping rate limit)
    *   Spanning Tree Protocol settings (`spanning-tree portfast`, `spanning-tree bpduguard enable`)

#### FastEthernet0/3
*   **Description**: Management-PC Access port
*   **Mode**: access
*   **Configuration Details**:
    *   `switchport mode access`
    *   `switchport access vlan 90`
    *   Port security enabled (`switchport port-security`)
    *   Spanning Tree Protocol settings (`spanning-tree portfast`, `spanning-tree bpduguard enable`)

## Port-Channel / EtherChannel
No Port-channel configuration is found.

## Routing Configuration

### Routing Protocol
No routing protocol is configured in the provided configuration.

### Static Routes
No static routes are present in the configuration.

### Default Route
The default route is not explicitly configured; however, a next-hop gateway of `10.90.0.254` is specified for VLAN 90's IP address.

### Inter-VLAN Routing
Inter-vlan routing is enabled on this switch (`ip routing` command).

## Spanning Tree Protocol

### STP Configuration
The spanning tree protocol is configured in PVST+ mode.

*   **Mode**: PVST+
*   **Root Bridge**: This switch is not the root bridge for any VLAN.
*   **Priority**: The priority values are set to 61440 for VLANs 11, 12, and 90.

### STP Features
The following STP features are enabled on various interfaces:

*   PortFast: Enabled on FastEthernet0/1, FastEthernet0/2, and FastEthernet0/3.
*   BPDU Guard: Enabled on FastEthernet0/1, FastEthernet0/2, and FastEthernet0/3.
*   Root Guard: Not configured.
*   Loop Guard: Not configured.
*   UDLD: Not configured.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
No FHRP configuration is found in the provided configuration.

## Quality of Service (QoS)

No QoS configuration is present in the provided configuration.

## Security Features

### Port Security
Port security is enabled on various interfaces:

*   FastEthernet0/1: Maximum MAC addresses allowed = 1, Violation action = restrict.
*   FastEthernet0/2: Maximum MAC addresses allowed = 1, Violation action = restrict.
*   FastEthernet0/3: Maximum MAC addresses allowed = 1, Violation action = restrict.

### DHCP Security
DHCP snooping is enabled globally and on various interfaces:

*   `ip dhcp snooping vlan 11`
*   `ip dhcp snooping vlan 12`
*   `ip dhcp snooping vlan 90`

The trusted ports are not explicitly configured; however, the command `ip dhcp snooping trust` is used to enable DHCP snooping on an interface.

### Dynamic ARP Inspection (DAI)
DHCP snooping and dynamic ARP inspection are enabled globally (`ip dhcp snooping`, `ip arp inspection vlan 11`, `ip arp inspection vlan 12`), but DAI is not explicitly configured.

### IP Source Guard
No IP source guard configuration is found in the provided configuration.

### Storm Control
Storm control is configured on various interfaces:

*   FastEthernet0/1: Broadcast level = 1.00.
*   FastEthernet0/2: Broadcast level = 1.00.
*   FastEthernet0/3: Broadcast level = 1.00.

## Access Control Lists (ACLs)

### ACL Configuration
An extended ACL named MGMT-MGMT is configured for management access control:

| Sequence Number | Action | Protocol | Source IP | Destination IP |
|-----------------|--------|----------|-----------|-----------------|
| 10              | permit | tcp      | any       | 10.91.0.0/255.255.255.255 eq 22 |
| 20              | permit | udp      | any       | 10.91.0.0/255.255.255.255 eq 69 |

## Network Services

### DHCP Server/Relay
No DHCP server or relay configuration is found in the provided configuration.

### NTP (Network Time Protocol)
NTP is configured with a single server:

*   `ntp authentication-key 15 md5 KomplekstPassord`
*   `ntp trusted-key 15`
*   `ntp authenticate`

The timezone setting is not specified in the configuration.

### SNMP (Simple Network Management Protocol)
SNMP version 3 is enabled, but community strings and trap receivers are not configured.

## CDP/LLDP
No CDP or LLDP configuration is found in the provided configuration.

## Syslog
Syslog logging is enabled with a buffer size of 4096:

*   `logging buffered 4096`
*   `logging host 10.91.0.10`

The logging level and other settings are not specified in the configuration.

## Other Services

### IP HTTP Server
No IP HTTP server configuration is found in the provided configuration.

## Best Practices Analysis

The following sections provide feedback on best practices:

### Good Practices Identified

*   The switch has a login banner set.
*   Port security is enabled for various interfaces.
*   DHCP snooping and ARP inspection are enabled globally.

### Potential Issues or Concerns
1.  **Security**: The configuration does not include any IP source guard settings, which could be used to prevent IP spoofing attacks.
2.  **Port Security**: While port security is enabled on some interfaces, the maximum number of MAC addresses allowed could be set lower for improved security.
3.  **DHCP Snooping and ARP Inspection**: Although DHCP snooping and ARP inspection are enabled globally, it would be beneficial to explicitly specify trusted ports.

### Recommendations for Improvement
1.  Configure IP source guard settings on all interfaces to prevent IP spoofing attacks.
2.  Set the maximum number of MAC addresses allowed lower than the default value (1) for improved security on port-security-enabled interfaces.
3.  Explicitly specify trusted ports for DHCP snooping and ARP inspection.

## Configuration Summary
- **Total VLANs**: 4
- **Total Configured Interfaces**: 6 active interfaces
- **Routing**: Enabled with inter-vlan routing
- **Spanning Tree**: PVST+ mode, Root bridge not this switch
- **Key Features Enabled**:
    *   Port security on various interfaces
    *   DHCP snooping and ARP inspection globally
    *   Storm control on various interfaces
- **Security Posture**: Good practices identified, but potential issues or concerns exist.
- **Overall Assessment**: The configuration appears to be secure, with good practices in place. However, there are opportunities for improvement.

## Appendix

### Uncommon or Complex Configurations
No uncommon or complex configurations were found that require additional explanation.

### Configuration Snippets
No relevant configuration snippets need to be included.