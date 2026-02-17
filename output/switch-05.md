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
- **Banner**: Configured (line: `banner login ^CUautorisert tilgang er forbudt. All aktivitet logges.^C`) ✓ VERIFIED  

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
    - IP: 10.10.0.3 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - HSRP: Configured (standby group 10) ✓ VERIFIED  
  - **VLAN 20**:  
    - Description: Gjest Gateway ✓ VERIFIED  
    - IP: 10.20.0.3 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - HSRP: Configured (standby group 20) ✓ VERIFIED  
  - **VLAN 30**:  
    - Description: Skrivere Gateway ✓ VERIFIED  
    - IP: 10.30.0.3 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - HSRP: Configured (standby group 30) ✓ VERIFIED  
  - **VLAN 50**:  
    - Description: VoIP Gateway ✓ VERIFIED  
    - IP: 10.50.0.3 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - HSRP: Configured (standby group 50) ✓ VERIFIED  
  - **VLAN 99**:  
    - Description: Management ✓ VERIFIED  
    - IP: 10.99.1.3 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - ACL In: `MGMT-ACCESS` (standard ACL) ✓ VERIFIED  

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
- **Port Security**: 0 interfaces enabled ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  

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
- AAA authentication with local user `netadmin` (privilege 15) ✓ VERIFIED  
- DHCP snooping enabled globally ✓ VERIFIED  
- CDP disabled to prevent lateral discovery ✓ VERIFIED  
- Guest VLAN (VLAN 20) restricted from internal network access via `BLOCK-GUEST-INTERNAL` ACL ✓ VERIFIED  
- Management access restricted via `MGMT-ACCESS` standard ACL ✓ VERIFIED  

#### ⚠ Areas for Improvement
- DHCP snooping VLANs not explicitly specified (currently enabled globally) ~ INFERRED  
- Port security not enabled on any interfaces ~ INFERRED  
- Dynamic ARP Inspection (DAI) not enabled ~ INFERRED  
- 802.1X not configured for access control ~ INFERRED  
- IP Source Guard not enabled to prevent IP spoofing ~ INFERRED  
- No password complexity requirements for local user `netadmin` ~ INFERRED  

#### Recommendations
- Specify VLANs for DHCP snooping to limit scope ~ INFERRED  
- Enable port security on access ports (if any) ~ INFERRED  
- Implement DAI to prevent ARP spoofing ~ INFERRED  
- Configure 802.1X for secure access control ~ INFERRED  
- Enable IP Source Guard to prevent IP address spoofing ~ INFERRED  
- Enforce password complexity policies for local users ~ INFERRED  

---

## Summary

This device, **dis-sw02**, operates as a **Distribution Layer switch** ~ INFERRED due to its role in aggregating traffic between access switches (aksess-sw03/04) and the core (core-sw01). It manages inter-VLAN routing for six VLANs (10, 20, 30, 50, 99, 666) and implements basic security features like SSH, AAA, and ACLs. The configuration is well-structured but lacks advanced security measures like port security and DAI. ~ INFERRED  

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-17T19:40:09.268938