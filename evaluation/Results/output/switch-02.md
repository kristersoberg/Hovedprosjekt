# Network Device Documentation: switch-02

## Device Information
- **Hostname**: switch-02 ✓ VERIFIED  
- **IOS Version**: 15.0(2)SE4 ✓ VERIFIED  
- **Domain Name**: firma.local ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: VLAN 99 ✓ VERIFIED  
- **IP Address**: 10.99.0.12 ✓ VERIFIED  
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED  
- **Default Gateway**: 10.99.0.1 ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **Console**: `line con 0` ✓ VERIFIED  
- **VTY Lines**: `line vty 0 4` ✓ VERIFIED  
- **VTY Transport Input**: `ssh` ✓ VERIFIED  
- **Banner**: Configured (Text: `Advarsel: Uautorisert tilgang er forbudt.`) ✓ VERIFIED  

---

## AAA Configuration
- **AAA**: Not enabled ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED  
- **VLAN IDs and Names**:  
  - VLAN 10: Brukere ✓ VERIFIED  
  - VLAN 20: Servere ✓ VERIFIED  
  - VLAN 50: VoIP ✓ VERIFIED  
  - VLAN 99: Management ✓ VERIFIED  
  - VLAN 666: Not named (native VLAN on trunk) ✓ VERIFIED  

- **SVI Details**:  
  - **VLAN 1**:  
    - Status: Shutdown ✓ VERIFIED  
  - **VLAN 99**:  
    - Description: Management ✓ VERIFIED  
    - IP: 10.99.0.12 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  

- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED  
- **Active (no shutdown)**: 6 ✓ VERIFIED  
- **Shutdown**: 20 ✓ VERIFIED  

### Active Interfaces
1. **FastEthernet0/1**  
   - Description: "Bruker-PC kontor 201" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Voice VLAN: 50 ✓ VERIFIED  
   - Port Security Violation Mode: Not configured ✓ VERIFIED  

2. **FastEthernet0/2**  
   - Description: "Bruker-PC kontor 202" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Voice VLAN: 50 ✓ VERIFIED  
   - Port Security Violation Mode: Not configured ✓ VERIFIED  

3. **FastEthernet0/3**  
   - Description: "Bruker-PC kontor 203" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Voice VLAN: 50 ✓ VERIFIED  
   - Port Security Violation Mode: Not configured ✓ VERIFIED  

4. **FastEthernet0/4**  
   - Description: "Bruker-PC kontor 204" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Voice VLAN: 50 ✓ VERIFIED  
   - Port Security Violation Mode: Not configured ✓ VERIFIED  

5. **FastEthernet0/5**  
   - Description: "Printer 2. etasje" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Port Security Violation Mode: Not configured ✓ VERIFIED  

6. **FastEthernet0/24**  
   - Description: "Uplink til dis-sw01" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 50, 99 ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED  
- **Global Features**: portfast-default ✓ VERIFIED  

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
- **NTP Server**: Not configured ✓ VERIFIED  
- **NTP Authentication**: Not configured ✓ VERIFIED  

### DNS
- **Domain Name**: firma.local ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED  
- **Default Gateway**: 10.99.0.1 ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only VTY access with version 2 and 60-second timeout ✓ VERIFIED  
- Console logging synchronous enabled for readability ✓ VERIFIED  
- PortFast and BPDU Guard enabled on access ports to prevent STP loops ✓ VERIFIED  

#### ⚠ Areas for Improvement
- **AAA not enabled** – No authentication/authorization for local or remote access ~ INFERRED  
- **No ACL on VTY lines** – Unrestricted SSH access could allow brute-force attacks ~ INFERRED  
- **DHCP Snooping and DAI not enabled** – Vulnerable to rogue DHCP servers and ARP spoofing ~ INFERRED  
- **Port security not configured** – No protection against MAC flooding or unauthorized device access ~ INFERRED  
- **NTP not configured** – Time synchronization missing for log correlation ~ INFERRED  

#### Recommendations
1. **Enable AAA** with local authentication and TACACS/RADIUS integration for secure access.  
2. **Configure an ACL** on VTY lines to restrict SSH access to trusted IP ranges.  
3. **Enable DHCP Snooping** on VLANs 10, 20, 50, and 99 to prevent rogue DHCP servers.  
4. **Implement port security** on access ports to limit MAC addresses per port.  
5. **Configure NTP** with a trusted time source for accurate log timestamps.  

---

## Summary

This device, **switch-02**, functions as an **Access Layer Switch** based on its configuration of access ports, voice VLANs, and a trunk uplink to a distribution switch. The configuration is minimal and lacks critical security features like AAA, DHCP Snooping, and port security. While basic security practices (SSH, PortFast) are in place, the device requires significant hardening to meet enterprise security standards.  

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-17T19:29:45.457694