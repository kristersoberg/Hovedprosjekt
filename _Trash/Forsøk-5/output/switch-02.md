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
- **Console Logging Synchronous**: Enabled ✓ VERIFIED  

---

## AAA Configuration
- **AAA**: Not enabled ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED  
- **VLAN IDs**: 10, 20, 50, 99, 666 ✓ VERIFIED  
- **VLAN Interfaces (SVIs)**:  
  - **VLAN 1**: Status: Shutdown ✓ VERIFIED  
  - **VLAN 99**:  
    - Description: Management ✓ VERIFIED  
    - IP: 10.99.0.12 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  
- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED  
- **Active (no shutdown)**: 6 ✓ VERIFIED  
- **Shutdown**: 20 ✓ VERIFIED  
- **Access Ports**: 5 ✓ VERIFIED  
- **Trunk Ports**: 1 ✓ VERIFIED  
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED  

**Key Active Interfaces**:  
- **FastEthernet0/1** - Bruker-PC kontor 201 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast + BPDU Guard enabled  
- **FastEthernet0/2** - Bruker-PC kontor 202 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast + BPDU Guard enabled  
- **FastEthernet0/3** - Bruker-PC kontor 203 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast + BPDU Guard enabled  
- **FastEthernet0/4** - Bruker-PC kontor 204 | Mode: access | VLAN: 10 | Voice VLAN: 50 | PortFast + BPDU Guard enabled  
- **FastEthernet0/5** - Printer 2. etasje | Mode: access | VLAN: 10 | PortFast + BPDU Guard enabled  
- **FastEthernet0/24** - Uplink til dis-sw01 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 10,20,50,99  

---

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED  
- **Global Features**: portfast-default ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled✓ VERIFIED  
- **Port Security**: Not enabled✓ VERIFIED  
- **IP Source Guard**: Not configured✓ VERIFIED  
- **CDP**: Enabled✓ VERIFIED  
- **LLDP**: Not enabled✓ VERIFIED  
- **802.1X**: Not configured✓ VERIFIED  

---

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  

### NTP
- **NTP Server**: Not configured✓ VERIFIED  
- **NTP Authentication**: Not configured✓ VERIFIED  

### DNS
- **DNS Domain Name**: firma.local ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED  
- **Default Gateway**: 10.99.0.1 ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only access with version 2 and 60-second timeout (config lines: `ip ssh version 2`, `ip ssh time-out 60`)  
- PortFast + BPDU Guard on all access ports (config lines: `spanning-tree portfast`, `spanning-tree bpduguard enable`)  
- Syslog configured to 10.99.0.50 (config line: `logging 10.99.0.50`)  
- Password encryption enabled (config line: `service password-encryption`)  

#### ⚠ Areas for Improvement
- No AAA authentication for console/VTY access (missing `login local` or RADIUS/TACACS)  
- No ACL protecting VTY lines (missing `access-class` configuration)  
- No DHCP snooping or DAI for VLANs 10, 20, 50, 99  
- No NTP configuration for time synchronization  
- No SNMP configuration for monitoring  

#### Recommendations
1. **Enable AAA** for console/VTY access with local authentication or RADIUS/TACACS.  
2. **Apply ACLs** to VTY lines to restrict SSH access to trusted IPs.  
3. **Enable DHCP snooping** and **DAI** for VLANs 10, 20, 50, 99.  
4. **Configure NTP** to synchronize time with a trusted source.  
5. **Enable SNMP** for monitoring and management.  
6. **Consider enabling port security** on access ports to prevent MAC flooding.  

---

## Summary

This device is an **Access Layer switch** (✓ INFERRED) based on its configuration of multiple access ports, VLAN segmentation, and lack of routing. It provides connectivity for end-user devices (PCs, printers) and VoIP phones, with a trunk uplink to a distribution switch. The configuration is functional but lacks critical security features like AAA, DHCP snooping, and NTP. The device role is clear, but the security posture requires significant improvement to meet best practices.  

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T17:55:07.284969