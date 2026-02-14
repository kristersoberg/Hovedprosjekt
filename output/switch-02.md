# Network Device Documentation: switch-02

## Device Information
- **Hostname**: switch-02 ✓ VERIFIED  
- **IOS Version**: 15.0(2)SE4 ✓ VERIFIED  
- **Domain Name**: firma.local ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: 99 ✓ VERIFIED  
- **IP Address**: 10.99.0.12 ✓ VERIFIED  
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED  
- **Default Gateway**: 10.99.0.1 ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **VTY Transport Input**: ssh ✓ VERIFIED  
- **VTY Access Class**: None (⚠ No ACL protection) ✓ VERIFIED  
- **Console Authentication**: None ✓ VERIFIED  

---

## AAA Configuration
- **AAA**: Not enabled ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED  
- **VLAN IDs**: 10, 20, 50, 99, 666 ✓ VERIFIED  

**VLAN Interfaces (SVIs):**  
- **VLAN 1**:  
  - Status: Shutdown ✓ VERIFIED  
- **VLAN 99**:  
  - Description: Management ✓ VERIFIED  
  - IP: 10.99.0.12 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  

**VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED  
- **Active (no shutdown)**: 6 ✓ VERIFIED  
- **Shutdown**: 20 ✓ VERIFIED  

**Key Active Interfaces**:  
- **FastEthernet0/1** - Bruker-PC kontor 201 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast: Enabled | BPDU Guard: Enabled  
- **FastEthernet0/2** - Bruker-PC kontor 202 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast: Enabled | BPDU Guard: Enabled  
- **FastEthernet0/3** - Bruker-PC kontor 203 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast: Enabled | BPDU Guard: Enabled  
- **FastEthernet0/4** - Bruker-PC kontor 204 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast: Enabled | BPDU Guard: Enabled  
- **FastEthernet0/5** - Printer 2. etasje | Mode: access | VLAN: 10 | PortFast: Enabled | BPDU Guard: Enabled  
- **FastEthernet0/24** - Uplink til dis-sw01 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 10,20,50,99  

---

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED  
- **Global Features**: portfast-default ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled✓ VERIFIED  
- **Port Security**: 0 interfaces enabled ✓ VERIFIED  
- **CDP**: Enabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  

---

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  

### NTP
- **NTP Server**: Not configured ✓ VERIFIED  
- **NTP Authentication**: Not configured ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED  
- **Default Gateway**: 10.99.0.1 ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only access with version 2 and 60-second timeout (lines `ip ssh version 2`, `ip ssh time-out 60`)  
- PortFast and BPDU Guard enabled on access ports (lines `spanning-tree portfast`, `spanning-tree bpduguard enable`)  
- Syslog logging configured to 10.99.0.50 (line `logging 10.99.0.50`)  
- No VLAN 1 traffic (VLAN 1 is shutdown)  

#### ⚠ Areas for Improvement
- AAA authentication is not enabled (missing `aaa new-model` configuration)  
- VTY lines lack access control (no `access-class` configured)  
- DHCP Snooping, DAI, and IP Source Guard are not enabled  
- NTP is not configured  
- No password complexity requirements for enable secret  

#### Recommendations
1. **Enable AAA authentication** for console and VTY lines.  
2. **Apply ACLs to VTY lines** to restrict SSH access to trusted IPs.  
3. **Enable DHCP Snooping** on VLANs 10, 20, 50, 99.  
4. **Configure NTP** with at least one server for time synchronization.  
5. **Implement 802.1X authentication** for secure user access.  
6. **Enable port security** on access ports to prevent MAC flooding.  

---

## Summary

This device is an **Access Layer switch** (✓ INFERRED) based on its configuration of multiple access ports, VLAN assignments for end-user devices, and lack of routing capabilities. The configuration is functional but lacks critical security features like AAA, DHCP Snooping, and NTP. The device serves as a local access point for users and printers in VLAN 10, with a trunk uplink to a distribution switch.  

**Overall Configuration Quality**: Basic functionality is achieved, but security and scalability improvements are required.  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T20:16:36.571563