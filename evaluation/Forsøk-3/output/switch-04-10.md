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

### VLAN Details:
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

### Key Interface Configurations:
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

### Access Control Lists:
- **Standard ACL 'MGMT-ACCESS'**: 3 entries ✓ VERIFIED  
- **Extended ACL 'BLOCK-GUEST-INTERNAL'**: 5 entries ✓ VERIFIED  

---

## Network Services

### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  
- **Logging Level**: informational ✓ VERIFIED  

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED  
- **NTP Authentication**: Disabled ✓ VERIFIED  

### Syslog
- **Syslog Enabled**: ✓ VERIFIED  
- **Syslog Server**: 10.99.0.50 ✓ VERIFIED  

### SNMP
- **SNMP**: Not configured ✓ VERIFIED  

### DNS
- **DNS Domain Name**: core.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

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
  - This device functions as a **Distribution Layer** switch.  
  - Justification: It has multiple VLAN interfaces (SVIs) with IP addresses, inter-VLAN routing is enabled, and it connects to both core and access switches.  
  - It does not have many access ports or port security, which would be typical of an access layer switch.  

---

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, ensuring secure remote access.  
- AAA is enabled with local authentication, providing centralized user control.  
- DHCP snooping is enabled globally, helping prevent rogue DHCP servers.  
- CDP is disabled, reducing the risk of lateral discovery.  
- Access control lists (ACLs) are configured to restrict management and internal traffic.  
- A banner is configured to warn unauthorized users.  

#### ⚠ Areas for Improvement
- Dynamic ARP Inspection (DAI) is not enabled, which could leave the network vulnerable to ARP spoofing.  
- Port security is not configured on any interfaces, which could allow unauthorized devices to connect.  
- IP Source Guard is not enabled, which could allow spoofed IP addresses to bypass ACLs.  
- 802.1X is not configured, which could leave wired access vulnerable to unauthorized devices.  
- VLAN 666 is used as a native VLAN on trunk ports but is not explicitly configured or documented, which could lead to VLAN leakage.  
- No routing protocols are configured, which may limit scalability in a larger network.  

#### Recommendations
- Enable **Dynamic ARP Inspection (DAI)** on VLANs where it is needed.  
- Implement **port security** on access ports to prevent unauthorized device access.  
- Enable **IP Source Guard** to prevent IP spoofing.  
- Consider implementing **802.1X** for wired access control.  
- Document and secure **VLAN 666** to prevent VLAN leakage.  
- Consider implementing **VTP** if VLAN consistency across switches is required.  
- Add **logging to ACLs** for better visibility into traffic patterns and potential threats.  
- Consider enabling **SNMP** for monitoring and management.  

---

## Summary

dis-sw01 is a **Distribution Layer** switch running Cisco IOS 15.2(2)E9. It provides inter-VLAN routing, connects to both core and access switches, and supports multiple VLANs with HSRP for redundancy. The configuration is well-structured and includes several security features such as SSH, AAA, and DHCP snooping. However, there are opportunities to improve security by enabling DAI, port security, and IP Source Guard. The device is well-suited for its role in the network, but additional hardening measures are recommended.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T10:44:34.555992