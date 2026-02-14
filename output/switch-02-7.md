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
- **VLAN Interfaces (SVIs)**: 2 configured ✓ VERIFIED  

### VLAN Interface Details
- **VLAN 1**  
  - Status: Shutdown ✓ VERIFIED  
- **VLAN 99**  
  - Description: Management ✓ VERIFIED  
  - IP: 10.99.0.12 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  

- **VLAN 10**  
  - Name: Brukere ✓ VERIFIED  
- **VLAN 20**  
  - Name: Servere ✓ VERIFIED  
- **VLAN 50**  
  - Name: VoIP ✓ VERIFIED  
- **VLAN 666**  
  - Native VLAN on trunk interface `FastEthernet0/24` ✓ VERIFIED  

- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED  
- **Active (no shutdown)**: 6 ✓ VERIFIED  
- **Shutdown**: 20 ✓ VERIFIED  
- **Access Ports**: 5 ✓ VERIFIED  
- **Trunk Ports**: 1 ✓ VERIFIED  
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED  

### Key Active Interfaces
- **FastEthernet0/1**  
  - Description: Bruker-PC kontor 201 ✓ VERIFIED  
  - Mode: access ✓ VERIFIED  
  - VLAN: 10 ✓ VERIFIED  
  - Voice VLAN: 50 ✓ VERIFIED  
  - PortFast: Enabled ✓ VERIFIED  
  - BPDU Guard: Enabled ✓ VERIFIED  

- **FastEthernet0/2**  
  - Description: Bruker-PC kontor 202 ✓ VERIFIED  
  - Mode: access ✓ VERIFIED  
  - VLAN: 10 ✓ VERIFIED  
  - Voice VLAN: 50 ✓ VERIFIED  
  - PortFast: Enabled ✓ VERIFIED  
  - BPDU Guard: Enabled ✓ VERIFIED  

- **FastEthernet0/3**  
  - Description: Bruker-PC kontor 203 ✓ VERIFIED  
  - Mode: access ✓ VERIFIED  
  - VLAN: 10 ✓ VERIFIED  
  - Voice VLAN: 50 ✓ VERIFIED  
  - PortFast: Enabled ✓ VERIFIED  
  - BPDU Guard: Enabled ✓ VERIFIED  

- **FastEthernet0/4**  
  - Description: Bruker-PC kontor 204 ✓ VERIFIED  
  - Mode: access ✓ VERIFIED  
  - VLAN: 10 ✓ VERIFIED  
  - Voice VLAN: 50 ✓ VERIFIED  
  - PortFast: Enabled ✓ VERIFIED  
  - BPDU Guard: Enabled ✓ VERIFIED  

- **FastEthernet0/5**  
  - Description: Printer 2. etasje ✓ VERIFIED  
  - Mode: access ✓ VERIFIED  
  - VLAN: 10 ✓ VERIFIED  
  - PortFast: Enabled ✓ VERIFIED  
  - BPDU Guard: Enabled ✓ VERIFIED  

- **FastEthernet0/24**  
  - Description: Uplink til dis-sw01 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 50, 99 ✓ VERIFIED  
  - Trunk Encapsulation: dot1q ✓ VERIFIED  
  - Nonegotiate: Enabled ✓ VERIFIED  

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED  
- **Global Features**: portfast-default ✓ VERIFIED  

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED  
- **Port Security**: Not enabled on any interface ✓ VERIFIED  
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
- A banner is configured for login sessions, providing legal notice.  
- Syslog is enabled with a remote server at 10.99.0.50, which is a good practice for centralized logging.  
- DNS lookup is disabled, reducing unnecessary traffic and potential DoS risks.  

#### ⚠ Areas for Improvement
- AAA is not enabled, which means there is no centralized authentication, authorization, or accounting.  
- No ACL is applied to VTY lines, leaving SSH access potentially open to unauthorized users.  
- DHCP Snooping and Dynamic ARP Inspection are not enabled, which increases the risk of DHCP spoofing and ARP poisoning attacks.  
- Port security is not enabled on any interface, which could allow unauthorized devices to connect.  
- NTP is not configured, which may lead to time synchronization issues.  
- SNMP is not configured, which limits monitoring and management capabilities.  
- LLDP is not enabled, which could be useful for network discovery and troubleshooting.  

#### Recommendations
- Enable AAA for centralized authentication and authorization.  
- Apply an ACL to VTY lines to restrict SSH access to trusted IP addresses.  
- Enable DHCP Snooping and configure trusted ports to prevent rogue DHCP servers.  
- Enable Dynamic ARP Inspection to prevent ARP spoofing.  
- Enable port security on access ports to limit the number of MAC addresses allowed.  
- Configure NTP with a trusted time source to ensure accurate timekeeping.  
- Enable SNMP with appropriate community strings and access controls for monitoring.  
- Consider enabling LLDP for network discovery and interoperability.  

## Summary

This device, **switch-02**, is an **Access Layer** switch based on its configuration, which includes multiple access ports, VLAN assignments, and no routing capabilities. It is configured with basic security features such as SSH and PortFast, but lacks advanced security mechanisms like DHCP Snooping, DAI, and port security. The configuration is functional but could benefit from additional hardening and monitoring features to improve security and manageability.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T13:43:43.356384