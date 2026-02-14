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

---

## AAA Configuration
- **AAA Enabled**: ✓ VERIFIED
- **Authentication Methods**:
  - `aaa authentication login default local` ✓ VERIFIED
  - `aaa authentication login CONSOLE local` ✓ VERIFIED
- **Authorization Methods**:
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
- **GigabitEthernet0/1** - Uplink til core-sw01 gig0/3 | Mode: trunk | Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED
- **GigabitEthernet0/2** - Uplink til core-sw01 gig0/4 | Mode: trunk | Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED
- **GigabitEthernet0/3** - Downlink aksess-sw03 fa0/24 | Mode: trunk | Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED
- **GigabitEthernet0/4** - Downlink aksess-sw04 fa0/24 | Mode: trunk | Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED
- **GigabitEthernet0/5** - Shutdown ✓ VERIFIED
- **GigabitEthernet0/6** - Shutdown ✓ VERIFIED

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
- **Port Security**: Not configured ✓ VERIFIED
- **IP Source Guard**: Not configured ✓ VERIFIED
- **Access Control Lists (ACLs)**:
  - Standard ACL 'MGMT-ACCESS': 3 entries ✓ VERIFIED
  - Extended ACL 'BLOCK-GUEST-INTERNAL': 5 entries ✓ VERIFIED
- **CDP**: Disabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED
- **802.1X**: Not configured ✓ VERIFIED

---

## Network Services

### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED
- **Logging Level**: informational ✓ VERIFIED (from `logging trap informational`)

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
  - `ip route 0.0.0.0 0.0.0.0 10.99.1.1` ✓ VERIFIED

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, providing secure remote access. ✓ VERIFIED
- AAA is enabled with local authentication for console and VTY access, ensuring user accountability. ✓ VERIFIED
- DHCP snooping is enabled globally, helping prevent rogue DHCP servers. ✓ VERIFIED
- A standard ACL (`MGMT-ACCESS`) is applied to the management VLAN to restrict access. ✓ VERIFIED
- An extended ACL (`BLOCK-GUEST-INTERNAL`) is configured to block internal traffic from the guest VLAN to other VLANs. ✓ VERIFIED
- CDP is disabled, reducing the risk of network discovery attacks. ✓ VERIFIED
- A banner is configured to warn unauthorized users. ✓ VERIFIED

#### ⚠ Areas for Improvement
- DHCP snooping is enabled globally but not restricted to specific VLANs. This could allow rogue DHCP servers in non-management VLANs. ~ INFERRED
- Dynamic ARP Inspection (DAI) is not enabled, which could leave the switch vulnerable to ARP spoofing. ~ INFERRED
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect. ~ INFERRED
- IP Source Guard is not enabled, which could allow spoofed IP addresses to bypass ACLs. ~ INFERRED
- SNMP is not configured, which could limit monitoring and management capabilities. ~ INFERRED
- NTP authentication is not enabled, which could allow time synchronization to be manipulated. ~ INFERRED

#### Recommendations
- Enable DHCP snooping on specific VLANs (e.g., VLAN 10, 20, 30, 50) to limit rogue DHCP server impact.
- Enable Dynamic ARP Inspection (DAI) on VLANs where it is needed.
- Enable port security on access ports to prevent unauthorized device access.
- Enable IP Source Guard on VLANs to prevent IP spoofing.
- Configure SNMP with appropriate community strings and access controls.
- Enable NTP authentication to secure time synchronization.
- Consider enabling 802.1X for secure user authentication on access ports.

---

## Summary

The device `dis-sw02` is a **Distribution Layer switch** based on its configuration, which includes multiple VLAN interfaces (SVIs), inter-VLAN routing, and trunking to both core and access switches. It is configured with a strong baseline of security features such as SSH, AAA, and ACLs, but lacks some advanced protections like DAI and port security. The configuration is well-structured and appears to be in good operational condition. ~ INFERRED

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T14:58:33.720369