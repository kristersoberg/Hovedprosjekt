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
- **Role**: Access Layer Switch ~ INFERRED  
  - Justification: The device has many access ports (5), no routing enabled, and is connected to end-user devices and a single trunk to a distribution switch. This is typical of an access-layer switch.

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a timeout of 60 seconds ✓ VERIFIED
- PortFast and BPDU Guard are enabled on access ports to prevent STP loops ✓ VERIFIED
- A banner is configured to warn unauthorized users ✓ VERIFIED
- Syslog is enabled with a remote server at 10.99.0.50 ✓ VERIFIED
- No unnecessary services are enabled (e.g., HTTP, Telnet) ✓ VERIFIED

#### ⚠ Areas for Improvement
- AAA is not enabled, so there is no centralized authentication, authorization, or accounting ✓ VERIFIED
- No ACL is applied to VTY lines, leaving SSH access potentially open to unauthorized users ✓ VERIFIED
- DHCP Snooping and Dynamic ARP Inspection are not enabled, leaving the network vulnerable to spoofing attacks ✓ VERIFIED
- Port Security is not enabled on any interfaces, which could allow unauthorized devices to connect ✓ VERIFIED
- NTP is not configured, which could lead to time synchronization issues and affect log correlation ✓ VERIFIED
- SNMP is not configured, which limits monitoring and management capabilities ✓ VERIFIED

#### Recommendations
- Enable AAA with local or remote authentication to secure access to the device ~ INFERRED
- Apply an ACL to VTY lines to restrict SSH access to trusted IP addresses ~ INFERRED
- Enable DHCP Snooping and configure trusted ports to prevent rogue DHCP servers ~ INFERRED
- Enable Dynamic ARP Inspection to prevent ARP spoofing ~ INFERRED
- Enable Port Security on access ports to limit the number of MAC addresses per port ~ INFERRED
- Configure NTP with a trusted time source to ensure accurate logging and synchronization ~ INFERRED
- Enable SNMP with appropriate community strings and access controls to improve monitoring ~ INFERRED

## Summary

switch-02 is an access-layer switch serving end-user devices and connecting to a distribution switch via a trunk port. It is configured with basic security features such as SSH and STP protection, but lacks advanced security mechanisms like AAA, DHCP Snooping, and Port Security. The configuration is minimal and functional, but improvements are needed to enhance security and monitoring capabilities.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T13:37:53.764559