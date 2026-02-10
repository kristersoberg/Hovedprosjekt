# Network Device Documentation: dis-sw01

## Device Information
- **Hostname**: dis-sw01 ✓ VERIFIED  
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED  
- **Domain Name**: core.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: 10 ✓ VERIFIED  
- **IP Address**: 10.10.0.2 ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **VTY Transport Input**: ssh ✓ VERIFIED  
- **VTY Access Class**: MGMT-ACCESS (in) ✓ VERIFIED  
- **Console Authentication**: CONSOLE ✓ VERIFIED  
- **Console Logging Synchronous**: Enabled ✓ VERIFIED  

---

## AAA Configuration
- **AAA Enabled**: ✓ VERIFIED  
- **Authentication Methods**:
  - `aaa authentication login default local` ✓ VERIFIED  
  - `aaa authentication login CONSOLE local` ✓ VERIFIED  
- **Authorization Method**:
  - `aaa authorization exec default local` ✓ VERIFIED  
- **Local Users**:
  - `netadmin` (privilege 15) ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 6 ✓ VERIFIED  
- **VLAN IDs**: 10, 20, 30, 50, 99, 666 ✓ VERIFIED  
- **VLAN Interfaces (SVIs)**: 6 configured ✓ VERIFIED  

### VLAN Details
- **VLAN 1**:
  - Status: Shutdown ✓ VERIFIED  
- **VLAN 10**:
  - Description: Ansatte Gateway ✓ VERIFIED  
  - IP: 10.10.0.2 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - HSRP: Configured ✓ VERIFIED  
- **VLAN 20**:
  - Description: Gjest Gateway ✓ VERIFIED  
  - IP: 10.20.0.2 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - HSRP: Configured ✓ VERIFIED  
- **VLAN 30**:
  - Description: Skrivere Gateway ✓ VERIFIED  
  - IP: 10.30.0.2 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - HSRP: Configured ✓ VERIFIED  
- **VLAN 50**:
  - Description: VoIP Gateway ✓ VERIFIED  
  - IP: 10.50.0.2 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - HSRP: Configured ✓ VERIFIED  
- **VLAN 99**:
  - Description: Management ✓ VERIFIED  
  - IP: 10.99.1.2 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - ACL In: MGMT-ACCESS ✓ VERIFIED  

- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 6 ✓ VERIFIED  
- **Active (no shutdown)**: 4 ✓ VERIFIED  
- **Shutdown**: 2 ✓ VERIFIED  
- **Access Ports**: 0 ✓ VERIFIED  
- **Trunk Ports**: 4 ✓ VERIFIED  
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED  

### Interface Details
- **GigabitEthernet0/1**:
  - Description: Uplink til core-sw01 gig0/1 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  
- **GigabitEthernet0/2**:
  - Description: Uplink til core-sw01 gig0/2 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  
- **GigabitEthernet0/3**:
  - Description: Downlink aksess-sw03 fa0/23 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  
- **GigabitEthernet0/4**:
  - Description: Downlink aksess-sw04 fa0/23 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  
- **GigabitEthernet0/5**:
  - Status: shutdown ✓ VERIFIED  
- **GigabitEthernet0/6**:
  - Status: shutdown ✓ VERIFIED  

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
- **DHCP Snooping**: ✓ Enabled on VLANs Not specified ✓ VERIFIED  
  - Information Option: Enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **Port Security**: Not enabled on any interfaces ✓ VERIFIED  
- **Access Control Lists (ACLs)**:
  - Standard ACL 'MGMT-ACCESS': 3 entries ✓ VERIFIED  
  - Extended ACL 'BLOCK-GUEST-INTERNAL': 5 entries ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  

---

## Network Services

### Logging
- **Syslog Enabled**: ✓ VERIFIED  
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  
- **Logging Level**: informational ✓ VERIFIED  

### NTP
- **NTP Enabled**: ✓ VERIFIED  
- **NTP Server**: 10.99.0.1 ✓ VERIFIED  
- **NTP Authentication**: Disabled ✓ VERIFIED  

### DNS
- **DNS Domain Name**: core.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

### SNMP
- **SNMP**: Not configured ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Enabled ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **Static Routes**:
  - `0.0.0.0 0.0.0.0 via 10.99.1.1` ✓ VERIFIED  

---

## Configuration Quality Assessment

### Device Role
- **Role**: ~ INFERRED  
  - This device is a **Distribution Layer** switch.  
  - Justification: It has multiple VLAN interfaces (SVIs) with IP addresses, inter-VLAN routing is enabled, and it connects to both core and access switches.  

---

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, preventing weak authentication methods.  
- AAA is enabled with local authentication for console and VTY access.  
- DHCP snooping is enabled globally, reducing the risk of rogue DHCP servers.  
- CDP is disabled, reducing the risk of lateral discovery.  
- A standard ACL (`MGMT-ACCESS`) is applied to VTY lines, restricting remote access to trusted subnets.  
- A guest VLAN (VLAN 20) is isolated from internal VLANs using an extended ACL (`BLOCK-GUEST-INTERNAL`).  
- A banner is configured to warn unauthorized users.  

#### ⚠ Areas for Improvement
- **DHCP Snooping VLANs**: DHCP snooping is enabled globally but not restricted to specific VLANs. This could allow rogue DHCP servers in untrusted VLANs.  
- **Dynamic ARP Inspection (DAI)**: Not enabled, which could leave the network vulnerable to ARP spoofing.  
- **Port Security**: Not enabled on any interfaces, which could allow unauthorized devices to connect.  
- **LLDP**: Not enabled, which could reduce visibility into connected devices.  
- **SNMP**: Not configured, which could limit monitoring and management capabilities.  
- **NTP Authentication**: Disabled, which could allow time spoofing and affect log integrity.  

#### Recommendations
- Enable **DHCP snooping on specific VLANs** (e.g., VLAN 10, 20, 30, 50) to limit trust to uplink interfaces only.  
- Enable **Dynamic ARP Inspection (DAI)** on VLANs where it is needed (e.g., VLAN 10, 20, 30, 50).  
- Enable **port security** on access ports to prevent unauthorized device access.  
- Enable **LLDP** to improve visibility into connected devices.  
- Configure **SNMP** with secure community strings and access control.  
- Enable **NTP authentication** to ensure accurate and secure time synchronization.  
- Consider enabling **IP Source Guard** on VLANs where it is needed to prevent IP spoofing.  

---

## Summary

The device `dis-sw01` is a **Distribution Layer switch** running Cisco IOS version 15.2(2)E9. It provides inter-VLAN routing for six VLANs (10, 20, 30, 50, 99, 666) and connects to both core and access switches. The configuration includes strong security practices such as SSH-only access, AAA authentication, and DHCP snooping, but lacks some advanced security features like DAI and port security. The device is well-managed with logging, NTP, and ACLs in place, but further hardening is recommended.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-10T21:35:40.009552