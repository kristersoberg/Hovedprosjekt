# Network Device Documentation: switch-03

## Device Information
- **Hostname**: switch-03 ✓ VERIFIED  
- **IOS Version**: 15.0(2)SE4 ✓ VERIFIED  
- **Domain Name**: intern.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: VLAN 99 ✓ VERIFIED  
- **IP Address**: 10.99.1.3 ✓ VERIFIED  
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **Console**: line con 0 ✓ VERIFIED  
- **VTY Lines**: line vty 0 4 ✓ VERIFIED  
- **VTY Transport Input**: ssh ✓ VERIFIED  
- **Banner**: Configured (login banner: "Uautorisert tilgang er forbudt. All aktivitet logges.") ✓ VERIFIED  

---

## AAA Configuration
- AAA: Not enabled ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED  
- **VLAN IDs and Names**:  
  - VLAN 10: Ansatte ✓ VERIFIED  
  - VLAN 20: Gjest ✓ VERIFIED  
  - VLAN 30: Skrivere ✓ VERIFIED  
  - VLAN 99: Mgmt ✓ VERIFIED  
  - VLAN 666: Not named (native VLAN on trunks) ✓ VERIFIED  

- **VLAN Interfaces (SVIs)**:  
  - **VLAN 1**: Status: Shutdown ✓ VERIFIED  
  - **VLAN 99**:  
    - Description: Management SVI ✓ VERIFIED  
    - IP: 10.99.1.3 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - ACL In: MGMT-ACCESS (in) ✓ VERIFIED  

- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED  
- **Active (no shutdown)**: 8 ✓ VERIFIED  
- **Shutdown**: 18 ✓ VERIFIED  

### Active Interfaces
1. **FastEthernet0/1**  
   - Description: "Ansatt-PC kontor A101" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: restrict) ✓ VERIFIED  

2. **FastEthernet0/2**  
   - Description: "Ansatt-PC kontor A102" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: restrict) ✓ VERIFIED  

3. **FastEthernet0/3**  
   - Description: "Ansatt-PC kontor A103" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: restrict) ✓ VERIFIED  

4. **FastEthernet0/4**  
   - Description: "Gjestenettverk moeterom B1" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 20 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: protect) ✓ VERIFIED  

5. **FastEthernet0/5**  
   - Description: "Gjestenettverk moeterom B2" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 20 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: protect) ✓ VERIFIED  

6. **FastEthernet0/6**  
   - Description: "Nettverksskriver 3. etasje" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 30 ✓ VERIFIED  
   - Port-Sec: ✓ (violation: shutdown) ✓ VERIFIED  

7. **FastEthernet0/23**  
   - Description: "Uplink-1 dis-sw01 fa0/3" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  

8. **FastEthernet0/24**  
   - Description: "Uplink-2 dis-sw02 fa0/3" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED  
- **Per-VLAN Priorities**:  
  - VLAN 10: 32768 ✓ VERIFIED  
  - VLAN 20: 32768 ✓ VERIFIED  
  - VLAN 30: 32768 ✓ VERIFIED  
  - VLAN 99: 32768 ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: ✓ Enabled on VLANs 10, 20, 30 ✓ VERIFIED  
  - Information Option: Disabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: ✓ Enabled on VLANs 10, 20, 30 ✓ VERIFIED  
- **Port Security**: Enabled on 6 interfaces (Fa0/1-3, Fa0/4-5, Fa0/6) ✓ VERIFIED  
- **Access Control Lists (ACLs)**:  
  - **Standard ACL 'MGMT-ACCESS'**:  
    - permit 10.99.0.0 0.0.0.255 ✓ VERIFIED  
    - permit 10.99.1.0 0.0.0.255 ✓ VERIFIED  
    - deny any ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  

---

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  
- **Logging Level**: warnings (via `logging trap warnings`) ✓ VERIFIED  

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED  
- **NTP Authentication**: Disabled ✓ VERIFIED  

### DNS
- **Domain Name**: intern.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only VTY access with version 2 and 60-second timeout (config lines: `ip ssh version 2`, `ip ssh time-out 60`)  
- Port security configured on 6 access ports with violation modes (e.g., `switchport port-security violation restrict`)  
- DHCP snooping and DAI enabled on VLANs 10, 20, 30 (config lines: `ip dhcp snooping vlan 10,20,30`, `ip arp inspection vlan 10,20,30`)  
- CDP disabled (config line: `no cdp run`)  
- Management access restricted via ACL `MGMT-ACCESS` (config lines: `access-class MGMT-ACCESS in`, `access-list standard MGMT-ACCESS`)  

#### ⚠ Areas for Improvement
- Missing 802.1X authentication for secure access control  
- No SNMP configuration for monitoring  
- AAA not enabled (local authentication only)  
- No IP Source Guard configuration despite DHCP snooping  
- Native VLAN 666 is non-standard and could be exploited (should be VLAN 1)  

#### Recommendations
- Enable 802.1X authentication for wired access ports  
- Configure SNMP with secure community strings and access controls  
- Implement AAA for centralized authentication/authorization  
- Enable IP Source Guard on VLANs with DHCP snooping  
- Change native VLAN on trunks to VLAN 1 for security best practices  

---

## Summary

**Device Role**: Access layer switch (~ INFERRED)  
- Justification: High number of access ports (6 active), port security, and no routing functionality.  

**Configuration Quality**: Good baseline security with SSH, port security, and DHCP snooping, but missing advanced features like 802.1X and AAA. (~ INFERRED)  

**Overall Purpose**: Provides wired access for employees, guests, and printers, with management access restricted to the 10.99.0.0/24 network. (~ INFERRED)  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-16T08:28:26.437806