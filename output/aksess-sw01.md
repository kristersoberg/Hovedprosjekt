# Network Device Documentation: aksess-sw01

## Device Information

The device, aksess-sw01, is running IOS version 12.2(37)SE1.

✓ Hostname: aksess-sw01
✓ IOS Version: 12.2(37)SE1
✓ Domain Name: krister.local
✓ Config Register: Not shown

## Management & Access

The management interface is configured on VLAN 90 with IP address 10.90.0.11 and subnet mask 255.255.255.0.

✓ Management VLAN: 90
✓ IP Address: 10.90.0.11
✓ Subnet Mask: 255.255.255.0
✓ Default Gateway: 10.90.0.254

SSH is enabled with version 2 and a timeout of 60 seconds.

✓ SSH Version: 2
✓ SSH Timeout: 60 seconds

Console access is configured on line con 0 with authentication set to console.

✓ Line: line con 0
✓ Authentication: console
✓ Logging Synchronous: True

VTY access is enabled on lines vty 0-4 with transport input set to ssh and authentication set to default.

✓ Lines: line vty 0 4
✓ Transport Input: ssh
✓ Authentication: default

## AAA Configuration

AAA is enabled, and the following authentication lists are configured:

✓ aaa authentication login console local
✓ aaa authentication login default group tacacs+ local

Authorization lists are also configured:

✓ aaa authorization exec default group tacacs+ local

Accounting is enabled with start-stop accounting on the default group.

✓ aaa accounting exec default start-stop group tacacs+

TACACS+ servers are configured at IP address 10.91.0.10.

✓ TACACS+ Servers: 10.91.0.10

Local users are also configured, including emergency-admin with privilege level 15.

✓ Local Users: emergency-admin (privilege 15)

## VLAN Configuration

There are a total of 4 VLANs referenced in the configuration:

✓ Total VLANs Referenced: 4
✓ VLAN IDs: 11, 12, 90, 666

Two VLAN interfaces (SVIs) are configured:

- **VLAN 1**
  - Status: Shutdown

- **VLAN 90**
  - Description: Management SVI
  - IP: 10.90.0.11 255.255.255.0
  - Status: Active
  - ACL In: MGMT-MGMT

## Physical Interfaces

There are a total of 26 interfaces on the device:

✓ Total Interfaces: 26

Only 4 interfaces are active (no shutdown):

✓ Active (no shutdown): 4

22 interfaces are in a shutdown state:

✓ Shutdown: 22

3 access ports are configured:

✓ Access Ports: 3

1 trunk port is configured:

✓ Trunk Ports: 1

Port security is enabled on 3 interfaces:

✓ Port Security Enabled: 3 interfaces

Some key interfaces include:

- **FastEthernet0/1** - PC4-Access port | Mode: access | VLAN: 11 | Port-Sec: ✓
- **FastEthernet0/2** - PC5-Access port | Mode: access | VLAN: 12 | Port-Sec: ✓
- **FastEthernet0/3** - Management-PC Access port | Mode: access | VLAN: 90 | Port-Sec: ✓
- **GigabitEthernet0/1** - dis-venstre-sw01 gig0/1 | Mode: trunk | Allowed VLANs: 11, 12, 90

## Spanning Tree Protocol

STP is enabled in PVST mode.

✓ STP Mode: pvst

Per-VLAN priorities are configured:

✓ Per-VLAN Priorities:
  - VLAN 11: 28672
  - VLAN 12: 28672
  - VLAN 90: 28672

## Security Features

DHCP snooping is enabled on VLANs 11 and 12.

✓ DHCP Snooping: Enabled on VLANs 11, 12

Dynamic ARP inspection is also enabled on VLANs 11 and 12:

✓ Dynamic ARP Inspection: Enabled on VLANs 11, 12

One standard ACL (MGMT-MGMT) is configured with 3 entries.

✓ Access Control Lists: 1 configured
✓ Standard ACL 'MGMT-MGMT': 3 entries

## Network Services

NTP is enabled with servers at IP address 10.91.0.123 and authentication enabled.

✓ NTP: Enabled
✓ Servers: 10.91.0.123
✓ Authentication: Enabled

Syslog is also enabled with servers at IP address 10.91.0.10.

✓ Syslog: Enabled
✓ Servers: 10.91.0.10

## Routing Configuration

IP routing is disabled, and the default gateway is set to 10.90.0.254.

✓ IP Routing: Disabled
✓ Default Gateway: 10.90.0.254

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths

- SSH-only access is enabled.
- DHCP snooping is configured on VLANs 11 and 12.
- Port security is enabled on multiple interfaces.

#### ⚠ Areas for Improvement

- The device has a large number of shutdown interfaces, which may indicate unnecessary configuration or potential security risks.
- Dynamic ARP inspection could be further secured by enabling it on more VLANs.
- NTP authentication should be reviewed to ensure it's properly configured.

#### Recommendations

- Review and remove any unnecessary shutdown interfaces.
- Consider enabling dynamic ARP inspection on additional VLANs.
- Verify NTP authentication is correctly configured.

## Summary

The aksess-sw01 device appears to be a managed switch with a focus on security features. It has a robust configuration for AAA, DHCP snooping, and port security. However, there are areas for improvement, including unnecessary shutdown interfaces and potential security risks. Overall, the device's configuration is well-structured and secure.

---

**Data Source**: Structured configuration analysis
**Generated**: 2026-01-05T14:28:49.897726