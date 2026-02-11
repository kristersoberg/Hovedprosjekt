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

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- **Syslog logging is enabled** with a remote server at 10.99.0.50 ✓ VERIFIED
- **NTP is configured** with a server at 10.99.0.1 ✓ VERIFIED
- **Banner is configured** for MOTD with a clear warning message: `^CLab-miljoe. Ingen produksjonsdata tillatt.^C` ✓ VERIFIED
- **PortFast is enabled** on all access ports to prevent STP loops ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH is not configured**, leaving the device vulnerable to Telnet-based attacks ✓ VERIFIED
- **VTY lines allow both SSH and Telnet**, and no ACL is applied to restrict access ✓ VERIFIED
- **No AAA authentication is configured**, allowing unauthenticated access to the console and VTY lines ✓ VERIFIED
- **No port security is enabled**, which could allow unauthorized devices to connect to the network ✓ VERIFIED
- **DHCP Snooping and Dynamic ARP Inspection are not enabled**, leaving the network vulnerable to DHCP spoofing and ARP poisoning attacks ✓ VERIFIED
- **No VLAN access control lists (VACLs) or ACLs** are configured to restrict traffic between VLANs ✓ VERIFIED

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines to secure remote access.
- **Configure AAA authentication** for console and VTY access to enforce user authentication.
- **Enable port security** on access ports to prevent unauthorized device access.
- **Enable DHCP Snooping** and configure trusted ports to prevent rogue DHCP servers.
- **Enable Dynamic ARP Inspection (DAI)** to prevent ARP spoofing attacks.
- **Apply ACLs to VTY lines** to restrict access to trusted IP addresses.
- **Consider enabling LLDP** for network discovery and troubleshooting.
- **Enable SNMP** if monitoring is required, and configure secure community strings and access controls.

## Summary

lab-sw01 is an **Access Layer switch** based on its configuration, which includes a large number of access ports, no routing, and a focus on end-user connectivity. The device is configured with basic network services such as NTP and syslog, but lacks several key security features that are essential for a production environment. The configuration is functional but requires significant hardening to meet enterprise security standards.

~ INFERRED: Based on the presence of multiple access ports and the absence of routing, this device is likely serving as an access switch in a lab or test environment.

~ INFERRED: The device is likely part of a VLAN-based network with VLANs 110 and 120 used for client and server traffic, respectively.

~ INFERRED: The presence of a trunk port (FastEthernet0/24) suggests that this switch connects to a distribution layer switch.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T06:03:50.777260