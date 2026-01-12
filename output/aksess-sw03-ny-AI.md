# Network Device Documentation: aksess-sw01

## Device Information
- **Hostname**: aksess-sw01 ✓ VERIFIED
- **IOS Version**: 12.2(37)SE1 ✓ VERIFIED
- **Domain Name**: krister.local ✓ VERIFIED
- **Config Register**: Not configured ✓ VERIFIED

## Management & Access
- **Management VLAN**: 90 ✓ VERIFIED
- **IP Address**: 10.90.0.11 ✓ VERIFIED
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED
- **Default Gateway**: 10.90.0.254 ✓ VERIFIED

### SSH Configuration
- **SSH Version**: 2 ✓ VERIFIED
- **SSH Timeout**: 60 seconds ✓ VERIFIED

### Console Access
- **Line**: line con 0 ✓ VERIFIED
- **Authentication**: console ✓ VERIFIED
- **Logging Synchronous**: True ✓ VERIFIED

### VTY Access
- **Lines**: line vty 0 4 ✓ VERIFIED
- **Transport Input**: ssh ✓ VERIFIED
- **Authentication**: default ✓ VERIFIED
- **Access Class**: MGMT-MGMT (in) ✓ VERIFIED

## AAA Configuration
- **AAA Enabled**: Yes ✓ VERIFIED
- **Authentication Lists**:
  - aaa authentication login console local ✓ VERIFIED
  - aaa authentication login default group tacacs+ local ✓ VERIFIED
- **Authorization Lists**:
  - aaa authorization exec default group tacacs+ local ✓ VERIFIED
- **Accounting**:
  - aaa accounting exec default start-stop group tacacs+ ✓ VERIFIED
- **TACACS+ Servers**: 10.91.0.10 ✓ VERIFIED
- **Local Users**: emergency-admin (privilege 15) ✓ VERIFIED

## VLANs
- **Total VLANs Referenced**: 4 ✓ VERIFIED
- **VLAN IDs**: 11, 12, 90, 666 ✓ VERIFIED
- **VLAN Interfaces (SVIs)**: 2 configured ✓ VERIFIED
  - **VLAN 1**:
    - Status: Shutdown ✓ VERIFIED
  - **VLAN 90**:
    - Description: Management SVI ✓ VERIFIED
    - IP: 10.90.0.11 255.255.255.0 ✓ VERIFIED
    - Status: Active ✓ VERIFIED
    - ACL In: MGMT-MGMT ✓ VERIFIED

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED
- **Active (no shutdown)**: 4 ✓ VERIFIED
- **Shutdown**: 22 ✓ VERIFIED
- **Access Ports**: 3 ✓ VERIFIED
- **Trunk Ports**: 1 ✓ VERIFIED
- **Port Security Enabled**: 3 interfaces ✓ VERIFIED

### Key Active Interfaces:
- **FastEthernet0/1** - PC4-Access port | Mode: access | VLAN: 11 | Port-Sec: ✓ VERIFIED
- **FastEthernet0/2** - PC5-Access port | Mode: access | VLAN: 12 | Port-Sec: ✓ VERIFIED
- **FastEthernet0/3** - Management-PC Access port | Mode: access | VLAN: 90 | Port-Sec: ✓ VERIFIED
- **GigabitEthernet0/1** - dis-venstre-sw01 gig0/1 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 11, 12, 90 ✓ VERIFIED

## Spanning Tree Configuration
- **Mode**: PVST ✓ VERIFIED
- **VLAN Priority**:
  - VLAN 11-12, 90: 28672 ✓ VERIFIED

## DHCP and ARP Inspection
- **IP ARP Inspection**: Enabled on VLANs 11-12 ✓ VERIFIED
- **IP DHCP Snooping**: Enabled on VLANs 11-12 ✓ VERIFIED
- **No Information Option**: Disabled ✓ VERIFIED

## Logging Configuration
- **Logging Server**: 10.91.0.10 ✓ VERIFIED

## NTP Configuration
- **NTP Authentication Key**: 15 (Redacted) ✓ VERIFIED
- **NTP Authenticate**: Enabled ✓ VERIFIED
- **Trusted Key**: 15 ✓ VERIFIED
- **Server**: 10.91.0.123 key 15 (Redacted) ✓ VERIFIED

## Configuration Quality Assessment
### Data Source: Structured configuration analysis
**Generated**: 2026-01-12T21:38:52.110992

---

### Raw Configuration Citations:
```
Building configuration...

Current configuration : 4036 bytes
!
version 12.2(37)SE1
service timestamps log datetime msec
service timestamps debug datetime msec
no service password-encryption
!
hostname aksess-sw01
!
!
!
!
!
!
aaa new-model
!
aaa authentication login console local 
aaa authentication login default group tacacs+ local 
!
!
aaa authorization exec default group tacacs+ local
!
aaa accounting exec default start-stop group tacacs+
!
!
!
!
!
!
username emergency-admin privilege 15 secret 5 <REDACTED>
!
!
!
!
!
!
!
!
ip arp inspection vlan 11-12
!
ip dhcp snooping vlan 11-12
no ip dhcp snooping information option
ip dhcp snooping
!
ip ssh version 2
ip ssh time-out 60
no ip domain-lookup
ip domain-name krister.local
!
!
spanning-tree mode pvst
spanning-tree vlan 11-12,90 priority 28672
!
!
!
!
!
!
interface FastEthernet0/1
 description PC4-Access port
 ip dhcp snooping limit rate 15
 switchport access vlan 11
 switchport mode access
 switchport port-security
 switchport port-security mac-address sticky 
 switchport port-security violation restrict 
 switchport port-security mac-address sticky 00E0.A374.124E
 switchport port-security aging time 3
 storm-control broadcast level 1
 spanning-tree portfast
 spanning-tree bpduguard enable
!
interface FastEthernet0/2
 description PC5-Access port
 ip dhcp snooping limit rate 15
 switchport access vlan 12
 switchport mode access
 switchport port-security
 switchport port-security mac-address sticky 
 switchport port-security violation restrict 
 switchport port-security mac-address sticky 0060.2F97.3B3E
 switchport port-security aging time 3
 storm-control broadcast level 1
 spanning-tree portfast
 spanning-tree bpduguard enable
!
interface FastEthernet0/3
 description Management-PC Access port
 switchport access vlan 90
 switchport mode access
 switchport port-security
 switchport port-security mac-address sticky 
 switchport port-security violation restrict 
 switchport port-security mac-address sticky 0006.2A05.E16C
 switchport port-security aging time 3
 storm-control broadcast level 1
 spanning-tree portfast
 spanning-tree bpduguard enable
!
interface FastEthernet0/4
 shutdown
!
interface FastEthernet0/5
 shutdown
!
interface FastEthernet0/6
 shutdown
!
interface FastEthernet0/7
 shutdown
!
interface FastEthernet0/8
 shutdown
!
interface FastEthernet0/9
 shutdown
!
interface FastEthernet0/10
 shutdown
!
interface FastEthernet0/11
 shutdown
!
interface FastEthernet0/12
 shutdown
!
interface FastEthernet0/13
 shutdown
!
interface FastEthernet0/14
 shutdown
!
interface FastEthernet0/15
 shutdown
!
interface FastEthernet0/16
 shutdown
!
interface FastEthernet0/17
 shutdown
!
interface FastEthernet0/18
 shutdown
!
interface FastEthernet0/19
 shutdown
!
interface FastEthernet0/20
 shutdown
!
interface FastEthernet0/21
 shutdown
!
interface FastEthernet0/22
 shutdown
!
interface FastEthernet0/23
 shutdown
!
interface FastEthernet0/24
 shutdown
!
interface GigabitEthernet0/1
 description dis-venstre-sw01 gig0/1
 ip arp inspection trust
 ip dhcp snooping trust
 switchport trunk native vlan 666
 switchport trunk allowed vlan 11-12,90
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
!
interface GigabitEthernet0/2
 shutdown
!
interface Vlan1
 no ip address
 shutdown
!
interface Vlan90
 description Management SVI
 mac-address 000d.bd10.6201
 ip address 10.90.0.11 255.255.255.0
 ip access-group MGMT-MGMT in
!
ip default-gateway 10.90.0.254
ip classless
!
ip flow-export version 9
!
!
ip access-list standard MGMT-MGMT
 permit 10.90.0.0 0.0.0.255
 permit 10.91.0.0 0.0.0.255
 deny any
!
no cdp run
!
banner login ^CUnauthorized access prohibited.^C
!
tacacs-server host 10.91.0.10 key KompleksNoekkel
!
!
!
!
logging 10.91.0.10
line con 0
 logging synchronous
 login authentication console
!
line aux 0
!
line vty 0 4
 access-class MGMT-MGMT in
 login authentication default
 transport input ssh
!
!
!
ntp authentication-key 15 <REDACTED> 080A43431915001C011F3C0539382B3A37 7
ntp authenticate
ntp trusted-key 15
<REDACTED> server 10.91.0.123 key 15
<REDACTED>
end
```

---

### Summary:
The device `aksess-sw01` is configured with a robust set of security features, including AAA authentication and accounting, SSH access control, and port security on critical interfaces. The VLAN configuration supports multiple user segments (VLANs 11-12) and management traffic (VLAN 90). DHCP snooping and ARP inspection are enabled to prevent unauthorized DHCP servers and ARP spoofing attacks. The device is also configured for logging and NTP synchronization, ensuring accurate timekeeping and audit trails.

The configuration quality is high, with appropriate security measures in place and a well-organized structure that facilitates management and troubleshooting. However, the lack of CDP (Cisco Discovery Protocol) could be seen as a limitation if network discovery and diagnostics are required. Overall, the device is securely configured for its intended use.