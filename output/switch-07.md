# Network Device Documentation: core-sw01

## Device Information
- **Hostname**: core-sw01 ✓ VERIFIED  
- **IOS Version**: 15.2(4)E10 ✓ VERIFIED  
- **Domain Name**: backbone.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: VLAN 10 ✓ VERIFIED  
- **IP Address**: 10.10.0.1/24 ✓ VERIFIED  
- **Default Gateway**: Not configured ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **VTY Transport Input**: SSH ✓ VERIFIED  
- **VTY Access Class**: MGMT-ACCESS (in) ✓ VERIFIED  
- **Console Authentication**: CONSOLE (local user) ✓ VERIFIED  
- **Console Logging Synchronous**: Enabled ✓ VERIFIED  

---

## AAA Configuration
- **AAA Enabled**: ✓ VERIFIED  
- **Authentication Methods**:  
  - `aaa authentication login default local` ✓ VERIFIED  
  - `aaa authentication login CONSOLE local` ✓ VERIFIED  
- **Authorization**:  
  - `aaa authorization exec default local` ✓ VERIFIED  
- **Accounting**:  
  - `aaa accounting exec default start-stop group tacacs+` ✓ VERIFIED  
- **TACACS+ Servers**: 10.99.0.40, 10.99.0.41 ✓ VERIFIED  
- **Local Users**:  
  - `coreAdmin` (privilege 15) ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 8 ✓ VERIFIED  
- **VLAN IDs**: 10, 20, 30, 50, 99, 100, 200, 666 ✓ VERIFIED  
- **SVI Configurations**:  
  - **VLAN 1**: Shutdown ✓ VERIFIED  
  - **VLAN 10**: Ansatte (10.10.0.1/24) - Active ✓ VERIFIED  
  - **VLAN 20**: Gjest (10.20.0.1/24) - Active ✓ VERIFIED  
  - **VLAN 30**: Skrivere (10.30.0.1/24) - Active ✓ VERIFIED  
  - **VLAN 50**: VoIP (10.50.0.1/24) - Active ✓ VERIFIED  
  - **VLAN 99**: Management (10.99.1.1/24) - Active, ACL In: MGMT-ACCESS ✓ VERIFIED  
  - **VLAN 100**: Server-Prod (10.100.0.1/24) - Active ✓ VERIFIED  
  - **VLAN 200**: Server-Dev (10.200.0.1/24) - Active ✓ VERIFIED  
- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 10 ✓ VERIFIED  
- **Active (no shutdown)**: 8 ✓ VERIFIED  
- **Shutdown**: 2 ✓ VERIFIED  
- **Trunk Ports**: 7 ✓ VERIFIED  
- **Key Active Interfaces**:  
  - **Port-channel1**: EtherChannel til dis-sw01 (trunk, VLANs 10,20,30,50,99) ✓ VERIFIED  
  - **Port-channel2**: EtherChannel til dis-sw02 (trunk, VLANs 10,20,30,50,99) ✓ VERIFIED  
  - **GigabitEthernet0/1**: dis-sw01 gig0/1 - Po1 (trunk, VLANs 10,20,30,50,99) ✓ VERIFIED  
  - **GigabitEthernet0/3**: dis-sw02 gig0/1 - Po2 (trunk, VLANs 10,20,30,50,99) ✓ VERIFIED  
  - **GigabitEthernet0/5**: Server-Prod svitsj (trunk, VLANs 100,200,99) ✓ VERIFIED  
  - **GigabitEthernet0/6**: WAN-ruter gig0/0 (routed, 10.255.0.1/30) ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED  
- **Port Security**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **Access Control Lists (ACLs)**:  
  - **Standard ACL MGMT-ACCESS**: 3 entries (10.99.0.0/24, 10.99.1.0/24, deny any) ✓ VERIFIED  
  - **Extended ACL DENY-GUEST-TO-INTERNAL**: 7 entries (denies VLAN 20 to internal VLANs) ✓ VERIFIED  

---

## Network Services
### Logging
- **Syslog Servers**: 10.99.0.50, 10.99.0.51 ✓ VERIFIED  
- **Logging Source Interface**: Vlan99 ✓ VERIFIED  
- **Logging Level**: informational ✓ VERIFIED  

### NTP
- **NTP Servers**: 129.240.2.6, 10.99.0.1 ✓ VERIFIED  
- **NTP Authentication**: Enabled (key 1) ✓ VERIFIED  

### DNS
- **Domain Name**: backbone.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Enabled ✓ VERIFIED  
- **Routing Protocol**: OSPF ✓ VERIFIED  
- **OSPF Configuration**:  
  - **Router ID**: 10.99.1.1 ✓ VERIFIED  
  - **Networks in Area 0**:  
    - 10.10.0.0/24  
    - 10.20.0.0/24  
    - 10.30.0.0/24  
    - 10.50.0.0/24  
    - 10.99.1.0/24  
    - 10.100.0.0/24  
    - 10.200.0.0/24  
    - 10.255.0.0/30  
  - **Passive Interfaces**: Vlan10, Vlan20, Vlan30, Vlan50, Vlan100, Vlan200 ✓ VERIFIED  
  - **Default Route**: `default-information originate` ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only VTY access with timeout (60s) ✓ VERIFIED  
- AAA authentication with local and TACACS+ integration ✓ VERIFIED  
- Syslog configured with remote servers and source interface (Vlan99) ✓ VERIFIED  
- CDP disabled to prevent lateral discovery ✓ VERIFIED  
- ACLs (MGMT-ACCESS, DENY-GUEST-TO-INTERNAL) enforce network segmentation ✓ VERIFIED  

#### ⚠ Areas for Improvement
- **DHCP Snooping**: Not enabled on VLANs (e.g., VLAN 10, 20, 30) ? UNCERTAIN  
- **Port Security**: No port security on access/trunk ports ? UNCERTAIN  
- **NTP**: NTP authentication is configured, but no key validation in raw config ? UNCERTAIN  
- **Native VLAN**: VLAN 666 used as native VLAN on trunks (not recommended) ? UNCERTAIN  

#### Recommendations
- Enable **DHCP Snooping** on VLANs 10, 20, 30, 50, 99, 100, 200 to prevent rogue DHCP servers.  
- Implement **port security** on access ports (if any) to prevent MAC flooding.  
- Validate **NTP key configuration** for authenticity.  
- Change **native VLAN** on trunks to a non-routed VLAN (e.g., VLAN 999) to mitigate VLAN hopping risks.  
- Enable **IP Source Guard** on VLANs with dynamic IP assignments.  

---

## Summary

**core-sw01** is a **core layer switch** operating as a routing and aggregation point for multiple VLANs (10, 20, 30, 50, 99, 100, 200). It uses OSPF for dynamic routing and EtherChannels for redundancy. The configuration includes strong AAA and SSH security practices but lacks critical features like DHCP snooping and port security. The device is well-documented and follows best practices for access control and logging.  

**Overall Configuration Quality**: Good, but requires security hardening for production environments.  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T20:32:54.973547