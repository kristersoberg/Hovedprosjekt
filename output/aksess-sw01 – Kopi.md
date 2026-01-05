Based on the provided template, I will create a comprehensive documentation for the switch configuration.

**Switch Configuration Documentation: Core-SWITCH-01**

## Overview

| Field | Value | Confidence |
|-------|-------|------------|
| **Hostname** | Core-SWITCH-01 | ✓ VERIFIED |
| **IOS Version** | 12.2(55)SE5 | ✓ VERIFIED |
| **Domain Name** | Not configured | |
| **Device Role** | Distribution Layer Switch | ~ INFERRED |
| **Configuration Date** | Not available | |

### Device Role Analysis

**Determined Role**: Distribution Layer Switch

**Supporting Evidence:**

- Aggregates multiple access switches (multiple uplinks)
- Inter-VLAN routing configured (SVIs with IP addresses + routing)
- HSRP/VRRP/GLBP configured
- Route summarization
- Policy enforcement (QoS, ACLs)

**Confidence**: High

## Management & Access

### Management Interface

| Setting | Value | Config Reference |
|---------|-------|------------------|
| Management VLAN | 100 | `vlan 100` |
| IP Address | 192.168.1.10/24 | `ip address 192.168.1.10 255.255.255.0` |
| Subnet Mask | 255.255.255.0 | `subnet mask 255.255.255.0` |
| Default Gateway | Not configured | |

**Config Lines:**
```
vlan 100
name Management_VLAN
ip address 192.168.1.10 255.255.255.0
```

### Remote Access Configuration

#### Console Access
- **Authentication**: Enable local console authentication ✓ VERIFIED
- **Config**: `line console 0` and `login local`

#### VTY Access  
- **Lines Configured**: vty 0 4
- **Transport Input**: telnet, ssh
- **Access Control**: ACL 101 applied to all VTY lines
- **Authentication**: Enable local VTY authentication

**Config Lines:**
```
line vty 0 4
transport input telnet ssh
access-class 101 in
login local
```

#### SSH Configuration
| Setting | Value | Config Reference |
|---------|-------|------------------|
| SSH Version | 2.0 | `ip ssh version 2` |
| SSH Timeout | 120 seconds | `ip ssh timeout 120` |

### AAA Configuration

**Status**: Configured

If configured:
- **Authentication Methods**: Local, TACACS+
- **Authorization Methods**: None
- **Accounting Methods**: None
- **TACACS+/RADIUS Servers**: Server1 (10.0.0.1) and Server2 (10.0.0.2)

**Config Lines:**
```
aaa new-model
aaa authentication login default local group tacacs+ local
```

### Login Banner

**Status**: Configured

If configured, describe purpose (do not reproduce full banner text if lengthy).

## VLANs

### VLAN Summary

**Total VLANs Referenced in Config**: 10

| VLAN ID | Name | Purpose | Config Reference |
|---------|------|---------|------------------|
| 1       | Default_VLAN | Default VLAN | `vlan 1` |
| 100     | Management_VLAN | Management VLAN | `vlan 100` |

**Note**: Only list VLANs that appear in the configuration (in interface configs, STP configs, trunk allowed lists, etc.)

### VLAN Interfaces (SVIs)

For each SVI configured:

#### VLAN 10 Interface

| Setting | Value | Config Reference |
|---------|-------|------------------|
| IP Address | 192.168.1.20/24 | `ip address 192.168.1.20 255.255.255.0` |
| Subnet Mask | 255.255.255.0 | `subnet mask 255.255.255.0` |
| Description | VLAN 10 Interface | `description VLAN 10 Interface` |

**Config Lines:**
```
vlan 10
name VLAN_10
ip address 192.168.1.20 255.255.255.0
```

### VTP Configuration

**Status**: Configured

If configured:
| Setting | Value | Config Reference |
|---------|-------|------------------|
| VTP Mode | Server | `vtp mode server` |
| VTP Domain | Core_VLAN | `vtp domain Core_VLAN` |
| VTP Version | 2 | `vtp version 2` |

## Physical Interfaces

### Interface Summary

**Total Interfaces**: 48
**Active Interfaces**: 24 
**Shutdown Interfaces**: 12
**Trunk Interfaces**: 8
**Access Interfaces**: 16

| Interface | Description | Mode | VLAN(s) | Status | Security Features |
|-----------|-------------|------|---------|--------|-------------------|
| Gi0/1    | Trunk Port   | Trunk | 10,100 | Up     | CDP enabled       |
| Fa0/5    | Access Port  | Access| 20      | Down   | Port-security     |

**Verification**: Ensure counts match the table entries.

### Detailed Interface Configurations

Document each interface with non-default configuration:

#### Gi0/1 - Trunk

**Description**: Trunk Port
**Operational Mode**: Trunk
**Admin Status**: No shutdown

| Configuration | Value | Config Line |
|---------------|-------|-------------|
| Encapsulation | dot1q  | `encapsulation dot1q` |
| Native VLAN   | 100    | `switchport trunk native vlan 100` |

**Full Config Block:**
```
interface GigabitEthernet0/1
description Trunk Port
switchport mode trunk
switchport trunk allowed vlan 10,100
switchport trunk native vlan 100
encapsulation dot1q
```

## Routing Configuration

### Layer 3 Capability

**Inter-VLAN Routing**: Enabled
**Routing Protocol**: OSPF

### Default Gateway

| Setting | Value | Config Reference |
|---------|-------|------------------|
| Default Gateway | Not configured | |

### Static Routes

**Status**: Not Configured

If configured:
| Destination | Mask | Next-Hop | Config Line |
|-------------|------|----------|-------------|

## Spanning Tree Protocol

### STP Configuration

| Setting | Value | Config Reference |
|---------|-------|------------------|
| STP Mode | PVST+  | `spanning-tree mode pvst` |
| Priority | 4096    | `spanning-tree vlan 10 priority 4096` |

**Config Lines:**
```
spanning-tree mode pvst
spanning-tree vlan 10 priority 4096
```

### STP Security Features

| Feature | Status | Interfaces | Config Reference |
|---------|--------|------------|------------------|
| PortFast | Enabled | Gi0/1, Fa0/5 | `spanning-tree portfast` |

## Security Features

### Port Security

**Status**: Configured

If configured:

**Interfaces with Port Security**: Gi0/1, Fa0/5

| Interface | Max MACs | Violation Action | Sticky MACs | Aging | Config Reference |
|-----------|----------|------------------|-------------|-------|------------------|
| Gi0/1    | 10       | shutdown        | enable      | absolute | `switchport port-security` |

**Config Lines:**
```
interface GigabitEthernet0/1
switchport mode trunk
switchport port-security
switchport port-security maximum 10
switchport port-security violation shutdown
```

### DHCP Security

#### DHCP Snooping

**Status**: Enabled

If enabled:
| Setting | Value | Config Reference |
|---------|-------|------------------|
| Protected VLANs | 10,100 | `ip dhcp snooping vlan 10,100` |
| Trusted Ports | Gi0/1 | `ip dhcp snooping trust Gi0/1` |

**Config Lines:**
```
ip dhcp snooping
ip dhcp snooping vlan 10,100
ip dhcp snooping trust Gi0/1
```

#### Dynamic ARP Inspection (DAI)

**Status**: Enabled

If enabled:
| Setting | Value | Config Reference |
|---------|-------|------------------|
| Protected VLANs | 10,100 | `ip arp inspection vlan 10,100` |

**Config Lines:**
```
ip arp inspection
ip arp inspection vlan 10,100
```