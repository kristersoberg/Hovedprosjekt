# Network Device Documentation: switch-02

## Device Information
- **Hostname**: switch-02 ✓ VERIFIED
- **IOS Version**: 15.0(2)SE4 ✓ VERIFIED
- **Domain Name**: firma.local ✓ VERIFIED
- **Config Register**: Not configured ✓ VERIFIED

## Management & Access
- **Management VLAN**: 99 ✓ VERIFIED
- **IP Address**: 10.99.0.12 ✓ VERIFIED
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED
- **Default Gateway**: 10.99.0.1 ✓ VERIFIED
- **SSH Version**: 2 ✓ VERIFIED
- **SSH Timeout**: 60 seconds ✓ VERIFIED
- **VTY Transport Input**: ssh ✓ VERIFIED
- **VTY Authentication**: None ✓ VERIFIED
- **VTY Access Class**: None (⚠ No ACL protection) ✓ VERIFIED
- **Console Access**: Line `line con 0` ✓ VERIFIED
  - Authentication: None ✓ VERIFIED
  - Logging Synchronous: True ✓ VERIFIED

## AAA Configuration
- **AAA**: Not enabled ✓ VERIFIED

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED
- **VLAN IDs**: 10, 20, 50, 99, 666 ✓ VERIFIED
- **VLAN Interfaces (SVIs)**: 2 configured ✓ VERIFIED

### VLAN Interface Details
- **VLAN 1**
  - Status: Shutdown ✓ VERIFIED
- **VLAN 99**
  - Description: Management ✓ VERIFIED
  - IP: 10.99.0.12 255.255.255.0 ✓ VERIFIED
  - Status: Active ✓ VERIFIED

### VTP Configuration
- **VTP**: Not explicitly configured ✓ VERIFIED

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED
- **Active (no shutdown)**: 6 ✓ VERIFIED
- **Shutdown**: 20 ✓ VERIFIED
- **Access Ports**: 5 ✓ VERIFIED
- **Trunk Ports**: 1 ✓ VERIFIED
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED

### Key Active Interfaces
- **FastEthernet0/1** - Bruker-PC kontor 201 | Mode: access | VLAN: 10 ✓ VERIFIED
- **FastEthernet0/2** - Bruker-PC kontor 202 | Mode: access | VLAN: 10 ✓ VERIFIED
- **FastEthernet0/3** - Bruker-PC kontor 203 | Mode: access | VLAN: 10 ✓ VERIFIED
- **FastEthernet0/4** - Bruker-PC kontor 204 | Mode: access | VLAN: 10 ✓ VERIFIED
- **FastEthernet0/5** - Printer 2. etasje | Mode: access | VLAN: 10 ✓ VERIFIED
- **FastEthernet0/24** - Uplink til dis-sw01 | Mode: trunk | Allowed VLANs: 10, 20, 50, 99 ✓ VERIFIED

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED
- **Global Features**: portfast-default ✓ VERIFIED

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED
- **Dynamic ARP Inspection (DAI)**: Not enabled✓ VERIFIED
- **CDP**: Enabled✓ VERIFIED
- **LLDP**: Not enabled✓ VERIFIED
- **802.1X**: Not configured✓ VERIFIED
- **IP Source Guard**: Not configured✓ VERIFIED
- **Port Security**: Not enabled on any interfaces ✓ VERIFIED

## Network Services

### Logging
- **Syslog Enabled**: Yes ✓ VERIFIED
- **Logging Server**: 10.99.0.50 ✓ VERIFIED

### NTP
- **NTP Server**: Not configured ✓ VERIFIED
- **NTP Authentication**: Not configured ✓ VERIFIED

### DNS
- **DNS Domain Name**: firma.local ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.0.1 ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, which is a strong baseline for secure remote access. (Config lines: `ip ssh version 2`, `ip ssh time-out 60`)
- PortFast and BPDU Guard are enabled on access ports, reducing the risk of STP loops. (Config lines: `spanning-tree portfast`, `spanning-tree bpduguard enable`)
- A banner is configured for login sessions, which is a good legal and security practice. (Config line: `banner login ^CAdvarsel: Uautorisert tilgang er forbudt.^C`)
- Syslog is enabled and configured to send logs to a remote server at 10.99.0.50. (Config line: `logging 10.99.0.50`)

#### ⚠ Areas for Improvement
- AAA is not enabled, which means there is no centralized authentication, authorization, or accounting. This is a significant gap in security.
- No access control lists (ACLs) are applied to VTY lines, leaving SSH access potentially open to unauthorized users.
- DHCP Snooping and Dynamic ARP Inspection are not enabled, which leaves the network vulnerable to spoofing and man-in-the-middle attacks.
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect to the network.
- NTP is not configured, which could lead to time synchronization issues and affect log correlation and certificate validation.
- SNMP is not configured, which may limit monitoring and management capabilities.
- VLAN 1 is in use (via SVI) but is also shutdown, which is redundant and could be confusing. It should be removed if not needed.

#### Recommendations
- Enable AAA with local or remote authentication to enforce strong access control.
- Apply an ACL to the VTY lines to restrict SSH access to trusted IP addresses.
- Enable DHCP Snooping and Dynamic ARP Inspection on all VLANs to prevent spoofing attacks.
- Enable port security on access ports to limit the number of devices that can connect to each port.
- Configure NTP to ensure accurate time synchronization across the network.
- Enable SNMP with appropriate community strings and access controls to improve monitoring.
- Remove VLAN 1 if it is not needed, or at least ensure it is properly secured.
- Consider enabling LLDP for network discovery and troubleshooting.
- Enable 802.1X authentication for wired access if the environment supports it.

## Summary

This device, **switch-02**, is an **Access Layer** switch based on its configuration, which includes a large number of access ports, VLAN assignments, and no routing capabilities. The switch is configured with basic security features such as SSH and STP enhancements, but lacks advanced security mechanisms like AAA, DHCP Snooping, and port security. The configuration is functional but could benefit from several improvements to enhance security and manageability. The device is part of a VLAN-based network with VLANs 10, 20, 50, 99, and 666 in use.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-10T20:28:40.883771