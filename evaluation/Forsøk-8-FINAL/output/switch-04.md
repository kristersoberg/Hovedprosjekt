# Network Device Documentation: dis-sw01

## Device Information
- **Hostname**: dis-sw01 ✓ VERIFIED  
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED  
- **Domain Name**: core.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: VLAN 10 ✓ VERIFIED  
- **IP Address**: 10.10.0.2 ✓ VERIFIED  
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **Console**: line con 0 ✓ VERIFIED  
- **VTY Lines**: line vty 0 4 ✓ VERIFIED  
- **VTY Transport Input**: ssh ✓ VERIFIED  
- **Banner**: Configured (Unauthorized access is forbidden. All activity is logged.) ✓ VERIFIED  

---

## AAA Configuration
- **AAA**: Enabled ✓ VERIFIED  
  - **Authentication Lists**:  
    - `aaa authentication login default local`  
    - `aaa authentication login CONSOLE local`  
  - **Authorization Lists**:  
    - `aaa authorization exec default local`  
  - **Local Users**:  
    - `netadmin` (privilege 15)  

---

## VLANs
- **Total VLANs Referenced**: 6 ✓ VERIFIED  
- **VLAN IDs and Names**:  
  - VLAN 10: Ansatte  
  - VLAN 20: Gjest  
  - VLAN 30: Skrivere  
  - VLAN 50: VoIP  
  - VLAN 99: Management  
  - VLAN 666: Native VLAN (not named)  

- **SVI Details**:  
  - **VLAN 1**:  
    - Status: Shutdown  
  - **VLAN 10**:  
    - Description: Ansatte Gateway  
    - IP: 10.10.0.2 255.255.255.0  
    - Status: Active  
    - HSRP: Configured  
  - **VLAN 20**:  
    - Description: Gjest Gateway  
    - IP: 10.20.0.2 255.255.255.0  
    - Status: Active  
    - HSRP: Configured  
  - **VLAN 30**:  
    - Description: Skrivere Gateway  
    - IP: 10.30.0.2 255.255.255.0  
    - Status: Active  
    - HSRP: Configured  
  - **VLAN 50**:  
    - Description: VoIP Gateway  
    - IP: 10.50.0.2 255.255.255.0  
    - Status: Active  
    - HSRP: Configured  
  - **VLAN 99**:  
    - Description: Management  
    - IP: 10.99.1.2 255.255.255.0  
    - Status: Active  
    - ACL In: MGMT-ACCESS  

- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 6 ✓ VERIFIED  
- **Active (no shutdown)**: 4 ✓ VERIFIED  
- **Shutdown**: 2 ✓ VERIFIED  

### Active Interfaces
1. **GigabitEthernet0/1**  
   - Description: "Uplink til core-sw01 gig0/1"  
   - Mode: trunk  
   - Encapsulation: dot1q  
   - Native VLAN: 666  
   - Allowed VLANs: 10, 20, 30, 50, 99  

2. **GigabitEthernet0/2**  
   - Description: "Uplink til core-sw01 gig0/2"  
   - Mode: trunk  
   - Encapsulation: dot1q  
   - Native VLAN: 666  
   - Allowed VLANs: 10, 20, 30, 50, 99  

3. **GigabitEthernet0/3**  
   - Description: "Downlink aksess-sw03 fa0/23"  
   - Mode: trunk  
   - Encapsulation: dot1q  
   - Native VLAN: 666  
   - Allowed VLANs: 10, 20, 30, 99  

4. **GigabitEthernet0/4**  
   - Description: "Downlink aksess-sw04 fa0/23"  
   - Mode: trunk  
   - Encapsulation: dot1q  
   - Native VLAN: 666  
   - Allowed VLANs: 10, 20, 30, 99  

- **Port Security Enabled**: 0 interfaces ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED  
- **Per-VLAN Priorities**:  
  - VLAN 10: 4096  
  - VLAN 20: 4096  
  - VLAN 30: 4096  
  - VLAN 50: 4096  
  - VLAN 99: 4096  

---

## Security Features
- **DHCP Snooping**: Enabled on VLANs Not specified ✓ VERIFIED  
  - Information Option: Enabled  
- **Dynamic ARP Inspection**: Not enabled ✓ VERIFIED  
- **Port Security**: Not configured ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  

### Access Control Lists
- **Standard ACL 'MGMT-ACCESS'**:  
  - `permit 10.99.0.0 0.0.0.255`  
  - `permit 10.99.1.0 0.0.0.255`  
  - `deny any`  

- **Extended ACL 'BLOCK-GUEST-INTERNAL'**:  
  - `deny ip 10.20.0.0 0.0.0.255 10.10.0.0 0.0.0.255`  
  - `deny ip 10.20.0.0 0.0.0.255 10.30.0.0 0.0.0.255`  
  - `deny ip 10.20.0.0 0.0.0.255 10.50.0.0 0.0.0.255`  
  - `deny ip 10.20.0.0 0.0.0.255 10.99.0.0 0.0.1.255`  
  - `permit ip 10.20.0.0 0.0.0.255 any`  

- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  

---

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED  
- **NTP Authentication**: Disabled ✓ VERIFIED  

### DNS
- **Domain Name**: core.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Enabled ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **Static Routes**:  
  - `0.0.0.0 0.0.0.0 via 10.99.1.1`  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only VTY access with timeout (line vty 0 4, `transport input ssh`)  
- DHCP snooping enabled (VLANs unspecified)  
- CDP disabled (prevents lateral discovery)  
- ACLs for management access and guest traffic isolation  
- Port security not required for trunk interfaces  

#### ⚠ Areas for Improvement
- **Missing Dynamic ARP Inspection (DAI)**: Vulnerable to ARP spoofing attacks  
- **No 802.1X**: Guest VLAN (VLAN 20) lacks authentication  
- **No IP Source Guard**: Vulnerable to IP spoofing  
- **DHCP Snooping VLANs unspecified**: Should explicitly define VLANs for enforcement  
- **No port security on access ports**: Not applicable here, but required for access layer  

#### Recommendations
- Enable **DAI** on VLANs with DHCP snooping  
- Implement **802.1X** for guest VLAN (VLAN 20)  
- Configure **IP Source Guard** on VLANs with DHCP snooping  
- Specify **VLANs for DHCP snooping** (e.g., VLANs 10, 20, 30, 50, 99)  
- Consider **port security** if access ports are added in the future  

---

## Summary

**Device Role**: Distribution layer switch (~ INFERRED)  
- Justification: Inter-VLAN routing (SVIs), trunk interfaces, and aggregation of access switches (aksess-sw03/04)  

**Configuration Quality**: High (~ INFERRED)  
- Comprehensive VLAN and routing configuration  
- Strong access control with ACLs  
- Missing critical security features (DAI, 802.1X)  

**Purpose**: Aggregates access switches and provides inter-VLAN routing for a multi-VLAN network (~ INFERRED)  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-17T19:36:17.620484