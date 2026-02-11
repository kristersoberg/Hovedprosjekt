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
- AAA is enabled with local authentication for both console and VTY access.  
- DHCP snooping is enabled globally, which helps prevent rogue DHCP servers.  
- CDP is disabled, reducing the risk of lateral discovery.  
- Access control lists (ACLs) are configured to restrict management access and block internal guest traffic.  
- A banner is configured to warn unauthorized users.  

#### ⚠ Areas for Improvement
- Dynamic ARP Inspection (DAI) is not enabled, which could leave the network vulnerable to ARP spoofing.  
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect.  
- IP Source Guard is not enabled, which could allow spoofed IP addresses to bypass ACLs.  
- 802.1X is not configured, which could leave wired access vulnerable to unauthorized devices.  
- VLAN 666 is used as a native VLAN on trunk ports but is not explicitly defined or documented.  
- DHCP snooping is enabled globally but not scoped to specific VLANs, which could reduce its effectiveness.  

#### Recommendations
- Enable Dynamic ARP Inspection (DAI) on VLANs where it is needed.  
- Enable port security on access ports to prevent unauthorized device connections.  
- Enable IP Source Guard on VLANs where it is needed to prevent IP spoofing.  
- Consider implementing 802.1X for wired access control.  
- Define and document VLAN 666, and consider using a VLAN ID in the 1006–4094 range for native VLANs to avoid conflicts.  
- Scope DHCP snooping to specific VLANs to improve security and reduce unnecessary traffic.  
- Consider enabling SNMP for monitoring and management.  

---

## Summary

The device `dis-sw01` is a **Distribution Layer switch** based on its configuration, which includes multiple VLAN interfaces (SVIs), inter-VLAN routing, and trunking to both core and access switches. It is configured with a strong baseline of security features, including SSH, AAA, and ACLs, but lacks some advanced protections like DAI and port security. The configuration is well-structured and follows best practices for a distribution switch in a multi-VLAN environment.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T08:46:49.362515