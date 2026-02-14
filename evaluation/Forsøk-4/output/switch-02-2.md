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
  - Description: Brukere ✓ VERIFIED  
- **VLAN 20**  
  - Description: Servere ✓ VERIFIED  
- **VLAN 50**  
  - Description: VoIP ✓ VERIFIED  
- **VLAN 666**  
  - Description: Not configured ✓ VERIFIED  

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
  - PortFast: enabled ✓ VERIFIED  
  - BPDU Guard: enabled ✓ VERIFIED  

- **FastEthernet0/2**  
  - Description: Bruker-PC kontor 202 ✓ VERIFIED  
  - Mode: access ✓ VERIFIED  
  - VLAN: 10 ✓ VERIFIED  
  - Voice VLAN: 50 ✓ VERIFIED  
  - PortFast: enabled ✓ VERIFIED  
  - BPDU Guard: enabled ✓ VERIFIED  

- **FastEthernet0/3**  
  - Description: Bruker-PC kontor 203 ✓ VERIFIED  
  - Mode: access ✓ VERIFIED  
  - VLAN: 10 ✓ VERIFIED  
  - Voice VLAN: 50 ✓ VERIFIED  
  - PortFast: enabled ✓ VERIFIED  
  - BPDU Guard: enabled ✓ VERIFIED  

- **FastEthernet0/4**  
  - Description: Bruker-PC kontor 204 ✓ VERIFIED  
  - Mode: access ✓ VERIFIED  
  - VLAN: 10 ✓ VERIFIED  
  - Voice VLAN: 50 ✓ VERIFIED  
  - PortFast: enabled ✓ VERIFIED  
  - BPDU Guard: enabled ✓ VERIFIED  

- **FastEthernet0/5**  
  - Description: Printer 2. etasje ✓ VERIFIED  
  - Mode: access ✓ VERIFIED  
  - VLAN: 10 ✓ VERIFIED  
  - PortFast: enabled ✓ VERIFIED  
  - BPDU Guard: enabled ✓ VERIFIED  

- **FastEthernet0/24**  
  - Description: Uplink til dis-sw01 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 50, 99 ✓ VERIFIED  
  - Trunk Encapsulation: dot1q ✓ VERIFIED  
  - Negotiation: disabled ✓ VERIFIED  

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
- SSH is enabled with version 2 and a 60-second timeout, providing secure remote access.  
- PortFast and BPDU Guard are enabled on access ports, reducing STP-related vulnerabilities.  
- A banner is configured for login sessions, warning unauthorized users.  
- Syslog is enabled with a remote logging server at 10.99.0.50, aiding in monitoring and auditing.  
- No unnecessary services are running (e.g., HTTP, Telnet).  

#### ⚠ Areas for Improvement
- AAA is not enabled, which limits authentication, authorization, and accounting capabilities.  
- No ACL is applied to VTY lines, leaving SSH access potentially open to unauthorized sources.  
- DHCP Snooping and Dynamic ARP Inspection are not enabled, increasing the risk of spoofing and man-in-the-middle attacks.  
- Port Security is not enabled on any interface, which could allow unauthorized devices to connect.  
- NTP is not configured, which may affect time synchronization and log correlation.  
- SNMP is not configured, which limits network monitoring and management capabilities.  
- VLAN 1 is not used and is shutdown, which is a good practice, but it should be explicitly removed if not needed.  

#### Recommendations
- Enable AAA with local or remote authentication to enforce user authentication and authorization.  
- Apply an ACL to VTY lines to restrict SSH access to trusted IP addresses.  
- Enable DHCP Snooping and configure trusted ports to prevent rogue DHCP servers.  
- Enable Dynamic ARP Inspection to prevent ARP spoofing.  
- Enable Port Security on access ports to limit the number of MAC addresses allowed per port.  
- Configure NTP with a trusted time source to ensure accurate timekeeping.  
- Enable SNMP with appropriate community strings and access controls for monitoring.  
- Consider removing VLAN 1 if it is not in use to reduce the attack surface.  
- Enable LLDP for network discovery and troubleshooting.  

## Summary

This device, **switch-02**, is an **Access Layer** switch, as evidenced by the large number of access ports and the presence of voice VLANs. It is configured with basic security features such as SSH and PortFast, but lacks advanced security mechanisms like DHCP Snooping and Port Security. The configuration is minimal and functional, but improvements are needed to enhance security and monitoring capabilities.

~ INFERRED: Based on the presence of a trunk port and VLAN interfaces, this switch likely connects to a distribution layer switch for inter-VLAN communication.  
~ INFERRED: The lack of routing and the presence of access ports indicate that this is not a distribution or core layer device.  

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T13:33:44.989323