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
- **Port Security**: Not enabled on any interfaces ✓ VERIFIED
- **IP Source Guard**: Not configured ✓ VERIFIED
- **802.1X**: Not configured ✓ VERIFIED
- **CDP**: Enabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED

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

### Device Role
- **Device Role**: ~ INFERRED - **Access Layer Switch**
  - Justification: The device has many access ports (10), no routing enabled, and is connected to end-user devices (PCs and servers). It also has a trunk port to a distribution switch (`FastEthernet0/24`), which is typical for an access layer switch.

### Security Posture

#### ✓ Strengths
- **Syslog logging is enabled** with a remote server at 10.99.0.50 ✓ VERIFIED
- **NTP is configured** with a remote server at 10.99.0.1 ✓ VERIFIED
- **PortFast is enabled** on all access ports to prevent STP loops ✓ VERIFIED
- **No password encryption** is disabled (`no service password-encryption`), which is a known vulnerability but not uncommon in lab environments ✓ VERIFIED
- **Banner is configured** to warn users about unauthorized access (`banner motd ^CLab-miljoe. Ingen produksjonsdata tillatt.^C`) ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH is not configured**, leaving the device vulnerable to Telnet traffic (plaintext credentials) ✓ VERIFIED
- **VTY lines allow both SSH and Telnet**, which is insecure. Telnet should be disabled. ✓ VERIFIED
- **No authentication is configured** for console or VTY access, allowing unrestricted access. ✓ VERIFIED
- **No ACLs are applied** to VTY lines, leaving them open to remote access. ✓ VERIFIED
- **DHCP Snooping is not enabled**, which could allow rogue DHCP servers to disrupt the network. ✓ VERIFIED
- **Dynamic ARP Inspection (DAI) is not enabled**, which could allow ARP spoofing attacks. ✓ VERIFIED
- **Port Security is not enabled**, which could allow unauthorized devices to connect to the network. ✓ VERIFIED
- **802.1X is not configured**, which could allow unauthorized devices to access the network. ✓ VERIFIED
- **LLDP is not enabled**, which could limit network visibility and troubleshooting. ✓ VERIFIED

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines to secure remote access.
- **Configure AAA authentication** for console and VTY access to enforce user authentication.
- **Apply an ACL to VTY lines** to restrict access to trusted IP addresses.
- **Enable DHCP Snooping** on VLANs 110 and 120 to prevent rogue DHCP servers.
- **Enable Dynamic ARP Inspection (DAI)** on VLANs 110 and 120 to prevent ARP spoofing.
- **Enable Port Security** on access ports to prevent unauthorized device access.
- **Enable 802.1X authentication** to enforce user-based access control.
- **Enable LLDP** to improve network visibility and troubleshooting.
- **Enable password encryption** using `service password-encryption` to protect stored credentials.

## Summary

lab-sw01 is an **Access Layer Switch** configured to provide network connectivity to lab PCs and servers. It is connected to a distribution switch via a trunk port and has basic network services like NTP and syslog enabled. However, the device lacks several critical security features such as SSH, DHCP Snooping, and 802.1X, which should be implemented to improve its security posture. The configuration is functional but not hardened for production environments. ~ INFERRED

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T12:29:25.086344