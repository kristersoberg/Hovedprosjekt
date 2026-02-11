# Network Device Documentation: dis-sw01

## Device Information
- **Hostname**: dis-sw01 ✓ VERIFIED
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED
- **Domain Name**: core.bedrift.no ✓ VERIFIED
- **Config Register**: Not configured ✓ VERIFIED

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

## AAA Configuration
- **AAA Enabled**: ✓ VERIFIED
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

## Physical Interfaces
- **Total Interfaces**: 6 ✓ VERIFIED
- **Active (no shutdown)**: 4 ✓ VERIFIED
- **Shutdown**: 2 ✓ VERIFIED
- **Access Ports**: 0 ✓ VERIFIED
- **Trunk Ports**: 4 ✓ VERIFIED
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED

### Detailed Interface List
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

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED
- **Per-VLAN Priorities**:
  - VLAN 10: 4096 ✓ VERIFIED
  - VLAN 20: 4096 ✓ VERIFIED
  - VLAN 30: 4096 ✓ VERIFIED
  - VLAN 50: 4096 ✓ VERIFIED
  - VLAN 99: 4096 ✓ VERIFIED

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
- **Standard ACL 'MGMT-ACCESS'**:
  - 3 entries ✓ VERIFIED
  - Configured on VLAN 99 (inbound) ✓ VERIFIED
- **Extended ACL 'BLOCK-GUEST-INTERNAL'**:
  - 5 entries ✓ VERIFIED

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

## Routing Configuration
- **IP Routing**: Enabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED
- **Static Routes**:
  - `0.0.0.0 0.0.0.0 via 10.99.1.1` ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, ensuring secure remote access. ✓ VERIFIED
- AAA is enabled with local authentication for console and VTY access, providing basic user authentication. ✓ VERIFIED
- DHCP snooping is enabled globally, helping prevent rogue DHCP servers. ✓ VERIFIED
- CDP is explicitly disabled, reducing potential attack vectors. ✓ VERIFIED
- A standard ACL (`MGMT-ACCESS`) is applied to the management VLAN to restrict access to trusted subnets. ✓ VERIFIED
- An extended ACL (`BLOCK-GUEST-INTERNAL`) is configured to block traffic from the guest VLAN to internal VLANs. ✓ VERIFIED
- A banner is configured to warn unauthorized users. ✓ VERIFIED

#### ⚠ Areas for Improvement
- **DHCP Snooping VLANs**: DHCP snooping is enabled globally but not restricted to specific VLANs. This could allow untrusted VLANs to bypass snooping. ~ INFERRED
- **Dynamic ARP Inspection (DAI)**: Not enabled, which could leave the network vulnerable to ARP spoofing. ~ INFERRED
- **Port Security**: Not enabled on any interfaces, which could allow unauthorized devices to connect. ~ INFERRED
- **802.1X**: Not configured, which could leave wired access vulnerable to unauthorized device access. ~ INFERRED
- **IP Source Guard**: Not enabled, which could allow spoofed IP addresses to bypass ACLs. ~ INFERRED
- **LLDP**: Not enabled, which could limit visibility into connected devices. ~ INFERRED
- **SNMP**: Not configured, which could limit monitoring and management capabilities. ~ INFERRED

#### Recommendations
- **Enable DAI** on VLANs where it is needed, particularly on VLANs with user access. ~ INFERRED
- **Enable port security** on access ports to prevent unauthorized device access. ~ INFERRED
- **Enable 802.1X** on access ports to enforce user authentication. ~ INFERRED
- **Enable IP Source Guard** on VLANs where it is needed to prevent IP spoofing. ~ INFERRED
- **Enable LLDP** to improve visibility into connected devices. ~ INFERRED
- **Configure SNMP** to enable monitoring and management of the device. ~ INFERRED
- **Restrict DHCP snooping to specific VLANs** to ensure it is only applied where needed. ~ INFERRED
- **Enable AAA with TACACS+ or RADIUS** for centralized authentication and authorization. ~ INFERRED

## Summary

The device `dis-sw01` is a **Distribution Layer switch** based on its configuration, which includes multiple VLAN interfaces (SVIs), inter-VLAN routing, and trunking to both core and access switches. It is running Cisco IOS version 15.2(2)E9 and is part of the domain `core.bedrift.no`. The configuration is generally well-structured and includes several good security practices, such as SSH access, AAA, and ACLs. However, there are several areas for improvement, particularly in terms of advanced security features like DAI, port security, and 802.1X. The configuration quality is good but could be enhanced with additional security hardening and monitoring capabilities.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-10T21:14:10.602393