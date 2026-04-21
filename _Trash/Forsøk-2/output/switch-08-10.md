# Network Device Documentation: lab-sw01

## Device Information
- **Hostname**: lab-sw01 ✓ VERIFIED
- **IOS Version**: 15.0(2)SE4 ✓ VERIFIED
- **Domain Name**: lab.bedrift.no ✓ VERIFIED
- **Config Register**: Not configured ✓ VERIFIED

## Management & Access
- **Management VLAN**: 99 ✓ VERIFIED
- **IP Address**: 10.99.1.8 ✓ VERIFIED
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED
- **SSH Version**: Not configured ✓ VERIFIED
- **SSH Timeout**: Not configured ✓ VERIFIED
- **VTY Transport Input**: ssh, telnet ✓ VERIFIED
- **VTY Authentication**: None ✓ VERIFIED
- **VTY Access Class**: None (⚠ No ACL protection) ✓ VERIFIED
- **Console Access**: Line `line con 0` with logging synchronous enabled ✓ VERIFIED

## AAA Configuration
- **AAA**: Not enabled ✓ VERIFIED

## VLANs
- **Total VLANs Referenced**: 4 ✓ VERIFIED
- **VLAN IDs**: 99, 110, 120, 666 ✓ VERIFIED
- **VLAN Interfaces (SVIs)**:
  - **VLAN 1**:
    - Status: Shutdown ✓ VERIFIED
  - **VLAN 99**:
    - Description: Management ✓ VERIFIED
    - IP: 10.99.1.8 255.255.255.0 ✓ VERIFIED
    - Status: Active ✓ VERIFIED
- **VTP Configuration**: Not explicitly configured ✓ VERIFIED

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED
- **Active (no shutdown)**: 11 ✓ VERIFIED
- **Shutdown**: 15 ✓ VERIFIED
- **Access Ports**: 10 ✓ VERIFIED
- **Trunk Ports**: 1 ✓ VERIFIED
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED

### Key Active Interfaces
- **FastEthernet0/1** - Lab-PC 1 | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/2** - Lab-PC 2 | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/3** - Lab-PC 3 | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/4** - Lab-PC 4 | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/5** - Lab-PC 5 | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/6** - Lab-PC 6 | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/7** - Lab-Server 1 | Mode: access | VLAN: 120 ✓ VERIFIED
- **FastEthernet0/8** - Lab-Server 2 | Mode: access | VLAN: 120 ✓ VERIFIED
- **FastEthernet0/9** - Lab-Server 3 | Mode: access | VLAN: 120 ✓ VERIFIED
- **FastEthernet0/10** - Lab-Server 4 | Mode: access | VLAN: 120 ✓ VERIFIED
- **FastEthernet0/24** - Uplink til dis-sw01 gig0/6 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 99, 110, 120 ✓ VERIFIED

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED
- **Dynamic ARP Inspection (DAI)**: Not enabled✓ VERIFIED
- **Port Security**: Not enabled on any interfaces ✓ VERIFIED
- **IP Source Guard**: Not configured ✓ VERIFIED
- **802.1X**: Not configured ✓ VERIFIED
- **CDP**: Enabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED

## Network Services

### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED
- **Logging Configuration Line**: `logging 10.99.0.50` ✓ VERIFIED

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED
- **NTP Authentication**: Disabled ✓ VERIFIED
- **NTP Configuration Line**: `ntp server 10.99.0.1` ✓ VERIFIED

### Syslog
- **Syslog Server**: 10.99.0.50 ✓ VERIFIED
- **Syslog Configuration Line**: `logging 10.99.0.50` ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

### DNS
- **DNS Domain Name**: lab.bedrift.no ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED

## Configuration Quality Assessment

### Device Role
- **Device Role**: ~ INFERRED - **Access Layer Switch**
  - Justification: The switch has many access ports (10), no routing enabled, and is connected to end-user devices (PCs and servers). It also has a trunk port to a likely distribution switch (`FastEthernet0/24`).

### Security Posture

#### ✓ Strengths
- **Syslog logging** is enabled and configured to send logs to a remote server (10.99.0.50) ✓ VERIFIED
- **NTP** is configured to synchronize time with a remote server (10.99.0.1) ✓ VERIFIED
- **PortFast** is enabled on all access ports to prevent STP delays ✓ VERIFIED
- **No password encryption** is disabled (`no service password-encryption`), which is a good practice for visibility during troubleshooting ✓ VERIFIED
- **Banner MOTD** is configured to warn users about the lab environment and data restrictions ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH is not configured**, leaving the device vulnerable to Telnet-based attacks (plaintext credentials) ✓ VERIFIED
- **VTY lines allow both SSH and Telnet**, but Telnet is insecure and should be disabled ✓ VERIFIED
- **No AAA authentication** is configured for console or VTY access, allowing unrestricted access ✓ VERIFIED
- **No ACLs** are applied to VTY lines, leaving remote access open to all sources ✓ VERIFIED
- **No port security** is enabled on access ports, increasing risk of unauthorized device access ✓ VERIFIED
- **DHCP Snooping** is not enabled, leaving the network vulnerable to rogue DHCP servers ✓ VERIFIED
- **Dynamic ARP Inspection (DAI)** is not enabled, increasing risk of ARP spoofing attacks ✓ VERIFIED
- **IP Source Guard** is not enabled, allowing potential IP spoofing attacks ✓ VERIFIED
- **802.1X** is not configured, leaving wired access unauthenticated ✓ VERIFIED

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines to secure remote access:
  ```plaintext
  ip ssh version 2
  line vty 0 4
   transport input ssh
  ```
- **Enable AAA authentication** for console and VTY access to enforce user authentication:
  ```plaintext
  aaa new-model
  aaa authentication login default local
  ```
- **Apply an ACL to VTY lines** to restrict access to trusted IP addresses:
  ```plaintext
  access-list 101 permit ip 10.99.1.0 0.0.0.255 any
  line vty 0 4
   access-class 101 in
  ```
- **Enable port security** on access ports to prevent unauthorized device access:
  ```plaintext
  switchport port-security
  switchport port-security maximum 1
  switchport port-security violation restrict
  ```
- **Enable DHCP Snooping** and configure trusted ports:
  ```plaintext
  ip dhcp snooping
  ip dhcp snooping vlan 110,120
  interface FastEthernet0/24
   ip dhcp snooping trust
  ```
- **Enable Dynamic ARP Inspection (DAI)** and configure trusted ports:
  ```plaintext
  ip arp inspection vlan 110,120
  interface FastEthernet0/24
   ip arp inspection trust
  ```
- **Enable IP Source Guard** to prevent IP spoofing:
  ```plaintext
  ip source binding static 10.110.0.10 mac 0000.0000.0000 vlan 110
  ```
- **Enable 802.1X authentication** for wired access to enforce user-based authentication:
  ```plaintext
  aaa authentication dot1x default group radius
  dot1x system-auth-control
  interface FastEthernet0/1
   authentication port-control auto
  ```

## Summary

lab-sw01 is an **Access Layer switch** serving a lab environment with multiple access ports connected to PCs and servers. It is configured with VLANs 99 (Management), 110 (Lab-Klienter), and 120 (Lab-Servere), and connects to a distribution switch via a trunk port. The device has basic network services like NTP and syslog enabled, but lacks critical security features such as SSH, AAA, port security, and DHCP snooping. The configuration is functional but requires significant hardening to meet enterprise security standards.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T12:54:15.919957