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
- **Console Access**: Line `line con 0` configured with logging synchronous enabled, no authentication ✓ VERIFIED

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

### Device Role
- **Role**: Access Layer Switch ~ INFERRED  
  - Justification: The switch has multiple access ports (5), no routing enabled, and a single trunk port for uplink. It is likely serving end-user devices and connecting to a distribution switch.

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, which is a good practice for secure remote access. (Config lines: `ip ssh version 2`, `ip ssh time-out 60`)
- PortFast and BPDU Guard are enabled on access ports, reducing the risk of STP loops. (Config lines: `spanning-tree portfast`, `spanning-tree bpduguard enable`)
- Syslog is enabled with a remote logging server, which is good for auditing and monitoring. (Config line: `logging 10.99.0.50`)
- Password encryption is enabled, protecting clear-text passwords. (Config line: `service password-encryption`)
- A banner is configured to warn unauthorized users. (Config line: `banner login ^CAdvarsel: Uautorisert tilgang er forbudt.^C`)

#### ⚠ Areas for Improvement
- AAA is not enabled, which means there is no centralized authentication, authorization, or accounting. This is a significant security gap.
- No access control lists (ACLs) are applied to VTY lines, allowing unrestricted SSH access. (Config line: `line vty 0 4` has no access-class)
- DHCP Snooping and Dynamic ARP Inspection are not enabled, leaving the network vulnerable to spoofing and man-in-the-middle attacks.
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect.
- NTP is not configured, which can lead to time synchronization issues and affect log correlation.
- SNMP is not configured, which limits monitoring and management capabilities.
- VLAN 1 is not used and is shutdown, which is good, but it should be explicitly removed or renamed for clarity.

#### Recommendations
- Enable AAA for centralized authentication and authorization.
- Apply an ACL to the VTY lines to restrict SSH access to trusted IP addresses.
- Enable DHCP Snooping and configure trusted ports to prevent rogue DHCP servers.
- Enable Dynamic ARP Inspection to prevent ARP spoofing.
- Enable port security on access ports to limit the number of MAC addresses per port.
- Configure NTP to ensure accurate time synchronization.
- Enable SNMP for monitoring and management.
- Remove or rename VLAN 1 to avoid confusion and potential misuse.
- Consider enabling LLDP for network discovery and troubleshooting.

## Summary

switch-02 is an access layer switch serving end-user devices and connecting to a distribution switch via a trunk port. It is configured with basic security features such as SSH, PortFast, and BPDU Guard, but lacks advanced security mechanisms like AAA, DHCP Snooping, and Dynamic ARP Inspection. The configuration is functional but could be significantly improved to enhance security and management capabilities.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T13:47:53.769573