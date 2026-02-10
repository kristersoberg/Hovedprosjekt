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
- **Authorization**:
  - `aaa authorization network default group radius` ✓ VERIFIED  
- **Accounting**:
  - `aaa accounting dot1x default start-stop group radius` ✓ VERIFIED  
- **RADIUS Servers**:
  - 10.99.0.30 ✓ VERIFIED  
  - 10.99.0.31 ✓ VERIFIED  
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

### Key Active Interfaces:
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
- **Port Security**: Enabled on 4 interfaces ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
  - Config Line: `no cdp run`  
- **LLDP**: Not enabled ✓ VERIFIED  
- **802.1X**: Enabled ✓ VERIFIED  
  - Config Line: `dot1x system-auth-control`  

---

## Network Services
### Logging
- **Syslog Enabled**: ✓ VERIFIED  
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  
- **Logging Trap Level**: informational ✓ VERIFIED  
  - Config Line: `logging 10.99.0.50`  

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
  - Config Line: `ip default-gateway 10.99.1.1`  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, ensuring secure remote access.  
- DHCP snooping is enabled on VLANs 10 and 20, preventing rogue DHCP servers.  
- Dynamic ARP Inspection (DAI) is enabled on VLANs 10 and 20, mitigating ARP spoofing.  
- Port security is enabled on 4 access ports, limiting unauthorized device connections.  
- 802.1X authentication is enabled, providing secure user and device authentication.  
- CDP is disabled, reducing potential attack vectors.  
- AAA is configured with RADIUS authentication and local fallback, ensuring strong access control.  
- A standard ACL (`MGMT-ACCESS`) is applied to the management interface, restricting access to trusted subnets.  

#### ⚠ Areas for Improvement
- NTP is not configured, which could impact time-based logging and security auditing.  
- IP Source Guard is not enabled, which could leave the network vulnerable to IP spoofing.  
- LLDP is not enabled, which could limit network discovery and troubleshooting capabilities.  
- No SNMP configuration is present, which may hinder monitoring and management.  
- No VLAN 1 is used for management; it is shutdown, which is a good practice, but VLAN 99 is used for management.  
- No VLAN-specific STP root guard or BPDU guard beyond what is already configured.  

#### Recommendations
- Enable NTP with at least one trusted NTP server to ensure accurate time synchronization.  
- Enable IP Source Guard on VLANs 10 and 20 to prevent IP spoofing.  
- Consider enabling LLDP for network discovery and troubleshooting.  
- Configure SNMP with appropriate community strings and access controls for monitoring.  
- Review and tighten the `MGMT-ACCESS` ACL to ensure it only allows necessary management traffic.  
- Consider enabling BPDU guard on all access ports to prevent STP attacks.  
- Ensure all unused interfaces remain in shutdown state to reduce attack surface.  

---

## Summary

`switch-06` is an **Access Layer** switch, as evidenced by the large number of access ports, port security, and 802.1X authentication. It is not performing routing and is connected to a distribution layer via trunk links. The configuration is generally well-structured and secure, with strong AAA, SSH, and Layer 2 security features in place. However, there are opportunities to improve with NTP, IP Source Guard, and SNMP configuration. The device is configured for secure management access and supports VLAN-based segmentation for user and guest traffic.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-10T22:19:41.004754