# Network Device Documentation: lab-sw01

## Device Information
- **Hostname**: lab-sw01 ✓ VERIFIED
- **IOS Version**: 15.0(2)SE4 ✓ VERIFIED
- **Domain Name**: lab.bedrift.no ✓ VERIFIED
- **Config Register**: Not configured ✓ VERIFIED

## Management & Access
- **Management VLAN**: 99 ✓ VERIFIED
- **IP Address**: 10.99.1.8 ✓ VERIFIED
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED
- **SSH Version**: Not configured ✓ VERIFIED
- **SSH Timeout**: Not configured ✓ VERIFIED
- **VTY Transport Input**: ssh, telnet ✓ VERIFIED
- **VTY Authentication**: None ✓ VERIFIED
- **VTY Access Class**: None (⚠ No ACL protection) ✓ VERIFIED
- **Console Authentication**: None ✓ VERIFIED
- **Console Logging Synchronous**: Enabled ✓ VERIFIED

## AAA Configuration
- **AAA**: Not enabled ✓ VERIFIED

## VLANs
- **Total VLANs Referenced**: 4 ✓ VERIFIED
- **VLAN IDs**: 99, 110, 120, 666 ✓ VERIFIED
- **VLAN Interfaces (SVIs)**: 2 configured ✓ VERIFIED

### VLAN Details
- **VLAN 1**
  - Status: Shutdown ✓ VERIFIED
- **VLAN 99**
  - Description: Management ✓ VERIFIED
  - IP: 10.99.1.8 255.255.255.0 ✓ VERIFIED
  - Status: Active ✓ VERIFIED

- **VLAN 110**
  - Description: Lab-Klienter ✓ VERIFIED (from `vlan 110 name Lab-Klienter`)
- **VLAN 120**
  - Description: Lab-Servere ✓ VERIFIED (from `vlan 120 name Lab-Servere`)
- **VLAN 666**
  - Description: Not configured ✓ VERIFIED

- **VTP Configuration**: Not explicitly configured ✓ VERIFIED

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED
- **Active (no shutdown)**: 11 ✓ VERIFIED
- **Shutdown**: 15 ✓ VERIFIED
- **Access Ports**: 10 ✓ VERIFIED
- **Trunk Ports**: 1 ✓ VERIFIED
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED

### Key Active Interfaces
- **FastEthernet0/1** - Lab-PC 1 | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/2** - Lab-PC 2 | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/3** - Lab-PC 3 | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/4** - Lab-PC 4 | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/5** - Lab-PC 5 | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/6** - Lab-PC 6 | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/7** - Lab-Server 1 | Mode: access | VLAN: 120 ✓ VERIFIED
- **FastEthernet0/8** - Lab-Server 2 | Mode: access | VLAN: 120 ✓ VERIFIED
- **FastEthernet0/9** - Lab-Server 3 | Mode: access | VLAN: 120 ✓ VERIFIED
- **FastEthernet0/10** - Lab-Server 4 | Mode: access | VLAN: 120 ✓ VERIFIED
- **FastEthernet0/24** - Uplink til dis-sw01 gig0/6 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 99, 110, 120 ✓ VERIFIED

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED
- **Dynamic ARP Inspection (DAI)**: Not enabled✓ VERIFIED
- **Port Security**: Not enabled on any interface ✓ VERIFIED
- **CDP**: Enabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED
- **802.1X**: Not configured ✓ VERIFIED
- **IP Source Guard**: Not configured ✓ VERIFIED

## Network Services

### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED
- **Logging Configuration Line**: `logging 10.99.0.50` ✓ VERIFIED

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED
- **NTP Authentication**: Disabled ✓ VERIFIED
- **NTP Configuration Line**: `ntp server 10.99.0.1` ✓ VERIFIED

### Syslog
- **Syslog Server**: 10.99.0.50 ✓ VERIFIED
- **Syslog Configuration Line**: `logging 10.99.0.50` ✓ VERIFIED

### DNS
- **DNS Domain Name**: lab.bedrift.no ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED
- **DNS Configuration Line**: `no ip domain-lookup` ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED
- **Routing Configuration Line**: `ip default-gateway 10.99.1.1` ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- **Management VLAN Isolation**: VLAN 99 is used for management and is isolated from user VLANs. ✓ VERIFIED
- **Syslog Logging**: Syslog is configured to send logs to 10.99.0.50. ✓ VERIFIED
- **NTP Synchronization**: NTP is configured to synchronize with 10.99.0.1. ✓ VERIFIED
- **DHCP Server Configuration**: DHCP pools are defined for VLANs 110 and 120 with IP exclusions and lease times. ✓ VERIFIED
- **PortFast on Access Ports**: PortFast is enabled on all access ports to reduce STP convergence time. ✓ VERIFIED
- **Banner Message**: A MOTD banner is configured to warn users about the lab environment. ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH Not Configured**: Telnet is still allowed on VTY lines. SSH should be configured and telnet disabled for secure remote access. ? UNCERTAIN (but strongly recommended)
- **VTY Access Not Restricted**: No ACL is applied to VTY lines, allowing unrestricted remote access. ? UNCERTAIN (but strongly recommended)
- **No AAA Authentication**: AAA is not enabled, so there is no centralized authentication, authorization, or accounting. ? UNCERTAIN (but strongly recommended)
- **No Port Security**: No port security is configured on access ports, which could allow unauthorized devices to connect. ? UNCERTAIN (but strongly recommended)
- **No DHCP Snooping or DAI**: These features are not enabled, leaving the network vulnerable to rogue DHCP servers and ARP spoofing. ? UNCERTAIN (but strongly recommended)
- **No SNMP Configuration**: SNMP is not configured, which limits network monitoring and management capabilities. ? UNCERTAIN (but strongly recommended)

#### Recommendations
- **Enable SSH and Disable Telnet**: Configure SSH with strong key pairs and disable telnet for secure remote access.
- **Apply ACLs to VTY Lines**: Restrict remote access to only authorized IP addresses.
- **Enable AAA**: Implement AAA for centralized authentication and authorization.
- **Enable Port Security**: Configure port security on access ports to limit the number of MAC addresses allowed.
- **Enable DHCP Snooping and DAI**: Protect against rogue DHCP servers and ARP spoofing.
- **Configure SNMP**: Enable SNMP for network monitoring and management.
- **Enable IP Source Guard**: Prevent IP spoofing by binding IP addresses to MAC addresses.
- **Enable 802.1X**: Implement 802.1X authentication for secure user and device access.

## Summary

lab-sw01 is an **Access Layer** switch, as evidenced by the large number of access ports and the absence of routing. It serves as a local switch for lab PCs and servers, connecting to a distribution switch via a trunk port. The configuration is functional but lacks several critical security features such as SSH, AAA, port security, and DHCP snooping. The device is configured with basic network services like NTP and syslog, but further hardening is required to meet enterprise security standards.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T12:51:54.892171