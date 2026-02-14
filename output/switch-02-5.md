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
- **FastEthernet0/1** - Bruker-PC kontor 201 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast + BPDU Guard enabled ✓ VERIFIED  
- **FastEthernet0/2** - Bruker-PC kontor 202 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast + BPDU Guard enabled ✓ VERIFIED  
- **FastEthernet0/3** - Bruker-PC kontor 203 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast + BPDU Guard enabled ✓ VERIFIED  
- **FastEthernet0/4** - Bruker-PC kontor 204 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast + BPDU Guard enabled ✓ VERIFIED  
- **FastEthernet0/5** - Printer 2. etasje | Mode: access | VLAN: 10 | PortFast + BPDU Guard enabled ✓ VERIFIED  
- **FastEthernet0/24** - Uplink til dis-sw01 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 10, 20, 50, 99 | Encapsulation: dot1q | Nonegotiate enabled ✓ VERIFIED  

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED  
- **Global Features**: portfast-default ✓ VERIFIED  

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED  
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
- Syslog is configured with a remote server at 10.99.0.50, enabling centralized logging.  
- A banner is configured for login sessions, providing legal notice and access control awareness.  

#### ⚠ Areas for Improvement
- AAA is not enabled, which means there is no centralized authentication, authorization, or accounting.  
- No access control lists (ACLs) are applied to VTY lines, leaving SSH access potentially open to unauthorized users.  
- DHCP Snooping, Dynamic ARP Inspection, and IP Source Guard are not enabled, which increases the risk of Layer 2 attacks.  
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect.  
- NTP is not configured, which may impact time-based security and logging correlation.  
- SNMP is not configured, which limits monitoring and management capabilities.  

#### Recommendations
- Enable AAA with local or remote authentication to enforce user authentication and authorization.  
- Apply an ACL to the VTY lines to restrict SSH access to trusted IP addresses.  
- Enable DHCP Snooping on VLANs 10, 20, 50, and 99 to prevent rogue DHCP servers.  
- Enable Dynamic ARP Inspection (DAI) and IP Source Guard to protect against ARP spoofing and IP spoofing.  
- Enable port security on access ports to limit the number of MAC addresses per port.  
- Configure NTP with a trusted time source to ensure accurate timestamps for logs and security events.  
- Enable SNMP with appropriate community strings and access controls for monitoring and management.  
- Consider enabling LLDP for network discovery and interoperability with non-Cisco devices.  

## Summary

This device, **switch-02**, is an **Access Layer switch** based on its configuration, which includes multiple access ports, VLAN assignments, and no routing capabilities. The switch is configured with basic security features such as SSH and PortFast, but lacks advanced Layer 2 security mechanisms like DHCP Snooping and Dynamic ARP Inspection. The configuration is functional but could benefit from additional hardening to improve security and operational visibility.

**Device Role**: Access Layer Switch ~ INFERRED  
**Security Posture**: Basic security in place, but lacks advanced protections ? UNCERTAIN  
**Configuration Quality**: Acceptable for a basic access switch, but improvements are recommended for security and monitoring ~ INFERRED  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T13:39:46.021192