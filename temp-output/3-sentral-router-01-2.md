# Switch Configuration Documentation: 3-sentral-router-01-2.txt

## Overview
- **Hostname**: sentral-router-01
- **IOS Version**: Unknown
- **Configuration Purpose**: This switch appears to be a centralized router, handling multiple VLANs and providing connectivity between them.
- **Last Modified**: Not available in the configuration
- **Domain Name**: krister.local

## Device Information
- **Model**: Not specified
- **System Image**: Not specified
- **Serial Number**: Not specified
- **Hardware Details**: The switch has at least two Gigabit Ethernet interfaces, each with multiple sub-interfaces configured for different VLANs.

## Management & Access

### Management Interfaces
The management interface is not explicitly defined in the configuration. However, based on the access-list MGMT-MGMT, it appears that traffic to and from 10.90.0.0/24 and 10.91.0.0/24 may be allowed for management purposes.

### Access Control & Security
- **Console Access**: The console line is configured with login authentication set to "console" and an executive timeout of 10 minutes.
```markdown
line con 0
 login authentication console
 exec-timeout 10 0
```
- **VTY Access**: The VTY lines are configured for SSH version 2, with a timeout of 60 seconds and three allowed authentication retries. The default authentication method is set to "default" group tacacs+ local.
```markdown
ip ssh version 2
ip ssh time-out 60
ip ssh authentication-retries 3

line vty 0 4
 login authentication default
 transport input ssh
```
- **Enable Password**: The enable secret password is configured as "3NA8le$cret!=3".
```markdown
enable secret 3NA8le$cret!=3
```
- **AAA Configuration**: TACACS+ server host and key are set, along with local authentication and authorization methods.
```markdown
aaa new-model
tacacs-server host 10.91.0.10 key KompleksNoekkel
aaa authentication login default group tacacs+ local
aaa authentication login console local
```
- **Login Banners**: A banner is configured to display an unauthorized access message.
```markdown
banner login ^CUnauthorized access prohibited.^C
```

### Management Access Lists
The MGMT-MGMT access-list allows traffic from 10.90.0.0/24 and 10.91.0.0/24 for management purposes.

## VLANs

### VLAN Database
| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      | Usergroup 1-1 | Access to VLAN 192.168.11.0/24 |
| 12      | Usergroup 1-2 | Access to VLAN 192.168.12.0/24 |
| 21      | Usergroup 2-1 | Access to VLAN 192.168.21.0/24 |
| 22      | Usergroup 2-2 | Access to VLAN 192.168.22.0/24 |
| 90      | Management LEFT SIDE | Management access to VLAN 10.90.0.0/24 |
| 91      | Management RIGHT-SIDE | Management access to VLAN 10.91.0.0/24 |

### VLAN Interfaces (SVIs)
- **VLAN 11 Interface**
```markdown
interface GigabitEthernet0/1.11
 description Usergroup 1-1
 encapsulation dot1Q 11
 ip address 192.168.11.254 255.255.255.0
 ip access-group USERS_TO_SERV21 in
 ip proxy-arp
 no shutdown
```
- **VLAN 12 Interface**
```markdown
interface GigabitEthernet0/1.12
 description Usergroup 1-2
 encapsulation dot1Q 12
 ip address 192.168.12.254 255.255.255.0
 ip access-group USERS_TO_SERV22 in
 ip proxy-arp
 no shutdown
```
- **Management VLAN Interface**
```markdown
interface GigabitEthernet0/1.90
 encapsulation dot1Q 90
 description Management LEFT SIDE
 ip address 10.90.0.254 255.255.255.0
 ip access-group MGMT-LEFT in
 ip proxy-arp
 no shutdown
```

### VTP Configuration
The switch is not configured as a VTP server, and there's no specific VTP configuration found.

## Physical Interfaces

### Interface Summary
| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| GigabitEthernet0/1 | dis-venstre-sw01 GIG0/2 | Access | 11,12 | Not specified | Up | STP enabled |
| GigabitEthernet0/1.11 | Usergroup 1-1 | Trunk | 11 | Not specified | Up | |
| GigabitEthernet0/1.12 | Usergroup 1-2 | Trunk | 12 | Not specified | Up | |
| GigabitEthernet0/1.90 | Management LEFT SIDE | Trunk | 90 | Not specified | Up | |
| GigabitEthernet0/2 | dis-hoyre-sw01 GIG0/2 | Access | 21,22 | Not specified | Up | STP enabled |
| GigabitEthernet0/2.21 | Usergroup 2-1 | Trunk | 21 | Not specified | Up | |
| GigabitEthernet0/2.22 | Usergroup 2-2 | Trunk | 22 | Not specified | Up | |
| GigabitEthernet0/2.91 | Management RIGHT-SIDE | Trunk | 91 | Not specified | Up | |

### Detailed Interface Configurations
- **GigabitEthernet0/1**
```markdown
interface GigabitEthernet0/1
 description dis-venstre-sw01 GIG0/2
 no ip address
 no shutdown
```
- **GigabitEthernet0/1.11**
```markdown
interface GigabitEthernet0/1.11
 description Usergroup 1-1
 encapsulation dot1Q 11
 ip address 192.168.11.254 255.255.255.0
 ip access-group USERS_TO_SERV21 in
 ip proxy-arp
 no shutdown
```
- **GigabitEthernet0/1.90**
```markdown
interface GigabitEthernet0/1.90
 encapsulation dot1Q 90
 description Management LEFT SIDE
 ip address 10.90.0.254 255.255.255.0
 ip access-group MGMT-LEFT in
 ip proxy-arp
 no shutdown
```

## Port-Channel / EtherChannel
There is no Port-Channel or EtherChannel configuration.

## Routing Configuration

### Routing Protocol
No routing protocol is configured.

### Static Routes
There are no static routes configured.

### Default Route
The default route is not explicitly configured.

### Inter-VLAN Routing
Inter-vlan routing appears to be enabled using the router-on-a-stick method, as each VLAN has a corresponding sub-interface on GigabitEthernet0/1 and GigabitEthernet0/2.

## Spanning Tree Protocol

### STP Configuration
The switch is running PVST+ mode for spanning tree protocol (STP), but no specific configuration details are provided.

### STP Features
- **PortFast**: Not configured.
- **BPDU Guard**: Not configured.
- **Root Guard**: Not configured.
- **Loop Guard**: Not configured.
- **UDLD**: Not configured.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
No FHRP configuration is found in the switch's configuration.

### Stack Configuration
The switch does not appear to be part of a stack.

## Quality of Service (QoS)

There is no QoS configuration present in the switch's configuration.

## Security Features

### Port Security
- **Port Security**: Not configured on any interfaces.
- **Maximum MAC addresses allowed**: Not specified.
- **Violation actions configured**: Not specified.
- **Static MAC addresses**: Not configured.

### DHCP Security
- **DHCP Snooping**: Disabled.
- **Trusted ports**: Not specified.
- **VLANs protected**: Not specified.

### Dynamic ARP Inspection (DAI)
- **Enabled/Disabled**: Disabled.
- **Trusted interfaces**: Not specified.
- **VLANs protected**: Not specified.

### IP Source Guard
- **Status and configuration**: Disabled.
- **Interfaces protected**: Not specified.

### Storm Control
- **Configuration**: Broadcast, multicast, unicast thresholds are not configured.
- **Interfaces configured**: Not specified.

## Access Control Lists (ACLs)

### ACL MGMT-MGMT
This standard access-list permits traffic from 10.90.0.0/24 and 10.91.0.0/24 for management purposes.

### ACL USERS_TO_SERV21
This extended access-list controls traffic to VLAN 192.168.11.0/24.

### ACL USERS_TO_SERV22
This extended access-list controls traffic to VLAN 192.168.12.0/24.

## Network Services

### DHCP Server/Relay
The switch is not configured as a DHCP server, but it does have DHCP pool configurations for VLANs 11 and 12.

### NTP (Network Time Protocol)
- **NTP Servers**: Not specified.
- **NTP Authentication**: Not configured.
- **Timezone**: Not set.

### SNMP (Simple Network Management Protocol)
SNMP configuration is not present in the switch's configuration.

## Best Practices Analysis

### Good Practices Identified
The use of meaningful VLAN names and descriptions, along with clear interface configurations, are good practices identified in this analysis.

### Potential Issues or Concerns
- **AAA Configuration**: The use of local authentication on some login methods may be a security concern.
- **Password Security**: The enable secret password is not encrypted.
- **Port Security**: No port security configuration is present for any interfaces, which could lead to MAC table overflow attacks if traffic is high.

### Recommendations for Improvement
1.  Implement more robust AAA configuration using TACACS+ or RADIUS servers and avoid local authentication methods where possible.
2.  Use more secure password configurations, such as encrypted enable secret passwords or even a password manager.
3.  Configure port security on all interfaces to prevent MAC table overflow attacks.
4.  Ensure that the switch is running the latest firmware version and apply any available security patches.

## Configuration Summary
- **Total VLANs**: 6
- **Total Configured Interfaces**: At least 8 active interfaces
- **Routing**: Inter-vlan routing appears enabled using router-on-a-stick method.
- **Spanning Tree**: PVST+ mode is running, but no specific STP configuration details are provided.
- **Key Features Enabled**: VTP, DHCP pools for VLANs 11 and 12, inter-vlan routing (router-on-a-stick), STP (PVST+).
- **Security Posture**: The switch has some security configurations, such as AAA and ACLs, but lacks certain best practices like port security and secure password management.
- **Overall Assessment**: This switch appears to be a centralized router handling multiple VLANs. However, it could benefit from additional security measures and more robust AAA configuration.

## Appendix

### Uncommon or Complex Configurations
There are no unusual or highly complex configurations that require additional explanation in this analysis.

### Configuration Snippets
No specific configuration snippets need to be included for this analysis.