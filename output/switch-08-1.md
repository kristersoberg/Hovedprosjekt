# Network Device Documentation: lab-sw01

## Device Information
- **Hostname**: lab-sw01 ✓ VERIFIED  
- **IOS Version**: 15.0(2)SE4 ✓ VERIFIED  
- **Domain Name**: lab.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

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

---

## AAA Configuration
- **AAA**: Not enabled ✓ VERIFIED  

---

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
  - Description: Lab-Klienter ✓ VERIFIED  
- **VLAN 120**  
  - Description: Lab-Servere ✓ VERIFIED  
- **VLAN 666**  
  - Description: Not configured ✓ VERIFIED  

- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

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

---

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled✓ VERIFIED  
- **Port Security**: Not enabled on any interface ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **CDP**: Enabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  

---

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

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **Routing Configuration Line**: `ip default-gateway 10.99.1.1` ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- **Syslog logging is enabled** with a remote server at 10.99.0.50 ✓ VERIFIED  
- **NTP is configured** with a remote server at 10.99.0.1 ✓ VERIFIED  
- **Banner is configured** with a message of the day (MOTD) to warn users about lab environment rules ✓ VERIFIED  
- **Spanning Tree Protocol (STP) is enabled in PVST mode**, which is appropriate for a Layer 2 network ✓ VERIFIED  

#### ⚠ Areas for Improvement
- **SSH is not configured**, leaving the device vulnerable to Telnet-based attacks. Telnet is insecure and should be disabled.  
- **VTY lines allow both SSH and Telnet**, which is a security risk. Telnet should be removed.  
- **No AAA authentication is configured**, meaning there is no centralized authentication mechanism.  
- **No access control lists (ACLs) are applied to VTY lines**, allowing unrestricted remote access.  
- **No port security is enabled**, which could prevent unauthorized devices from connecting to the switch.  
- **DHCP Snooping and Dynamic ARP Inspection (DAI) are not enabled**, leaving the network vulnerable to DHCP spoofing and ARP poisoning attacks.  
- **No SNMP is configured**, which could be a missed opportunity for monitoring and management.  

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines.  
- **Implement AAA authentication** for console and VTY access.  
- **Apply access control lists (ACLs)** to restrict remote access to trusted IP addresses.  
- **Enable port security** on access ports to prevent unauthorized device access.  
- **Enable DHCP Snooping and DAI** on VLANs 110 and 120 to improve network security.  
- **Enable SNMP** with appropriate community strings and access controls for monitoring.  
- **Consider enabling LLDP** for network discovery and troubleshooting.  

---

## Summary

The device **lab-sw01** is an **Access Layer switch** based on its configuration, which includes a large number of access ports, no routing, and VLAN-based segmentation. It is configured for a lab environment with VLANs 110 and 120 for client and server traffic, respectively. The switch has a basic level of network services (NTP, syslog) but lacks several key security features such as SSH, port security, and DHCP Snooping. The configuration is functional but requires significant hardening to meet enterprise security standards.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T01:03:02.439944