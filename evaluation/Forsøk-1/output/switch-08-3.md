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
  - **Status**: Shutdown ✓ VERIFIED
- **VLAN 99**
  - **Description**: Management ✓ VERIFIED
  - **IP Address**: 10.99.1.8 ✓ VERIFIED
  - **Subnet Mask**: 255.255.255.0 ✓ VERIFIED
  - **Status**: Active ✓ VERIFIED

- **VLAN 110**
  - **Description**: Lab-Klienter ✓ VERIFIED (from `vlan 110 name Lab-Klienter`)
- **VLAN 120**
  - **Description**: Lab-Servere ✓ VERIFIED (from `vlan 120 name Lab-Servere`)
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
- **DNS Lookup**: Disabled ✓ VERIFIED (from `no ip domain-lookup`)

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED

## Configuration Quality Assessment

### Device Role
- **Device Role**: ~ INFERRED - **Access Layer Switch**
  - Justification: The device has many access ports (10), no routing enabled, and is likely connecting end-user devices (PCs and servers) to the network. The presence of a trunk port suggests it connects to a distribution layer switch.

### Security Posture

#### ✓ Strengths
- **Syslog logging is enabled** ✓ VERIFIED (logs sent to 10.99.0.50)
- **NTP is configured** ✓ VERIFIED (synchronizing with 10.99.0.1)
- **PortFast is enabled on access ports** ✓ VERIFIED (prevents STP delays)
- **Banner is configured** ✓ VERIFIED (motd banner: `Lab-miljoe. Ingen produksjonsdata tillatt.`)

#### ⚠ Areas for Improvement
- **SSH is not configured** ⚠ INFERRED - Telnet is still allowed on VTY lines, which is insecure.
- **VTY lines lack authentication** ⚠ INFERRED - No AAA or local authentication is configured.
- **No ACLs are applied to VTY lines** ⚠ INFERRED - No access control for remote access.
- **No port security is enabled** ⚠ INFERRED - No MAC address filtering on access ports.
- **DHCP Snooping is not enabled** ⚠ INFERRED - No protection against rogue DHCP servers.
- **Dynamic ARP Inspection is not enabled** ⚠ INFERRED - No protection against ARP spoofing.
- **No SNMP is configured** ⚠ INFERRED - No network monitoring or management via SNMP.

#### Recommendations
- **Enable SSH and disable Telnet** on VTY lines to secure remote access.
- **Implement AAA authentication** for console and VTY access.
- **Apply access control lists (ACLs)** to VTY lines to restrict remote access to trusted IPs.
- **Enable port security** on access ports to prevent unauthorized device connections.
- **Enable DHCP Snooping** on VLANs 110 and 120 to prevent rogue DHCP servers.
- **Enable Dynamic ARP Inspection (DAI)** on VLANs 110 and 120 to prevent ARP spoofing.
- **Configure SNMP** for network monitoring and management.
- **Enable IP Source Guard** on access ports to prevent IP spoofing.
- **Consider enabling 802.1X authentication** for secure user access to the network.

## Summary

lab-sw01 is an **Access Layer switch** configured to connect end-user devices (PCs and servers) to VLANs 110 and 120, with a management VLAN (VLAN 99) for administrative access. The switch is running Cisco IOS 15.0(2)SE4 and is part of the `lab.bedrift.no` domain. While it has some basic security features like logging and NTP, it lacks critical security controls such as SSH, port security, and DHCP Snooping. The configuration is functional but requires significant hardening to meet enterprise security standards.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T06:05:52.109139