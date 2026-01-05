# Network Device Documentation: aksess-sw01

## Device Information

The device, aksess-sw01, is running IOS version 12.2(37)SE1.

### Hostname and Domain Name

✓ VERIFIED - The hostname of the device is aksess-sw01.
✓ VERIFIED - The domain name of the device is krister.local.

## Management & Access

The management configuration for aksess-sw01 includes:

- **Management VLAN:** 90
- **IP Address:** 10.90.0.11
- **Subnet Mask:** 255.255.255.0
- **Default Gateway:** 10.90.0.254

### SSH Configuration

✓ VERIFIED - The device supports SSH version 2.
✓ VERIFIED - The SSH timeout is set to 60 seconds.

### Console Access

✓ VERIFIED - Console access is enabled on line con 0.
✓ VERIFIED - Authentication for console access is set to "console".
✓ VERIFIED - Logging synchronous is enabled.

### VTY Access

✓ VERIFIED - VTY access is configured on lines vty 0-4.
✓ VERIFIED - The transport input for VTY access is set to SSH.
✓ VERIFIED - Authentication for VTY access is set to "default".
✓ VERIFIED - An access class of MGMT-MGMT (in) is applied.

## AAA Configuration

AAA is enabled on aksess-sw01. The following authentication lists are configured:

- **Console Authentication:** aaa authentication login console local
- **Default Authentication:** aaa authentication login default group tacacs+ local

The following authorization list is configured:

- **Exec Authorization:** aaa authorization exec default group tacacs+ local

Accounting is enabled, and the following accounting list is configured:

- **Exec Accounting:** aaa accounting exec default start-stop group tacacs+

## VLAN Configuration

There are 4 VLANs referenced in the configuration.

### VLAN IDs

✓ VERIFIED - The VLAN IDs are: 11, 12, 90, 666

### VLAN Interfaces (SVIs)

Two SVIs are configured:

- **VLAN 1:** Shutdown
- **VLAN 90:** Description "Management SVI", IP address 10.90.0.11/24, Status Active, ACL In: MGMT-MGMT

## Physical Interfaces

There are a total of 26 interfaces on aksess-sw01.

### Interface Statistics

✓ VERIFIED - Total interfaces: 26
✓ VERIFIED - Active (no shutdown): 4
✓ VERIFIED - Shutdown: 22
✓ VERIFIED - Access Ports: 3
✓ VERIFIED - Trunk Ports: 1
✓ VERIFIED - Port Security Enabled: 3 interfaces

### Detailed Interface List

- **FastEthernet0/1:** PC4-Access port, Mode: access, VLAN: 11, Port-Sec: ✓
- **FastEthernet0/2:** PC5-Access port, Mode: access, VLAN: 12, Port-Sec: ✓
- **FastEthernet0/3:** Management-PC Access port, Mode: access, VLAN: 90, Port-Sec: ✓
- **GigabitEthernet0/1:** dis-venstre-sw01 gig0/1, Mode: trunk, Allowed VLANs: 11, 12, 90

## Spanning Tree Protocol

✓ VERIFIED - STP mode is set to pvst.
✓ VERIFIED - Per-VLAN priorities are configured:
  - VLAN 11: 28672
  - VLAN 12: 28672
  - VLAN 90: 28672

## Security Features

### DHCP Snooping

✓ VERIFIED - DHCP snooping is enabled on VLANs 11 and 12.
✓ VERIFIED - Information option is disabled.

### Dynamic ARP Inspection

✓ VERIFIED - Dynamic ARP inspection is enabled on VLANs 11 and 12.

### Access Control Lists

- **Standard ACL 'MGMT-MGMT':** 3 entries

## Network Services

### NTP

✓ VERIFIED - NTP is enabled.
✓ VERIFIED - Servers: 10.91.0.123
✓ VERIFIED - Authentication is enabled.

### Syslog

✓ VERIFIED - Syslog is enabled.
✓ VERIFIED - Servers: 10.91.0.10

## Routing Configuration

- **IP Routing:** Disabled
- **Default Gateway:** 10.90.0.254

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths

* SSH-only access is configured, which reduces the risk of unauthorized access.
* DHCP snooping and dynamic ARP inspection are enabled on VLANs 11 and 12, which helps prevent malicious activity.
* Port security is enabled on multiple interfaces, which limits the number of MAC addresses that can be learned.

#### ⚠ Areas for Improvement

* The device does not have a configured VTP domain or password, which could lead to unauthorized changes to the VLAN configuration.
* There are no ACLs configured on any interfaces except for the MGMT-MGMT ACL on VLAN 90.
* The device is not configured with a DNS server or lookup.

#### Recommendations

* Configure a VTP domain and password to prevent unauthorized changes to the VLAN configuration.
* Implement additional ACLs on all interfaces to control traffic flow.
* Configure a DNS server and enable DNS lookup to improve network services.

## Summary

The aksess-sw01 device is an access layer switch with multiple access ports, port security enabled, and no routing protocols configured. The device has a good security posture due to SSH-only access, DHCP snooping, dynamic ARP inspection, and port security. However, there are areas for improvement, including configuring VTP, implementing additional ACLs, and enabling DNS services.

---

**Data Source**: Structured configuration analysis
**Generated**: 2026-01-05T14:33:00.601466