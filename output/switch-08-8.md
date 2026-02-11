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
- **VLAN Interfaces (SVIs)**: 2 configured ✓ VERIFIED

### VLAN Interface Details
- **VLAN 1**
  - Status: Shutdown ✓ VERIFIED
- **VLAN 99**
  - Description: Management ✓ VERIFIED
  - IP: 10.99.1.8 255.255.255.0 ✓ VERIFIED
  - Status: Active ✓ VERIFIED

- **VLAN 110**
  - Description: Lab-Klienter ✓ VERIFIED (from raw config)
- **VLAN 120**
  - Description: Lab-Servere ✓ VERIFIED (from raw config)
- **VLAN 666**
  - Native VLAN on trunk interface FastEthernet0/24 ✓ VERIFIED (from raw config)

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
- **Routing Configuration Line**: `ip default-gateway 10.99.1.1` ✓ VERIFIED

## Configuration Quality Assessment

### Device Role
- **Device Role**: ~ INFERRED - **Access Layer Switch**
  - Justification: The device has many access ports (10), no routing enabled, and is connected to end-user devices (PCs and servers). It also has a trunk interface to a likely distribution switch (`dis-sw01`), which is typical of an access-layer switch.

### Security Posture

#### ✓ Strengths
- **Syslog logging is enabled** ✓ VERIFIED - Logs are sent to 10.99.0.50.
- **NTP is configured** ✓ VERIFIED - Time synchronization is enabled with server 10.99.0.1.
- **PortFast is enabled on access ports** ✓ VERIFIED - Prevents STP delays on end-user ports.
- **No password encryption is used** ✓ VERIFIED - `no service password-encryption` is configured, which is a known security risk, but this is explicitly stated in the configuration.
- **Banner is configured** ✓ VERIFIED - `banner motd` is set to "Lab-miljoe. Ingen produksjonsdata tillatt." to warn users this is a lab environment.

#### ⚠ Areas for Improvement
- **SSH is not configured** ⚠ INFERRED - Telnet is still allowed on VTY lines, which is insecure.
- **VTY lines have no authentication** ⚠ INFERRED - No AAA or local authentication is configured for remote access.
- **No ACLs are applied to VTY lines** ⚠ INFERRED - No access control for remote management.
- **No port security is enabled** ⚠ INFERRED - No protection against MAC flooding or unauthorized device access.
- **DHCP Snooping is not enabled** ⚠ INFERRED - No protection against rogue DHCP servers.
- **Dynamic ARP Inspection is not enabled** ⚠ INFERRED - No protection against ARP spoofing.
- **IP Source Guard is not enabled** ⚠ INFERRED - No protection against IP spoofing.
- **802.1X is not configured** ⚠ INFERRED - No port-based authentication for wired devices.
- **AAA is not enabled** ⚠ INFERRED - No centralized authentication, authorization, or accounting.

#### Recommendations
- **Enable SSH and disable Telnet** - Replace `transport input ssh telnet` with `transport input ssh` to secure remote access.
- **Implement AAA for VTY lines** - Configure local or RADIUS/TACACS+ authentication for remote access.
- **Apply ACLs to VTY lines** - Restrict remote access to trusted IP addresses.
- **Enable port security on access ports** - Limit the number of MAC addresses per port to prevent MAC flooding.
- **Enable DHCP Snooping** - Protect against rogue DHCP servers by enabling it on VLANs 110 and 120.
- **Enable Dynamic ARP Inspection (DAI)** - Prevent ARP spoofing by enabling DAI on VLANs 110 and 120.
- **Enable IP Source Guard** - Prevent IP spoofing by enabling it on VLANs 110 and 120.
- **Enable 802.1X authentication** - Secure wired access by enabling port-based authentication.
- **Enable password encryption** - Use `service password-encryption` to protect clear-text passwords in the configuration.
- **Enable LLDP** - If interoperability with non-Cisco devices is needed, enable LLDP for device discovery.

## Summary

The device **lab-sw01** is an **Access Layer Switch** configured for a lab environment. It provides connectivity to PCs and servers in VLANs 110 and 120, with a trunk interface to a distribution switch. The configuration includes basic network services like NTP and syslog, but lacks essential security features such as SSH, port security, and dynamic ARP inspection. The device is not suitable for production use due to its lack of security hardening and absence of routing capabilities.

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T01:23:05.463902