# Network Device Documentation: aksess-sw01

## Device Information
- Hostname: aksess-sw01 ✓ VERIFIED
- IOS Version: 12.2(37)SE1 ✓ VERIFIED
- Domain Name: krister.local ✓ VERIFIED
- Config Register: Not shown (Not configured)

## Management & Access
- Management IP Address: 10.90.0.11 ✓ VERIFIED
- Default Gateway: 10.90.0.254 ✓ VERIFIED
- SSH Version: 2 ✓ VERIFIED
- SSH Timeout: 60 seconds ✓ VERIFIED
- VTY Settings:
  - Lines: line vty 0 4 ✓ VERIFIED
  - Transport Input: ssh ✓ VERIFIED
  - Authentication: default ✓ VERIFIED

## AAA Configuration
- AAA is enabled ✓ VERIFIED
- Authentication Lists:
  - aaa authentication login console local ✓ VERIFIED
  - aaa authentication login default group tacacs+ local ✓ VERIFIED
- Authorization Lists:
  - aaa authorization exec default group tacacs+ local ✓ VERIFIED
- Accounting:
  - aaa accounting exec default start-stop group tacacs+ ✓ VERIFIED
- TACACS+ Servers: 10.91.0.10 ✓ VERIFIED
- Local Users:
  - emergency-admin (privilege 15) ✓ VERIFIED

## VLANs
- Total VLANs Referenced: 4 ✓ VERIFIED
- VLAN IDs: 11, 12, 90, 666 ✓ VERIFIED
- VLAN Interfaces (SVIs): 2 configured
  - **VLAN 1**
    - Status: Shutdown ✓ VERIFIED
  - **VLAN 90**
    - Description: Management SVI ✓ VERIFIED
    - IP Address: 10.90.0.11 255.255.255.0 ✓ VERIFIED
    - Status: Active ✓ VERIFIED
    - ACL In: MGMT-MGMT (in) ✓ VERIFIED

## Physical Interfaces
- Total Interfaces: 26 ✓ VERIFIED
- Active (no shutdown): 4
- Shutdown: 22
- Access Ports: 3
- Trunk Ports: 1
- Port Security Enabled: 3 interfaces
- Key Active Interfaces:
  - **FastEthernet0/1**
    - Description: PC4-Access port ✓ VERIFIED
    - Mode: access ✓ VERIFIED
    - VLAN: 11 ✓ VERIFIED
    - Port-Sec: ✓ VERIFIED (switchport port-security)
  - **FastEthernet0/2**
    - Description: PC5-Access port ✓ VERIFIED
    - Mode: access ✓ VERIFIED
    - VLAN: 12 ✓ VERIFIED
    - Port-Sec: ✓ VERIFIED (switchport port-security)
  - **FastEthernet0/3**
    - Description: Management-PC Access port ✓ VERIFIED
    - Mode: access ✓ VERIFIED
    - VLAN: 90 ✓ VERIFIED
    - Port-Sec: ✓ VERIFIED (switchport port-security)

## Spanning Tree Protocol
- STP Mode: pvst ✓ VERIFIED
- Per-VLAN Priorities:
  - VLAN 11: 28672 ✓ VERIFIED
  - VLAN 12: 28672 ✓ VERIFIED
  - VLAN 90: 28672 ✓ VERIFIED

## Security Features
- DHCP Snooping: Enabled on VLANs 11, 12
  - Information Option: Disabled
- Dynamic ARP Inspection: Enabled on VLANs 11, 12
- Access Control Lists:
  - Standard ACL 'MGMT-MGMT': 3 entries
- CDP: Disabled ✓ VERIFIED

## Network Services
- Syslog: Enabled
  - Servers: 10.91.0.10
- NTP: Not configured
- SNMP: Not configured
- DNS Domain Name: krister.local
- DNS Lookup: Disabled

## Routing Configuration
- IP Routing: Disabled
- Default Gateway: 10.90.0.254

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only access for management
- DHCP snooping enabled on VLANs 11, 12
- Port security enabled on interfaces
- CDP is disabled

#### ⚠ Areas for Improvement
- Missing features: NTP, SNMP, IP Source Guard
- No routing protocols configured (IP Routing is disabled)

#### Recommendations
- Configure NTP and SNMP services
- Enable IP Source Guard on VLANs 11, 12
- Consider enabling routing protocols for inter-VLAN communication

## Summary
The aksess-sw01 device appears to be a distribution layer switch with multiple access ports, port security enabled, and DHCP snooping configured. However, it lacks NTP and SNMP services, and IP Source Guard is not enabled on VLANs 11, 12.

---

**Data Source**: Structured configuration analysis
**Generated**: 2026-01-07T21:35:06.234938