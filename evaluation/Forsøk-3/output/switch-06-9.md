# Network Device Documentation: switch-06

## Device Information
- **Hostname**: switch-06 ✓ VERIFIED
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED
- **Domain Name**: secure.bedrift.no ✓ VERIFIED
- **Config Register**: Not configured ✓ VERIFIED

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
  - Config Line: `interface FastEthernet0/1` ✓ VERIFIED
- **FastEthernet0/2**:
  - Description: 802.1X-port kontor C302
  - Mode: access
  - VLAN: 10
  - Port-Sec: ✓
  - Config Line: `interface FastEthernet0/2` ✓ VERIFIED
- **FastEthernet0/3**:
  - Description: 802.1X-port kontor C303
  - Mode: access
  - VLAN: 10
  - Port-Sec: ✓
  - Config Line: `interface FastEthernet0/3` ✓ VERIFIED
- **FastEthernet0/4**:
  - Description: 802.1X-port kontor C304
  - Mode: access
  - VLAN: 10
  - Port-Sec: ✓
  - Config Line: `interface FastEthernet0/4` ✓ VERIFIED
- **FastEthernet0/23**:
  - Description: Uplink-1 dis-sw01 gig0/5
  - Mode: trunk
  - Allowed VLANs: 10, 20, 99, 999
  - Config Line: `interface FastEthernet0/23` ✓ VERIFIED
- **FastEthernet0/24**:
  - Description: Uplink-2 dis-sw02 gig0/5
  - Mode: trunk
  - Allowed VLANs: 10, 20, 99, 999
  - Config Line: `interface FastEthernet0/24` ✓ VERIFIED

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED
- **Per-VLAN Priorities**:
  - VLAN 10: 32768 ✓ VERIFIED
  - VLAN 20: 32768 ✓ VERIFIED
  - VLAN 99: 32768 ✓ VERIFIED

## Security Features
- **DHCP Snooping**: ✓ Enabled on VLANs 10, 20 ✓ VERIFIED
  - Information Option: Disabled ✓ VERIFIED
- **Dynamic ARP Inspection (DAI)**: ✓ Enabled on VLANs 10, 20 ✓ VERIFIED
- **Port Security**: ✓ Enabled on 4 interfaces ✓ VERIFIED
- **802.1X Authentication**: ✓ Enabled ✓ VERIFIED
- **CDP**: Disabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED
- **IP Source Guard**: Not configured ✓ VERIFIED
- **Access Control Lists (ACLs)**:
  - Standard ACL 'MGMT-ACCESS': 3 entries ✓ VERIFIED
    - `permit 10.99.0.0 0.0.0.255`
    - `permit 10.99.1.0 0.0.0.255`
    - `deny any`
    - Config Line: `ip access-list standard MGMT-ACCESS` ✓ VERIFIED

## Network Services
### Logging
- **Syslog Enabled**: ✓ VERIFIED
- **Logging Server**: 10.99.0.50 ✓ VERIFIED
- **Logging Level**: informational ✓ VERIFIED

### NTP
- **NTP Server**: Not configured ✓ VERIFIED
- **NTP Authentication**: Not configured ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

### DNS
- **DNS Domain Name**: secure.bedrift.no ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, ensuring secure remote access.
- Port security is enabled on 4 access ports, limiting unauthorized device connections.
- 802.1X authentication is enabled, providing secure user and device authentication.
- DHCP snooping is enabled on VLANs 10 and 20, preventing rogue DHCP servers.
- Dynamic ARP Inspection (DAI) is enabled on VLANs 10 and 20, mitigating ARP spoofing.
- CDP is disabled, reducing potential attack vectors.
- A standard ACL (`MGMT-ACCESS`) is applied to the management interface, restricting access to trusted subnets.
- AAA is enabled with RADIUS authentication and local fallback, ensuring strong user authentication.
- A banner is configured to warn unauthorized users.

#### ⚠ Areas for Improvement
- NTP is not configured, which could impact time-based logging and security.
- SNMP is not configured, which may limit monitoring and management capabilities.
- IP Source Guard is not enabled, which could leave the network vulnerable to IP spoofing.
- LLDP is not enabled, which may limit network discovery and troubleshooting.
- No logging to a remote syslog server is configured beyond the single IP address.
- No rate limiting or throttling is configured for SSH access.
- No access control is applied to the console port beyond local authentication.
- No VLAN-specific STP root guard or BPDU guard is configured beyond what is already in place.

#### Recommendations
- Configure NTP with at least one NTP server to ensure accurate time synchronization.
- Enable SNMP with appropriate community strings and access control to improve monitoring.
- Enable IP Source Guard on VLANs 10 and 20 to prevent IP spoofing.
- Consider enabling LLDP for network discovery and troubleshooting.
- Add rate limiting to SSH access to prevent brute-force attacks.
- Add access control to the console port using a local ACL.
- Consider enabling STP root guard on uplink ports to prevent accidental STP root changes.
- Review and tighten the `MGMT-ACCESS` ACL to ensure it only allows necessary management traffic.

## Summary

This device, **switch-06**, is an **Access Layer** switch, as evidenced by the large number of access ports, port security, and 802.1X authentication. It is not performing routing and is primarily responsible for connecting end-user devices to the network. The configuration is well-structured and includes several strong security features such as SSH, 802.1X, DHCP snooping, and DAI. However, there are areas for improvement, particularly in time synchronization, monitoring, and additional security hardening.

~ INFERRED: Based on the configuration, this switch is likely located in a user-access area, such as an office or classroom, and is connected to a distribution layer switch via trunk ports.

~ INFERRED: The use of VLANs 10, 20, 99, 666, and 999 suggests a segmented network design with roles for employees, guests, management, and quarantine.

~ INFERRED: The presence of RADIUS servers and 802.1X indicates a centralized authentication and authorization model, likely part of a larger enterprise network.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T11:35:07.408681