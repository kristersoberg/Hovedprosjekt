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
- **Console Authentication**: None ✓ VERIFIED
- **Console Logging Synchronous**: Enabled ✓ VERIFIED

---

## AAA Configuration
- **AAA**: Not enabled ✓ VERIFIED

---

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
- **IP Source Guard**: Not configured ✓ VERIFIED
- **802.1X**: Not configured ✓ VERIFIED
- **CDP**: Enabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED

---

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

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- **Syslog logging is enabled** and configured to send logs to 10.99.0.50 ✓ VERIFIED
- **NTP is enabled** with a configured server at 10.99.0.1 ✓ VERIFIED
- **PortFast is enabled** on all access ports to prevent STP loops ✓ VERIFIED
- **Banner is configured** to warn users about the lab environment and unauthorized access ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH is not configured**, leaving the device vulnerable to Telnet-based attacks ✓ VERIFIED
- **VTY lines allow both SSH and Telnet**, which is a security risk due to Telnet's lack of encryption ✓ VERIFIED
- **No authentication is configured** for console or VTY access, allowing unrestricted access ✓ VERIFIED
- **No ACLs are applied** to VTY lines, leaving remote access open to potential brute-force attacks ✓ VERIFIED
- **DHCP Snooping, DAI, and IP Source Guard are not enabled**, leaving the network vulnerable to spoofing and rogue DHCP servers ✓ VERIFIED
- **Port security is not enabled**, increasing the risk of unauthorized device connections ✓ VERIFIED
- **AAA is not enabled**, preventing centralized authentication, authorization, and accounting ✓ VERIFIED

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines to secure remote access (~ INFERRED)
- **Configure authentication** for console and VTY access using local or TACACS+/RADIUS (~ INFERRED)
- **Apply an ACL** to VTY lines to restrict access to trusted IP addresses (~ INFERRED)
- **Enable DHCP Snooping** on VLANs 110 and 120 to prevent rogue DHCP servers (~ INFERRED)
- **Enable Dynamic ARP Inspection (DAI)** on VLANs 110 and 120 to prevent ARP spoofing (~ INFERRED)
- **Enable IP Source Guard** on VLANs 110 and 120 to prevent IP spoofing (~ INFERRED)
- **Enable port security** on access ports to limit the number of MAC addresses per port (~ INFERRED)
- **Enable AAA** for centralized user authentication and access control (~ INFERRED)

---

## Summary

The device **lab-sw01** is an **Access Layer switch** (~ INFERRED) based on its configuration, which includes a large number of access ports, VLAN-based segmentation, and no routing capabilities. The switch is configured with basic network services such as NTP and syslog, but lacks essential security features like SSH, AAA, and dynamic security protocols. The configuration is functional for a lab environment but would require significant hardening for production use.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T01:21:04.537299