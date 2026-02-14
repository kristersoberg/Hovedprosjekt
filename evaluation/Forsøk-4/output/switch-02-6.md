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
- **VTY Access Class**: Not configured (⚠ No ACL protection) ✓ VERIFIED
- **Console Access**: Line `line con 0` with no authentication and logging synchronous enabled ✓ VERIFIED

## AAA Configuration
- **AAA**: Not enabled ✓ VERIFIED

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED
- **VLAN IDs**: 10, 20, 50, 99, 666 ✓ VERIFIED

**VLAN Interfaces (SVIs):**
- **VLAN 1**:
  - Status: Shutdown ✓ VERIFIED
- **VLAN 99**:
  - Description: Management ✓ VERIFIED
  - IP: 10.99.0.12 255.255.255.0 ✓ VERIFIED
  - Status: Active ✓ VERIFIED

**VTP Configuration**:
- Not explicitly configured ✓ VERIFIED

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED
- **Active (no shutdown)**: 6 ✓ VERIFIED
- **Shutdown**: 20 ✓ VERIFIED
- **Access Ports**: 5 ✓ VERIFIED
- **Trunk Ports**: 1 ✓ VERIFIED
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED

**Key Active Interfaces:**
- **FastEthernet0/1** - Bruker-PC kontor 201 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast and BPDU Guard enabled ✓ VERIFIED
- **FastEthernet0/2** - Bruker-PC kontor 202 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast and BPDU Guard enabled ✓ VERIFIED
- **FastEthernet0/3** - Bruker-PC kontor 203 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast and BPDU Guard enabled ✓ VERIFIED
- **FastEthernet0/4** - Bruker-PC kontor 204 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast and BPDU Guard enabled ✓ VERIFIED
- **FastEthernet0/5** - Printer 2. etasje | Mode: access | VLAN: 10 | PortFast and BPDU Guard enabled ✓ VERIFIED
- **FastEthernet0/24** - Uplink til dis-sw01 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 10, 20, 50, 99 | Encapsulation: dot1q | Nonegotiate enabled ✓ VERIFIED

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
- **Logging Server**: 10.99.0.50 ✓ VERIFIED

### NTP
- **NTP Server**: Not configured ✓ VERIFIED
- **NTP Authentication**: Not configured ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

### DNS
- **DNS Domain Name**: firma.local ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.0.1 ✓ VERIFIED

## Configuration Quality Assessment

### Device Role
- **Device Role**: ~ INFERRED - This is an **Access Layer** switch. It has multiple access ports, no routing enabled, and a single trunk port for uplink to a distribution switch. It also supports voice VLANs and uses PortFast and BPDU Guard on access ports.

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, which is a strong security practice. ✓ VERIFIED
- PortFast and BPDU Guard are enabled on access ports, reducing the risk of STP loops. ✓ VERIFIED
- A banner is configured for login sessions, providing legal notice. ✓ VERIFIED
- Syslog is enabled with a remote logging server at 10.99.0.50. ✓ VERIFIED
- DNS lookup is disabled, preventing potential DNS-based attacks. ✓ VERIFIED

#### ⚠ Areas for Improvement
- AAA is not enabled, which means there is no centralized authentication, authorization, or accounting. ~ INFERRED
- No ACL is applied to VTY lines, leaving SSH access potentially open to unauthorized users. ✓ VERIFIED
- DHCP Snooping, Dynamic ARP Inspection, and IP Source Guard are not enabled, leaving the network vulnerable to spoofing and rogue device attacks. ✓ VERIFIED
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect. ✓ VERIFIED
- NTP is not configured, which may impact time-based security and logging. ✓ VERIFIED
- SNMP is not configured, which may limit monitoring and management capabilities. ✓ VERIFIED

#### Recommendations
- Enable AAA for centralized authentication and authorization. ~ INFERRED
- Apply an ACL to VTY lines to restrict SSH access to trusted IP addresses. ~ INFERRED
- Enable DHCP Snooping on VLANs 10, 20, 50, and 99 to prevent rogue DHCP servers. ~ INFERRED
- Enable Dynamic ARP Inspection (DAI) on VLANs 10, 20, 50, and 99 to prevent ARP spoofing. ~ INFERRED
- Enable IP Source Guard on access ports to prevent IP spoofing. ~ INFERRED
- Enable port security on access ports to limit the number of MAC addresses per port. ~ INFERRED
- Configure NTP with a trusted time source to ensure accurate timekeeping. ~ INFERRED
- Enable SNMP with appropriate community strings and access controls for monitoring. ~ INFERRED

## Summary

This device, **switch-02**, is an **Access Layer** switch with multiple access ports and a single trunk port for uplink. It supports VLANs for user, server, and VoIP traffic, and has a management VLAN configured with an IP address for remote access. The configuration is generally clean and includes some good security practices such as SSH and PortFast. However, several security features are missing, including AAA, DHCP Snooping, and port security. The device is logging to a remote syslog server, but lacks NTP and SNMP configuration. ~ INFERRED

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T13:41:42.249251