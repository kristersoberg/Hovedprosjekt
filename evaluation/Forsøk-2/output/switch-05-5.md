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

### Detailed Interface List
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

### Static Routes
- **0.0.0.0 0.0.0.0 via 10.99.1.1** ✓ VERIFIED

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, providing secure remote access.
- AAA is enabled with local authentication and authorization, ensuring user accountability.
- DHCP snooping is enabled, helping prevent rogue DHCP servers.
- CDP is disabled, reducing the risk of network discovery attacks.
- A standard ACL (`MGMT-ACCESS`) is applied to the management VLAN to restrict access.
- An extended ACL (`BLOCK-GUEST-INTERNAL`) is configured to block internal traffic from the guest VLAN to other VLANs.
- Logging is enabled with a remote syslog server, aiding in auditing and troubleshooting.
- A banner is configured to warn unauthorized users.

#### ⚠ Areas for Improvement
- **DHCP Snooping VLANs**: DHCP snooping is enabled globally but not restricted to specific VLANs. It should be limited to VLANs where it is needed (e.g., VLAN 10, 20, 30, 50).
- **Dynamic ARP Inspection (DAI)**: Not enabled. DAI should be configured to prevent ARP spoofing attacks.
- **Port Security**: Not enabled on any interfaces. Port security should be implemented on access ports to prevent unauthorized device access.
- **802.1X**: Not configured. If the network supports it, 802.1X should be enabled for stronger access control.
- **IP Source Guard**: Not enabled. IP source guard should be configured to prevent IP spoofing.
- **LLDP**: Not enabled. LLDP could be used for network discovery and monitoring.
- **SNMP**: Not configured. If monitoring is required, SNMP should be configured with appropriate access controls.
- **VTP**: Not configured. If VLANs are managed centrally, VTP should be considered for consistency.

#### Recommendations
- Enable **DHCP snooping** on specific VLANs (e.g., VLAN 10, 20, 30, 50).
- Enable **Dynamic ARP Inspection (DAI)** on VLANs where it is needed.
- Enable **port security** on access ports to prevent unauthorized device access.
- Consider enabling **802.1X** for stronger user authentication.
- Enable **IP source guard** to prevent IP spoofing.
- Enable **LLDP** for network discovery and monitoring.
- Configure **SNMP** with appropriate access controls if monitoring is required.
- Consider implementing **VTP** if VLANs are managed centrally.
- Ensure **ACLs** are regularly reviewed and updated to reflect current security policies.

---

## Summary

The device `dis-sw02` is a **Distribution Layer switch** based on its configuration, which includes VLAN interfaces (SVIs), inter-VLAN routing, and trunking to both core and access switches. It is running Cisco IOS version 15.2(2)E9 and is part of the domain `core.bedrift.no`. The configuration is generally well-structured and includes several good security practices, such as SSH access, AAA, and ACLs. However, there are areas for improvement, particularly in the areas of dynamic ARP inspection, port security, and IP source guard. The configuration quality is good, but it could be enhanced with additional security features and regular audits.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T09:16:24.196889