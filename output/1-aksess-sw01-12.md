# Switch Configuration Documentation: 1-aksess-sw01-12.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: This appears to be a switch configured for management and access purposes, with specific settings for security, VLANs, and physical interfaces.
- **Last Modified**: Not available in the configuration file.
- **Domain Name**: krister.local

## Device Information
- **Model**: Not explicitly mentioned.
- **System Image**: The boot image is not specified.
- **Serial Number**: Not provided in the configuration.
- **Hardware Details**: No specific hardware-related information is provided.

## Management & Access

### Management Interfaces
The switch has a management VLAN (VLAN 90) with IP addressing and access restrictions:

- **Management VLAN and IP Addressing**:
  - VLAN 90: ip address 10.90.0.11 255.255.255.0
- **Default Gateway Configuration**: ip default-gateway 10.90.0.254
- **Management Protocols Enabled**: SSH is enabled (ip ssh version 2).

### Access Control & Security

#### Console Access
- **Console Line Configuration**: The console line configuration is set with login authentication and synchronous logging.

```bash
line con 0
 login authentication console
 exec-timeout 10 0
 logging synchronous
```

#### VTY Access
- **Line Configuration**: Telnet/SSH access is enabled on lines vty 0-4, allowing SSH transport only.
  - line vty 0 4 
    login authentication default 
    transport input ssh

```bash
transport input ssh
```
- **Access Class Restrictions**: An ACL (MGMT-MGMT) is applied to restrict VTY access.

#### Enable Password
- **Enable Secret Configuration**: The enable secret password is set with a high level of encryption.
  - enable secret 3NA8le$cret!=1

```bash
enable secret 3NA8le$cret!=1
```

#### AAA Configuration
The switch uses TACACS+ for authentication, authorization, and accounting. Local authentication and authorization are also configured as fallbacks.

- **AAA Authentication**: 
  - aaa authentication login default group tacacs+ local

```bash
aaa authentication login default group tacacs+ local
```
- **AAA Authorization**:
  - aaa authorization exec default group tacacs+ local

```bash
aaa authorization exec default group tacacs+ local
```
- **AAA Accounting**: 
  - aaa accounting exec default start-stop group tacacs+

```bash
aaa accounting exec default start-stop group tacacs+
```

#### Login Banners
A login banner is configured to display a message when users attempt to access the switch.

- **Login Banner**:
  - banner login ^CUnauthorized access prohibited.^C

```bash
banner login ^CUnauthorized access prohibited.^C
```

### Management Access Lists
An ACL (MGMT-MGMT) is applied to restrict management access based on IP addresses:

- **ACL MGMT-MGMT**: 
  permit 10.90.0.0 0.0.0.255
  permit 10.91.0.0 0.0.0.255

```bash
ip access-list standard MGMT-MGMT
 permit 10.90.0.0 0.0.0.255
 permit 10.91.0.0 0.0.0.255
 deny   any
```

## VLANs

### VLAN Database
| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      | Usergroup1-1    | Access VLAN for user group 1 |
| 12      | Usergroup1-2    | Access VLAN for user group 2 |
| 90      | Admin-Mgmt-LEFT | Management VLAN (SVI) |
| 666     | native-trunk   | Native VLAN for trunking |

### VLAN Interfaces (SVIs)
#### VLAN 11 Interface
- **VLAN 11 Interface**: ip address is not configured explicitly, but the switchport access vlan 11 command assigns it to VLAN 11.
- **Description**: None provided.

```bash
switchport access vlan 11
```

#### VLAN 12 Interface
- **VLAN 12 Interface**: ip address is not configured explicitly, but the switchport access vlan 12 command assigns it to VLAN 12.
- **Description**: None provided.

```bash
switchport access vlan 12
```

#### VLAN 90 Interface (Management SVI)
- **VLAN 90 Interface**: 
  - ip address 10.90.0.11 255.255.255.0
  - Description: Management SVI.
- **DHCP Helper**: None configured.

```bash
interface Vlan90
 description Management SVI
 ip address 10.90.0.11 255.255.255.0
 ip access-group MGMT-MGMT in
 no shutdown
```

## Physical Interfaces

### Interface Summary
| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| GigabitEthernet0/1   | dis-venstre-sw01 gig0/1  | trunk    | 11,12,90  | auto/auto   | up            | switchport trunk encapsulation dot1q; switchport mode trunk |
| FastEthernet0/1      | PC4-Access port       | access   | 11        | auto/auto   | up            | switchport port-security; spanning-tree portfast; spanning-tree bpduguard enable |
| FastEthernet0/2      | PC5-Access port       | access   | 12        | auto/auto   | up            | switchport port-security; spanning-tree portfast; spanning-tree bpduguard enable |
| FastEthernet0/3      | Management-PC Access port | access   | 90        | auto/auto   | up            | switchport port-security; spanning-tree portfast; spanning-tree bpduguard enable |

### Detailed Interface Configurations

#### GigabitEthernet0/1
- **Description**: dis-venstre-sw01 gig0/1
- **Mode**: trunk
- **Configuration Details**:
  - switchport trunk encapsulation dot1q
  - switchport mode trunk
  - switchport nonegotiate
  - switchport trunk native vlan 666
  - switchport trunk allowed vlan 11,12,90

```bash
interface GigabitEthernet0/1
 no shutdown
 description dis-venstre-sw01 gig0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
 switchport trunk native vlan 666
 switchport trunk allowed vlan 11,12,90
 ip dhcp snooping trust
 ip arp inspection trust
```

#### FastEthernet0/1 (PC Access Port)
- **Description**: PC4-Access port
- **Mode**: access
- **Configuration Details**:
  - switchport mode access
  - switchport access vlan 11
  - switchport port-security
  - switchport port-security maximum 1
  - switchport port-security violation restrict
  - switchport port-security aging time 3
  - switchport port-security mac-address sticky
  - ip dhcp snooping limit rate 15
  - spanning-tree portfast
  - spanning-tree bpduguard enable

```bash
interface FastEthernet0/1
 no shutdown
 description PC4-Access port
 switchport mode access 
 switchport access vlan 11
 switchport port-security
 switchport port-security maximum 1 
 switchport port-security violation restrict
 switchport port-security aging time 3
 switchport port-security mac-address sticky
 ip dhcp snooping limit rate 15
 spanning-tree portfast
 spanning-tree bpduguard enable
 storm-control broadcast level 1.00
```

#### FastEthernet0/2 (PC Access Port)
- **Description**: PC5-Access port
- **Mode**: access
- **Configuration Details**:
  - switchport mode access
  - switchport access vlan 12
  - switchport port-security
  - switchport port-security maximum 1
  - switchport port-security violation restrict
  - switchport port-security aging time 3
  - switchport port-security mac-address sticky
  - ip dhcp snooping limit rate 15
  - spanning-tree portfast
  - spanning-tree bpduguard enable

```bash
interface FastEthernet0/2
 no shutdown
 description PC5-Access port
 switchport mode access 
 switchport access vlan 12
 switchport port-security
 switchport port-security maximum 1 
 switchport port-security violation restrict
 switchport port-security aging time 3
 switchport port-security mac-address sticky
 ip dhcp snooping limit rate 15
 spanning-tree portfast
 spanning-tree bpduguard enable
 storm-control broadcast level 1.00
```

#### FastEthernet0/3 (Management PC Access Port)
- **Description**: Management-PC Access port
- **Mode**: access
- **Configuration Details**:
  - switchport mode access
  - switchport access vlan 90
  - switchport port-security
  - switchport port-security maximum 1
  - switchport port-security violation restrict
  - switchport port-security aging time 3
  - switchport port-security mac-address sticky
  - spanning-tree portfast
  - spanning-tree bpduguard enable

```bash
interface FastEthernet0/3
 no shutdown
 description Management-PC Access port
 switchport mode access 
 switchport access vlan 90
 switchport port-security
 switchport port-security maximum 1 
 switchport port-security violation restrict
 switchport port-security aging time 3
 switchport port-security mac-address sticky
 spanning-tree portfast
 spanning-tree bpduguard enable
 storm-control broadcast level 1.00
```

### Unused Interfaces
- There are 21 unused interfaces in the shutdown state.
- Default configurations for unused ports:

```bash
interface range FastEthernet0/4-24
 shutdown
```
```bash
interface GigabitEthernet0/2 
 shutdown
```

## Port-Channel / EtherChannel

Not configured.

## Routing Configuration

### Routing Protocol
None configured.

### Static Routes
No static routes are explicitly defined in the configuration.

### Default Route
- The default route is not present in the configuration, but it's possible to configure one with the ip default-gateway command:

```bash
ip default-gateway 10.90.0.254
```

### Inter-VLAN Routing
Inter-vlan routing is likely enabled due to the presence of a router-on-a-stick setup using VLAN interfaces.

## Spanning Tree Protocol

### STP Configuration
- **Mode**: PVST+ (not explicitly mentioned, but common on Cisco switches)
- **Root Bridge**: Not explicitly configured as root for any VLAN.
- **Priority**: The priority is set to 61440 for the specified VLANs:

```bash
spanning-tree vlan 11,12,90 priority 61440
```

### STP Features
- **PortFast**: Enabled on multiple interfaces (see interface configurations above).
- **BPDU Guard**: Not explicitly configured, but it's a good practice to enable BPDU guard for all trunk ports.
- **Root Guard**: Not configured.
- **Loop Guard**: Not configured.
- **UDLD**: Not configured.

### Per-VLAN STP Status
Not applicable in this configuration.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
None configured.

### Stack Configuration
This switch is not part of a stack, as indicated by the absence of any stack-related configurations.

### Redundant Links
No redundant link configurations are present in the provided configuration.

## Quality of Service (QoS)

Not configured.

## Security Features

### Port Security
- **Interfaces with port security enabled**: FastEthernet0/1, FastEthernet0/2, and FastEthernet0/3.
- **Maximum MAC addresses allowed**: 1 for each interface.
- **Violation actions configured**: restrict on all interfaces.
- **Static MAC addresses (if configured)**: None.

### DHCP Security
- **DHCP Snooping**: Enabled.
- **Trusted interfaces**: GigabitEthernet0/1 is trusted.

```bash
ip dhcp snooping vlan 11,12
```

### Dynamic ARP Inspection (DAI)
- Status: Enabled.
- Trusted interfaces: GigabitEthernet0/1 is trusted.

```bash
ip arp inspection vlan 11,12
```

### IP Source Guard
Not configured.

### Storm Control
- **Configuration**: Broadcast level 1.00 on multiple interfaces.
- **Interfaces configured**: FastEthernet0/1, FastEthernet0/2, and FastEthernet0/3.

```bash
storm-control broadcast level 1.00
```

### Access Control Lists (ACLs)
An ACL named MGMT-MGMT is applied to restrict management access.

## Network Services

### DHCP Server/Relay
- **DHCP Relay**: Not configured.
- **Helper addresses**: None.

### NTP (Network Time Protocol)
- **NTP Servers**: 10.91.0.123 with MD5 authentication.
- **NTP Authentication**: MD5 key 15.

```bash
ntp authentication-key 15 md5 KomplekstPassord
```

### SNMP (Simple Network Management Protocol)
Not configured.

### Syslog
- **Logging Level**: The logging buffer size is set to 4096, but the level is not explicitly mentioned.
- **Logging Hosts**: One remote syslog server at IP address 10.91.0.10.

```bash
logging buffered 4096 
```

## Best Practices Analysis

### Good Practices Identified
1. Port security is enabled on access ports.
2. DHCP snooping and DAI are configured to improve network security.

### Potential Issues or Concerns
- The switch's IOS version is unknown, which may make it vulnerable to unpatched security issues.
- There are multiple unused interfaces in the shutdown state; consider removing them from the configuration if not needed.
- PortFast is enabled on multiple trunk ports, which may lead to spanning tree convergence issues.

### Recommendations for Improvement
1. Update to a supported IOS version.
2. Remove unused interfaces and review port configurations.
3. Consider reconfiguring PortFast to only enable it on access ports.

## Configuration Summary

*Total VLANs*: 4 (11, 12, 90, 666)
*Total Configured Interfaces*: 7
*Routing*: Not enabled.
*Spanning Tree*: PVST+ mode with a root priority of 61440 for specified VLANs.
*Key Features Enabled*: Port security on access ports, DHCP snooping, DAI, and storm control.
*Security Posture*: This switch has some basic security features enabled but may be vulnerable due to unknown IOS version.
*Overall Assessment*: The configuration provides adequate security settings; however, the lack of a supported IOS version raises concerns about potential vulnerabilities.