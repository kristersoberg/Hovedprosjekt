# Network Device Documentation: lab-sw01

## Device Information
- **Hostname**: lab-sw01 ✓ VERIFIED  
- **IOS Version**: 15.0(2)SE4 ✓ VERIFIED  
- **Domain Name**: lab.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: VLAN 99 ✓ VERIFIED  
- **IP Address**: 10.99.1.8 ✓ VERIFIED  
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **SSH Version**: Not configured ✓ VERIFIED  
- **SSH Timeout**: Not configured ✓ VERIFIED  
- **Console**: line con 0 ✓ VERIFIED  
  - Authentication: None ✓ VERIFIED  
  - Logging Synchronous: Enabled ✓ VERIFIED  
- **VTY Lines**: line vty 0 4 ✓ VERIFIED  
  - Transport Input: ssh, telnet ✓ VERIFIED  
  - Authentication: None ✓ VERIFIED  
  - Access Class: None (⚠ No ACL protection) ✓ VERIFIED  
- **Banner**: Configured (line: `banner motd ^CLab-miljoe. Ingen produksjonsdata tillatt.^C`) ✓ VERIFIED  

---

## AAA Configuration
- AAA: Not enabled ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 4 ✓ VERIFIED  
- **VLAN IDs and Names**:  
  - VLAN 99: Management ✓ VERIFIED  
  - VLAN 110: Lab-Klienter ✓ VERIFIED  
  - VLAN 120: Lab-Servere ✓ VERIFIED  
  - VLAN 666: Not named ✓ VERIFIED  

- **VLAN Interfaces (SVIs)**:  
  - **VLAN 1**:  
    - Status: Shutdown ✓ VERIFIED  
  - **VLAN 99**:  
    - Description: Management ✓ VERIFIED  
    - IP: 10.99.1.8 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  

- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED  
- **Active (no shutdown)**: 11 ✓ VERIFIED  
- **Shutdown**: 15 ✓ VERIFIED  

### Active Interfaces:
1. **FastEthernet0/1**  
   - Description: Lab-PC 1 ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 110 ✓ VERIFIED  

2. **FastEthernet0/2**  
   - Description: Lab-PC 2 ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 110 ✓ VERIFIED  

3. **FastEthernet0/3**  
   - Description: Lab-PC 3 ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 110 ✓ VERIFIED  

4. **FastEthernet0/4**  
   - Description: Lab-PC 4 ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 110 ✓ VERIFIED  

5. **FastEthernet0/5**  
   - Description: Lab-PC 5 ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 110 ✓ VERIFIED  

6. **FastEthernet0/6**  
   - Description: Lab-PC 6 ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 110 ✓ VERIFIED  

7. **FastEthernet0/7**  
   - Description: Lab-Server 1 ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 120 ✓ VERIFIED  

8. **FastEthernet0/8**  
   - Description: Lab-Server 2 ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 120 ✓ VERIFIED  

9. **FastEthernet0/9**  
   - Description: Lab-Server 3 ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 120 ✓ VERIFIED  

10. **FastEthernet0/10**  
    - Description: Lab-Server 4 ✓ VERIFIED  
    - Mode: access ✓ VERIFIED  
    - VLAN: 120 ✓ VERIFIED  

11. **FastEthernet0/24**  
    - Description: Uplink til dis-sw01 gig0/6 ✓ VERIFIED  
    - Mode: trunk ✓ VERIFIED  
    - Encapsulation: dot1q ✓ VERIFIED  
    - Native VLAN: 666 ✓ VERIFIED  
    - Allowed VLANs: 99, 110, 120 ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED  
- **CDP**: Enabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED  

---

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED  
- **NTP Authentication**: Disabled ✓ VERIFIED  

### DNS
- **Domain Name**: lab.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- VLAN segmentation for client (110), server (120), and management (99) traffic ✓ VERIFIED  
- Spanning Tree Protocol (PVST) enabled for loop prevention ✓ VERIFIED  
- NTP configured for time synchronization ✓ VERIFIED  
- Syslog configured for centralized logging ✓ VERIFIED  

#### ⚠ Areas for Improvement
- **SSH not configured** – Telnet is allowed on VTY lines (line: `transport input ssh telnet`) ⚠ INFERRED  
- **No AAA authentication** – Console/VTY lines use no authentication ⚠ INFERRED  
- **No port security** – No violation modes configured on access ports ⚠ INFERRED  
- **Missing security features**: DHCP snooping, DAI, IP source guard, 802.1X ⚠ INFERRED  
- **No ACLs** – VTY lines lack access control ⚠ INFERRED  

#### Recommendations
1. **Enable SSH** and disable Telnet on VTY lines (line: `transport input ssh`) ~ INFERRED  
2. **Implement AAA** for console/VTY authentication ~ INFERRED  
3. **Enable port security** on access ports (e.g., `switchport port-security violation restrict`) ~ INFERRED  
4. **Enable DHCP snooping** on VLANs 110 and 120 ~ INFERRED  
5. **Configure ACLs** to restrict VTY access to trusted IPs ~ INFERRED  
6. **Enable LLDP** for network discovery ~ INFERRED  

---

## Summary

lab-sw01 is an **Access Layer Switch** ✓ INFERRED, providing connectivity for lab clients (VLAN 110) and servers (VLAN 120). It uses VLAN 99 for management and has a trunk uplink to a distribution switch. The configuration is minimal and lacks critical security features like SSH, AAA, and port security. While basic services (NTP, syslog) are configured, the device requires hardening to meet enterprise security standards.  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-16T08:49:29.819402