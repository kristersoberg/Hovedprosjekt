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
- **Authorization Method**:
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

### Active Interfaces
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
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED
- **Access Control Lists (ACLs)**:
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

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

### DNS
- **DNS Domain Name**: core.bedrift.no ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Enabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED
- **Static Routes**:
  - `0.0.0.0 0.0.0.0 via 10.99.1.1` ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, ensuring secure remote access. ✓ VERIFIED
- AAA is enabled with local authentication for console and VTY lines, providing basic access control. ✓ VERIFIED
- DHCP snooping is enabled globally, which helps prevent rogue DHCP servers. ✓ VERIFIED
- A standard ACL (`MGMT-ACCESS`) is applied to VTY lines to restrict remote access to trusted subnets. ✓ VERIFIED
- An extended ACL (`BLOCK-GUEST-INTERNAL`) is configured to block traffic from the guest VLAN to internal VLANs. ✓ VERIFIED
- CDP is disabled, reducing the risk of network discovery attacks. ✓ VERIFIED
- A banner is configured to warn unauthorized users. ✓ VERIFIED

#### ⚠ Areas for Improvement
- **DHCP Snooping VLANs**: DHCP snooping is enabled globally but not explicitly configured on specific VLANs. This could reduce its effectiveness. ~ INFERRED
- **Dynamic ARP Inspection (DAI)**: Not enabled, which could leave the switch vulnerable to ARP spoofing attacks. ~ INFERRED
- **Port Security**: Not enabled on any interfaces, which could allow unauthorized devices to connect. ~ INFERRED
- **802.1X**: Not configured, which could leave the network vulnerable to unauthorized access. ~ INFERRED
- **IP Source Guard**: Not enabled, which could allow spoofed IP addresses to be used. ~ INFERRED
- **LLDP**: Not enabled, which could reduce visibility into connected devices. ~ INFERRED
- **SNMP**: Not configured, which could reduce monitoring and management capabilities. ~ INFERRED

#### Recommendations
- **Enable DHCP Snooping on Specific VLANs**: Apply `ip dhcp snooping vlan 10,20,30,50,99` to ensure it is active on all relevant VLANs.
- **Enable Dynamic ARP Inspection (DAI)**: Configure DAI on VLANs where it is needed to prevent ARP spoofing.
- **Enable Port Security**: Enable port security on access ports to prevent unauthorized device access.
- **Enable 802.1X**: Implement 802.1X authentication for secure user and device access.
- **Enable IP Source Guard**: Enable IP source guard on VLANs to prevent IP spoofing.
- **Enable LLDP**: Enable LLDP to improve network visibility and device discovery.
- **Configure SNMP**: Configure SNMP for monitoring and management.
- **Enable NTP Authentication**: If NTP is used for time-sensitive operations, enable authentication to prevent time spoofing.

## Summary

The device `dis-sw02` is a **Distribution Layer** switch, as it is configured with multiple VLAN interfaces (SVIs), inter-VLAN routing, and trunking to both core and access switches. It is running Cisco IOS version 15.2(2)E9 and is part of the domain `core.bedrift.no`. The configuration is generally well-structured and includes several security best practices, but there are areas for improvement, particularly in advanced security features like DAI, port security, and 802.1X.

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T14:47:00.467766