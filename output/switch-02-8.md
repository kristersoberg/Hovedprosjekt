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
- **VTY Access Class**: None (⚠ No ACL protection) ✓ VERIFIED
- **Console Access**: Line `line con 0` configured with logging synchronous, no authentication ✓ VERIFIED

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
- **FastEthernet0/24** - Uplink til dis-sw01 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 10,20,50,99 | Encapsulation: dot1q | Nonegotiate enabled

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

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, which is a strong baseline for secure remote access.
- PortFast and BPDU Guard are enabled on access ports, reducing the risk of STP loops.
- A banner is configured for login sessions, providing legal notice and deterrence.
- Syslog is enabled and configured to send logs to a remote server at 10.99.0.50, which is a good practice for centralized logging.

#### ⚠ Areas for Improvement
- AAA is not enabled, which means there is no centralized authentication, authorization, or accounting.
- No access control lists (ACLs) are applied to VTY lines, leaving SSH access potentially open to unauthorized users.
- DHCP Snooping, Dynamic ARP Inspection, and IP Source Guard are not enabled, which leaves the network vulnerable to spoofing and rogue device attacks.
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect.
- NTP is not configured, which may lead to time synchronization issues and affect log correlation.
- SNMP is not configured, which limits the ability to monitor and manage the device remotely.
- VLAN 1 is active but in a shutdown state, which is unnecessary and could be removed for clarity.

#### Recommendations
- Enable AAA with local or remote authentication to enforce user authentication and authorization.
- Apply an ACL to the VTY lines to restrict SSH access to trusted IP addresses.
- Enable DHCP Snooping on VLANs 10, 20, 50, and 99 to prevent rogue DHCP servers.
- Enable Dynamic ARP Inspection (DAI) on the same VLANs to prevent ARP spoofing.
- Enable IP Source Guard on access ports to prevent IP spoofing.
- Enable port security on access ports to limit the number of MAC addresses allowed per port.
- Configure NTP to ensure accurate time synchronization for logging and troubleshooting.
- Enable SNMP with appropriate community strings and access controls for remote monitoring.
- Remove VLAN 1 configuration or ensure it is not used, as it is a default VLAN and can be a security risk if not properly managed.

## Summary

switch-02 is an **Access Layer** switch, as evidenced by the large number of access ports, the presence of PortFast and BPDU Guard, and the absence of routing. It serves as a local access point for end-user devices and connects to a distribution switch via a trunk port. The configuration is generally clean and includes some good security practices, but lacks several critical security features such as AAA, DHCP Snooping, and DAI. The device is configured to log to a remote syslog server, which is a positive step toward centralized monitoring.

~ INFERRED: Based on the presence of VLANs and trunking, it is likely part of a larger VLAN-based network with a distribution layer switch.

~ INFERRED: The device appears to be in a controlled environment, given the presence of a banner and logging, but lacks enterprise-grade security features.

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T09:49:35.091650