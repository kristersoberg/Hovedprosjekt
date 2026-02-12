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
- **IP Source Guard**: Not configured ✓ VERIFIED
- **802.1X**: Not configured ✓ VERIFIED
- **CDP**: Enabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED

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

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

### DNS
- **DNS Domain Name**: lab.bedrift.no ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED

## Configuration Quality Assessment

### Device Role
- **Device Role**: ~ INFERRED - **Access Layer Switch**
  - Justification: The device has many access ports (10), no routing enabled, and is likely connecting end-user devices (PCs and servers) to the network. It also has a trunk port to a distribution switch (`dis-sw01`), which is typical for an access layer device.

### Security Posture

#### ✓ Strengths
- **Syslog logging is enabled** with a remote server at 10.99.0.50 ✓ VERIFIED
- **NTP is configured** with a remote server at 10.99.0.1 ✓ VERIFIED
- **PortFast is enabled** on all access ports to prevent STP loops ✓ VERIFIED
- **No password encryption** is disabled (`no service password-encryption`), which is a known security risk, but this is a lab environment, so it may be acceptable for simplicity. ~ INFERRED
- **Banner is configured** to warn users about lab environment and data restrictions ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH is not configured**, leaving the device vulnerable to Telnet traffic, which is unencrypted. ~ INFERRED
- **VTY lines allow both SSH and Telnet**, which is insecure. Telnet should be disabled. ~ INFERRED
- **No authentication is configured** for console or VTY access. ~ INFERRED
- **No ACLs are applied** to VTY lines, allowing unrestricted remote access. ~ INFERRED
- **DHCP Snooping is not enabled**, leaving the network vulnerable to rogue DHCP servers. ~ INFERRED
- **Dynamic ARP Inspection (DAI) is not enabled**, leaving the network vulnerable to ARP spoofing. ~ INFERRED
- **Port Security is not enabled**, allowing unauthorized devices to connect to the switch. ~ INFERRED
- **802.1X is not configured**, leaving the network vulnerable to unauthorized device access. ~ INFERRED
- **No SNMP configuration** is present, which may be acceptable in a lab, but should be configured in production. ~ INFERRED

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines to secure remote access. ~ INFERRED
- **Configure AAA authentication** for console and VTY access to enforce user authentication. ~ INFERRED
- **Apply an ACL to VTY lines** to restrict access to trusted IP addresses. ~ INFERRED
- **Enable DHCP Snooping** on VLANs 110 and 120 to prevent rogue DHCP servers. ~ INFERRED
- **Enable Dynamic ARP Inspection (DAI)** on VLANs 110 and 120 to prevent ARP spoofing. ~ INFERRED
- **Enable Port Security** on access ports to prevent unauthorized device connections. ~ INFERRED
- **Enable 802.1X authentication** to enforce device and user authentication. ~ INFERRED
- **Enable SNMP** with secure community strings and access control for monitoring. ~ INFERRED
- **Enable password encryption** with `service password-encryption` to protect stored credentials. ~ INFERRED

## Summary

lab-sw01 is an **Access Layer switch** configured to connect end-user devices (PCs and servers) to the network. It has 10 active access ports and one trunk port to a distribution switch. The device is managed via VLAN 99 with an IP address of 10.99.1.8 and uses NTP and syslog for time synchronization and logging. However, the configuration lacks several key security features such as SSH, DHCP Snooping, and Port Security, which should be implemented to improve the security posture. The device is likely part of a lab environment, as indicated by the banner and lack of production-grade security. ~ INFERRED

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T12:45:06.922268