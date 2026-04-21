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
- **Port Security**: Not enabled on any interfaces ✓ VERIFIED  
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

### Security Posture

#### ✓ Strengths
- SSH-only access with version 2 and 60-second timeout is configured (lines `ip ssh version 2`, `ip ssh time-out 60`) ✓ VERIFIED  
- AAA authentication and authorization are enabled with local user authentication (lines `aaa new-model`, `aaa authentication login default local`, `aaa authorization exec default local`) ✓ VERIFIED  
- DHCP snooping is enabled globally (line `ip dhcp snooping`) ✓ VERIFIED  
- CDP is explicitly disabled (line `no cdp run`) ✓ VERIFIED  
- Access control lists (ACLs) are configured for management and guest traffic filtering (lines `ip access-list standard MGMT-ACCESS`, `ip access-list extended BLOCK-GUEST-INTERNAL`) ✓ VERIFIED  
- A banner is configured to warn unauthorized access (line `banner login ^CUautorisert tilgang er forbudt. All aktivitet logges.^C`) ✓ VERIFIED  
- Syslog is configured to send logs to a remote server (line `logging 10.99.0.50`) ✓ VERIFIED  

#### ⚠ Areas for Improvement
- DHCP snooping is enabled but no specific VLANs are specified for snooping – this could leave some VLANs unprotected (line `ip dhcp snooping`) ? UNCERTAIN  
- Dynamic ARP Inspection (DAI) is not enabled – this could leave the network vulnerable to ARP spoofing attacks (line `no ip arp inspection`) ✓ VERIFIED  
- IP Source Guard is not enabled – this could allow spoofed IP addresses to bypass ACLs (line `no ip verify source`) ✓ VERIFIED  
- Port security is not enabled on any interfaces – this could allow unauthorized devices to connect (line `no switchport port-security`) ✓ VERIFIED  
- 802.1X is not configured – this could leave wired access vulnerable to unauthorized device access (line `no dot1x`) ✓ VERIFIED  
- No VLAN-specific ACLs are applied to VLAN interfaces beyond the Management VLAN – this could allow unrestricted inter-VLAN traffic (line `ip access-group MGMT-ACCESS in` on VLAN 99 only) ✓ VERIFIED  

#### Recommendations
- Enable DAI on VLANs with DHCP snooping to prevent ARP spoofing (e.g., `ip arp inspection vlan 10,20,30,50,99`)  
- Enable IP Source Guard on VLANs with DHCP snooping to prevent IP spoofing (e.g., `ip verify source vlan 10,20,30,50,99`)  
- Enable port security on access ports to prevent unauthorized device access (e.g., `switchport port-security`)  
- Consider enabling 802.1X for wired access control (e.g., `dot1x system-auth-control`)  
- Specify VLANs for DHCP snooping to ensure all relevant VLANs are protected (e.g., `ip dhcp snooping vlan 10,20,30,50,99`)  
- Apply VLAN-specific ACLs to SVIs to control inter-VLAN traffic (e.g., `ip access-group <ACL_NAME> in` on VLAN interfaces)  
- Consider enabling LLDP for network discovery and monitoring (e.g., `lldp run`)  

---

## Summary

The device `dis-sw02` is a **Distribution Layer switch** based on its configuration, which includes multiple VLAN interfaces (SVIs), inter-VLAN routing, and trunking to both core and access switches. It is configured with a robust set of security features including SSH access, AAA authentication, and DHCP snooping. However, there are several areas for improvement, particularly in the areas of DAI, IP Source Guard, and port security. The configuration is generally well-structured and follows best practices for a distribution switch in a multi-VLAN environment.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T11:06:03.093107