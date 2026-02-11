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
- **Port Security**: Not enabled on any interface ✓ VERIFIED
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

### Device Role Determination (~ INFERRED)
- **Device Role**: Access Layer Switch
  - Justification: The switch has many access ports (10), no routing enabled, and is likely connecting end-user devices (PCs and servers) to the network. It also has a trunk port to a distribution switch, indicating it is at the access layer.

### Security Posture

#### ✓ Strengths
- **Syslog is enabled** and configured to send logs to 10.99.0.50 ✓ VERIFIED
- **NTP is enabled** and configured to synchronize with 10.99.0.1 ✓ VERIFIED
- **PortFast is enabled** on all access ports, reducing STP convergence time ✓ VERIFIED
- **No password encryption** is disabled, which is a best practice for security (though this is a configuration choice, not a security feature) ✓ VERIFIED

#### ⚠ Areas for Improvement
- **SSH is not configured**, leaving the device vulnerable to Telnet-based attacks ✓ VERIFIED
- **VTY lines allow Telnet**, which is insecure and should be disabled ✓ VERIFIED
- **No AAA authentication** is configured, meaning there is no centralized authentication mechanism ✓ VERIFIED
- **No access control lists (ACLs)** are applied to VTY lines, allowing unrestricted remote access ✓ VERIFIED
- **No port security** is enabled, leaving the switch vulnerable to MAC flooding and unauthorized device access ✓ VERIFIED
- **DHCP Snooping and Dynamic ARP Inspection** are not enabled, leaving the network vulnerable to rogue DHCP servers and ARP spoofing ✓ VERIFIED
- **No password is set for the console**, allowing physical access without authentication ✓ VERIFIED

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines to secure remote access (~ INFERRED)
- **Implement AAA authentication** for console and VTY access to enforce centralized authentication (~ INFERRED)
- **Apply ACLs to VTY lines** to restrict remote access to trusted IP addresses (~ INFERRED)
- **Enable port security** on access ports to prevent MAC flooding and unauthorized device access (~ INFERRED)
- **Enable DHCP Snooping** and **Dynamic ARP Inspection** to protect against rogue DHCP servers and ARP spoofing (~ INFERRED)
- **Set a password for the console** to prevent unauthorized physical access (~ INFERRED)
- **Enable IP Source Guard** to prevent IP spoofing (~ INFERRED)
- **Enable 802.1X authentication** for secure user and device authentication (~ INFERRED)

## Summary
The device **lab-sw01** is an **Access Layer Switch** configured to connect end-user devices (PCs and servers) to the network. It has a trunk port to a distribution switch and is configured with VLANs 99 (Management), 110 (Lab-Klienter), and 120 (Lab-Servere). The configuration is basic and lacks several critical security features, including SSH, AAA, port security, and DHCP Snooping. The device is configured with NTP and syslog for monitoring, but overall, it requires significant hardening to meet enterprise security standards.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T01:10:04.009865