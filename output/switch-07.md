# Network Device Documentation: core-sw01

## Device Information
- **Hostname**: core-sw01 ✓ VERIFIED  
- **IOS Version**: 15.2(4)E10 ✓ VERIFIED  
- **Domain Name**: backbone.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: VLAN 10 ✓ VERIFIED  
- **IP Address**: 10.10.0.1 ✓ VERIFIED  
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED  
- **Default Gateway**: None ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **Console**: line con 0 ✓ VERIFIED  
- **VTY Lines**: line vty 0 4 ✓ VERIFIED  
- **VTY Transport Input**: ssh ✓ VERIFIED  
- **Banner**: Configured (login banner: "ADVARSEL: Kun autorisert tilgang. All aktivitet logges.") ✓ VERIFIED  

---

## AAA Configuration
- **AAA**: Enabled ✓ VERIFIED  
  - **Authentication Lists**:  
    - `aaa authentication login default local` ✓ VERIFIED  
    - `aaa authentication login CONSOLE local` ✓ VERIFIED  
  - **Authorization Lists**:  
    - `aaa authorization exec default local` ✓ VERIFIED  
  - **Accounting**:  
    - `aaa accounting exec default start-stop group tacacs+` ✓ VERIFIED  
  - **TACACS+ Servers**: 10.99.0.40, 10.99.0.41 ✓ VERIFIED  
  - **Local Users**:  
    - `coreAdmin` (privilege 15) ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 8 ✓ VERIFIED  
- **VLAN IDs and Names**:  
  - VLAN 10: Ansatte ✓ VERIFIED  
  - VLAN 20: Gjest ✓ VERIFIED  
  - VLAN 30: Skrivere ✓ VERIFIED  
  - VLAN 50: VoIP ✓ VERIFIED  
  - VLAN 99: Management ✓ VERIFIED  
  - VLAN 100: Server-Prod ✓ VERIFIED  
  - VLAN 200: Server-Dev ✓ VERIFIED  
  - VLAN 666: Native VLAN (not named) ✓ VERIFIED  

- **SVI Details**:  
  - **VLAN 1**: Status: Shutdown ✓ VERIFIED  
  - **VLAN 10**: IP: 10.10.0.1 255.255.255.0 | Status: Active ✓ VERIFIED  
  - **VLAN 20**: IP: 10.20.0.1 255.255.255.0 | Status: Active ✓ VERIFIED  
  - **VLAN 30**: IP: 10.30.0.1 255.255.255.0 | Status: Active ✓ VERIFIED  
  - **VLAN 50**: IP: 10.50.0.1 255.255.255.0 | Status: Active ✓ VERIFIED  
  - **VLAN 99**: IP: 10.99.1.1 255.255.255.0 | ACL In: MGMT-ACCESS | Status: Active ✓ VERIFIED  
  - **VLAN 100**: IP: 10.100.0.1 255.255.255.0 | Status: Active ✓ VERIFIED  
  - **VLAN 200**: IP: 10.200.0.1 255.255.255.0 | Status: Active ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 10 ✓ VERIFIED  
- **Active (no shutdown)**: 8 ✓ VERIFIED  
- **Shutdown**: 2 ✓ VERIFIED  

### Active Interfaces
1. **Port-channel1**  
   - Description: "EtherChannel til dis-sw01" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  

2. **Port-channel2**  
   - Description: "EtherChannel til dis-sw02" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  

3. **GigabitEthernet0/1**  
   - Description: "dis-sw01 gig0/1 - Po1" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  

4. **GigabitEthernet0/2**  
   - Description: "dis-sw01 gig0/2 - Po1" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  

5. **GigabitEthernet0/3**  
   - Description: "dis-sw02 gig0/1 - Po2" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  

6. **GigabitEthernet0/4**  
   - Description: "dis-sw02 gig0/2 - Po2" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  

7. **GigabitEthernet0/5**  
   - Description: "Server-Prod svitsj" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 99, 100, 200 ✓ VERIFIED  

8. **GigabitEthernet0/6**  
   - Description: "WAN-ruter gig0/0" ✓ VERIFIED  
   - Mode: None ✓ VERIFIED  
   - Subnet: 255.255.255.252 ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED  
- **Per-VLAN Priorities**: Not configured ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED  
- **Port Security**: Not configured on any interfaces ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  

### Access Control Lists (ACLs)
- **Standard ACL 'MGMT-ACCESS'**:  
  - `permit 10.99.0.0 0.0.0.255` ✓ VERIFIED  
  - `permit 10.99.1.0 0.0.0.255` ✓ VERIFIED  
  - `deny any` ✓ VERIFIED  

- **Extended ACL 'DENY-GUEST-TO-INTERNAL'**:  
  - `deny ip 10.20.0.0 0.0.0.255 10.10.0.0 0.0.0.255` ✓ VERIFIED  
  - `deny ip 10.20.0.0 0.0.0.255 10.30.0.0 0.0.0.255` ✓ VERIFIED  
  - `deny ip 10.20.0.0 0.0.0.255 10.50.0.0 0.0.0.255` ✓ VERIFIED  
  - `deny ip 10.20.0.0 0.0.0.255 10.99.0.0 0.0.1.255` ✓ VERIFIED  
  - `deny ip 10.20.0.0 0.0.0.255 10.100.0.0 0.0.0.255` ✓ VERIFIED  
  - `deny ip 10.20.0.0 0.0.0.255 10.200.0.0 0.0.0.255` ✓ VERIFIED  
  - `permit ip any any` ✓ VERIFIED  

---

## Network Services
### Logging
- **Logging Server**: 10.99.0.50, 10.99.0.51 ✓ VERIFIED  
- **Logging Source Interface**: Vlan99 ✓ VERIFIED  

### NTP
- **NTP Server**: 129.240.2.6, 10.99.0.1 ✓ VERIFIED  
- **NTP Authentication**: Enabled with key 1 ✓ VERIFIED  

### DNS
- **Domain Name**: backbone.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Enabled ✓ VERIFIED  
- **Routing Protocol**: OSPF ✓ VERIFIED  
  - **Router ID**: 10.99.1.1 ✓ VERIFIED  
  - **Networks**:  
    - 10.10.0.0 255.255.255.0 area 0 ✓ VERIFIED  
    - 10.20.0.0 255.255.255.0 area 0 ✓ VERIFIED  
    - 10.30.0.0 255.255.255.0 area 0 ✓ VERIFIED  
    - 10.50.0.0 255.255.255.0 area 0 ✓ VERIFIED  
    - 10.99.1.0 255.255.255.0 area 0 ✓ VERIFIED  
    - 10.100.0.0 255.255.255.0 area 0 ✓ VERIFIED  
    - 10.200.0.0 255.255.255.0 area 0 ✓ VERIFIED  
    - 10.255.0.0 255.255.255.252 area 0 ✓ VERIFIED  
  - **Passive Interfaces**: Vlan10, Vlan20, Vlan30, Vlan50, Vlan100, Vlan200 ✓ VERIFIED  
  - **Default Route**: `default-information originate` ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only VTY access with version 2 and 60-second timeout ✓ VERIFIED  
- AAA authentication with local and TACACS+ integration ✓ VERIFIED  
- Management VLAN (VLAN 99) with ACL (`MGMT-ACCESS`) restricting access ✓ VERIFIED  
- Extended ACL (`DENY-GUEST-TO-INTERNAL`) blocking guest VLAN (VLAN 20) traffic to internal networks ✓ VERIFIED  
- CDP disabled to prevent lateral discovery ✓ VERIFIED  

#### ⚠ Areas for Improvement
- DHCP snooping and Dynamic ARP Inspection (DAI) are not enabled, leaving VLANs vulnerable to spoofing attacks ? UNCERTAIN  
- Port security is not configured on any interfaces, increasing risk of unauthorized device access ? UNCERTAIN  
- 802.1X is not implemented, missing layer of endpoint authentication ? UNCERTAIN  
- Native VLAN 666 is not named, increasing risk of misconfiguration ? UNCERTAIN  

#### Recommendations
- Enable DHCP snooping on VLANs 10, 20, 30, 50, 99, 100, 200 to prevent rogue DHCP servers  
- Implement port security on access ports (if any) to limit MAC addresses per port  
- Consider enabling 802.1X for endpoint authentication on VLANs requiring stricter access control  
- Rename native VLAN 666 to a descriptive name (e.g., "Native-Untagged") for clarity  
- Ensure NTP servers are reachable and synchronized to prevent time-based vulnerabilities  

---

## Summary

**Device Role**: Core layer switch (~ INFERRED)  
- High-speed trunk ports, routing protocols (OSPF), and inter-VLAN routing indicate a core/distribution role.  
- Aggregates traffic between access switches (dis-sw01, dis-sw02) and connects to a WAN router.  

**Configuration Quality**:  
- Strong security practices for management access and ACLs are in place.  
- Missing critical security features (DHCP snooping, port security) could expose the network to lateral threats.  
- Configuration is well-documented and logically structured.  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-17T19:47:39.137356