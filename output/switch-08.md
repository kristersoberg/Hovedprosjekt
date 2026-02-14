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
- **SSH Configuration**: Not explicitly configured ✓ VERIFIED  
- **VTY Transport Input**: ssh, telnet ✓ VERIFIED  
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
  - **VLAN 1**: Shutdown ✓ VERIFIED  
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

### Key Active Interfaces:
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
- **FastEthernet0/24** - Uplink til dis-sw01 gig0/6 | Mode: trunk | Native VLAN: 666 | Allowed VLANs: 99,110,120 ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED  
- **Port Security**: Not enabled on any interfaces ✓ VERIFIED  
- **CDP**: Enabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  

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

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- VLAN segmentation for management (VLAN 99) and user traffic (VLANs 110/120) ✓ VERIFIED  
- STP mode (PVST) configured for loop prevention ✓ VERIFIED  
- Syslog and NTP configured for auditing and time synchronization ✓ VERIFIED  
- PortFast enabled on access ports to prevent STP loops (config lines: `spanning-tree portfast` on interfaces FastEthernet0/1-10) ✓ VERIFIED  

#### ⚠ Areas for Improvement
- **SSH not configured** - VTY lines allow Telnet (insecure) ✓ VERIFIED  
- **No AAA authentication** - Console/VTY access lacks authentication ✓ VERIFIED  
- **No DHCP snooping or DAI** - Vulnerable to DHCP spoofing and ARP poisoning attacks ✓ VERIFIED  
- **No port security** - No protection against MAC flooding or unauthorized device access ✓ VERIFIED  
- **No ACLs on VTY lines** - Open Telnet/SSH access without source IP restrictions ✓ VERIFIED  

#### Recommendations
- **Enable SSH** and disable Telnet on VTY lines (e.g., `transport input ssh`) ~ INFERRED  
- **Implement AAA** for console/VTY access (e.g., `aaa authentication login default local`) ~ INFERRED  
- **Enable DHCP snooping** on VLANs 110/120 (e.g., `ip dhcp snooping vlan 110,120`) ~ INFERRED  
- **Enable port security** on access ports (e.g., `switchport port-security`) ~ INFERRED  
- **Configure ACLs** to restrict VTY access to trusted IPs (e.g., `access-class 10 in`) ~ INFERRED  

---

## Summary

lab-sw01 is an **Access Layer Switch** ✓ INFERRED, providing connectivity for lab PCs and servers in VLANs 110/120, with a dedicated management VLAN (VLAN 99). The configuration includes basic VLAN segmentation and STP, but lacks critical security features like SSH, AAA, and DHCP snooping. The device is configured for a lab environment with minimal routing requirements.  

**Overall Configuration Quality**:  
- **✓ Good**: VLAN design, STP, NTP/Syslog  
- **⚠ Needs Improvement**: Security hardening, access control, and authentication  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T18:25:25.804659