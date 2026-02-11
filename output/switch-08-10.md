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
- **Console Access**: Line `line con 0` with logging synchronous enabled ✓ VERIFIED

## AAA Configuration
- **AAA**: Not enabled ✓ VERIFIED

## VLANs
- **Total VLANs Referenced**: 4 ✓ VERIFIED
- **VLAN IDs**: 99, 110, 120, 666 ✓ VERIFIED
- **VLAN Interfaces (SVIs)**: 2 configured ✓ VERIFIED

### VLAN Details
- **VLAN 1**
  - **Status**: Shutdown ✓ VERIFIED
- **VLAN 99**
  - **Description**: Management ✓ VERIFIED
  - **IP Address**: 10.99.1.8 ✓ VERIFIED
  - **Subnet Mask**: 255.255.255.0 ✓ VERIFIED
  - **Status**: Active ✓ VERIFIED

- **VLAN 110**
  - **Description**: Lab-Klienter ✓ VERIFIED
- **VLAN 120**
  - **Description**: Lab-Servere ✓ VERIFIED
- **VLAN 666**
  - **Description**: Not configured ✓ VERIFIED

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
- **CDP**: Enabled✓ VERIFIED
- **LLDP**: Not enabled✓ VERIFIED
- **802.1X**: Not configured✓ VERIFIED
- **IP Source Guard**: Not configured✓ VERIFIED
- **Port Security**: Not enabled on any interface ✓ VERIFIED

## Network Services

### Logging
- **Syslog Server**: 10.99.0.50 ✓ VERIFIED
- **Syslog Configuration Line**: `logging 10.99.0.50` ✓ VERIFIED

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED
- **NTP Authentication**: Disabled ✓ VERIFIED
- **NTP Configuration Line**: `ntp server 10.99.0.1` ✓ VERIFIED

### DNS
- **DNS Domain Name**: lab.bedrift.no ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- **Syslog logging is enabled** with a remote server at 10.99.0.50 ✓ VERIFIED
- **NTP is configured** with a remote server at 10.99.0.1 ✓ VERIFIED
- **PortFast is enabled** on all access ports to prevent STP loops ✓ VERIFIED
- **Banner is configured** to warn users about the lab environment: `banner motd ^CLab-miljoe. Ingen produksjonsdata tillatt.^C` ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH is not configured**, leaving the device vulnerable to Telnet traffic (plaintext credentials) ✓ VERIFIED
- **VTY lines allow both SSH and Telnet**, and no ACL is applied to restrict access ✓ VERIFIED
- **No AAA authentication is enabled**, allowing unauthenticated access to the device ✓ VERIFIED
- **No port security is enabled**, leaving access ports open to MAC flooding and unauthorized device access ✓ VERIFIED
- **DHCP Snooping and Dynamic ARP Inspection are not enabled**, leaving the network vulnerable to rogue DHCP servers and ARP spoofing ✓ VERIFIED
- **No VLAN access control lists (VACLs) or ACLs** are configured to restrict inter-VLAN traffic ✓ VERIFIED
- **SNMP is not configured**, which could be a missed opportunity for monitoring and management ✓ VERIFIED

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines to secure remote access.
- **Apply an ACL to VTY lines** to restrict access to trusted IP addresses.
- **Enable AAA authentication** to enforce user authentication for console and VTY access.
- **Enable port security** on all access ports to prevent MAC flooding and unauthorized device access.
- **Enable DHCP Snooping** and configure trusted ports to prevent rogue DHCP servers.
- **Enable Dynamic ARP Inspection (DAI)** to prevent ARP spoofing.
- **Enable IP Source Guard** to prevent IP spoofing.
- **Enable SNMP** with appropriate community strings and access control for monitoring.
- **Consider enabling 802.1X** for secure user and device authentication on access ports.

## Summary

The device **lab-sw01** is an **Access Layer switch** based on its configuration, which includes a large number of access ports, VLANs for client and server traffic, and no routing capabilities. The configuration is functional but lacks several key security features that are essential for a production environment. The device is part of a lab environment, as indicated by the banner and VLAN naming conventions. The configuration quality is acceptable for a lab setting but would require significant hardening for use in a production network.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T01:27:55.761397