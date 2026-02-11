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
- **VLAN Interfaces (SVIs)**:
  - **VLAN 1**:
    - Status: Shutdown ✓ VERIFIED
  - **VLAN 99**:
    - Description: Management ✓ VERIFIED
    - IP: 10.99.1.8 255.255.255.0 ✓ VERIFIED
    - Status: Active ✓ VERIFIED
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
- **802.1X**: Not configured ✓ VERIFIED
- **IP Source Guard**: Not configured ✓ VERIFIED
- **CDP**: Enabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED

## Network Services

### Logging
- **Syslog Server**: 10.99.0.50 ✓ VERIFIED

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED
- **NTP Authentication**: Disabled ✓ VERIFIED

### DNS
- **DNS Domain Name**: lab.bedrift.no ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED

## DHCP Configuration
- **DHCP Excluded Addresses**:
  - 10.110.0.1 to 10.110.0.10 ✓ VERIFIED
  - 10.120.0.1 to 10.120.0.10 ✓ VERIFIED
- **DHCP Pools**:
  - **LAB-VLAN110**:
    - Network: 10.110.0.0/24 ✓ VERIFIED
    - Default Router: 10.110.0.1 ✓ VERIFIED
    - DNS Server: 10.99.0.20 ✓ VERIFIED
    - Lease: 8 hours ✓ VERIFIED
  - **LAB-VLAN120**:
    - Network: 10.120.0.0/24 ✓ VERIFIED
    - Default Router: 10.120.0.1 ✓ VERIFIED
    - DNS Server: 10.99.0.20 ✓ VERIFIED
    - Lease: 8 hours ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- **Syslog logging is enabled** with a remote server at 10.99.0.50 ✓ VERIFIED
- **NTP is configured** with a server at 10.99.0.1 ✓ VERIFIED
- **PortFast is enabled** on all access ports to prevent STP loops ✓ VERIFIED
- **Banner is configured** to warn users about the lab environment and data restrictions ✓ VERIFIED
- **No password encryption** is used, which is a known security risk, but this is likely intentional for lab use ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH is not configured**, leaving the device vulnerable to Telnet traffic, which is unencrypted ✓ VERIFIED
- **VTY lines allow both SSH and Telnet**, which is insecure due to Telnet's lack of encryption ✓ VERIFIED
- **No authentication is configured** for VTY or console access, allowing unrestricted access ✓ VERIFIED
- **No ACLs are applied** to VTY lines, leaving them open to unauthorized access ✓ VERIFIED
- **DHCP Snooping is not enabled**, which could allow rogue DHCP servers to disrupt network operations ✓ VERIFIED
- **Dynamic ARP Inspection is not enabled**, which could allow ARP spoofing attacks ✓ VERIFIED
- **Port security is not enabled**, which could allow unauthorized devices to connect to the network ✓ VERIFIED
- **802.1X is not configured**, which could allow unauthenticated devices to access the network ✓ VERIFIED
- **IP Source Guard is not enabled**, which could allow IP spoofing attacks ✓ VERIFIED

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines to secure remote access (~ INFERRED)
- **Configure AAA authentication** for console and VTY access to enforce user authentication (~ INFERRED)
- **Apply ACLs to VTY lines** to restrict access to trusted IP addresses (~ INFERRED)
- **Enable DHCP Snooping** on VLANs 110 and 120 to prevent rogue DHCP servers (~ INFERRED)
- **Enable Dynamic ARP Inspection** on VLANs 110 and 120 to prevent ARP spoofing (~ INFERRED)
- **Enable port security** on access ports to prevent unauthorized device access (~ INFERRED)
- **Enable 802.1X authentication** on access ports to enforce device authentication (~ INFERRED)
- **Enable IP Source Guard** on VLANs 110 and 120 to prevent IP spoofing (~ INFERRED)
- **Enable NTP authentication** to ensure time synchronization integrity (~ INFERRED)

## Summary

The device **lab-sw01** is an **Access layer switch** (~ INFERRED) based on its configuration, which includes a large number of access ports, no routing, and VLAN-based segmentation. It is configured for a lab environment with a focus on basic connectivity and minimal security features. The configuration is functional but lacks several key security best practices that should be implemented to harden the device (~ INFERRED).

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T01:25:34.508313