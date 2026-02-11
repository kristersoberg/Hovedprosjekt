# Network Device Documentation: switch-06

## Device Information
- **Hostname**: switch-06 ✓ VERIFIED  
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED  
- **Domain Name**: secure.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: 99 ✓ VERIFIED  
- **IP Address**: 10.99.1.6 ✓ VERIFIED  
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **VTY Transport Input**: ssh ✓ VERIFIED  
- **VTY Authentication**: None ✓ VERIFIED  
- **VTY Access Class**: MGMT-ACCESS (in) ✓ VERIFIED  
- **Console Authentication**: CONSOLE ✓ VERIFIED  
- **Console Logging Synchronous**: True ✓ VERIFIED  

---

## AAA Configuration
- **AAA Enabled**: ✓ VERIFIED  
- **Authentication Methods**:
  - `aaa authentication login default group radius local` ✓ VERIFIED  
  - `aaa authentication login CONSOLE local` ✓ VERIFIED  
  - `aaa authentication dot1x default group radius` ✓ VERIFIED  
- **Authorization Methods**:
  - `aaa authorization network default group radius` ✓ VERIFIED  
- **Accounting Methods**:
  - `aaa accounting dot1x default start-stop group radius` ✓ VERIFIED  
- **RADIUS Servers**: 10.99.0.30, 10.99.0.31 ✓ VERIFIED  
- **Local Users**:
  - `emergency-admin` (privilege 15) ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED  
- **VLAN IDs**: 10, 20, 99, 666, 999 ✓ VERIFIED  
- **VLAN Interfaces (SVIs)**:
  - **VLAN 1**:
    - Status: Shutdown ✓ VERIFIED  
  - **VLAN 99**:
    - Description: Management SVI ✓ VERIFIED  
    - IP: 10.99.1.6 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
    - ACL In: MGMT-ACCESS ✓ VERIFIED  
- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED  
- **Active (no shutdown)**: 6 ✓ VERIFIED  
- **Shutdown**: 20 ✓ VERIFIED  
- **Access Ports**: 4 ✓ VERIFIED  
- **Trunk Ports**: 2 ✓ VERIFIED  
- **Port Security Enabled**: 4 interfaces ✓ VERIFIED  

### Key Active Interfaces
- **FastEthernet0/1**:
  - Description: 802.1X-port kontor C301  
  - Mode: access  
  - VLAN: 10  
  - Port-Sec: ✓  
  - Config Line: `interface FastEthernet0/1`  
- **FastEthernet0/2**:
  - Description: 802.1X-port kontor C302  
  - Mode: access  
  - VLAN: 10  
  - Port-Sec: ✓  
  - Config Line: `interface FastEthernet0/2`  
- **FastEthernet0/3**:
  - Description: 802.1X-port kontor C303  
  - Mode: access  
  - VLAN: 10  
  - Port-Sec: ✓  
  - Config Line: `interface FastEthernet0/3`  
- **FastEthernet0/4**:
  - Description: 802.1X-port kontor C304  
  - Mode: access  
  - VLAN: 10  
  - Port-Sec: ✓  
  - Config Line: `interface FastEthernet0/4`  
- **FastEthernet0/23**:
  - Description: Uplink-1 dis-sw01 gig0/5  
  - Mode: trunk  
  - Allowed VLANs: 10, 20, 99, 999  
  - Config Line: `interface FastEthernet0/23`  
- **FastEthernet0/24**:
  - Description: Uplink-2 dis-sw02 gig0/5  
  - Mode: trunk  
  - Allowed VLANs: 10, 20, 99, 999  
  - Config Line: `interface FastEthernet0/24`  

---

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED  
- **Per-VLAN Priorities**:
  - VLAN 10: 32768 ✓ VERIFIED  
  - VLAN 20: 32768 ✓ VERIFIED  
  - VLAN 99: 32768 ✓ VERIFIED  
- **Config Line**: `spanning-tree mode rapid-pvst`  

---

## Security Features
- **DHCP Snooping**: ✓ Enabled on VLANs 10, 20 ✓ VERIFIED  
  - Information Option: Disabled ✓ VERIFIED  
  - Config Line: `ip dhcp snooping vlan 10,20`  
- **Dynamic ARP Inspection (DAI)**: ✓ Enabled on VLANs 10, 20 ✓ VERIFIED  
  - Config Line: `ip arp inspection vlan 10,20`  
- **Port Security**: ✓ Enabled on 4 interfaces ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **802.1X**: ✓ Enabled ✓ VERIFIED  
  - Config Line: `dot1x system-auth-control`  
- **CDP**: Disabled ✓ VERIFIED  
  - Config Line: `no cdp run`  
- **LLDP**: Not enabled ✓ VERIFIED  

---

## Network Services

### Logging
- **Syslog Enabled**: ✓ VERIFIED  
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  
- **Logging Trap Level**: informational ✓ VERIFIED  
- **Config Line**: `logging 10.99.0.50`  

### NTP
- **NTP Server**: Not configured ✓ VERIFIED  
- **NTP Authentication**: Not configured ✓ VERIFIED  

### SNMP
- **SNMP**: Not configured ✓ VERIFIED  

### DNS
- **DNS Domain Name**: secure.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  
  - Config Line: `no ip domain-lookup`  

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **Config Line**: `ip default-gateway 10.99.1.1`  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a timeout of 60 seconds ✓ VERIFIED  
- Port security is enabled on 4 access ports ✓ VERIFIED  
- DHCP snooping is enabled on VLANs 10 and 20 ✓ VERIFIED  
- Dynamic ARP Inspection (DAI) is enabled on VLANs 10 and 20 ✓ VERIFIED  
- 802.1X authentication is enabled for secure user access ✓ VERIFIED  
- CDP is disabled, reducing potential attack surface ✓ VERIFIED  
- AAA is configured with RADIUS and local fallback for login and dot1x ✓ VERIFIED  
- A standard ACL (`MGMT-ACCESS`) is applied to the management interface for access control ✓ VERIFIED  

#### ⚠ Areas for Improvement
- NTP is not configured, which may impact time-based logging and security auditing ? UNCERTAIN  
- IP Source Guard is not configured, which could help prevent IP spoofing ? UNCERTAIN  
- SNMP is not configured, which may limit monitoring capabilities ? UNCERTAIN  
- No explicit logging of failed login attempts or 802.1X authentication failures ? UNCERTAIN  
- No rate limiting or throttling for SSH or RADIUS requests ? UNCERTAIN  

#### Recommendations
- ~ INFERRED: Enable NTP with a trusted server to ensure accurate time synchronization for logs and security events.  
- ~ INFERRED: Consider enabling IP Source Guard on VLANs 10 and 20 to prevent IP spoofing.  
- ~ INFERRED: Enable SNMP with secure community strings and access control for monitoring.  
- ~ INFERRED: Add logging for failed SSH and 802.1X authentication attempts to improve security visibility.  
- ~ INFERRED: Consider implementing rate limiting for SSH and RADIUS to prevent brute-force attacks.  
- ~ INFERRED: Review and tighten the `MGMT-ACCESS` ACL to limit access to only necessary IP ranges.  

---

## Summary

This device, **switch-06**, is an **Access Layer switch** based on its configuration, which includes multiple access ports with 802.1X authentication, port security, and VLAN tagging. It connects to a distribution layer via two trunk links and provides management access via VLAN 99. The configuration is well-structured and includes strong security features such as SSH, AAA, DHCP snooping, and DAI. However, there are opportunities to enhance security further by enabling NTP, IP Source Guard, and more detailed logging.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T09:33:17.683880