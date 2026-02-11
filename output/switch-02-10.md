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
- **FastEthernet0/1** - Bruker-PC kontor 201 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast: enabled | BPDU Guard: enabled
- **FastEthernet0/2** - Bruker-PC kontor 202 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast: enabled | BPDU Guard: enabled
- **FastEthernet0/3** - Bruker-PC kontor 203 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast: enabled | BPDU Guard: enabled
- **FastEthernet0/4** - Bruker-PC kontor 204 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast: enabled | BPDU Guard: enabled
- **FastEthernet0/5** - Printer 2. etasje | Mode: access | VLAN: 10 | PortFast: enabled | BPDU Guard: enabled
- **FastEthernet0/24** - Uplink til dis-sw01 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 10, 20, 50, 99 | Encapsulation: dot1q | Negotiation: disabled

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED
- **Global Features**: portfast-default ✓ VERIFIED

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED
- **Dynamic ARP Inspection (DAI)**: Not enabled✓ VERIFIED
- **Port Security**: Not enabled on any interfaces ✓ VERIFIED
- **802.1X**: Not configured ✓ VERIFIED
- **IP Source Guard**: Not configured ✓ VERIFIED
- **CDP**: Enabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED

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

### Device Role
- **Device Role**: ~ INFERRED
  - This device is likely an **Access Layer Switch** due to the high number of access ports, presence of voice VLANs, and lack of routing.
  - The presence of a trunk port suggests it connects to a Distribution Layer switch.

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, which is a good practice for secure remote access.
- PortFast and BPDU Guard are enabled on access ports, reducing the risk of STP loops.
- The default gateway is configured, and the management VLAN is isolated from user VLANs.
- Syslog is enabled with a remote logging server, which is a good operational practice.

#### ⚠ Areas for Improvement
- AAA is not enabled, which means there is no centralized authentication, authorization, or accounting.
- No ACLs are applied to VTY lines, leaving SSH access potentially open to unauthorized users.
- DHCP Snooping, DAI, and IP Source Guard are not enabled, which leaves the network vulnerable to spoofing and rogue DHCP servers.
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect.
- NTP is not configured, which may impact time-sensitive operations and logging.
- SNMP is not configured, which limits monitoring and management capabilities.
- VLAN 1 is not used and is shutdown, which is good, but it should be explicitly removed or renamed for clarity.

#### Recommendations
- Enable AAA with local or remote authentication to improve access control.
- Apply an ACL to the VTY lines to restrict SSH access to trusted IP addresses.
- Enable DHCP Snooping on VLANs 10, 20, 50, and 99 to prevent rogue DHCP servers.
- Enable Dynamic ARP Inspection (DAI) on the same VLANs to prevent ARP spoofing.
- Enable IP Source Guard on access ports to prevent IP spoofing.
- Enable port security on access ports to limit the number of MAC addresses per port.
- Configure NTP with a trusted time source to ensure accurate timestamps in logs.
- Enable SNMP with appropriate community strings and access controls for monitoring.
- Consider disabling CDP if it is not needed, as it can be used for reconnaissance.
- Remove or rename VLAN 1 to avoid confusion and potential misuse.

## Summary

switch-02 is an **Access Layer Switch** configured with multiple access ports for end-user devices and a single trunk port connecting to a Distribution Layer switch. It is managed via VLAN 99 with SSH access and logs to a remote syslog server. The configuration is generally clean and functional, but lacks several key security features such as AAA, DHCP Snooping, and port security. These should be implemented to improve the device's security posture and operational robustness.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T08:11:04.474381