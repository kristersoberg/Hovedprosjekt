# Network Device Documentation: dis-sw02

## Device Information
- **Hostname**: dis-sw02 ✓ VERIFIED  
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED  
- **Domain Name**: core.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: VLAN 10 ✓ VERIFIED  
- **IP Address**: 10.10.0.3 ✓ VERIFIED  
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED  
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
- **SVIs (VLAN Interfaces)**: 6 configured ✓ VERIFIED  

### VLAN Interface Details
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

### Active Interface Details
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
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  

### Access Control Lists (ACLs)
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
- **Role**: ~ INFERRED  
  - This device is a **Distribution Layer** switch.  
  - Justification: It has multiple VLAN interfaces (SVIs) with IP addresses, inter-VLAN routing is enabled, and it connects to both core and access switches.  

---

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, preventing weak protocol usage.  
- AAA is enabled with local authentication, ensuring user accountability.  
- DHCP snooping is enabled globally, reducing the risk of rogue DHCP servers.  
- CDP is disabled, reducing the risk of lateral discovery.  
- A standard ACL (`MGMT-ACCESS`) is applied to the management VLAN, restricting access to trusted subnets.  
- An extended ACL (`BLOCK-GUEST-INTERNAL`) is configured to block internal traffic from the guest VLAN.  
- A banner is configured to warn unauthorized users.  

#### ⚠ Areas for Improvement
- Dynamic ARP Inspection (DAI) is not enabled, which could allow ARP spoofing attacks.  
- Port security is not enabled on any interfaces, leaving the switch vulnerable to MAC flooding and unauthorized device access.  
- IP Source Guard is not enabled, which could allow spoofed IP traffic.  
- 802.1X is not configured, leaving wired access vulnerable to unauthorized device connections.  
- VLAN 666 is used as the native VLAN on trunk ports, which is a security risk if not properly secured.  
- No SNMP configuration is present, which could hinder monitoring and management.  

#### Recommendations
- Enable **Dynamic ARP Inspection (DAI)** on VLANs where it is needed.  
- Enable **IP Source Guard** on VLANs to prevent IP spoofing.  
- Implement **port security** on access ports to prevent MAC flooding and unauthorized device access.  
- Consider enabling **802.1X** for secure wired access.  
- Change the **native VLAN** on trunk ports to a non-routed VLAN (e.g., VLAN 999) to reduce security risks.  
- Configure **SNMP** with appropriate community strings and access controls.  
- Consider enabling **LLDP** for network discovery and documentation.  

---

## Summary

dis-sw02 is a **Distribution Layer** switch running Cisco IOS 15.2(2)E9. It serves as an aggregation point between access switches and the core, with multiple VLAN interfaces and inter-VLAN routing enabled. The configuration includes basic security features such as SSH, AAA, and DHCP snooping, but lacks advanced protections like DAI, port security, and 802.1X. The configuration is generally well-structured and follows best practices for a distribution switch, but additional hardening is recommended to improve security posture.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T11:11:50.880756