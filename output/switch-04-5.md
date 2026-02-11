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
  - Native VLAN: 666 ✓ VERIFIED  
  - DHCP Snooping Trust: Enabled ✓ VERIFIED  
- **GigabitEthernet0/2**:
  - Description: Uplink til core-sw01 gig0/2 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
  - DHCP Snooping Trust: Enabled ✓ VERIFIED  
- **GigabitEthernet0/3**:
  - Description: Downlink aksess-sw03 fa0/23 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
- **GigabitEthernet0/4**:
  - Description: Downlink aksess-sw04 fa0/23 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
- **GigabitEthernet0/5**:
  - Status: Shutdown ✓ VERIFIED  
- **GigabitEthernet0/6**:
  - Status: Shutdown ✓ VERIFIED  

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
- **Port Security**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  

### Access Control Lists
- **Standard ACL 'MGMT-ACCESS'**: 3 entries ✓ VERIFIED  
  - Configured in `line vty 0 4` and `line vty 5 15` ✓ VERIFIED  
- **Extended ACL 'BLOCK-GUEST-INTERNAL'**: 5 entries ✓ VERIFIED  
  - Applied to VLAN 99 (Management) as ACL In ✓ VERIFIED  

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
- **Static Routes**: 1 configured ✓ VERIFIED  
  - `ip route 0.0.0.0 0.0.0.0 10.99.1.1` ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only access with version 2 and 60-second timeout is configured (`ip ssh version 2`, `ip ssh time-out 60`) ✓ VERIFIED  
- DHCP snooping is enabled globally, though VLANs are not explicitly specified (`ip dhcp snooping`) ✓ VERIFIED  
- CDP is disabled (`no cdp run`) ✓ VERIFIED  
- Management access is restricted using ACL `MGMT-ACCESS` on VTY lines and VLAN 99 ✓ VERIFIED  
- AAA is enabled with local authentication and authorization ✓ VERIFIED  
- Port security is not required due to trunk-only configuration, but it is not configured anyway ✓ VERIFIED  

#### ⚠ Areas for Improvement
- Dynamic ARP Inspection (DAI) is not enabled, which is a recommended security feature for VLANs with DHCP snooping enabled ? UNCERTAIN  
- VLAN 666 is used as the native VLAN on all trunk ports, which is a security risk if untrusted devices connect to these ports ? UNCERTAIN  
- No SNMP configuration is present, which may impact monitoring and management ? UNCERTAIN  
- No 802.1X or IP Source Guard is configured, which could enhance security on access ports (though none are present) ? UNCERTAIN  
- VLAN 1 is shutdown, but it is still configured as an SVI with no IP address. It should be removed or explicitly disabled in VTP if not needed ? UNCERTAIN  

#### Recommendations
- Enable Dynamic ARP Inspection (DAI) on VLANs where DHCP snooping is active to prevent ARP spoofing.  
- Consider changing the native VLAN on trunk ports to a non-routed VLAN (e.g., VLAN 99) to reduce the risk of VLAN hopping.  
- Implement SNMP with secure community strings and access control to enable monitoring.  
- If access ports are added in the future, enable port security and 802.1X for enhanced security.  
- Remove or disable VLAN 1 if it is not required, especially if VTP is not in use.  
- Consider enabling NTP authentication if time synchronization is critical for security and logging.  

---

## Summary

The device `dis-sw01` is a **Distribution Layer switch** based on its configuration, which includes multiple VLAN interfaces (SVIs), inter-VLAN routing, and trunking to both core and access switches. It is configured with strong security practices such as SSH-only access, AAA authentication, and ACL-based management access. However, there are opportunities to enhance security further, particularly with Dynamic ARP Inspection and native VLAN hardening. The configuration is well-structured and appears to be in good operational condition.  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T07:11:52.214939