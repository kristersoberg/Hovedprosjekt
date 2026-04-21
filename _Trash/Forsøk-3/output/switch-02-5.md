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
- **VTY Access Class**: None (⚠ No ACL protection) ✓ VERIFIED
- **Console Access**: Line `line con 0` with no authentication and logging synchronous enabled ✓ VERIFIED

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

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a timeout of 60 seconds, which is a good practice for secure remote access.
- PortFast and BPDU Guard are enabled on access ports, reducing the risk of STP loops.
- A banner is configured for login sessions, providing legal notice and deterrence.
- Syslog is enabled with a remote server at 10.99.0.50, which is a good practice for centralized logging.

#### ⚠ Areas for Improvement
- AAA is not enabled, which means there is no centralized authentication, authorization, or accounting.
- No ACL is applied to VTY lines, leaving SSH access potentially open to unauthorized users.
- DHCP Snooping, Dynamic ARP Inspection, and IP Source Guard are not enabled, which could leave the network vulnerable to spoofing and other Layer 2 attacks.
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect.
- 802.1X is not configured, which means there is no port-based authentication for wired devices.
- NTP is not configured, which could lead to time synchronization issues and affect log correlation.
- SNMP is not configured, which limits the ability to monitor and manage the device remotely.
- VLAN 1 is active but has no IP address and is shutdown, which is unnecessary and could be removed.

#### Recommendations
- Enable AAA with local or remote authentication to improve access control.
- Apply an ACL to VTY lines to restrict SSH access to trusted IP addresses.
- Enable DHCP Snooping, Dynamic ARP Inspection, and IP Source Guard on appropriate VLANs to improve Layer 2 security.
- Enable port security on access ports to prevent unauthorized device connections.
- Configure 802.1X for port-based authentication on access ports.
- Configure NTP with a trusted time source to ensure accurate timekeeping.
- Enable SNMP with appropriate community strings and access controls for remote monitoring.
- Remove VLAN 1 if it is not needed, or configure it with a purpose if it is to be used.
- Consider enabling LLDP for network discovery and troubleshooting.

## Summary

switch-02 is an **Access Layer** switch, as evidenced by the large number of access ports, the presence of PortFast and BPDU Guard, and the lack of routing configuration. It serves as a local access point for end-user devices and connects to a distribution switch via a trunk port. The configuration is generally clean and includes some good security practices, but there are several areas where security could be improved, particularly in terms of Layer 2 protections and centralized authentication.

~ INFERRED: Based on the configuration, this switch is likely located in a user-access area, such as an office or workstation environment, and is part of a larger network with a distribution layer.

~ INFERRED: The lack of routing and the presence of multiple access ports indicate that this is not a core or distribution switch.

## Data Source

Structured configuration analysis  
**Generated**: 2026-02-14T09:43:40.386655