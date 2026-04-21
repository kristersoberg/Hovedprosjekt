# Network Device Documentation: switch-02

## Device Information
- **Hostname**: switch-02 ✓ VERIFIED
- **IOS Version**: 15.0(2)SE4 ✓ VERIFIED
- **Domain Name**: firma.local ✓ VERIFIED
- **Config Register**: Not configured ✓ VERIFIED

## Management & Access
- **Management VLAN**: 99 ✓ VERIFIED
- **IP Address**: 10.99.0.12 ✓ VERIFIED
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED
- **Default Gateway**: 10.99.0.1 ✓ VERIFIED
- **SSH Version**: 2 ✓ VERIFIED
- **SSH Timeout**: 60 seconds ✓ VERIFIED
- **VTY Transport Input**: ssh ✓ VERIFIED
- **VTY Access Class**: None (⚠ No ACL protection) ✓ VERIFIED
- **Console Access**: Line `line con 0` with no authentication and logging synchronous enabled ✓ VERIFIED

## AAA Configuration
- **AAA**: Not enabled ✓ VERIFIED

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED
- **VLAN IDs**: 10, 20, 50, 99, 666 ✓ VERIFIED
- **VLAN Interfaces (SVIs)**:
  - **VLAN 1**:
    - Status: Shutdown ✓ VERIFIED
  - **VLAN 99**:
    - Description: Management ✓ VERIFIED
    - IP: 10.99.0.12 255.255.255.0 ✓ VERIFIED
    - Status: Active ✓ VERIFIED
- **VTP Configuration**: Not explicitly configured ✓ VERIFIED

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED
- **Active (no shutdown)**: 6 ✓ VERIFIED
- **Shutdown**: 20 ✓ VERIFIED
- **Access Ports**: 5 ✓ VERIFIED
- **Trunk Ports**: 1 ✓ VERIFIED
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED

### Key Active Interfaces
- **FastEthernet0/1** - Bruker-PC kontor 201 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast and BPDU Guard enabled ✓ VERIFIED
- **FastEthernet0/2** - Bruker-PC kontor 202 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast and BPDU Guard enabled ✓ VERIFIED
- **FastEthernet0/3** - Bruker-PC kontor 203 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast and BPDU Guard enabled ✓ VERIFIED
- **FastEthernet0/4** - Bruker-PC kontor 204 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast and BPDU Guard enabled ✓ VERIFIED
- **FastEthernet0/5** - Printer 2. etasje | Mode: access | VLAN: 10 | PortFast and BPDU Guard enabled ✓ VERIFIED
- **FastEthernet0/24** - Uplink til dis-sw01 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 10, 20, 50, 99 | Encapsulation: dot1q | Nonegotiate enabled ✓ VERIFIED

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED
- **Global Features**: portfast-default ✓ VERIFIED

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED
- **Dynamic ARP Inspection (DAI)**: Not enabled✓ VERIFIED
- **Port Security**: Not enabled on any interfaces ✓ VERIFIED
- **802.1X**: Not configured ✓ VERIFIED
- **IP Source Guard**: Not configured ✓ VERIFIED
- **CDP**: Enabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED

## Network Services

### Logging
- **Syslog Enabled**: Yes ✓ VERIFIED
- **Logging Server**: 10.99.0.50 ✓ VERIFIED

### NTP
- **NTP Server**: Not configured ✓ VERIFIED
- **NTP Authentication**: Not configured ✓ VERIFIED

### DNS
- **DNS Domain Name**: firma.local ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.0.1 ✓ VERIFIED

## Configuration Quality Assessment

### Device Role
- **Device Role**: ~ INFERRED
  - This device is likely an **Access Layer Switch** due to the presence of multiple access ports, voice VLANs, and no routing enabled.
  - The trunk port to a distribution switch (FastEthernet0/24) suggests it connects to a higher layer in the network.

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, which is a good practice for secure remote access. ✓ VERIFIED
- PortFast and BPDU Guard are enabled on access ports, reducing the risk of STP loops. ✓ VERIFIED
- A banner is configured for login sessions, which is a compliance best practice. ✓ VERIFIED
- Syslog is enabled and configured to send logs to a remote server (10.99.0.50), aiding in monitoring and auditing. ✓ VERIFIED

#### ⚠ Areas for Improvement
- AAA is not enabled, which means there is no centralized authentication, authorization, or accounting. This is a significant security gap. ✓ VERIFIED
- No ACL is applied to VTY lines, leaving SSH access potentially open to unauthorized users. ✓ VERIFIED
- DHCP Snooping, Dynamic ARP Inspection, and IP Source Guard are not enabled, which leaves the network vulnerable to spoofing and rogue DHCP servers. ✓ VERIFIED
- Port security is not enabled on any interfaces, which could allow unauthorized devices to connect. ✓ VERIFIED
- NTP is not configured, which may affect time-based security and logging. ✓ VERIFIED
- LLDP is not enabled, which could limit network discovery and troubleshooting capabilities. ✓ VERIFIED

#### Recommendations
- Enable AAA for centralized authentication and authorization.
- Apply an ACL to VTY lines to restrict SSH access to trusted IP addresses.
- Enable DHCP Snooping and configure trusted ports to prevent rogue DHCP servers.
- Enable Dynamic ARP Inspection to prevent ARP spoofing.
- Enable IP Source Guard to prevent IP spoofing.
- Enable port security on access ports to limit the number of devices per port.
- Configure NTP to synchronize the device clock with a trusted time source.
- Enable LLDP for network discovery and interoperability with other vendors' equipment.
- Consider enabling 802.1X for port-based authentication to enhance access control.

## Summary

This device, **switch-02**, is an **Access Layer Switch** in a typical three-tier network architecture. It provides connectivity to end-user devices and connects to a distribution switch via a trunk port. The configuration includes basic security features such as SSH and PortFast, but lacks advanced security mechanisms like AAA, DHCP Snooping, and port security. The device is configured to log to a remote syslog server, which is a good practice for monitoring. Overall, the configuration is functional but requires several improvements to meet enterprise security standards.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T08:09:08.016172