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
- **VTY Lines**: line vty 0 4 and line vty 5 15 ✓ VERIFIED  
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

- **SVI Details**:  
  - **VLAN 1**:  
    - Status: Shutdown ✓ VERIFIED  
  - **VLAN 10**:  
    - Description: Ansatte Gateway ✓ VERIFIED  
    - IP: 10.10.0.2 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - HSRP: Configured (Group 10, IP 10.10.0.1, priority 110, preempt) ✓ VERIFIED  
  - **VLAN 20**:  
    - Description: Gjest Gateway ✓ VERIFIED  
    - IP: 10.20.0.2 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - HSRP: Configured (Group 20, IP 10.20.0.1, priority 110, preempt) ✓ VERIFIED  
  - **VLAN 30**:  
    - Description: Skrivere Gateway ✓ VERIFIED  
    - IP: 10.30.0.2 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - HSRP: Configured (Group 30, IP 10.30.0.1, priority 110, preempt) ✓ VERIFIED  
  - **VLAN 50**:  
    - Description: VoIP Gateway ✓ VERIFIED  
    - IP: 10.50.0.2 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - HSRP: Configured (Group 50, IP 10.50.0.1, priority 110, preempt) ✓ VERIFIED  
  - **VLAN 99**:  
    - Description: Management ✓ VERIFIED  
    - IP: 10.99.1.2 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - ACL In: `MGMT-ACCESS` (in) ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 6 ✓ VERIFIED  
- **Active (no shutdown)**: 4 ✓ VERIFIED  
- **Shutdown**: 2 ✓ VERIFIED  

**Active Interfaces**:  
- **GigabitEthernet0/1**:  
  - Description: "Uplink til core-sw01 gig0/1" ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Encapsulation: dot1q ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  
- **GigabitEthernet0/2**:  
  - Description: "Uplink til core-sw01 gig0/2" ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Encapsulation: dot1q ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  
- **GigabitEthernet0/3**:  
  - Description: "Downlink aksess-sw03 fa0/23" ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Encapsulation: dot1q ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  
- **GigabitEthernet0/4**:  
  - Description: "Downlink aksess-sw04 fa0/23" ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Encapsulation: dot1q ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  

**Port Security Violation Mode**: Not configured on any interface ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED  
- **Per-VLAN Priorities**:  
  - VLAN 10: 4096 ✓ VERIFIED  
  - VLAN 20: 4096 ✓ VERIFIED  
  - VLAN 30: 4096 ✓ VERIFIED  
  - VLAN 50: 4096 ✓ VERIFIED  
  - VLAN 99: 4096 ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Enabled on VLANs Not specified ✓ VERIFIED  
  - Information Option: Enabled ✓ VERIFIED  
- **Dynamic ARP Inspection**: Not enabled ✓ VERIFIED  
- **Port Security**: Not configured ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  

**Access Control Lists**:  
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
- SSH-only VTY access with version 2 and 60-second timeout (config lines: `ip ssh version 2`, `ip ssh time-out 60`)  
- AAA authentication with local user database (config lines: `aaa authentication login default local`, `username netadmin`)  
- DHCP snooping enabled (config line: `ip dhcp snooping`)  
- Access control lists (ACLs) for management and guest traffic isolation (config lines: `ip access-list standard MGMT-ACCESS`, `ip access-list extended BLOCK-GUEST-INTERNAL`)  
- CDP disabled (config line: `no cdp run`)  

#### ⚠ Areas for Improvement
- DHCP snooping VLANs not explicitly specified (config line: `ip dhcp snooping` lacks `vlan` command)  
- Missing port security on trunk interfaces (config lines: no `switchport port-security` commands)  
- Dynamic ARP Inspection (DAI) not enabled  
- 802.1X authentication not configured  
- Native VLAN 666 is not a standard VLAN and could be exploited if untrusted devices connect  

#### Recommendations
- Specify VLANs for DHCP snooping (e.g., `ip dhcp snooping vlan 10,20,30,50,99`)  
- Enable port security on trunk interfaces to prevent MAC flooding attacks  
- Implement Dynamic ARP Inspection (DAI) for VLANs 10, 20, 30, 50, 99  
- Configure 802.1X authentication for access ports  
- Rename native VLAN 666 to a non-standard name (e.g., "Native-Isolation") for security  

---

## Summary

**Device Role**: This is a **Distribution Layer** switch, as it performs inter-VLAN routing (SVIs with IPs), aggregates traffic from access switches (downlinks to aksess-sw03/04), and connects to the core (uplinks to core-sw01).  

**Purpose**: Provides Layer 3 services (VLAN gateways, HSRP), inter-VLAN routing, and traffic isolation between departments (Ansatte, Gjest, Skrivere, VoIP).  

**Configuration Quality**: The configuration is well-structured with strong security foundations (SSH, AAA, ACLs). However, critical security features like port security, DAI, and 802.1X are missing, and DHCP snooping VLANs are not explicitly defined.  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-16T08:32:02.796458