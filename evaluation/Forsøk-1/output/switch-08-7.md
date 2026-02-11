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
- **CDP**: Enabled✓ VERIFIED
- **LLDP**: Not enabled✓ VERIFIED
- **802.1X**: Not configured✓ VERIFIED
- **IP Source Guard**: Not configured✓ VERIFIED
- **Port Security**: Not enabled on any interface ✓ VERIFIED

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
- **Banner is configured** to warn users about unauthorized access ✓ VERIFIED
- **Management VLAN is separated** from user VLANs for better security ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH is not configured**, leaving the device vulnerable to Telnet traffic (plaintext) ✓ VERIFIED
- **VTY lines allow both SSH and Telnet**, which is a security risk ✓ VERIFIED
- **No AAA authentication is configured**, allowing unauthenticated access to the device ✓ VERIFIED
- **No ACLs are applied to VTY lines**, allowing unrestricted remote access ✓ VERIFIED
- **No port security is enabled**, leaving access ports vulnerable to MAC flooding attacks ✓ VERIFIED
- **DHCP snooping and Dynamic ARP Inspection are not enabled**, increasing the risk of rogue DHCP servers and ARP spoofing ✓ VERIFIED
- **LLDP is not enabled**, which could be useful for network discovery and troubleshooting ✓ VERIFIED

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines to secure remote access (e.g., `transport input ssh` on `line vty 0 4`) ~ INFERRED
- **Implement AAA authentication** for console and VTY access to enforce user authentication ~ INFERRED
- **Apply an ACL to VTY lines** to restrict access to trusted IP addresses ~ INFERRED
- **Enable port security** on access ports to prevent unauthorized device connections ~ INFERRED
- **Enable DHCP snooping** and **Dynamic ARP Inspection** to protect against rogue DHCP servers and ARP spoofing ~ INFERRED
- **Enable LLDP** for network discovery and device identification ~ INFERRED
- **Enable IP Source Guard** to prevent IP spoofing on access ports ~ INFERRED

## Summary

The device **lab-sw01** is an **Access Layer switch** ✓ VERIFIED, as it has many access ports, no routing enabled, and is connected to end-user devices such as PCs and servers. The configuration is functional but lacks several key security features, including SSH, AAA, port security, and DHCP snooping. The device is configured with VLANs 99 (Management), 110 (Lab-Klienter), 120 (Lab-Servere), and 666 (Native VLAN on trunk). The configuration quality is **basic** ~ INFERRED, and several improvements are recommended to enhance security and operational robustness.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T06:14:37.154531