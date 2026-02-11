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
  - Justification: The device has many access ports (10), no routing enabled, and is connected to end-user devices (PCs and servers). It also has a trunk port to a likely distribution switch (`FastEthernet0/24`), which is typical for an access layer switch.

### Security Posture

#### ✓ Strengths
- **Syslog logging is enabled** and configured to send logs to 10.99.0.50 ✓ VERIFIED
- **NTP is enabled** with a configured server (10.99.0.1) ✓ VERIFIED
- **PortFast is enabled** on all access ports, reducing STP convergence time ✓ VERIFIED
- **No password encryption** is used, which is a known security risk, but this is a lab environment and may be intentional ? UNCERTAIN
- **Banner is configured** to warn users this is a lab environment: `banner motd ^CLab-miljoe. Ingen produksjonsdata tillatt.^C` ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH is not configured**, and VTY lines allow both SSH and Telnet. Telnet is insecure and should be disabled. ? UNCERTAIN
- **VTY lines have no authentication** and no access control (no ACL). This is a significant security gap. ✓ VERIFIED
- **AAA is not enabled**, so there is no centralized authentication, authorization, or accounting. ✓ VERIFIED
- **DHCP Snooping and Dynamic ARP Inspection are not enabled**, leaving the network vulnerable to spoofing and man-in-the-middle attacks. ✓ VERIFIED
- **Port security is not enabled** on any interface, which could allow unauthorized devices to connect. ✓ VERIFIED
- **No SNMP configuration** is present, which may be intentional for a lab device, but it limits monitoring capabilities. ✓ VERIFIED

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines to secure remote access.
- **Implement AAA** for centralized authentication and authorization.
- **Enable DHCP Snooping** and **Dynamic ARP Inspection** on VLANs 110 and 120 to improve security.
- **Enable port security** on access ports to prevent unauthorized device access.
- **Apply access control lists (ACLs)** to VTY lines to restrict access to trusted IP addresses.
- **Enable IP Source Guard** to prevent IP spoofing.
- **Consider enabling SNMP** if monitoring is required, and configure it securely.
- **Enable password encryption** using `service password-encryption` to protect clear-text passwords.

## Summary

lab-sw01 is an **Access Layer Switch** in a lab environment, providing connectivity to PCs and servers in VLANs 110 and 120. It has a management VLAN (VLAN 99) with an assigned IP address and is connected to a distribution switch via a trunk port. The configuration is minimal and lacks several security features that would be expected in a production environment. While it is suitable for a lab setting, it would require significant hardening before deployment in a production network.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T06:08:09.268206