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
- **SVI Interfaces (VLAN Interfaces)**: 6 configured ✓ VERIFIED

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
  - Native VLAN: 666 ✓ VERIFIED
  - DHCP Snooping Trust: Enabled ✓ VERIFIED
- **GigabitEthernet0/2**:
  - Description: Uplink til core-sw01 gig0/4 ✓ VERIFIED
  - Mode: trunk ✓ VERIFIED
  - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED
  - Native VLAN: 666 ✓ VERIFIED
  - DHCP Snooping Trust: Enabled ✓ VERIFIED
- **GigabitEthernet0/3**:
  - Description: Downlink aksess-sw03 fa0/24 ✓ VERIFIED
  - Mode: trunk ✓ VERIFIED
  - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED
  - Native VLAN: 666 ✓ VERIFIED
- **GigabitEthernet0/4**:
  - Description: Downlink aksess-sw04 fa0/24 ✓ VERIFIED
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
  - VLAN 10: 8192 ✓ VERIFIED
  - VLAN 20: 8192 ✓ VERIFIED
  - VLAN 30: 8192 ✓ VERIFIED
  - VLAN 50: 8192 ✓ VERIFIED
  - VLAN 99: 8192 ✓ VERIFIED

---

## Security Features
- **DHCP Snooping**: Enabled ✓ VERIFIED
  - VLANs: Not specified ✓ VERIFIED
  - Information Option: Enabled ✓ VERIFIED
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED
- **Port Security**: Not configured ✓ VERIFIED
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

### Device Role
- **Role**: Distribution Layer Switch ~ INFERRED
  - Justification: The device has multiple VLAN interfaces (SVIs) with IP addresses, inter-VLAN routing enabled, and trunk ports connecting to both core and access switches. This is typical of a distribution layer switch.

---

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, preventing weak authentication methods. ✓ VERIFIED
- AAA is enabled with local authentication for console and VTY access, ensuring user accountability. ✓ VERIFIED
- DHCP snooping is enabled globally, helping prevent rogue DHCP servers. ✓ VERIFIED
- CDP is disabled, reducing the risk of lateral discovery attacks. ✓ VERIFIED
- A standard ACL (`MGMT-ACCESS`) is applied to the management VLAN, restricting access to trusted subnets. ✓ VERIFIED
- An extended ACL (`BLOCK-GUEST-INTERNAL`) is configured to block traffic from the guest VLAN to internal VLANs. ✓ VERIFIED

#### ⚠ Areas for Improvement
- **DHCP Snooping VLAN Scope**: DHCP snooping is enabled globally but not scoped to specific VLANs. This could allow rogue DHCP servers in untrusted VLANs. ? UNCERTAIN
- **Dynamic ARP Inspection (DAI)**: Not enabled, which could leave the switch vulnerable to ARP spoofing. ? UNCERTAIN
- **Port Security**: Not configured on any interfaces, which could allow unauthorized devices to connect. ? UNCERTAIN
- **802.1X**: Not configured, which could leave the network vulnerable to unauthorized access. ? UNCERTAIN
- **IP Source Guard**: Not configured, which could allow spoofed IP addresses. ? UNCERTAIN
- **LLDP**: Not enabled, which could reduce visibility into connected devices. ? UNCERTAIN
- **SNMP**: Not configured, which could reduce monitoring and management capabilities. ? UNCERTAIN

#### Recommendations
- **Scope DHCP Snooping to Specific VLANs**: Apply `ip dhcp snooping vlan` to VLANs 10, 20, 30, 50, and 99 to limit the scope of protection.
- **Enable Dynamic ARP Inspection (DAI)**: Enable DAI on VLANs where it is needed to prevent ARP spoofing.
- **Enable Port Security**: Enable port security on access ports to prevent unauthorized device access.
- **Enable 802.1X**: If the network supports it, enable 802.1X for secure user authentication.
- **Enable IP Source Guard**: Enable IP source guard on VLANs to prevent IP spoofing.
- **Enable LLDP**: Enable LLDP to improve visibility into connected devices.
- **Configure SNMP**: Configure SNMP with appropriate community strings and access controls to enable monitoring and management.
- **Enable IP Source Guard**: Enable IP source guard on VLANs to prevent IP spoofing.

---

## Summary

The device `dis-sw02` is a distribution layer switch running Cisco IOS version 15.2(2)E9. It serves as an aggregation point between access switches and the core, with multiple VLAN interfaces and inter-VLAN routing enabled. The configuration includes strong security features such as SSH, AAA, and ACLs, but lacks some advanced protections like DAI and port security. The configuration is well-structured and follows best practices for a distribution layer switch.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T09:30:23.115818