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
- **Access Control Lists (ACLs)**:
  - Standard ACL 'MGMT-ACCESS': 3 entries ✓ VERIFIED

## Network Services
### Logging
- **Syslog Enabled**: ✓ VERIFIED
- **Logging Server**: 10.99.0.50 ✓ VERIFIED
- **Logging Trap Level**: informational ✓ VERIFIED (from `logging trap informational`)

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
- SSH is enabled with version 2 and a timeout of 60 seconds ✓ VERIFIED
- AAA is enabled with RADIUS authentication and local fallback ✓ VERIFIED
- DHCP snooping is enabled on VLANs 10 and 20 ✓ VERIFIED
- Dynamic ARP Inspection (DAI) is enabled on VLANs 10 and 20 ✓ VERIFIED
- Port security is enabled on 4 access ports ✓ VERIFIED
- 802.1X is enabled for secure device authentication ✓ VERIFIED
- CDP is disabled, reducing potential attack surface ✓ VERIFIED
- Management access is restricted via ACL `MGMT-ACCESS` ✓ VERIFIED
- A local emergency admin user is configured with privilege 15 ✓ VERIFIED

#### ⚠ Areas for Improvement
- NTP is not configured, which may impact time-based security and logging ✓ VERIFIED
- SNMP is not configured, which may limit monitoring and management capabilities ✓ VERIFIED
- IP Source Guard is not enabled, which could help prevent IP spoofing ✓ VERIFIED
- LLDP is not enabled, which could be useful for network discovery and troubleshooting ✓ VERIFIED
- No explicit logging of failed login attempts or 802.1X authentication failures is configured ~ INFERRED
- No rate limiting or throttling for SSH or RADIUS is configured ~ INFERRED

#### Recommendations
- Enable and configure NTP with at least one NTP server for accurate timekeeping ~ INFERRED
- Consider enabling SNMP for network monitoring and management ~ INFERRED
- Enable IP Source Guard on VLANs 10 and 20 to prevent IP spoofing ~ INFERRED
- Enable LLDP for network discovery and troubleshooting ~ INFERRED
- Add logging for failed SSH and 802.1X authentication attempts to improve security visibility ~ INFERRED
- Consider implementing rate limiting for SSH and RADIUS to prevent brute-force attacks ~ INFERRED

## Summary

This device, **switch-06**, is an **Access Layer** switch based on its configuration, which includes multiple access ports with port security, 802.1X authentication, and no routing enabled. It is configured with VLANs for user segmentation and has a management VLAN with secure access controls. The device is running Cisco IOS version 15.2(2)E9 and is part of the domain `secure.bedrift.no`.

The configuration is generally well-structured and includes several strong security features such as AAA, 802.1X, DHCP snooping, and DAI. However, there are areas for improvement, particularly in time synchronization and network monitoring capabilities.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T11:30:07.183482