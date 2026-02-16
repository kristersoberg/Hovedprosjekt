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
- **Banner**: Configured (login banner) ✓ VERIFIED  

---

## AAA Configuration
- **AAA**: Enabled ✓ VERIFIED  
  - **Authentication Lists**:  
    - `aaa authentication login default local`  
    - `aaa authentication login CONSOLE local`  
  - **Authorization Lists**:  
    - `aaa authorization exec default local`  
  - **Accounting**:  
    - `aaa accounting exec default start-stop group tacacs+`  
  - **TACACS+ Servers**: 10.99.0.40, 10.99.0.41 ✓ VERIFIED  
  - **Local Users**:  
    - `coreAdmin` (privilege 15) ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 8 ✓ VERIFIED  
- **VLAN IDs and Names**:  
  - VLAN 10: Ansatte  
  - VLAN 20: Gjest  
  - VLAN 30: Skrivere  
  - VLAN 50: VoIP  
  - VLAN 99: Management  
  - VLAN 100: Server-Prod  
  - VLAN 200: Server-Dev  
  - VLAN 666: Not named (referenced in trunk native VLAN)  
- **SVI Details**:  
  - **VLAN 1**: Shutdown  
  - **VLAN 10**: Active, IP 10.10.0.1/24  
  - **VLAN 20**: Active, IP 10.20.0.1/24  
  - **VLAN 30**: Active, IP 10.30.0.1/24  
  - **VLAN 50**: Active, IP 10.50.0.1/24  
  - **VLAN 99**: Active, IP 10.99.1.1/24, ACL In: MGMT-ACCESS  
  - **VLAN 100**: Active, IP 10.100.0.1/24  
  - **VLAN 200**: Active, IP 10.200.0.1/24  

---

## Physical Interfaces
- **Total Interfaces**: 10 ✓ VERIFIED  
- **Active (no shutdown)**: 8 ✓ VERIFIED  
- **Shutdown**: 2 (GigabitEthernet0/7, GigabitEthernet0/8) ✓ VERIFIED  

### Active Interfaces
1. **Port-channel1**  
   - Description: "EtherChannel til dis-sw01"  
   - Mode: trunk  
   - Encapsulation: dot1q  
   - Native VLAN: 666  
   - Allowed VLANs: 10, 20, 30, 50, 99  

2. **Port-channel2**  
   - Description: "EtherChannel til dis-sw02"  
   - Mode: trunk  
   - Encapsulation: dot1q  
   - Native VLAN: 666  
   - Allowed VLANs: 10, 20, 30, 50, 99  

3. **GigabitEthernet0/1**  
   - Description: "dis-sw01 gig0/1 - Po1"  
   - Mode: trunk  
   - Encapsulation: dot1q  
   - Native VLAN: 666  
   - Allowed VLANs: 10, 20, 30, 50, 99  

4. **GigabitEthernet0/2**  
   - Description: "dis-sw01 gig0/2 - Po1"  
   - Mode: trunk  
   - Encapsulation: dot1q  
   - Native VLAN: 666  
   - Allowed VLANs: 10, 20, 30, 50, 99  

5. **GigabitEthernet0/3**  
   - Description: "dis-sw02 gig0/1 - Po2"  
   - Mode: trunk  
   - Encapsulation: dot1q  
   - Native VLAN: 666  
   - Allowed VLANs: 10, 20, 30, 50, 99  

6. **GigabitEthernet0/4**  
   - Description: "dis-sw02 gig0/2 - Po2"  
   - Mode: trunk  
   - Encapsulation: dot1q  
   - Native VLAN: 666  
   - Allowed VLANs: 10, 20, 30, 50, 99  

7. **GigabitEthernet0/5**  
   - Description: "Server-Prod svitsj"  
   - Mode: trunk  
   - Encapsulation: dot1q  
   - Native VLAN: 666  
   - Allowed VLANs: 99, 100, 200  

8. **GigabitEthernet0/6**  
   - Description: "WAN-ruter gig0/0"  
   - Mode: None  
   - Subnet: 255.255.255.252  

---

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED  
- **Per-VLAN Priorities**: Not configured ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED  
- **Port Security**: Not enabled on any interfaces ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  

### Access Control Lists (ACLs)
- **Standard ACL 'MGMT-ACCESS'**:  
  - `permit 10.99.0.0 0.0.0.255`  
  - `permit 10.99.1.0 0.0.0.255`  
  - `deny any`  

- **Extended ACL 'DENY-GUEST-TO-INTERNAL'**:  
  - `deny ip 10.20.0.0 0.0.0.255 10.10.0.0 0.0.0.255`  
  - `deny ip 10.20.0.0 0.0.0.255 10.30.0.0 0.0.0.255`  
  - `deny ip 10.20.0.0 0.0.0.255 10.50.0.0 0.0.0.255`  
  - `deny ip 10.20.0.0 0.0.0.255 10.99.0.0 0.0.1.255`  
  - `deny ip 10.20.0.0 0.0.0.255 10.100.0.0 0.0.0.255`  
  - `deny ip 10.20.0.0 0.0.0.255 10.200.0.0 0.0.0.255`  
  - `permit ip any any`  

---

## Network Services
### Logging
- **Logging Server**: 10.99.0.50, 10.99.0.51 ✓ VERIFIED  
- **Logging Source Interface**: Vlan99 ✓ VERIFIED  

### NTP
- **NTP Server**: Not configured ✓ VERIFIED  
- **NTP Authentication**: Not configured ✓ VERIFIED  

### DNS
- **Domain Name**: backbone.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Enabled ✓ VERIFIED  
- **Routing Protocol**: OSPF  
  - **Router ID**: 10.99.1.1  
  - **Networks**:  
    - 10.10.0.0/24 area 0  
    - 10.20.0.0/24 area 0  
    - 10.30.0.0/24 area 0  
    - 10.50.0.0/24 area 0  
    - 10.99.1.0/24 area 0  
    - 10.100.0.0/24 area 0  
    - 10.200.0.0/24 area 0  
    - 10.255.0.0/30 area 0  
  - **Passive Interfaces**: Vlan10, Vlan20, Vlan30, Vlan50, Vlan100, Vlan200  
  - **Default Route**: `default-information originate`  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only access with version 2 and 60-second timeout  
- AAA authentication with local and TACACS+ integration  
- ACLs for management access and guest traffic isolation  
- CDP disabled to prevent lateral discovery  

#### ⚠ Areas for Improvement
- Missing DHCP snooping and port security for VLANs  
- No NTP configuration for time synchronization  
- No 802.1X or IP source guard for endpoint validation  
- Native VLAN 666 is unassigned and could be exploited  

#### Recommendations
- Enable DHCP snooping on VLANs 10, 20, 30, 50, 99, 100, 200  
- Implement port security on access ports (if any)  
- Configure NTP with trusted servers and authentication  
- Rename VLAN 666 to a descriptive name and ensure it's not used  
- Consider enabling 802.1X for endpoint authentication  

---

## Summary

**Device Role**: Core layer switch (~ INFERRED)  
- Aggregates distribution switches (dis-sw01, dis-sw02)  
- Provides routing between VLANs and external WAN connectivity  
- Centralizes management and security policies  

**Configuration Quality**:  
- Comprehensive VLAN and routing configuration ✓ VERIFIED  
- Strong access control via ACLs and AAA ✓ VERIFIED  
- Missing critical security features like DHCP snooping and NTP ~ INFERRED  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-16T08:44:23.301353