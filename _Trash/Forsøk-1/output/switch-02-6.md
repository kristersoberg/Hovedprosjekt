# Network Device Documentation: switch-02

## Device Information
- **Hostname**: switch-02 ✓ VERIFIED
- **IOS Version**: 15.0(2)SE4 ✓ VERIFIED
- **Domain Name**: firma.local ✓ VERIFIED
- **Config Register**: Not shown ✓ VERIFIED

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
- **Console Access**: Line `line con 0` with logging synchronous enabled ✓ VERIFIED

## AAA Configuration
- **AAA**: Not enabled ✓ VERIFIED

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED
- **VLAN IDs**: 10, 20, 50, 99, 666 ✓ VERIFIED
- **VLAN Interfaces (SVIs)**:
  - **VLAN 1**:
    - Status: Shutdown ✓ VERIFIED
  - **VLAN 99**:
    - Description: Management ✓ VERIFIED
    - IP: 10.99.0.12 255.255.255.0 ✓ VERIFIED
    - Status: Active ✓ VERIFIED
- **VTP Configuration**: Not explicitly configured ✓ VERIFIED

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED
- **Active (no shutdown)**: 6 ✓ VERIFIED
- **Shutdown**: 20 ✓ VERIFIED
- **Access Ports**: 5 ✓ VERIFIED
- **Trunk Ports**: 1 ✓ VERIFIED
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED

### Key Active Interfaces
- **FastEthernet0/1** - Bruker-PC kontor 201 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast enabled | BPDU Guard enabled
- **FastEthernet0/2** - Bruker-PC kontor 202 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast enabled | BPDU Guard enabled
- **FastEthernet0/3** - Bruker-PC kontor 203 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast enabled | BPDU Guard enabled
- **FastEthernet0/4** - Bruker-PC kontor 204 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast enabled | BPDU Guard enabled
- **FastEthernet0/5** - Printer 2. etasje | Mode: access | VLAN: 10 | PortFast enabled | BPDU Guard enabled
- **FastEthernet0/24** - Uplink til dis-sw01 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 10, 20, 50, 99 | Encapsulation: dot1q | Nonegotiate enabled

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

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.0.1 ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, which is a strong baseline for secure remote access.
- PortFast and BPDU Guard are enabled on access ports, reducing the risk of STP loops.
- A banner is configured to warn unauthorized users.
- Syslog is enabled and configured to send logs to a remote server at 10.99.0.50.

#### ⚠ Areas for Improvement
- AAA is not enabled, which means there is no centralized authentication, authorization, or accounting.
- No access control lists (ACLs) are applied to VTY lines, leaving SSH access potentially open to unauthorized users.
- DHCP Snooping and Dynamic ARP Inspection are not enabled, which increases the risk of DHCP spoofing and ARP poisoning attacks.
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect.
- NTP is not configured, which may lead to time synchronization issues and affect log correlation.
- SNMP is not configured, which limits monitoring and management capabilities.
- IP Source Guard is not enabled, which could allow spoofed IP addresses to be used on the network.

#### Recommendations
- Enable AAA with local or remote authentication to enforce user authentication and authorization.
- Apply an ACL to the VTY lines to restrict SSH access to trusted IP addresses.
- Enable DHCP Snooping and configure trusted ports to prevent rogue DHCP servers.
- Enable Dynamic ARP Inspection to prevent ARP spoofing.
- Enable port security on access ports to limit the number of MAC addresses allowed per port.
- Configure NTP with a trusted time source to ensure accurate timekeeping.
- Enable SNMP with appropriate community strings and access controls to allow monitoring.
- Enable IP Source Guard to prevent IP address spoofing.
- Consider enabling LLDP for network discovery and troubleshooting.
- Review and document all VLANs and their purposes to ensure clarity and reduce misconfiguration risks.

## Summary

switch-02 is an **Access Layer** switch, as evidenced by the large number of access ports and the absence of routing. It serves as a local access point for end-user devices and connects to a distribution switch via a trunk port. The configuration is generally clean and includes some good security practices, such as SSH and PortFast with BPDU Guard. However, there are several security gaps, including the lack of AAA, DHCP Snooping, and port security. The device is configured to send logs to a remote syslog server, which is a positive step for monitoring and auditing.

~ INFERRED: Based on the configuration and interface usage, this switch is likely located in a user-access area, such as an office or workstation environment.

~ INFERRED: The lack of routing and the presence of multiple access ports suggest that this is not a distribution or core switch.

~ INFERRED: The presence of a trunk port to "dis-sw01" suggests that this switch is connected to a distribution layer switch.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-10T20:38:14.709082