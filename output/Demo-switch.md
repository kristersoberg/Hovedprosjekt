# Network Device Documentation: dis-sw02

## Device Information
- **Hostname**: dis-sw02 ✓ VERIFIED  
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED  
- **Domain Name**: core.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: VLAN 10 ✓ VERIFIED  
- **IP Address**: 10.10.0.3 ✓ VERIFIED  
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
  - `aaa authentication login default local` ✓ VERIFIED  
  - `aaa authentication login CONSOLE local` ✓ VERIFIED  
- **Authorization Lists**:  
  - `aaa authorization exec default local` ✓ VERIFIED  
- **Local Users**:  
  - `netadmin` (privilege 15) ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 6 ✓ VERIFIED  
- **VLAN IDs and Names**:  
  - VLAN 10: Ansatte ✓ VERIFIED  
  - VLAN 20: Gjest ✓ VERIFIED  
  - VLAN 30: Skrivere ✓ VERIFIED  
  - VLAN 50: VoIP ✓ VERIFIED  
  - VLAN 99: Management ✓ VERIFIED  
  - VLAN 666: Native VLAN (not named) ✓ VERIFIED  

- **VLAN Interfaces (SVIs)**:  
  - **VLAN 1**:  
    - Status: Shutdown ✓ VERIFIED  
  - **VLAN 10**:  
    - Description: Ansatte Gateway ✓ VERIFIED  
    - IP: 10.10.0.3 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - HSRP: Configured (Group 10, IP 10.10.0.1, priority 90) ✓ VERIFIED  
  - **VLAN 20**:  
    - Description: Gjest Gateway ✓ VERIFIED  
    - IP: 10.20.0.3 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - HSRP: Configured (Group 20, IP 10.20.0.1, priority 90) ✓ VERIFIED  
  - **VLAN 30**:  
    - Description: Skrivere Gateway ✓ VERIFIED  
    - IP: 10.30.0.3 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - HSRP: Configured (Group 30, IP 10.30.0.1, priority 90) ✓ VERIFIED  
  - **VLAN 50**:  
    - Description: VoIP Gateway ✓ VERIFIED  
    - IP: 10.50.0.3 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - HSRP: Configured (Group 50, IP 10.50.0.1, priority 90) ✓ VERIFIED  
  - **VLAN 99**:  
    - Description: Management ✓ VERIFIED  
    - IP: 10.99.1.3 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - ACL In: `MGMT-ACCESS` (in) ✓ VERIFIED  

- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 6 ✓ VERIFIED  
- **Active (no shutdown)**: 4 ✓ VERIFIED  
- **Shutdown**: 2 ✓ VERIFIED  

### Active Interfaces
1. **GigabitEthernet0/1**  
   - Description: "Uplink til core-sw01 gig0/3" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  

2. **GigabitEthernet0/2**  
   - Description: "Uplink til core-sw01 gig0/4" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  

3. **GigabitEthernet0/3**  
   - Description: "Downlink aksess-sw03 fa0/24" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  

4. **GigabitEthernet0/4**  
   - Description: "Downlink aksess-sw04 fa0/24" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  

- **Port Security Enabled**: 0 interfaces ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED  
- **Per-VLAN Priorities**:  
  - VLAN 10: 8192 ✓ VERIFIED  
  - VLAN 20: 8192 ✓ VERIFIED  
  - VLAN 30: 8192 ✓ VERIFIED  
  - VLAN 50: 8192 ✓ VERIFIED  
  - VLAN 99: 8192 ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Enabled on VLANs Not specified ✓ VERIFIED  
  - Information Option: Enabled ✓ VERIFIED  
- **Dynamic ARP Inspection**: Not enabled ✓ VERIFIED  
- **Port Security**: Not configured ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  

### Access Control Lists
- **Standard ACL 'MGMT-ACCESS'**:  
  - `permit 10.99.0.0 0.0.0.255` ✓ VERIFIED  
  - `permit 10.99.1.0 0.0.0.255` ✓ VERIFIED  
  - `deny any` ✓ VERIFIED  

- **Extended ACL 'BLOCK-GUEST-INTERNAL'**:  
  - `deny ip 10.20.0.0 0.0.0.255 10.10.0.0 0.0.0.255` ✓ VERIFIED  
  - `deny ip 10.20.0.0 0.0.0.255 10.30.0.0 0.0.0.255` ✓ VERIFIED  
  - `deny ip 10.20.0.0 0.0.0.255 10.50.0.0 0.0.0.255` ✓ VERIFIED  
  - `deny ip 10.20.0.0 0.0.0.255 10.99.0.0 0.0.1.255` ✓ VERIFIED  
  - `permit ip 10.20.0.0 0.0.0.255 any` ✓ VERIFIED  

- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  

---

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  
- **Logging Level**: informational ✓ VERIFIED  

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
  - `0.0.0.0 0.0.0.0 via 10.99.1.1` ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only VTY access with version 2 and 60-second timeout ✓ VERIFIED  
- DHCP snooping enabled (though VLANs unspecified) ✓ VERIFIED  
- CDP disabled to prevent lateral discovery ✓ VERIFIED  
- ACLs configured for management access and guest VLAN isolation ✓ VERIFIED  
- Local AAA authentication with privilege 15 user ✓ VERIFIED  

#### ⚠ Areas for Improvement
- DHCP snooping VLANs not explicitly defined (should specify VLANs 10, 20, 30, 50, 99) ? UNCERTAIN  
- Missing Dynamic ARP Inspection (DAI) for VLANs with SVIs ? UNCERTAIN  
- No port security on access ports (though no access ports exist) ✓ VERIFIED  
- Native VLAN 666 is non-standard and should be renamed or removed ? UNCERTAIN  
- No 802.1X or IP Source Guard for enhanced security ? UNCERTAIN  

#### Recommendations
- Specify VLANs for DHCP snooping (e.g., `ip dhcp snooping vlan 10,20,30,50,99`)  
- Enable DAI on VLANs with SVIs (VLANs 10, 20, 30, 50, 99)  
- Rename native VLAN 666 to a non-default value (e.g., VLAN 999)  
- Add port security to access ports if access ports are introduced  
- Consider enabling 802.1X for guest VLAN (VLAN 20)  

---

## Summary

**Device Role**: This is a **Distribution Layer** switch, as it hosts multiple VLAN interfaces (SVIs), performs inter-VLAN routing, and connects to both core and access switches. ~ INFERRED  

**Configuration Quality**: The configuration is well-structured with strong security practices (SSH, ACLs, DHCP snooping). However, missing features like DAI and explicit DHCP snooping VLANs could improve security. ~ INFERRED  

**Purpose**: This switch serves as a distribution layer device, aggregating traffic from access switches and providing routing between VLANs. It also acts as a management gateway for the network. ~ INFERRED  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-04-25T21:37:44.615761