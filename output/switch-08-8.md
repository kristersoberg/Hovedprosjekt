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

### VLAN Interface Details
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
- **Port Security**: Not enabled on any interface ✓ VERIFIED
- **CDP**: Enabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED
- **802.1X**: Not configured ✓ VERIFIED
- **IP Source Guard**: Not configured ✓ VERIFIED

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
- **Syslog logging is enabled** and configured to send logs to 10.99.0.50 ✓ VERIFIED
- **NTP is enabled** with a configured server at 10.99.0.1 ✓ VERIFIED
- **PortFast is enabled** on all access ports to prevent STP loops ✓ VERIFIED
- **Banner is configured** to warn users about the lab environment and unauthorized access ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH is not configured**, leaving the device vulnerable to Telnet traffic which is unencrypted ✓ VERIFIED
- **VTY lines allow both SSH and Telnet**, but Telnet is not secure and should be disabled ✓ VERIFIED
- **No authentication is configured** for VTY or console access, allowing unrestricted access ✓ VERIFIED
- **No ACLs are applied** to VTY lines, leaving them open to unauthorized remote access ✓ VERIFIED
- **DHCP Snooping is not enabled**, which could allow rogue DHCP servers to operate on the network ✓ VERIFIED
- **Dynamic ARP Inspection is not enabled**, which could allow ARP spoofing attacks ✓ VERIFIED
- **Port security is not enabled**, which could allow unauthorized devices to connect to the network ✓ VERIFIED
- **802.1X is not configured**, which could allow unauthenticated devices to access the network ✓ VERIFIED
- **LLDP is not enabled**, which could limit network discovery and troubleshooting capabilities ✓ VERIFIED

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines to secure remote access. Example: `transport input ssh` on `line vty 0 4` ✓ VERIFIED
- **Configure AAA authentication** for console and VTY access to enforce user authentication. Example: `aaa new-model`, `aaa authentication login default local` ✓ INFERRED
- **Apply an ACL to VTY lines** to restrict access to trusted IP addresses. Example: `access-class 100 in` on `line vty 0 4` ✓ INFERRED
- **Enable DHCP Snooping** on VLANs 110 and 120 to prevent rogue DHCP servers. Example: `ip dhcp snooping vlan 110,120` ✓ INFERRED
- **Enable Dynamic ARP Inspection (DAI)** on VLANs 110 and 120 to prevent ARP spoofing. Example: `ip arp inspection vlan 110,120` ✓ INFERRED
- **Enable port security** on access ports to limit the number of MAC addresses per port. Example: `switchport port-security` ✓ INFERRED
- **Enable 802.1X authentication** on access ports to enforce device authentication. Example: `dot1x port-control auto` ✓ INFERRED
- **Enable LLDP** to improve network visibility and troubleshooting. Example: `lldp run` ✓ INFERRED

## Summary

This device, **lab-sw01**, is an **Access Layer switch** based on its configuration, which includes a large number of access ports, VLANs for end-user devices, and no routing capabilities. The configuration is functional but lacks several key security features that are recommended for production environments. The device is part of a lab environment, as indicated by the MOTD banner and the presence of VLANs for lab clients and servers. The configuration quality is acceptable for a lab setting but would require significant hardening for use in a production network.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T12:49:34.233420