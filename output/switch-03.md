# Network Device Documentation: switch-03

## Device Information
- **Hostname**: switch-03 ✓ VERIFIED  
- **IOS Version**: 15.0(2)SE4 ✓ VERIFIED  
- **Domain Name**: intern.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: 99 ✓ VERIFIED  
- **IP Address**: 10.99.1.3 ✓ VERIFIED  
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **Console**: line con 0 ✓ VERIFIED  
- **VTY Lines**: line vty 0 4 ✓ VERIFIED  
- **VTY Transport Input**: ssh ✓ VERIFIED  
- **Banner**: Configured (line: `banner login ^CUautorisert tilgang er forbudt. All aktivitet logges.^C`) ✓ VERIFIED  

---

## AAA Configuration
- **AAA**: Not enabled ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED  
- **VLAN IDs and Names**:  
  - VLAN 10: Ansatte ✓ VERIFIED  
  - VLAN 20: Gjest ✓ VERIFIED  
  - VLAN 30: Skrivere ✓ VERIFIED  
  - VLAN 99: Mgmt ✓ VERIFIED  
  - VLAN 666: Not configured ✓ VERIFIED  

- **VLAN Interfaces (SVIs)**:  
  - **VLAN 1**: Status: Shutdown ✓ VERIFIED  
  - **VLAN 99**:  
    - Description: Management SVI ✓ VERIFIED  
    - IP: 10.99.1.3 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - ACL In: MGMT-ACCESS ✓ VERIFIED  

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
- **Dynamic ARP Inspection**: ✓ Enabled on VLANs 10, 20, 30 ✓ VERIFIED  
- **Access Control Lists**:  
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

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED  
- **NTP Authentication**: Disabled ✓ VERIFIED  

### DNS
- **Domain Name**: intern.bedrift.no ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only VTY access with version 2 and 60-second timeout ✓ VERIFIED  
- Port security configured on 6 access ports with violation modes (restrict/protect/shutdown) ✓ VERIFIED  
- DHCP snooping and Dynamic ARP Inspection enabled on VLANs 10, 20, 30 ✓ VERIFIED  
- CDP disabled to prevent lateral discovery ✓ VERIFIED  
- Management access restricted via ACL `MGMT-ACCESS` ✓ VERIFIED  

#### ⚠ Areas for Improvement
- **802.1X** is not configured, leaving access ports vulnerable to unauthorized device access ~ INFERRED  
- **SNMP** is not configured, missing monitoring and management capabilities ~ INFERRED  
- **Unused ports** (18 shutdown) should be explicitly secured with port security or shutdown ~ INFERRED  
- **Native VLAN 666** on trunks is non-standard and could be exploited ~ INFERRED  

#### Recommendations
- Enable **802.1X** on all access ports for stronger endpoint authentication ~ INFERRED  
- Configure **SNMP** with secure community strings and access control ~ INFERRED  
- Apply **port security** to all unused ports or ensure they remain shutdown ~ INFERRED  
- Change **native VLAN** on trunks to a non-routed VLAN (e.g., VLAN 99) to mitigate VLAN hopping ~ INFERRED  
- Enable **IP Source Guard** on VLANs 10, 20, 30 to prevent IP spoofing ~ INFERRED  

---

## Summary

This device, **switch-03**, is an **Access Layer Switch** serving end-user devices (employees, guests, printers) and connecting to distribution switches via dual uplinks. It employs strong port security, DHCP snooping, and SSH access control. However, missing features like 802.1X and SNMP reduce its security and manageability. The configuration is well-structured but requires modernization to align with best practices.  

**Device Role**: Access Layer Switch ~ INFERRED  
**Security Posture**: Moderate (good practices present but gaps exist) ~ INFERRED  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-17T19:32:30.125750