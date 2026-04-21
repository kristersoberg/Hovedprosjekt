# Network Device Documentation: dis-sw02

## Device Information
- **Hostname**: dis-sw02 ✓ VERIFIED
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED
- **Domain Name**: core.bedrift.no ✓ VERIFIED
- **Config Register**: Not configured ✓ VERIFIED

## Management & Access
- **Management VLAN**: 10 ✓ VERIFIED
- **IP Address**: 10.10.0.3 ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED
- **SSH Version**: 2 ✓ VERIFIED
- **SSH Timeout**: 60 seconds ✓ VERIFIED
- **VTY Transport Input**: ssh ✓ VERIFIED
- **VTY Access Class**: MGMT-ACCESS (in) ✓ VERIFIED

## AAA Configuration
- **AAA Enabled**: ✓ Enabled ✓ VERIFIED
- **Authentication Methods**:
  - `aaa authentication login default local` ✓ VERIFIED
  - `aaa authentication login CONSOLE local` ✓ VERIFIED
- **Authorization Methods**:
  - `aaa authorization exec default local` ✓ VERIFIED
- **Local Users**:
  - `netadmin` (privilege 15) ✓ VERIFIED

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

## Physical Interfaces
- **Total Interfaces**: 6 ✓ VERIFIED
- **Active (no shutdown)**: 4 ✓ VERIFIED
- **Shutdown**: 2 ✓ VERIFIED

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

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED
- **Per-VLAN Priorities**:
  - VLAN 10: 8192 ✓ VERIFIED
  - VLAN 20: 8192 ✓ VERIFIED
  - VLAN 30: 8192 ✓ VERIFIED
  - VLAN 50: 8192 ✓ VERIFIED
  - VLAN 99: 8192 ✓ VERIFIED

## Security Features
- **DHCP Snooping**: ✓ Enabled on VLANs Not specified ✓ VERIFIED
  - Information Option: Enabled ✓ VERIFIED
- **Dynamic ARP Inspection**: Not enabled ✓ VERIFIED
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED
- **Access Control Lists**:
  - Standard ACL 'MGMT-ACCESS': 3 entries ✓ VERIFIED
  - Extended ACL 'BLOCK-GUEST-INTERNAL': 5 entries ✓ VERIFIED
- **CDP**: Disabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED
- **802.1X**: Not configured ✓ VERIFIED
- **IP Source Guard**: Not configured ✓ VERIFIED

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED
- **Logging Level**: informational ✓ VERIFIED (from `logging trap informational`)

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED
- **NTP Authentication**: Disabled ✓ VERIFIED

### Syslog
- **Syslog Enabled**: ✓ Enabled ✓ VERIFIED

### DNS
- **DNS Domain Name**: core.bedrift.no ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Enabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED
- **Static Routes**:
  - 0.0.0.0 0.0.0.0 via 10.99.1.1 ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, providing secure remote access. (Config lines: `ip ssh version 2`, `ip ssh time-out 60`)
- AAA is enabled with local authentication for both console and VTY access, ensuring user accountability. (Config lines: `aaa new-model`, `aaa authentication login default local`, `aaa authentication login CONSOLE local`)
- DHCP snooping is enabled globally, helping prevent rogue DHCP servers. (Config line: `ip dhcp snooping`)
- A standard ACL (`MGMT-ACCESS`) is applied to VTY lines, restricting management access to specific subnets. (Config lines: `access-class MGMT-ACCESS in`, `ip access-list standard MGMT-ACCESS`)
- CDP is explicitly disabled, reducing the risk of network discovery attacks. (Config line: `no cdp run`)
- A banner is configured to warn unauthorized users. (Config line: `banner login ^CUautorisert tilgang er forbudt. All aktivitet logges.^C`)
- Syslog is configured to send logs to a remote server, aiding in monitoring and auditing. (Config line: `logging 10.99.0.50`)

#### ⚠ Areas for Improvement
- DHCP snooping is enabled but not scoped to specific VLANs, which could allow rogue DHCP servers in untrusted VLANs.
- Dynamic ARP Inspection (DAI) is not enabled, which could leave the network vulnerable to ARP spoofing attacks.
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect to the switch.
- 802.1X is not configured, which could leave the network vulnerable to unauthorized access.
- IP Source Guard is not enabled, which could allow spoofed IP addresses to be used on the network.
- No VLAN-specific ACLs are applied to restrict inter-VLAN traffic, which could allow lateral movement within the network.
- No routing protocol is configured, which could limit scalability and redundancy in the network.

#### Recommendations
- Scope DHCP snooping to specific VLANs to prevent rogue DHCP servers in untrusted segments.
- Enable Dynamic ARP Inspection (DAI) to prevent ARP spoofing attacks.
- Enable port security on access ports to prevent unauthorized device access.
- Implement 802.1X for secure user and device authentication.
- Enable IP Source Guard to prevent IP address spoofing.
- Apply VLAN-specific ACLs to restrict inter-VLAN traffic and improve segmentation.
- Consider implementing a routing protocol (e.g., EIGRP or OSPF) to improve scalability and redundancy.
- Enable SNMP for device monitoring and management.
- Enable LLDP for network discovery and documentation.

## Summary

dis-sw02 is a **Distribution Layer** switch, as evidenced by the presence of multiple VLAN interfaces (SVIs), inter-VLAN routing, and trunking to both core and access switches. The device is configured with a strong baseline of security features, including SSH, AAA, and DHCP snooping. However, there are several areas for improvement, particularly in the areas of port security, dynamic ARP inspection, and VLAN-specific access control. The configuration is well-structured and follows best practices for a distribution switch in a multi-VLAN environment.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T02:57:44.485354