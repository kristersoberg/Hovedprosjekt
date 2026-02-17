# Network Device Documentation: switch-06

## Device Information
- **Hostname**: switch-06 ✓ VERIFIED  
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED  
- **Domain Name**: secure.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: VLAN 99 ✓ VERIFIED  
- **IP Address**: 10.99.1.6 ✓ VERIFIED  
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **Console**: `line con 0` ✓ VERIFIED  
- **VTY Lines**: `line vty 0 4` ✓ VERIFIED  
- **VTY Transport Input**: `ssh` ✓ VERIFIED  
- **Banner**: Configured (login banner: `ADVARSEL: Kun autorisert tilgang. All aktivitet overvakes og logges.`) ✓ VERIFIED  

---

## AAA Configuration
- **AAA**: Enabled ✓ VERIFIED  
- **Authentication Lists**:  
  - `aaa authentication login default group radius local`  
  - `aaa authentication login CONSOLE local`  
  - `aaa authentication dot1x default group radius`  
- **Authorization Lists**:  
  - `aaa authorization network default group radius`  
- **Accounting**:  
  - `aaa accounting dot1x default start-stop group radius`  
- **RADIUS Servers**: 10.99.0.30, 10.99.0.31 ✓ VERIFIED  
- **Local Users**:  
  - `emergency-admin` (privilege 15) ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED  
- **VLAN IDs and Names**:  
  - VLAN 10: Ansatte-Autentisert  
  - VLAN 20: Gjest-Begrenset  
  - VLAN 99: Management  
  - VLAN 666: (Unnamed)  
  - VLAN 999: Karantene  
- **SVI Details**:  
  - **VLAN 1**: Shutdown  
  - **VLAN 99**:  
    - Description: Management SVI  
    - IP: 10.99.1.6 255.255.255.0  
    - Status: Active  
    - ACL In: `MGMT-ACCESS`  

---

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED  
- **Active (no shutdown)**: 6 ✓ VERIFIED  
- **Shutdown**: 20 ✓ VERIFIED  

### Active Interfaces
1. **FastEthernet0/1**  
   - Description: `802.1X-port kontor C301`  
   - Mode: access  
   - VLAN: 10  
   - Port-Sec: ✓ (violation: restrict)  

2. **FastEthernet0/2**  
   - Description: `802.1X-port kontor C302`  
   - Mode: access  
   - VLAN: 10  
   - Port-Sec: ✓ (violation: restrict)  

3. **FastEthernet0/3**  
   - Description: `802.1X-port kontor C303`  
   - Mode: access  
   - VLAN: 10  
   - Port-Sec: ✓ (violation: restrict)  

4. **FastEthernet0/4**  
   - Description: `802.1X-port kontor C304`  
   - Mode: access  
   - VLAN: 10  
   - Port-Sec: ✓ (violation: restrict)  

5. **FastEthernet0/23**  
   - Description: `Uplink-1 dis-sw01 gig0/5`  
   - Mode: trunk  
   - Encapsulation: dot1q  
   - Native VLAN: 666  
   - Allowed VLANs: 10, 20, 99, 999  

6. **FastEthernet0/24**  
   - Description: `Uplink-2 dis-sw02 gig0/5`  
   - Mode: trunk  
   - Encapsulation: dot1q  
   - Native VLAN: 666  
   - Allowed VLANs: 10, 20, 99, 999  

---

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED  
- **Per-VLAN Priorities**:  
  - VLAN 10: 32768  
  - VLAN 20: 32768  
  - VLAN 99: 32768  

---

## Security Features
- **DHCP Snooping**: Enabled on VLANs 10, 20 ✓ VERIFIED  
  - Information Option: Disabled  
- **Dynamic ARP Inspection**: Enabled on VLANs 10, 20 ✓ VERIFIED  
- **Access Control Lists**:  
  - **Standard ACL `MGMT-ACCESS`**:  
    - `permit 10.99.0.0 0.0.0.255`  
    - `permit 10.99.1.0 0.0.0.255`  
    - `deny any`  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  
- **802.1X**: Enabled ✓ VERIFIED  
- **Port Security**: Enabled on 4 interfaces (violation: restrict) ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  

---

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  
- **Logging Level**: informational  

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
- SSH-only VTY access with version 2 and 60-second timeout  
- Port security with violation mode `restrict` on 4 access ports  
- DHCP snooping and Dynamic ARP Inspection enabled on VLANs 10, 20  
- 802.1X authentication configured for access ports  
- Management access restricted via ACL `MGMT-ACCESS`  
- CDP disabled to prevent lateral discovery  

#### ⚠ Areas for Improvement
- NTP not configured (critical for log correlation and time-based security)  
- SNMP not configured (missing monitoring and management capabilities)  
- IP Source Guard not enabled (could prevent IP spoofing)  
- No VTP configuration (risk of VLAN mismanagement if expanded)  
- No LLDP for network discovery and troubleshooting  

#### Recommendations
- Enable and configure NTP with secure authentication  
- Implement SNMP for device monitoring  
- Enable IP Source Guard on VLANs 10 and 20  
- Consider enabling LLDP for network visibility  
- Document VLAN 666 purpose and ensure it's not used for sensitive traffic  

---

## Summary

**Device Role**: Access layer switch (~ INFERRED)  
- Justification: High number of access ports with port security and 802.1X, no routing enabled, and trunk uplinks to distribution switches.  

**Configuration Quality**: Strong security baseline with critical features like 802.1X, DHCP snooping, and port security. Missing NTP and SNMP could impact operational visibility and forensic analysis.  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-17T19:44:01.411146