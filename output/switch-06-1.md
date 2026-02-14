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
- **RADIUS Servers**:
  - 10.99.0.30 ✓ VERIFIED
  - 10.99.0.31 ✓ VERIFIED
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
- **FastEthernet0/2**:
  - Description: 802.1X-port kontor C302
  - Mode: access
  - VLAN: 10
  - Port-Sec: ✓
- **FastEthernet0/3**:
  - Description: 802.1X-port kontor C303
  - Mode: access
  - VLAN: 10
  - Port-Sec: ✓
- **FastEthernet0/4**:
  - Description: 802.1X-port kontor C304
  - Mode: access
  - VLAN: 10
  - Port-Sec: ✓
- **FastEthernet0/23**:
  - Description: Uplink-1 dis-sw01 gig0/5
  - Mode: trunk
  - Allowed VLANs: 10, 20, 99, 999
- **FastEthernet0/24**:
  - Description: Uplink-2 dis-sw02 gig0/5
  - Mode: trunk
  - Allowed VLANs: 10, 20, 99, 999

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED
- **Per-VLAN Priorities**:
  - VLAN 10: 32768 ✓ VERIFIED
  - VLAN 20: 32768 ✓ VERIFIED
  - VLAN 99: 32768 ✓ VERIFIED

## Security Features
- **DHCP Snooping**:
  - Enabled on VLANs 10, 20 ✓ VERIFIED
  - Information Option: Disabled ✓ VERIFIED
- **Dynamic ARP Inspection (DAI)**:
  - Enabled on VLANs 10, 20 ✓ VERIFIED
- **Port Security**:
  - Enabled on 4 interfaces ✓ VERIFIED
- **802.1X**:
  - Enabled ✓ VERIFIED
- **CDP**:
  - Disabled ✓ VERIFIED
- **LLDP**:
  - Not enabled ✓ VERIFIED
- **IP Source Guard**:
  - Not configured ✓ VERIFIED

## Network Services
### Logging
- **Syslog Enabled**: ✓ VERIFIED
- **Logging Server**: 10.99.0.50 ✓ VERIFIED
- **Logging Trap Level**: informational ✓ VERIFIED

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
- AAA is enabled with RADIUS authentication for login and 802.1X, and local fallback for console access.
- DHCP snooping is enabled on VLANs 10 and 20, preventing rogue DHCP servers.
- Dynamic ARP Inspection (DAI) is enabled on VLANs 10 and 20, mitigating ARP spoofing.
- Port security is enabled on 4 access ports, limiting unauthorized device connections.
- CDP is disabled, reducing potential attack surface.
- A standard ACL (`MGMT-ACCESS`) is applied to the management interface, restricting access to specific subnets.
- 802.1X is enabled on access ports, enforcing device authentication before network access.

#### ⚠ Areas for Improvement
- **NTP is not configured**, which could lead to time synchronization issues and affect log correlation.
- **SNMP is not configured**, which limits monitoring and management capabilities.
- **IP Source Guard is not enabled**, which could allow spoofed IP addresses to bypass security controls.
- **LLDP is not enabled**, which could hinder network discovery and troubleshooting.
- **No password complexity policy is enforced**, as the configuration does not specify one.
- **No rate limiting or throttling is configured for SSH**, which could leave the device vulnerable to brute-force attacks.
- **No logging to a remote syslog server is configured beyond the single server**, which could be a single point of failure.

#### Recommendations
- **Enable NTP** with at least one trusted server to ensure accurate timekeeping.
- **Enable SNMP** with appropriate community strings and access controls for monitoring.
- **Enable IP Source Guard** on VLANs 10 and 20 to prevent IP spoofing.
- **Enable LLDP** to improve network visibility and troubleshooting.
- **Implement a password policy** using `username` and `secret` commands with complexity requirements.
- **Add rate limiting to SSH** using `ip ssh rate-limit` to prevent brute-force attacks.
- **Add a second syslog server** to provide redundancy and ensure log availability.

## Summary

This device, **switch-06**, is an **Access layer switch** based on its configuration, which includes multiple access ports with 802.1X authentication, port security, and no routing enabled. It is configured with VLANs for management, employee access, guest access, and quarantine, and it connects to a distribution layer via two trunk links.

The configuration is generally well-structured and includes several strong security features such as AAA, 802.1X, DHCP snooping, and DAI. However, there are notable gaps in NTP, SNMP, and IP Source Guard, which should be addressed to improve the device's security and manageability.

**Overall, the configuration is functional and secure, but it can be enhanced with additional hardening and monitoring features.**

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T15:11:53.945040