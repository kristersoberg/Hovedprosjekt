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
- SSH is enabled with version 2 and a timeout of 60 seconds, which is a good practice for secure remote access.
- PortFast and BPDU Guard are enabled on access ports, which helps prevent STP loops and unauthorized device connections.
- A banner is configured on login (`banner login ^CAdvarsel: Uautorisert tilgang er forbudt.^C`), which is a good legal and security practice.
- Syslog is enabled and configured to send logs to 10.99.0.50, which is a good operational practice for monitoring and auditing.

#### ⚠ Areas for Improvement
- AAA is not enabled, which means there is no centralized authentication, authorization, or accounting for user access.
- VTY lines do not have an access class configured, leaving them open to potential unauthorized access.
- No ACLs are applied to VTY lines or management interfaces, which could allow unrestricted SSH access.
- DHCP Snooping, Dynamic ARP Inspection, and IP Source Guard are not enabled, which leaves the network vulnerable to spoofing and rogue device attacks.
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect to the network.
- NTP is not configured, which could lead to time synchronization issues and affect log correlation and certificate validation.
- SNMP is not configured, which limits the ability to monitor and manage the device remotely.
- VLAN 1 is not used and is shutdown, which is good, but it should be explicitly removed or renamed for clarity.

#### Recommendations
- Enable AAA with local or remote authentication to improve access control.
- Apply an access list to VTY lines to restrict SSH access to trusted IP addresses.
- Enable DHCP Snooping on VLANs 10, 20, 50, and 99 to prevent rogue DHCP servers.
- Enable Dynamic ARP Inspection (DAI) on VLANs 10, 20, 50, and 99 to prevent ARP spoofing.
- Enable IP Source Guard on VLANs 10, 20, 50, and 99 to prevent IP spoofing.
- Enable port security on access ports to limit the number of devices that can connect.
- Configure NTP with a trusted time source to ensure accurate timekeeping.
- Configure SNMP with appropriate community strings and access controls to enable remote monitoring.
- Remove or rename VLAN 1 to avoid confusion and potential misuse.

## Summary

This device, **switch-02**, is an **Access Layer** switch based on its configuration, which includes multiple access ports, VLAN assignments, and no routing capabilities. It is configured with basic security features such as SSH and STP enhancements, but lacks advanced security mechanisms like DHCP Snooping, DAI, and port security. The configuration is functional but could benefit from additional hardening and monitoring features to improve security and operational visibility.

~ INFERRED: Based on the presence of access ports and lack of routing, this is likely an access-layer switch in a typical three-tier network architecture.

~ INFERRED: The device appears to be part of a small to medium-sized network, possibly in an office or enterprise environment.

## Data Source

- **Structured configuration analysis**
- **Generated**: 2026-02-11T08:07:07.747208