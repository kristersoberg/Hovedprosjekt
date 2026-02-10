# Network Device Documentation: dis-sw02

## Device Information
- **Hostname**: dis-sw02 ✓ VERIFIED  
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED  
- **Domain Name**: core.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: 10 ✓ VERIFIED  
- **IP Address**: 10.10.0.3 ✓ VERIFIED  
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
  - IP: 10.10.0.3 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - HSRP: Configured ✓ VERIFIED  
- **VLAN 20**:
  - Description: Gjest Gateway ✓ VERIFIED  
  - IP: 10.20.0.3 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - HSRP: Configured ✓ VERIFIED  
- **VLAN 30**:
  - Description: Skrivere Gateway ✓ VERIFIED  
  - IP: 10.30.0.3 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - HSRP: Configured ✓ VERIFIED  
- **VLAN 50**:
  - Description: VoIP Gateway ✓ VERIFIED  
  - IP: 10.50.0.3 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - HSRP: Configured ✓ VERIFIED  
- **VLAN 99**:
  - Description: Management ✓ VERIFIED  
  - IP: 10.99.1.3 255.255.255.0 ✓ VERIFIED  
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
  - Description: Uplink til core-sw01 gig0/3 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  
- **GigabitEthernet0/2**:
  - Description: Uplink til core-sw01 gig0/4 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  
- **GigabitEthernet0/3**:
  - Description: Downlink aksess-sw03 fa0/24 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  
- **GigabitEthernet0/4**:
  - Description: Downlink aksess-sw04 fa0/24 ✓ VERIFIED  
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
  - VLAN 10: 8192 ✓ VERIFIED  
  - VLAN 20: 8192 ✓ VERIFIED  
  - VLAN 30: 8192 ✓ VERIFIED  
  - VLAN 50: 8192 ✓ VERIFIED  
  - VLAN 99: 8192 ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: ✓ Enabled on VLANs Not specified ✓ VERIFIED  
  - Information Option: Enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED  
- **Port Security**: Not enabled on any interfaces ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  

### Access Control Lists
- **Standard ACL 'MGMT-ACCESS'**: 3 entries ✓ VERIFIED  
- **Extended ACL 'BLOCK-GUEST-INTERNAL'**: 5 entries ✓ VERIFIED  

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

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, ensuring secure remote access.  
- AAA is enabled with local authentication for console and VTY access.  
- DHCP snooping is enabled globally, which helps prevent rogue DHCP servers.  
- CDP is explicitly disabled, reducing potential attack vectors.  
- A standard ACL (`MGMT-ACCESS`) is applied to VTY lines to restrict remote access.  
- An extended ACL (`BLOCK-GUEST-INTERNAL`) is configured to block internal traffic from the guest VLAN.  
- A banner is configured to warn unauthorized users.  

#### ⚠ Areas for Improvement
- DHCP snooping is enabled but not scoped to specific VLANs, which could reduce its effectiveness.  
- Dynamic ARP Inspection (DAI) is not enabled, which could leave the network vulnerable to ARP spoofing.  
- IP Source Guard is not enabled, which could allow spoofed IP addresses to bypass ACLs.  
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect.  
- 802.1X is not configured, which could leave access ports vulnerable to unauthorized access.  
- SNMP is not configured, which could limit monitoring and management capabilities.  

#### Recommendations
- Enable DAI on VLANs where it is needed to prevent ARP spoofing.  
- Enable IP Source Guard on VLANs to prevent IP spoofing.  
- Enable port security on access ports to prevent unauthorized device connections.  
- Consider enabling 802.1X on access ports for stronger authentication.  
- Scope DHCP snooping to specific VLANs to improve its effectiveness.  
- Configure SNMP with secure community strings and access control.  
- Ensure all VLANs have appropriate ACLs and security policies applied.  

---

## Summary

dis-sw02 is a **Distribution Layer** switch, as evidenced by the presence of multiple VLAN interfaces (SVIs), inter-VLAN routing, and trunking to both core and access switches. It is configured with a strong baseline of security features, including SSH, AAA, and ACLs. However, there are several areas for improvement, particularly in the areas of dynamic ARP inspection, IP source guard, and port security. The device is well-integrated into the network with proper routing and management capabilities.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-10T21:47:11.966928