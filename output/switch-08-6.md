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
- **Console Access**: Line con 0, no authentication, logging synchronous enabled ✓ VERIFIED

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
  - Justification: The device has many access ports (10), no routing enabled, and is connected to end-user devices (PCs and servers). It also has a trunk port to a likely distribution switch (`FastEthernet0/24`), which is typical for an access layer switch.

### Security Posture

#### ✓ Strengths
- **Syslog logging is enabled** and configured to send logs to 10.99.0.50 ✓ VERIFIED
- **NTP is enabled** and configured to synchronize with 10.99.0.1 ✓ VERIFIED
- **Banner is configured** for MOTD: `Lab-miljoe. Ingen produksjonsdata tillatt.` ✓ VERIFIED
- **PortFast is enabled** on all access ports to prevent STP delays ✓ VERIFIED
- **No service password-encryption** is enabled, which is a best practice for security (plaintext passwords are not stored) ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH is not configured**, and VTY lines allow both SSH and Telnet. Telnet is insecure and should be disabled. ~ INFERRED
- **VTY lines have no authentication** and no access control (ACL). ~ INFERRED
- **Console access has no authentication**, which is a security risk. ~ INFERRED
- **No AAA configuration** is present, which limits centralized authentication and accounting. ~ INFERRED
- **No port security** is enabled on access ports, which could prevent unauthorized device access. ~ INFERRED
- **DHCP Snooping, DAI, and IP Source Guard** are not enabled, which are essential for mitigating Layer 2 attacks. ~ INFERRED
- **802.1X is not configured**, which could be used to enforce user authentication on access ports. ~ INFERRED

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines to secure remote access.
- **Configure AAA** for centralized authentication and accounting.
- **Implement port security** on access ports to prevent unauthorized device connections.
- **Enable DHCP Snooping, DAI, and IP Source Guard** to improve Layer 2 security.
- **Add authentication** to console and VTY lines using local or AAA-based authentication.
- **Apply access control lists (ACLs)** to VTY lines to restrict access to trusted IP addresses.
- **Enable SNMP** if needed for monitoring, and configure it securely with read-only community strings and access restrictions.
- **Enable 802.1X** if the environment supports it for user-based authentication.

## Summary

The device **lab-sw01** is an **Access Layer Switch** serving end-user devices in a lab environment. It is configured with multiple access ports for PCs and servers, a trunk port to a distribution switch, and basic network services such as NTP and syslog. The configuration is minimal and lacks several security features that are recommended for production environments. While the device is functional, it requires additional hardening to meet enterprise security standards.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T01:18:56.009607