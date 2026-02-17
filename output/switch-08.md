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
- **Console**: line con 0 ✓ VERIFIED
- **VTY Lines**: line vty 0 4 ✓ VERIFIED
- **VTY Transport Input**: ssh, telnet ✓ VERIFIED
- **Banner**: Configured (Message: "Lab-miljoe. Ingen produksjonsdata tillatt.") ✓ VERIFIED

## AAA Configuration
- AAA: Not enabled ✓ VERIFIED

## VLANs
- **Total VLANs Referenced**: 4 ✓ VERIFIED
- **VLAN IDs and Names**:
  - VLAN 99: Management ✓ VERIFIED
  - VLAN 110: Lab-Klienter ✓ VERIFIED
  - VLAN 120: Lab-Servere ✓ VERIFIED
  - VLAN 666: Native VLAN (not named) ✓ VERIFIED
- **VLAN Interfaces (SVIs)**:
  - **VLAN 1**: Status: Shutdown ✓ VERIFIED
  - **VLAN 99**: Description: Management | IP: 10.99.1.8 255.255.255.0 | Status: Active ✓ VERIFIED
- **VTP Configuration**: Not explicitly configured ✓ VERIFIED

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED
- **Active (no shutdown)**: 11 ✓ VERIFIED
- **Shutdown**: 15 ✓ VERIFIED

**Active Interfaces**:
- **FastEthernet0/1** — Description: "Lab-PC 1" | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/2** — Description: "Lab-PC 2" | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/3** — Description: "Lab-PC 3" | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/4** — Description: "Lab-PC 4" | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/5** — Description: "Lab-PC 5" | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/6** — Description: "Lab-PC 6" | Mode: access | VLAN: 110 ✓ VERIFIED
- **FastEthernet0/7** — Description: "Lab-Server 1" | Mode: access | VLAN: 120 ✓ VERIFIED
- **FastEthernet0/8** — Description: "Lab-Server 2" | Mode: access | VLAN: 120 ✓ VERIFIED
- **FastEthernet0/9** — Description: "Lab-Server 3" | Mode: access | VLAN: 120 ✓ VERIFIED
- **FastEthernet0/10** — Description: "Lab-Server 4" | Mode: access | VLAN: 120 ✓ VERIFIED
- **FastEthernet0/24** — Description: "Uplink til dis-sw01 gig0/6" | Mode: trunk | Encapsulation: dot1q | Native VLAN: 666 | Allowed VLANs: 99, 110, 120 ✓ VERIFIED

**Shutdown Interfaces**: FastEthernet0/11, FastEthernet0/12, FastEthernet0/13, FastEthernet0/14, FastEthernet0/15, FastEthernet0/16, FastEthernet0/17, FastEthernet0/18, FastEthernet0/19, FastEthernet0/20, FastEthernet0/21, FastEthernet0/22, FastEthernet0/23, GigabitEthernet0/1, GigabitEthernet0/2 ✓ VERIFIED

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED
- **Dynamic ARP Inspection**: Not enabled ✓ VERIFIED
- **CDP**: Enabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED
- **802.1X**: Not configured ✓ VERIFIED
- **IP Source Guard**: Not configured ✓ VERIFIED
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED
- **NTP Authentication**: Disabled ✓ VERIFIED

### DNS
- **Domain Name**: lab.bedrift.no ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- Management VLAN (VLAN 99) is isolated and configured with an IP address ✓ VERIFIED
- Syslog is enabled with a remote server (10.99.0.50) ✓ VERIFIED
- NTP is configured for time synchronization ✓ VERIFIED
- PortFast is enabled on all access ports to prevent STP loops ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH is not configured** – Telnet is allowed on VTY lines, which is insecure. SSH should be enabled and Telnet disabled. ~ INFERRED
- **AAA is not enabled** – No authentication/authorization for remote access. ~ INFERRED
- **No port security** – No protection against MAC flooding or unauthorized device connections. ~ INFERRED
- **DHCP snooping and Dynamic ARP Inspection are not enabled** – Vulnerable to DHCP spoofing and ARP poisoning attacks. ~ INFERRED
- **No ACLs on VTY lines** – No access control for remote management. ~ INFERRED
- **Native VLAN 666 is not named** – Poor documentation and potential security risk. ~ INFERRED

#### Recommendations
1. **Enable SSH and disable Telnet** – Configure SSH with strong key pairs and disable Telnet on VTY lines. ~ INFERRED
2. **Implement AAA** – Configure local or remote authentication for console and VTY access. ~ INFERRED
3. **Enable port security** – Limit MAC addresses on access ports to prevent unauthorized access. ~ INFERRED
4. **Enable DHCP snooping and Dynamic ARP Inspection** – Protect against DHCP and ARP spoofing attacks. ~ INFERRED
5. **Configure ACLs for VTY access** – Restrict remote management to trusted IP addresses. ~ INFERRED
6. **Name native VLAN 666** – Improve documentation and reduce security risks. ~ INFERRED

## Summary

lab-sw01 is an **Access Layer Switch** ✓ INFERRED, providing connectivity for lab clients and servers in VLANs 110 and 120. It has a basic configuration with minimal security features, making it vulnerable to common network attacks. The configuration quality is **moderate**, with essential services like NTP and syslog enabled, but critical security features are missing. Immediate improvements are recommended to harden the device's security posture. ~ INFERRED

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-17T19:57:24.655020