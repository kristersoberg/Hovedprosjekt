# Network Device Documentation: aksess-sw01

## Device Information
- Hostname: aksess-sw01 ✓
- IOS Version: 12.2(37)SE1 ✓
- Domain Name: krister.local ✓
- Config Register: Not shown (Not configured)

## Management & Access
- Management VLAN: 90 ✓
- IP Address: 10.90.0.11 ✓
- Subnet Mask: 255.255.255.0 ✓
- Default Gateway: 10.90.0.254 ✓
- SSH Version: 2 ✓
- SSH Timeout: 60 seconds ✓

## AAA Configuration
- AAA is enabled ✓
- Authentication Lists:
  - aaa authentication login console local ✓
  - aaa authentication login default group tacacs+ local ✓
- Authorization Lists:
  - aaa authorization exec default group tacacs+ local ✓
- Accounting:
  - aaa accounting exec default start-stop group tacacs+ ✓

## VLANs
- Total VLANs Referenced: 4 ✓
- VLAN IDs: 11, 12, 90, 666 ✓
- VLAN Interfaces (SVIs): 2 configured
  - **VLAN 1**: Shutdown ✓
  - **VLAN 90**: Description "Management SVI", IP: 10.90.0.11 255.255.255.0, Status: Active, ACL In: MGMT-MGMT

## Physical Interfaces
- Total Interfaces: 26 ✓
- Active (no shutdown): 4 ✓
- Shutdown: 22 ✓
- Access Ports: 3 ✓
- Trunk Ports: 1 ✓
- Port Security Enabled: 3 interfaces ✓
- **FastEthernet0/1**: PC4-Access port, Mode: access, VLAN: 11, Port-Sec: ✓
- **FastEthernet0/2**: PC5-Access port, Mode: access, VLAN: 12, Port-Sec: ✓
- **FastEthernet0/3**: Management-PC Access port, Mode: access, VLAN: 90, Port-Sec: ✓

## Spanning Tree Protocol
- STP Mode: pvst ✓
- Per-VLAN Priorities:
  - VLAN 11: 28672 ✓
  - VLAN 12: 28672 ✓
  - VLAN 90: 28672 ✓

## Security Features
- DHCP Snooping: Enabled on VLANs 11, 12 (✓)
- Dynamic ARP Inspection: Enabled on VLANs 11, 12 (✓)
- Access Control Lists: 1 configured
  - Standard ACL 'MGMT-MGMT': 3 entries
- CDP: Disabled (✓)

## Network Services
- Syslog: Enabled (✓)
  - Servers: 10.91.0.10
- DNS Domain Name: krister.local (✓)
- DNS Lookup: Disabled

## Routing Configuration
- IP Routing: Disabled (✓)
- Default Gateway: 10.90.0.254 (✓)

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only access for management
- DHCP snooping enabled on VLANs 11, 12
- Port security enabled on multiple interfaces
- Syslog server configured

#### ⚠ Areas for Improvement
- No routing protocols configured (IP Routing is disabled)
- No IP source guard or DAI configured
- No 802.1X authentication configured
- CDP is disabled (may be a security risk in some environments)

#### Recommendations
- Enable IP routing and configure a routing protocol (e.g., OSPF, EIGRP) for inter-VLAN routing.
- Configure IP source guard on VLANs with DHCP snooping enabled to prevent MAC spoofing attacks.
- Consider enabling 802.1X authentication for switch ports.
- Review CDP configuration to ensure it aligns with organizational security policies.

## Summary
The aksess-sw01 device appears to be a distribution layer switch, given its configuration and features. It has multiple VLANs configured, including VLANs 11, 12, and 90, which are used for access ports, trunk ports, and management purposes, respectively. The device also has DHCP snooping enabled on VLANs 11 and 12, port security enabled on multiple interfaces, and a syslog server configured.

---

**Data Source**: Structured configuration analysis
**Generated**: 2026-01-07T15:00:10.751007