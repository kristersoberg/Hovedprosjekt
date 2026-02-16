# Network Device Documentation: aksess-sw10

## Device Information
- **Hostname**: aksess-sw10 ✓ VERIFIED  
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED  
- **Domain Name**: prod.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: 99 ✓ VERIFIED  
- **IP Address**: 10.99.1.10 ✓ VERIFIED  
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **Console**: line con 0 ✓ VERIFIED  
- **VTY Lines**: line vty 0 4 ✓ VERIFIED  
- **VTY Transport Input**: ssh ✓ VERIFIED  
- **Banner**: Configured ✓ VERIFIED  

---

## AAA Configuration
- **AAA**: Enabled ✓ VERIFIED  

**Authentication Lists**:  
- `aaa authentication login default group tacacs+ local` ✓ VERIFIED  
- `aaa authentication login CONSOLE local` ✓ VERIFIED  
- `aaa authentication enable default group tacacs+ enable` ✓ VERIFIED  

**Authorization Lists**:  
- `aaa authorization exec default group tacacs+ local` ✓ VERIFIED  
- `aaa authorization commands 15 default group tacacs+ local` ✓ VERIFIED  

**Accounting**:  
- `aaa accounting exec default start-stop group tacacs+` ✓ VERIFIED  
- `aaa accounting commands 15 default start-stop group tacacs+` ✓ VERIFIED  

**TACACS+ Servers**: 10.99.0.40, 10.99.0.41 ✓ VERIFIED  

**Local Users**:  
- `emergency-admin` (privilege 15) ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 7 ✓ VERIFIED  
- **VLAN IDs and Names**:  
  - VLAN 10: Kontor-1etg ✓ VERIFIED  
  - VLAN 20: Kontor-2etg ✓ VERIFIED  
  - VLAN 30: Kontor-3etg ✓ VERIFIED  
  - VLAN 40: Fellesareal ✓ VERIFIED  
  - VLAN 50: VoIP ✓ VERIFIED  
  - VLAN 99: Management ✓ VERIFIED  
  - VLAN 666: Not configured ✓ VERIFIED  

**VLAN Interfaces (SVIs)**:  
- **VLAN 1**:  
  - Status: Shutdown ✓ VERIFIED  
- **VLAN 99**:  
  - Description: Management SVI ✓ VERIFIED  
  - IP: 10.99.1.10 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - ACL In: MGMT-ACCESS ✓ VERIFIED  

**VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 27 ✓ VERIFIED  
- **Active (no shutdown)**: 11 ✓ VERIFIED  
- **Shutdown**: 16 ✓ VERIFIED  

**Active Interfaces**:  
1. **FastEthernet0/1**  
   - Description: "Kontor 101 - 1. etasje" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: restrict) ✓ VERIFIED  

2. **FastEthernet0/2**  
   - Description: "Kontor 102 - 1. etasje" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: restrict) ✓ VERIFIED  

3. **FastEthernet0/3**  
   - Description: "Kontor 103 - 1. etasje" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: restrict) ✓ VERIFIED  

4. **FastEthernet0/4**  
   - Description: "Kontor 201 - 2. etasje" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 20 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: restrict) ✓ VERIFIED  

5. **FastEthernet0/5**  
   - Description: "Kontor 202 - 2. etasje" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 20 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: restrict) ✓ VERIFIED  

6. **FastEthernet0/6**  
   - Description: "Kontor 301 - 3. etasje" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 30 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: restrict) ✓ VERIFIED  

7. **FastEthernet0/7**  
   - Description: "Fellesareal kantine" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 40 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: protect) ✓ VERIFIED  

8. **FastEthernet0/8**  
   - Description: "Fellesareal resepsjon" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 40 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: protect) ✓ VERIFIED  

9. **FastEthernet0/23**  
   - Description: "Uplink-1 dis-sw01 - Po3 member" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 30, 40, 50, 99 ✓ VERIFIED  

10. **FastEthernet0/24**  
    - Description: "Uplink-2 dis-sw01 - Po3 member" ✓ VERIFIED  
    - Mode: trunk ✓ VERIFIED  
    - Encapsulation: dot1q ✓ VERIFIED  
    - Native VLAN: 666 ✓ VERIFIED  
    - Allowed VLANs: 10, 20, 30, 40, 50, 99 ✓ VERIFIED  

11. **Port-channel3**  
    - Description: "EtherChannel til dis-sw01" ✓ VERIFIED  
    - Mode: trunk ✓ VERIFIED  
    - Encapsulation: dot1q ✓ VERIFIED  
    - Native VLAN: 666 ✓ VERIFIED  
    - Allowed VLANs: 10, 20, 30, 40, 50, 99 ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED  
- **Per-VLAN Priorities**:  
  - VLAN 10: 32768 ✓ VERIFIED  
  - VLAN 20: 32768 ✓ VERIFIED  
  - VLAN 30: 32768 ✓ VERIFIED  
  - VLAN 40: 32768 ✓ VERIFIED  
  - VLAN 50: 32768 ✓ VERIFIED  
  - VLAN 99: 32768 ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Enabled on VLANs 10, 20, 30, 40, 50 ✓ VERIFIED  
  - Information Option: Disabled ✓ VERIFIED  
- **Dynamic ARP Inspection**: Enabled on VLANs 10, 20, 30, 40, 50 ✓ VERIFIED  
- **Port Security Enabled**: 8 interfaces ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  

**Access Control Lists**:  
- **Standard ACL 'MGMT-ACCESS'**:  
  - `permit 10.99.0.0 0.0.0.255` ✓ VERIFIED  
  - `permit 10.99.1.0 0.0.0.255` ✓ VERIFIED  
  - `deny any log` ✓ VERIFIED  

---

## Network Services
### Logging
- **Logging Server**: 10.99.0.50, 10.99.0.51 ✓ VERIFIED  

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED  
- **NTP Authentication**: Enabled ✓ VERIFIED  

### DNS
- **Domain Name**: prod.bedrift.no ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only VTY access with version 2 and timeout (config line: `ip ssh version 2`, `ip ssh time-out 60`)  
- AAA with TACACS+ integration for authentication, authorization, and accounting  
- Port security with sticky MAC addresses and violation modes (e.g., `switchport port-security violation restrict`)  
- DHCP snooping and DAI enabled on VLANs 10-50  
- CDP disabled to prevent lateral discovery  
- Management access restricted via ACL `MGMT-ACCESS`  

#### ⚠ Areas for Improvement
- 802.1X not configured for wired access control  
- IP Source Guard not enabled despite DHCP snooping  
- Native VLAN 666 is non-standard and could be exploited if untrusted  
- No NTP authentication for the second NTP server (config line: `<REDACTED> server 10.99.0.1 key 15`)  

#### Recommendations
- Enable 802.1X for wired endpoints to enforce authentication  
- Implement IP Source Guard on VLANs with DHCP snooping  
- Change native VLAN to a non-routed VLAN (e.g., VLAN 999)  
- Ensure all NTP servers use authentication keys  
- Consider enabling SNMPv3 for secure management  

---

## Summary

**Device Role**: Access layer switch (~ INFERRED)  
- Justification: High number of access ports with port security, no routing, and trunk uplinks to distribution layer.  

**Overall Configuration Quality**: Strong security baseline with critical protections (DHCP snooping, DAI, AAA), but missing advanced controls like 802.1X and IP Source Guard.  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-16T07:59:05.634888