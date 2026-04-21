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

- **GigabitEthernet0/5**:
  - Status: Shutdown ✓ VERIFIED  
  - Config Line: `shutdown`  

- **GigabitEthernet0/6**:
  - Status: Shutdown ✓ VERIFIED  
  - Config Line: `shutdown`  

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
- **DHCP Snooping**: Enabled ✓ VERIFIED  
  - Information Option: Enabled ✓ VERIFIED  
  - VLANs: Not specified ✓ VERIFIED  
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
- **Syslog Server**: 10.99.0.50 ✓ VERIFIED  
- **Logging Level**: informational ✓ VERIFIED  
  - Config Line: `logging trap informational`  

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED  
- **NTP Authentication**: Disabled ✓ VERIFIED  
  - Config Line: `ntp server 10.99.0.1`  

### DNS
- **DNS Domain Name**: core.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  
  - Config Line: `no ip domain-lookup`  

### SNMP
- **SNMP**: Not configured ✓ VERIFIED  

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
- SSH-only VTY access with version 2 and 60-second timeout ✓ VERIFIED  
- AAA authentication and authorization with local user database ✓ VERIFIED  
- DHCP snooping enabled with information option ✓ VERIFIED  
- CDP is explicitly disabled ✓ VERIFIED  
- Management access is restricted via ACL 'MGMT-ACCESS' ✓ VERIFIED  
- Syslog and NTP are configured for operational visibility and time synchronization ✓ VERIFIED  

#### ⚠ Areas for Improvement
- Dynamic ARP Inspection (DAI) is not enabled, which could leave the network vulnerable to ARP spoofing attacks ? UNCERTAIN  
- Port security is not configured on any interfaces, which could allow unauthorized device access ? UNCERTAIN  
- 802.1X is not configured, which could leave wired access vulnerable to unauthorized device connections ? UNCERTAIN  
- IP Source Guard is not enabled, which could allow spoofed IP addresses to bypass ACLs ? UNCERTAIN  
- VLAN 1 is active but has no IP address and is shutdown, which is unnecessary and could be removed ? UNCERTAIN  
- Native VLAN 666 is used on trunk ports, which is not a best practice (should be unused or non-routed) ? UNCERTAIN  

#### Recommendations
- Enable Dynamic ARP Inspection (DAI) on VLANs where DHCP snooping is active.  
- Implement port security on access ports to prevent unauthorized device access.  
- Enable 802.1X for secure wired access control.  
- Enable IP Source Guard to prevent IP spoofing.  
- Remove VLAN 1 configuration if it is not needed.  
- Consider changing the native VLAN on trunk ports to an unused VLAN (e.g., VLAN 999) to prevent VLAN hopping attacks.  
- Ensure all VLANs with DHCP snooping enabled are explicitly listed in the configuration.  

---

## Summary

dis-sw02 is a **Distribution Layer switch** (~ INFERRED) based on its configuration of multiple VLANs with SVIs, inter-VLAN routing, and trunking to both core and access switches. The device is configured with strong management and security practices, including SSH-only access, AAA, and ACLs. However, there are several areas for improvement, particularly in Layer 2 security features such as DAI, port security, and IP Source Guard. The configuration is well-structured and follows best practices in many areas, but additional hardening is recommended to fully secure the device.  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T09:19:12.118923