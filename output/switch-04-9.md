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
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
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

### Static Routes:
- **0.0.0.0 0.0.0.0 via 10.99.1.1** ✓ VERIFIED  

---

## Configuration Quality Assessment

### Device Role
- **Role**: ~ INFERRED  
  - This device is a **Distribution Layer** switch.  
  - Justification: It has multiple VLAN interfaces (SVIs) with IP addresses, inter-VLAN routing enabled, and trunk ports connecting to both core and access switches. It does not have many access ports or port security, which is typical of access layer switches.  

---

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, preventing weak authentication methods.  
- AAA is enabled with local authentication for console and VTY access.  
- DHCP snooping is enabled globally, which helps prevent rogue DHCP servers.  
- CDP is disabled, reducing the risk of network discovery attacks.  
- Management access is restricted via ACL `MGMT-ACCESS`, limiting access to specific subnets.  
- Guest VLAN traffic is restricted via extended ACL `BLOCK-GUEST-INTERNAL`, preventing internal communication.  
- Logging is enabled to 10.99.0.50, which is a good practice for auditing and troubleshooting.  

#### ⚠ Areas for Improvement
- Dynamic ARP Inspection (DAI) is not enabled, which could leave the network vulnerable to ARP spoofing.  
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect.  
- IP Source Guard is not enabled, which could allow spoofed IP addresses to bypass ACLs.  
- 802.1X is not configured, which could leave wired access vulnerable to unauthorized device access.  
- VLAN 666 is used as the native VLAN on trunk ports, which is a security risk if it is not properly secured.  
- No SNMP configuration is present, which could hinder monitoring and management.  

#### Recommendations
- Enable **Dynamic ARP Inspection (DAI)** on VLANs where it is needed.  
- Enable **IP Source Guard** on VLANs where it is needed to prevent IP spoofing.  
- Enable **port security** on access ports to prevent unauthorized device access.  
- Consider enabling **802.1X** for wired access control.  
- Change the **native VLAN** on trunk ports to a non-routed VLAN (e.g., VLAN 999) to reduce the risk of VLAN hopping.  
- Implement **SNMP** with secure community strings and access control.  
- Consider enabling **LLDP** for network discovery and monitoring.  

---

## Summary

dis-sw01 is a **Distribution Layer** switch running Cisco IOS 15.2(2)E9. It provides inter-VLAN routing for multiple VLANs, including management, employee, guest, printer, and VoIP networks. The device is configured with secure access controls, including SSH, AAA, and ACLs, and has a strong logging and NTP configuration. However, there are several security features missing, such as DAI, port security, and 802.1X, which should be implemented to improve the security posture.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-10T21:32:55.432645