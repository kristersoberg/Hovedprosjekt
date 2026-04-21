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
- **CDP**: Enabled✓ VERIFIED
- **LLDP**: Not enabled✓ VERIFIED
- **802.1X**: Not configured✓ VERIFIED
- **IP Source Guard**: Not configured✓ VERIFIED
- **Port Security**: Not enabled on any interface ✓ VERIFIED

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED

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

### Device Role
- **Role**: ~ INFERRED - This device functions as an **Access Layer Switch**. It has numerous access ports (10), no routing enabled, and provides connectivity to end devices (PCs and servers). The presence of a trunk port suggests it connects to a distribution layer switch.

### Security Posture

#### ✓ Strengths
- **DHCP Server Configuration**: DHCP pools are configured for VLANs 110 and 120, providing centralized IP address management. ✓ VERIFIED
- **NTP and Logging**: NTP and syslog are enabled, which is a good practice for time synchronization and centralized logging. ✓ VERIFIED
- **Banner Message**: A MOTD banner is configured to warn users about the lab environment. ✓ VERIFIED
- **PortFast on Access Ports**: PortFast is enabled on all access ports, reducing STP convergence time. ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH Not Configured**: Telnet is still allowed on VTY lines, which is insecure. SSH should be configured and telnet disabled. ? UNCERTAIN (but strongly recommended)
- **No AAA Authentication**: AAA is not enabled, so there is no centralized authentication, authorization, or accounting. ? UNCERTAIN (but strongly recommended)
- **No ACLs on VTY Lines**: VTY lines are open to all, which is a security risk. Access should be restricted using ACLs. ? UNCERTAIN (but strongly recommended)
- **No Port Security**: No port security is enabled, which could help prevent unauthorized device access. ? UNCERTAIN (but strongly recommended)
- **No DHCP Snooping or DAI**: These features are not enabled, leaving the network vulnerable to rogue DHCP servers and ARP spoofing. ? UNCERTAIN (but strongly recommended)

#### Recommendations
- **Enable SSH and Disable Telnet**:
  - Add `transport input ssh` to VTY lines and remove `telnet`.
  - Configure `ip ssh version 2` and set a timeout.
- **Implement AAA**:
  - Enable AAA and configure RADIUS or TACACS+ for authentication.
- **Apply ACLs to VTY Lines**:
  - Create and apply an ACL to restrict VTY access to trusted IP addresses.
- **Enable Port Security**:
  - Enable port security on access ports to limit the number of MAC addresses allowed.
- **Enable DHCP Snooping and DAI**:
  - Enable DHCP snooping on VLANs 110 and 120.
  - Enable DAI on the same VLANs to prevent ARP spoofing.
- **Enable SNMP with Secure Configuration**:
  - If SNMP is required, configure it with a secure community string and restrict access via ACLs.
- **Enable IP Source Guard**:
  - Enable IP source guard on access ports to prevent IP spoofing.

## Summary

lab-sw01 is an **Access Layer Switch** providing connectivity to lab PCs and servers in VLANs 110 and 120. It is configured with a management VLAN (VLAN 99) and a trunk port for uplink to a distribution switch. The device has a basic configuration with some good practices (NTP, logging, DHCP pools), but lacks several critical security features such as SSH, AAA, port security, and DHCP snooping. ~ INFERRED

The configuration is functional but could be significantly improved to meet enterprise security standards. ✓ VERIFIED

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T06:19:05.166858