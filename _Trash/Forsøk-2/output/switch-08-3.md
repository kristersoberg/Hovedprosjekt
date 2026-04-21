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
  - Description: Lab-Klienter (from raw config) ? UNCERTAIN  
- **VLAN 120**  
  - Description: Lab-Servere (from raw config) ? UNCERTAIN  
- **VLAN 666**  
  - Native VLAN on trunk interface (FastEthernet0/24) ✓ VERIFIED  

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
- **CDP**: Enabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  

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

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- **Syslog logging** is enabled and configured to send logs to 10.99.0.50 ✓ VERIFIED  
- **NTP** is enabled with a configured server (10.99.0.1) ✓ VERIFIED  
- **PortFast** is enabled on all access ports to prevent STP loops ✓ VERIFIED  
- **Banner MOTD** is configured to warn users about lab environment and data restrictions ✓ VERIFIED  

#### ⚠ Areas for Improvement
- **SSH is not configured**, leaving the device vulnerable to Telnet traffic (plaintext) ⚠ INFERRED  
- **VTY lines allow both SSH and Telnet**, which is insecure ⚠ INFERRED  
- **No authentication is configured** for console or VTY access ⚠ INFERRED  
- **No ACLs are applied** to VTY lines for access control ⚠ INFERRED  
- **DHCP Snooping**, **DAI**, and **IP Source Guard** are not enabled, leaving the network vulnerable to spoofing and rogue DHCP servers ⚠ INFERRED  
- **Port security** is not enabled on any interface, increasing risk of unauthorized device access ⚠ INFERRED  
- **802.1X** is not configured, leaving wired access unauthenticated ⚠ INFERRED  

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines to secure remote access  
- **Configure AAA** with local or TACACS+ authentication for console and VTY access  
- **Apply ACLs** to VTY lines to restrict access to trusted IP addresses  
- **Enable DHCP Snooping** on VLANs 110 and 120 to prevent rogue DHCP servers  
- **Enable Dynamic ARP Inspection (DAI)** on VLANs 110 and 120 to prevent ARP spoofing  
- **Enable IP Source Guard** on VLANs 110 and 120 to prevent IP spoofing  
- **Enable port security** on access ports to limit unauthorized device connections  
- **Enable 802.1X** for wired authentication if required by policy  
- **Enable SNMP** if monitoring is required, and configure secure community strings  

---

## Summary

This device, **lab-sw01**, is an **Access Layer switch** based on its configuration, which includes many access ports, no routing, and VLAN interfaces for management and client/server VLANs. The configuration is functional but lacks several key security features, including SSH, AAA, DHCP Snooping, and port security. The device is configured for a lab environment with a clear separation of client and server VLANs, and it uses a default gateway for management access. The configuration quality is acceptable for a lab setting but would require significant hardening for production use.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T12:38:38.637895