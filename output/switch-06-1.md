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
- **802.1X**: ✓ Enabled ✓ VERIFIED
- **IP Source Guard**: Not configured ✓ VERIFIED
- **CDP**: Disabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED
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
- **Config Line**: `logging 10.99.0.50` ✓ VERIFIED

### NTP
- **NTP Server**: Not configured ✓ VERIFIED
- **NTP Authentication**: Not configured ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

### DNS
- **DNS Domain Name**: secure.bedrift.no ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED
- **Config Line**: `no ip domain-lookup` ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED
- **Config Line**: `ip default-gateway 10.99.1.1` ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, ensuring secure remote access.
- AAA is enabled with RADIUS authentication for login and 802.1X, and local fallback for console access.
- DHCP snooping is enabled on VLANs 10 and 20, preventing rogue DHCP servers.
- Dynamic ARP Inspection is enabled on VLANs 10 and 20, mitigating ARP spoofing.
- Port security is enabled on 4 access ports, limiting unauthorized device connections.
- CDP is explicitly disabled, reducing potential attack vectors.
- A standard ACL (`MGMT-ACCESS`) is applied to the management interface, restricting access to trusted subnets.
- 802.1X is enabled on access ports, enforcing user and device authentication.

#### ⚠ Areas for Improvement
- **NTP is not configured**, which could lead to time synchronization issues and affect log correlation.
- **SNMP is not configured**, which may limit monitoring and management capabilities.
- **LLDP is not enabled**, which could hinder network discovery and troubleshooting.
- **IP Source Guard is not configured**, which could leave the network vulnerable to IP spoofing.
- **VLAN 1 is shutdown**, but it is still defined. It should be removed or explicitly deleted to avoid confusion.
- **VTP is not configured**, which is acceptable for an access-layer switch, but should be documented as such.
- **No banner is configured for VTY lines**, which could reduce visibility of security policies during remote access.

#### Recommendations
- **Enable and configure NTP** to ensure accurate time synchronization across the network.
- **Enable SNMP** with appropriate community strings and access controls for monitoring.
- **Enable LLDP** to improve network visibility and troubleshooting.
- **Enable IP Source Guard** on VLANs 10 and 20 to prevent IP spoofing.
- **Remove VLAN 1** if it is not in use to avoid confusion and reduce attack surface.
- **Add a banner to VTY lines** to inform users of security policies and legal consequences.
- **Consider enabling portfast on all access ports** to reduce STP delays, but ensure BPDU guard is in place to prevent loops.
- **Review and document the purpose of VLAN 666 and 999**, as they are referenced but not described.

## Summary

This device, **switch-06**, is an **Access-layer switch** based on its configuration, which includes multiple access ports with port security, 802.1X authentication, and trunk uplinks to a distribution layer. It is configured with strong security features such as DHCP snooping, DAI, and AAA with RADIUS integration. The device is managed via a dedicated management VLAN (VLAN 99) with SSH-only access and an ACL restricting access to trusted subnets. The configuration is well-structured and follows best practices for access-layer security and management. However, there are a few areas for improvement, particularly in time synchronization and monitoring capabilities.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-10T22:06:21.077158