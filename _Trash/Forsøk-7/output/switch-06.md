# Network Device Documentation: switch-06

## Device Information
- **Hostname**: switch-06 ✓ VERIFIED  
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED  
- **Domain Name**: secure.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: 99 ✓ VERIFIED  
- **IP Address**: 10.99.1.6 ✓ VERIFIED  
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **Console**: line con 0 ✓ VERIFIED  
- **VTY Lines**: line vty 0 4 ✓ VERIFIED  
- **VTY Transport Input**: ssh ✓ VERIFIED  
- **Banner**: Configured (login banner: "ADVARSEL: Kun autorisert tilgang. All aktivitet overvakes og logges.") ✓ VERIFIED  

---

## AAA Configuration
- **AAA**: Enabled ✓ VERIFIED  
**Authentication Lists**:  
  - `aaa authentication login default group radius local` ✓ VERIFIED  
  - `aaa authentication login CONSOLE local` ✓ VERIFIED  
  - `aaa authentication dot1x default group radius` ✓ VERIFIED  
**Authorization Lists**:  
  - `aaa authorization network default group radius` ✓ VERIFIED  
**Accounting**:  
  - `aaa accounting dot1x default start-stop group radius` ✓ VERIFIED  
**RADIUS Servers**: 10.99.0.30, 10.99.0.31 ✓ VERIFIED  
**Local Users**:  
  - `emergency-admin` (privilege 15) ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED  
- **VLAN IDs and Names**:  
  - VLAN 10: Ansatte-Autentisert ✓ VERIFIED  
  - VLAN 20: Gjest-Begrenset ✓ VERIFIED  
  - VLAN 99: Management ✓ VERIFIED  
  - VLAN 666: Not configured (native VLAN on trunks) ✓ VERIFIED  
  - VLAN 999: Karantene ✓ VERIFIED  
- **VLAN Interfaces (SVIs)**:  
  - **VLAN 1**: Status: Shutdown ✓ VERIFIED  
  - **VLAN 99**:  
    - Description: Management SVI ✓ VERIFIED  
    - IP: 10.99.1.6 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - ACL In: MGMT-ACCESS (standard) ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED  
- **Active (no shutdown)**: 6 ✓ VERIFIED  
- **Shutdown**: 20 ✓ VERIFIED  

**Active Interfaces**:  
1. **FastEthernet0/1**  
   - Description: "802.1X-port kontor C301" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: restrict) ✓ VERIFIED  
2. **FastEthernet0/2**  
   - Description: "802.1X-port kontor C302" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: restrict) ✓ VERIFIED  
3. **FastEthernet0/3**  
   - Description: "802.1X-port kontor C303" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: restrict) ✓ VERIFIED  
4. **FastEthernet0/4**  
   - Description: "802.1X-port kontor C304" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: restrict) ✓ VERIFIED  
5. **FastEthernet0/23**  
   - Description: "Uplink-1 dis-sw01 gig0/5" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 99, 999 ✓ VERIFIED  
6. **FastEthernet0/24**  
   - Description: "Uplink-2 dis-sw02 gig0/5" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 99, 999 ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED  
**Per-VLAN Priorities**:  
  - VLAN 10: 32768 ✓ VERIFIED  
  - VLAN 20: 32768 ✓ VERIFIED  
  - VLAN 99: 32768 ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Enabled on VLANs 10, 20 ✓ VERIFIED  
  - Information Option: Disabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Enabled on VLANs 10, 20 ✓ VERIFIED  
- **Access Control Lists (ACLs)**:  
  - **Standard ACL 'MGMT-ACCESS'**:  
    - `permit 10.99.0.0 0.0.0.255` ✓ VERIFIED  
    - `permit 10.99.1.0 0.0.0.255` ✓ VERIFIED  
    - `deny any` ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  
- **802.1X**: Enabled ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  

---

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  
- **Logging Level**: informational ✓ VERIFIED  

### NTP
- **NTP Server**: Not configured ✓ VERIFIED  
- **NTP Authentication**: Not configured ✓ VERIFIED  

### DNS
- **Domain Name**: secure.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only VTY access with version 2 and 60-second timeout (config lines: `ip ssh version 2`, `ip ssh time-out 60`) ✓ VERIFIED  
- Port security with violation mode `restrict` on 4 access ports (config lines: `switchport port-security violation restrict`) ✓ VERIFIED  
- DHCP snooping and DAI enabled on VLANs 10, 20 (config lines: `ip dhcp snooping vlan 10,20`, `ip arp inspection vlan 10,20`) ✓ VERIFIED  
- 802.1X authentication with RADIUS integration (config lines: `dot1x system-auth-control`, `aaa authentication dot1x default group radius`) ✓ VERIFIED  
- CDP disabled (config line: `no cdp run`) ✓ VERIFIED  

#### ⚠ Areas for Improvement
- NTP not configured (missing time synchronization) ? UNCERTAIN  
- SNMP not configured (missing monitoring capabilities) ? UNCERTAIN  
- No LLDP for network discovery ? UNCERTAIN  
- No IP Source Guard configured despite DHCP snooping (missing IP spoofing protection) ? UNCERTAIN  
- No password complexity requirements for local user `emergency-admin` ? UNCERTAIN  

#### Recommendations
- Configure NTP with authentication for time synchronization  
- Enable SNMP with secure community strings for monitoring  
- Implement LLDP for network device discovery  
- Enable IP Source Guard on VLANs with DHCP snooping  
- Enforce password complexity policies for local users  

---

## Summary

This device is an **Access Layer Switch** (~ INFERRED) based on its configuration of 802.1X authentication, port security, and trunk uplinks to distribution switches. The configuration quality is **Good** (~ INFERRED) with strong security practices like SSH, DHCP snooping, and 802.1X, but lacks some monitoring and time synchronization capabilities. The device serves as an edge switch for authenticated employee access (VLAN 10) and guest access (VLAN 20), with a dedicated management VLAN (VLAN 99).  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-16T08:40:59.906889