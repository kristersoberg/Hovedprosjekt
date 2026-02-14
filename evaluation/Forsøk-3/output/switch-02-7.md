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
- **VTY Authentication**: None ✓ VERIFIED
- **VTY Access Class**: None (⚠ No ACL protection) ✓ VERIFIED
- **Console Access**: Line `line con 0` ✓ VERIFIED
  - Authentication: None ✓ VERIFIED
  - Logging Synchronous: True ✓ VERIFIED

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
- **FastEthernet0/1** - Bruker-PC kontor 201 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast: enabled | BPDU Guard: enabled
- **FastEthernet0/2** - Bruker-PC kontor 202 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast: enabled | BPDU Guard: enabled
- **FastEthernet0/3** - Bruker-PC kontor 203 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast: enabled | BPDU Guard: enabled
- **FastEthernet0/4** - Bruker-PC kontor 204 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast: enabled | BPDU Guard: enabled
- **FastEthernet0/5** - Printer 2. etasje | Mode: access | VLAN: 10 | PortFast: enabled | BPDU Guard: enabled
- **FastEthernet0/24** - Uplink til dis-sw01 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 10, 20, 50, 99 | Encapsulation: dot1q | Negotiation: disabled

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED
- **Global Features**: portfast-default ✓ VERIFIED

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED
- **Dynamic ARP Inspection (DAI)**: Not enabled✓ VERIFIED
- **Port Security**: Not enabled on any interface ✓ VERIFIED
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
- **Device Role**: ~ INFERRED - **Access Layer Switch**
  - Justification: The switch has many access ports (5 active), no routing enabled, and is connected to end-user devices (PCs, printers). It also has a trunk port to a likely distribution switch (`FastEthernet0/24`), which is typical of an access layer device.

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a timeout of 60 seconds ✓ VERIFIED
- PortFast and BPDU Guard are enabled on access ports to prevent STP loops ✓ VERIFIED
- Syslog is enabled with a remote server at 10.99.0.50 ✓ VERIFIED
- Password encryption is enabled ✓ VERIFIED
- A banner is configured to warn unauthorized users ✓ VERIFIED

#### ⚠ Areas for Improvement
- AAA is not enabled, so there is no centralized authentication ✓ VERIFIED
- No ACL is applied to VTY lines, leaving SSH access potentially open to all IPs ✓ VERIFIED
- DHCP Snooping, DAI, and IP Source Guard are not enabled, leaving the network vulnerable to spoofing and rogue DHCP servers ✓ VERIFIED
- Port security is not enabled on any interface, increasing the risk of unauthorized device access ✓ VERIFIED
- No NTP server is configured, which may affect log and event timestamp accuracy ✓ VERIFIED
- CDP is enabled, which could be a security risk in certain environments ✓ VERIFIED

#### Recommendations
- Enable AAA for centralized authentication and authorization
- Apply an ACL to VTY lines to restrict SSH access to trusted IPs
- Enable DHCP Snooping on VLANs 10, 20, 50, and 99 to prevent rogue DHCP servers
- Enable Dynamic ARP Inspection (DAI) on VLANs 10, 20, 50, and 99 to prevent ARP spoofing
- Enable IP Source Guard on VLANs 10, 20, 50, and 99 to prevent IP spoofing
- Enable port security on access ports to limit the number of MAC addresses per port
- Configure an NTP server to ensure accurate time synchronization
- Consider disabling CDP if it is not required for network discovery

## Summary

switch-02 is an access layer switch serving end-user devices in VLANs 10, 20, 50, and 99. It connects to a distribution switch via a trunk port and provides basic Layer 2 connectivity. The configuration is functional but lacks several key security features, including AAA, DHCP Snooping, and port security. The device uses SSH for secure remote access and logs to a remote syslog server. Overall, the configuration is minimal and could benefit from additional hardening to improve security and compliance. ✓ VERIFIED

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T09:47:36.059886