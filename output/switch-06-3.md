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
- **DHCP Snooping**: ✓ Enabled on VLANs 10, 20 ✓ VERIFIED
  - Information Option: Disabled ✓ VERIFIED
- **Dynamic ARP Inspection (DAI)**: ✓ Enabled on VLANs 10, 20 ✓ VERIFIED
- **Port Security**: ✓ Enabled on 4 interfaces ✓ VERIFIED
- **802.1X**: ✓ Enabled ✓ VERIFIED
- **CDP**: ✓ Disabled ✓ VERIFIED
- **LLDP**: ? UNCERTAIN (Not enabled)
- **IP Source Guard**: ? UNCERTAIN (Not configured)

## Network Services
### Logging
- **Syslog Enabled**: ✓
- **Logging Server**: 10.99.0.50 ✓ VERIFIED
- **Logging Trap Level**: informational ✓ VERIFIED

### NTP
- **NTP Server**: ? UNCERTAIN (Configuration lines are redacted)
- **NTP Authentication**: ✓ Enabled ✓ VERIFIED
  - Authentication Key: 1 ✓ VERIFIED
  - Trusted Key: 1 ✓ VERIFIED

### SNMP
- **SNMP**: ? UNCERTAIN (Not configured)

### DNS
- **DNS Domain Name**: secure.bedrift.no ✓ VERIFIED
- **DNS Lookup**: ✓ Disabled ✓ VERIFIED

## Routing Configuration
- **IP Routing**: ? UNCERTAIN (Disabled)
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is configured with version 2 and a 60-second timeout, ensuring secure remote access.
- AAA is enabled with RADIUS authentication for login and 802.1X, and local fallback for console access.
- DHCP snooping is enabled on VLANs 10 and 20, preventing rogue DHCP servers.
- Dynamic ARP Inspection (DAI) is enabled on VLANs 10 and 20, mitigating ARP spoofing.
- Port security is enabled on 4 access ports, limiting unauthorized device connections.
- CDP is explicitly disabled, reducing potential attack surface.
- A standard ACL (`MGMT-ACCESS`) is applied to the management VLAN, restricting access to trusted subnets.
- 802.1X is enabled with RADIUS authentication, enforcing user and device authentication on access ports.
- Syslog is enabled with a remote logging server, ensuring auditability and monitoring.
- NTP is configured with authentication, ensuring accurate time synchronization and preventing time-based attacks.

#### ⚠ Areas for Improvement
- **NTP Configuration**: NTP server IP addresses are redacted, making it difficult to verify the source of time synchronization.
- **SNMP**: SNMP is not configured, which could be a gap in monitoring and management capabilities.
- **LLDP**: LLDP is not enabled, which could hinder network discovery and troubleshooting.
- **IP Source Guard**: Not configured, which could leave the network vulnerable to IP spoofing.
- **VLAN 1**: VLAN 1 is shutdown, but it is still referenced in the configuration. It should be removed or explicitly deleted.
- **VTP**: VTP is not configured, which is acceptable in a non-trunking or non-VLAN-distributed environment, but should be documented.
- **Banner**: The login banner is configured, but it should be reviewed for compliance with organizational policies.

#### Recommendations
- **Enable IP Source Guard** on VLANs 10 and 20 to prevent IP spoofing.
- **Enable LLDP** if network discovery and interoperability with non-Cisco devices is required.
- **Review and document VLAN 1** usage or remove it from the configuration.
- **Ensure NTP server IPs are documented** and verify their trustworthiness.
- **Enable SNMP** if required for monitoring and management.
- **Review and update the login banner** to ensure it complies with organizational policies and legal requirements.
- **Consider enabling portfast on trunk ports** if they connect to other switches and do not expect BPDUs.
- **Ensure all RADIUS server keys are securely stored and rotated periodically**.

## Summary

The device `switch-06` is an **Access Layer switch** based on its configuration, which includes multiple access ports with 802.1X authentication, port security, and VLAN-based services. It is not performing routing and is connected to a distribution layer via trunk links. The configuration is well-structured and includes strong security features such as AAA, 802.1X, DHCP snooping, and DAI. However, there are areas for improvement, particularly in NTP documentation, SNMP configuration, and IP source guard. The device is configured for secure remote access via SSH and has a clear management VLAN with access control.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T09:38:39.348771