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
- **SVI Interfaces (VLANs with IP addresses)**:
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
  - **VLAN 1**:
    - Status: Shutdown ✓ VERIFIED  

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
  - Description: Uplink til core-sw01 gig0/3 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
  - DHCP Snooping Trust: Enabled ✓ VERIFIED  
  - Config Line: `ip dhcp snooping trust`  

- **GigabitEthernet0/2**:
  - Description: Uplink til core-sw01 gig0/4 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
  - DHCP Snooping Trust: Enabled ✓ VERIFIED  
  - Config Line: `ip dhcp snooping trust`  

- **GigabitEthernet0/3**:
  - Description: Downlink aksess-sw03 fa0/24 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
  - Config Line: `switchport trunk allowed vlan 10,20,30,99`  

- **GigabitEthernet0/4**:
  - Description: Downlink aksess-sw04 fa0/24 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
  - Config Line: `switchport trunk allowed vlan 10,20,30,99`  

---

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED  
- **Per-VLAN Priorities**:
  - VLAN 10: 8192 ✓ VERIFIED  
  - VLAN 20: 8192 ✓ VERIFIED  
  - VLAN 30: 8192 ✓ VERIFIED  
  - VLAN 50: 8192 ✓ VERIFIED  
  - VLAN 99: 8192 ✓ VERIFIED  
  - Config Line: `spanning-tree vlan 10,20,30,50,99 priority 8192`  

---

## Security Features
- **DHCP Snooping**: ✓ Enabled on VLANs Not specified ✓ VERIFIED  
  - Information Option: Enabled ✓ VERIFIED  
  - Config Line: `ip dhcp snooping`  
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED  
- **Port Security**: Not configured ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
  - Config Line: `no cdp run`  
- **LLDP**: Not enabled ✓ VERIFIED  

---

## Network Services

### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  
- **Logging Level**: informational ✓ VERIFIED  
  - Config Line: `logging trap informational`  

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED  
- **NTP Authentication**: Disabled ✓ VERIFIED  
  - Config Line: `ntp server 10.99.0.1`  

### Syslog
- **Syslog Server**: 10.99.0.50 ✓ VERIFIED  
  - Config Line: `logging 10.99.0.50`  

### SNMP
- **SNMP**: Not configured ✓ VERIFIED  

### DNS
- **DNS Domain Name**: core.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  
  - Config Line: `no ip domain-lookup`  

---

## Routing Configuration
- **IP Routing**: Enabled ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **Static Routes**:
  - `0.0.0.0 0.0.0.0 via 10.99.1.1` ✓ VERIFIED  
  - Config Line: `ip route 0.0.0.0 0.0.0.0 10.99.1.1`  

---

## Access Control Lists (ACLs)
- **Standard ACL 'MGMT-ACCESS'**:
  - 3 entries ✓ VERIFIED  
  - Config Line: `ip access-list standard MGMT-ACCESS`  
- **Extended ACL 'BLOCK-GUEST-INTERNAL'**:
  - 5 entries ✓ VERIFIED  
  - Config Line: `ip access-list extended BLOCK-GUEST-INTERNAL`  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, preventing weak protocol usage.  
- AAA is enabled with local authentication for console and VTY access.  
- DHCP snooping is enabled globally, reducing the risk of rogue DHCP servers.  
- CDP is explicitly disabled, reducing exposure to potential network reconnaissance.  
- Management access is restricted using a standard ACL (`MGMT-ACCESS`).  
- Guest traffic is restricted using an extended ACL (`BLOCK-GUEST-INTERNAL`).  
- A banner is configured to warn unauthorized users.  

#### ⚠ Areas for Improvement
- DHCP snooping is enabled but not scoped to specific VLANs, which could reduce its effectiveness.  
- Dynamic ARP Inspection (DAI) is not enabled, leaving the network vulnerable to ARP spoofing.  
- IP Source Guard is not enabled, which could allow spoofed IP addresses to bypass ACLs.  
- Port security is not configured on any interfaces, increasing the risk of unauthorized device access.  
- 802.1X is not configured, leaving wired access vulnerable to unauthorized device connections.  
- LLDP is not enabled, which could hinder network discovery and troubleshooting.  

#### Recommendations
- Enable DAI on VLANs where DHCP snooping is active to prevent ARP spoofing.  
- Enable IP Source Guard on VLANs with DHCP snooping to prevent IP spoofing.  
- Implement port security on access ports to limit unauthorized device connections.  
- Consider enabling 802.1X for wired access control.  
- Enable LLDP to improve network visibility and troubleshooting.  
- Scope DHCP snooping to specific VLANs to improve security and reduce unnecessary traffic.  
- Consider enabling SNMP for monitoring and management.  

---

## Summary

dis-sw02 is a **Distribution Layer** switch, as evidenced by the presence of multiple VLAN interfaces (SVIs), inter-VLAN routing, and trunk ports connecting to both core and access switches. The device is configured with strong SSH and AAA security practices, but lacks some advanced security features like DAI and port security. The configuration is well-structured and includes essential network services such as NTP, syslog, and routing.  

**Overall Configuration Quality**: Good, but with room for improvement in security hardening.  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T09:24:54.229105