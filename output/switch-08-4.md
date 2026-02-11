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
  - IP Address: 10.99.1.8 255.255.255.0 ✓ VERIFIED  
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
- **FastEthernet0/1** - Lab-PC 1 | Mode: access | VLAN: 110 | PortFast enabled ✓ VERIFIED  
- **FastEthernet0/2** - Lab-PC 2 | Mode: access | VLAN: 110 | PortFast enabled ✓ VERIFIED  
- **FastEthernet0/3** - Lab-PC 3 | Mode: access | VLAN: 110 | PortFast enabled ✓ VERIFIED  
- **FastEthernet0/4** - Lab-PC 4 | Mode: access | VLAN: 110 | PortFast enabled ✓ VERIFIED  
- **FastEthernet0/5** - Lab-PC 5 | Mode: access | VLAN: 110 | PortFast enabled ✓ VERIFIED  
- **FastEthernet0/6** - Lab-PC 6 | Mode: access | VLAN: 110 | PortFast enabled ✓ VERIFIED  
- **FastEthernet0/7** - Lab-Server 1 | Mode: access | VLAN: 120 | PortFast enabled ✓ VERIFIED  
- **FastEthernet0/8** - Lab-Server 2 | Mode: access | VLAN: 120 | PortFast enabled ✓ VERIFIED  
- **FastEthernet0/9** - Lab-Server 3 | Mode: access | VLAN: 120 | PortFast enabled ✓ VERIFIED  
- **FastEthernet0/10** - Lab-Server 4 | Mode: access | VLAN: 120 | PortFast enabled ✓ VERIFIED  
- **FastEthernet0/24** - Uplink til dis-sw01 gig0/6 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 99, 110, 120 | Encapsulation: dot1q ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED  
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
- **Syslog logging** is enabled with a remote server at 10.99.0.50 ✓ VERIFIED  
- **NTP** is configured with a remote server at 10.99.0.1 ✓ VERIFIED  
- **PortFast** is enabled on all access ports to prevent STP loops ✓ VERIFIED  
- **Banner MOTD** is configured to warn users about lab environment and data restrictions ✓ VERIFIED  

#### ⚠ Areas for Improvement
- **SSH is not configured**, leaving the device vulnerable to Telnet traffic (plaintext) ⚠ INFERRED  
- **VTY lines** allow both SSH and Telnet without authentication or ACLs ⚠ INFERRED  
- **No AAA configuration** is present, which is a best practice for access control ⚠ INFERRED  
- **No port security** is enabled, leaving access ports open to unauthorized MAC addresses ⚠ INFERRED  
- **No DHCP snooping** or **Dynamic ARP Inspection** is enabled, increasing risk of spoofing attacks ⚠ INFERRED  
- **No IP Source Guard** is configured, allowing potential IP spoofing ⚠ INFERRED  
- **No ACLs** are applied to VTY lines or management interface ⚠ INFERRED  

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines to secure remote access  
- **Implement AAA** for authentication, authorization, and accounting  
- **Enable port security** on all access ports to prevent unauthorized device access  
- **Enable DHCP snooping** and **Dynamic ARP Inspection** to protect against spoofing attacks  
- **Apply ACLs** to VTY lines and the management interface to restrict access to trusted IPs  
- **Enable IP Source Guard** to prevent IP spoofing  
- **Consider enabling SNMP** for monitoring and management  
- **Enable LLDP** for network discovery and troubleshooting  

---

## Summary

This device, **lab-sw01**, is an **Access Layer switch** based on its configuration, which includes a large number of access ports, VLANs for client and server traffic, and no routing capabilities. The switch is configured with basic management and logging features, but lacks several critical security features such as SSH, AAA, port security, and DHCP snooping. The configuration is functional for a lab environment but would require significant hardening for production use.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T12:40:50.552183