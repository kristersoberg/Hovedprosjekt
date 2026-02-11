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
- **CDP**: Enabled✓ VERIFIED
- **LLDP**: Not enabled✓ VERIFIED
- **802.1X**: Not configured✓ VERIFIED
- **IP Source Guard**: Not configured✓ VERIFIED
- **Port Security**: Not enabled on any interface✓ VERIFIED

---

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

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- **Management VLAN is separate from user VLANs** (~ INFERRED): VLAN 99 is used for management, which is a good practice.
- **Spanning Tree Protocol (STP) is enabled in PVST mode** (~ INFERRED): This helps prevent Layer 2 loops.
- **PortFast is enabled on access ports** (~ INFERRED): This reduces STP convergence time on access ports.
- **NTP is configured** (~ INFERRED): Ensures accurate time for logs and security events.
- **Syslog is configured** (~ INFERRED): Logs are sent to a remote server for centralized monitoring.
- **Banner is configured** (~ INFERRED): The `banner motd` provides a legal notice to users.

#### ⚠ Areas for Improvement
- **SSH is not configured** (~ INFERRED): Telnet is still allowed on VTY lines, which is insecure.
- **VTY lines lack authentication** (~ INFERRED): No AAA or local authentication is configured for remote access.
- **No ACLs are applied to VTY lines** (~ INFERRED): Remote access is uncontrolled.
- **No port security is enabled** (~ INFERRED): No MAC address filtering or limiting on access ports.
- **DHCP Snooping is not enabled** (~ INFERRED): No protection against rogue DHCP servers.
- **Dynamic ARP Inspection is not enabled** (~ INFERRED): No protection against ARP spoofing.
- **802.1X is not configured** (~ INFERRED): No port-based authentication for wired devices.
- **No SNMP is configured** (~ INFERRED): No network monitoring or device discovery.

#### Recommendations
- **Enable SSH and disable Telnet** (~ INFERRED): Configure `transport input ssh` on VTY lines and remove `telnet`.
- **Implement AAA for remote access** (~ INFERRED): Use local or TACACS+/RADIUS authentication for VTY lines.
- **Apply ACLs to VTY lines** (~ INFERRED): Restrict access to trusted IP addresses.
- **Enable port security on access ports** (~ INFERRED): Limit the number of MAC addresses per port.
- **Enable DHCP Snooping and configure trusted ports** (~ INFERRED): Protect against rogue DHCP servers.
- **Enable Dynamic ARP Inspection (DAI)** (~ INFERRED): Prevent ARP spoofing attacks.
- **Enable 802.1X authentication** (~ INFERRED): Secure wired access with port-based authentication.
- **Enable SNMP for monitoring** (~ INFERRED): Configure SNMP community strings and enable traps.
- **Enable IP Source Guard** (~ INFERRED): Prevent IP spoofing on access ports.

---

## Summary

The device **lab-sw01** is an **Access Layer switch** (~ INFERRED), as evidenced by the large number of access ports and the absence of routing or aggregation features. It is configured with VLANs 99 (Management), 110 (Lab-Klienter), 120 (Lab-Servere), and 666 (Native VLAN on trunk). The switch is managed via VLAN 99 with an IP address of 10.99.1.8. It uses PVST for STP and has basic network services like NTP and syslog enabled. However, the configuration lacks several key security features such as SSH, port security, and DHCP Snooping. (~ INFERRED)

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T01:16:45.599121