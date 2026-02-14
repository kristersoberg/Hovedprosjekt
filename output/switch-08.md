# Network Device Documentation: lab-sw01

## Device Information
- **Hostname**: lab-sw01 ✓ VERIFIED  
- **IOS Version**: 15.0(2)SE4 ✓ VERIFIED  
- **Domain Name**: lab.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: 99 ✓ VERIFIED  
- **IP Address**: 10.99.1.8/24 ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **SSH Version**: Not configured ✓ VERIFIED  
- **SSH Timeout**: Not configured ✓ VERIFIED  
- **VTY Transport Input**: ssh, telnet ✓ VERIFIED  
- **VTY Authentication**: None ✓ VERIFIED  
- **VTY ACL Protection**: None (⚠ No ACL protection) ✓ VERIFIED  
- **Console Authentication**: None ✓ VERIFIED  
- **Console Logging Synchronous**: Enabled ✓ VERIFIED  

---

## AAA Configuration
- **AAA Enabled**: No ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 4 ✓ VERIFIED  
- **VLAN IDs**: 99, 110, 120, 666 ✓ VERIFIED  
- **VLAN Interfaces (SVIs)**:  
  - **VLAN 1**: Shutdown ✓ VERIFIED  
  - **VLAN 99**:  
    - Description: Management ✓ VERIFIED  
    - IP: 10.99.1.8/24 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED  
- **Active (no shutdown)**: 11 ✓ VERIFIED  
- **Shutdown**: 15 ✓ VERIFIED  
- **Access Ports**: 10 ✓ VERIFIED  
- **Trunk Ports**: 1 ✓ VERIFIED  
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED  

**Key Active Interfaces**:  
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
- **FastEthernet0/24** - Uplink til dis-sw01 gig0/6 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 99,110,120 ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED  
- **Port Security**: Not enabled on any interfaces ✓ VERIFIED  
- **CDP**: Enabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  

---

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED  
- **NTP Authentication**: Disabled ✓ VERIFIED  

### DNS
- **DNS Domain Name**: lab.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- **NTP and Syslog Enabled**: NTP synchronization and centralized logging are configured for operational visibility.  
- **Spanning Tree (PVST)**: Prevents Layer 2 loops in the network.  
- **DHCP Pools Configured**: VLAN-specific DHCP pools (LAB-VLAN110, LAB-VLAN120) provide structured IP assignment.  

#### ⚠ Areas for Improvement
- **Missing SSH Configuration**: Telnet is allowed on VTY lines (line vty 0 4), exposing credentials in plaintext.  
- **No AAA Authentication**: Console and VTY access lack authentication (no `login` or `login local`).  
- **No Port Security**: Access ports are vulnerable to MAC flooding and unauthorized device connections.  
- **Missing DHCP Snooping and DAI**: Vulnerable to rogue DHCP servers and ARP spoofing.  
- **Unprotected VTY Lines**: No ACLs restrict remote access (e.g., `access-class` on VTY lines).  

#### Recommendations
1. **Enable SSH and Disable Telnet**:  
   - Configure `transport input ssh` on VTY lines.  
   - Remove `transport input telnet` (currently in `line vty 0 4`).  
2. **Implement AAA Authentication**:  
   - Enable `aaa new-model` and configure local or RADIUS/TACACS+ authentication.  
3. **Enable Port Security**:  
   - Apply `switchport port-security` on access ports (e.g., `FastEthernet0/1-10`).  
4. **Enable DHCP Snooping and DAI**:  
   - Configure `ip dhcp snooping` and `ip arp inspection` for VLANs 110 and 120.  
5. **Secure VTY Lines**:  
   - Apply an ACL to restrict access (e.g., `access-class 100 in` on `line vty 0 4`).  

---

## Summary

lab-sw01 is an **Access Layer Switch** serving lab environments (VLANs 110 for clients, 120 for servers). It provides Layer 2 connectivity with basic management via VLAN 99. The configuration lacks critical security features like SSH, AAA, and port security, exposing it to potential threats. Immediate improvements are required to align with enterprise security standards.  

**Device Role**: Access Layer Switch (~ INFERRED)  
**Security Posture**: Weak due to missing authentication and security features (~ INFERRED)  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T20:36:42.777728