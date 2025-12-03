# Switch Configuration Documentation: 1-aksess-sw01-11.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: This switch configuration appears designed for a managed network, likely as part of a campus infrastructure with a focus on security and management features.
- **Last Modified**: 2025-12-03T20:45:56.923478 (Generated timestamp from analyzer)
- **Domain Name**: krister.local

## Device Information
- **Model**: Not specified in the configuration file, but based on interface types (e.g., GigabitEthernet0/1), it's likely a Cisco Catalyst switch.
- **System Image**: Unknown due to lack of information about the boot image or system version.
- **Serial Number**: Not available in the provided configuration.
- **Hardware Details**: The switch has various interfaces, including FastEthernet and Gigabit Ethernet ports.

## Management & Access

### Management Interfaces
The management interface is configured on VLAN 90 with IP address 10.90.0.11/24:
- **Management VLAN and IP addressing**:
  - VLAN: 90 (Admin-Mgmt-LEFT)
  - IP Address: 10.90.0.11/24
- **Default gateway configuration**: ip default-gateway 10.90.0.254
- **Management protocols enabled**: SSH version 2 is enabled on the management interface.

### Access Control & Security

#### Console Access
The console line is configured with authentication using the "console" method:
```cisco
line con 0
 login authentication console
 exec-timeout 10 0
 logging synchronous
```
This configuration requires local authentication for console access.

#### VTY Access
VTY (Telnet/SSH) access is enabled on lines 0-4 with default authentication:
```cisco
line vty 0 4
 login authentication default
 transport input ssh
 access-class MGMT-MGMT in
```
This configuration uses the "default" group for authentication, which includes both local and TACACS+ methods.

#### Enable Password
The enable secret password is set to an encrypted value:
```cisco
enable secret 3NA8le$cret!=1
```
This password provides privileged access to the switch.

#### AAA Configuration
AAA (Authentication, Authorization, and Accounting) is configured with multiple methods for authentication and authorization:

- **Authentication**: The default method uses TACACS+ followed by local:
```cisco
aaa authentication login default group tacacs+ local
```
- **Authorization**: Exec authorization also uses TACACS+ followed by local:
```cisco
aaa authorization exec default group tacacs+ local
```
- **Accounting**: Accounting is enabled for exec sessions with TACACS+ as the primary method:
```cisco
aaa accounting exec default start-stop group tacacs+
```

#### Login Banners
A login banner is set to display an unauthorized access message:
```cisco
banner login ^CUnauthorized access prohibited.^C
```
This banner will be displayed when users attempt to log in.

### Management Access Lists
The ACL "MGMT-MGMT" is defined for management traffic on VLAN 90. The ACL permits traffic from two networks (10.90.0.0/24 and 10.91.0.0/24) but denies all other traffic:
```cisco
ip access-list standard MGMT-MGMT
 permit 10.90.0.0 0.0.0.255
 permit 10.91.0.0 0.0.0.255
 deny   any
```
This ACL restricts management access to the two specified networks.

## VLANs

### VLAN Database

| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      | Usergroup1-1 | Client VLAN |
| 12      | Usergroup1-2 | Client VLAN |
| 90      | Admin-Mgmt-LEFT | Management VLAN |
| 666     | native-trunk | Trunk VLAN (Native) |

### VLAN Interfaces (SVIs)

#### VLAN 11 Interface
```cisco
interface Vlan11
 description Usergroup1-1
```
No additional settings are configured for this interface.

#### VLAN 12 Interface
```cisco
interface Vlan12
 description Usergroup1-2
```
No additional settings are configured for this interface.

#### VLAN 90 Interface
- **VLAN 90 Interface**:
  - IP Address: 10.90.0.11/24
  - Description: Management SVI
  - DHCP Helper: Not configured
  - HSRP/VRRP: Not configured

### VTP Configuration
The switch is in a VTP domain but does not specify the domain name:
```cisco
vtp mode transparent
```
This configuration implies that the switch will forward VLAN information from other switches in its VTP domain.

## Physical Interfaces

### Interface Summary

| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| Gig 0/1   | dis-venstre-sw01 gig0/1 | Trunk  | native (666) | Not specified | Up    | None             |
| Fas 0/1   | PC4-Access port        | Access | 11          | Not specified | Up    | Port-security     |
| Fas 0/2   | PC5-Access port        | Access | 12          | Not specified | Up    | Port-security     |
| Fas 0/3   | Management-PC Access port | Access | 90          | Not specified | Up    | Port-security     |

### Detailed Interface Configurations

#### GigabitEthernet 0/1
```cisco
interface GigabitEthernet0/1
 description dis-venstre-sw01 gig0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
 switchport trunk native vlan 666
 switchport trunk allowed vlan 11,12,90
 ip dhcp snooping trust
 ip arp inspection trust
```
This interface is configured as a trunk with VLANs 11, 12, and 90 allowed. DHCP snooping and ARP inspection are enabled on this interface.

#### FastEthernet 0/1
```cisco
interface FastEthernet0/1
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
This interface is configured as an access port on VLAN 11 with port security enabled.

#### FastEthernet 0/2
```cisco
interface FastEthernet0/2
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
This interface is configured as an access port on VLAN 12 with port security enabled.

#### FastEthernet 0/3
```cisco
interface FastEthernet0/3
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
This interface is configured as an access port on VLAN 90 with port security enabled.

## Port-Channel / EtherChannel

No Port-Channel or EtherChannel configurations are present in the provided configuration file.

## Routing Configuration

### Routing Protocol

No routing protocols (OSPF, EIGRP, RIP, BGP) are explicitly configured in this switch configuration.

### Static Routes
Static routes are not configured in the provided configuration.

### Default Route
The default route is set to 10.90.0.254:
```cisco
ip default-gateway 10.90.0.254
```
This route will be used when a destination network is not found in the routing table.

## Spanning Tree Protocol

### STP Configuration
STP is enabled with Rapid-PVST mode:
```cisco
spanning-tree vlan 11,12,90 priority 61440
```
The switch has set its own priority to 61440 for VLANs 11, 12, and 90.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
No HSRP, VRRP, or GLBP configurations are present in the provided configuration file.

### Stack Configuration
This switch is not part of a stack as there's no information about other switches connected to it for forming a stack.

## Quality of Service (QoS)

No QoS configurations are explicitly defined in this switch configuration.