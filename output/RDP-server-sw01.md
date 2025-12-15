# Switch Configuration Documentation: RDP-server-sw01.txt

## Overview
- **Hostname**: RDP-server-sw01
- **IOS Version**: 12.2(37)SE1
- **Configuration Purpose**: The switch is likely configured as a managed switch providing access control, security features, and network services to the attached devices.
- **Last Modified**: Not specified in the configuration file
- **Domain Name**: krister.local

## Device Information
- **Model**: Not explicitly mentioned in the configuration file. However, based on the interfaces listed (e.g., FastEthernet0/1, GigabitEthernet0/1), it's likely a Cisco Catalyst switch.
- **System Image**: The system image is version 12.2(37)SE1.
- **Serial Number**: Not specified in the configuration file
- **Hardware Details**: Based on the interfaces and features enabled (e.g., Spanning Tree Protocol, VLANs), the hardware details are consistent with a Cisco Catalyst switch.

## Management & Access

### Management Interfaces
Document all management-related interface configurations:

* The switch has an IP address of 10.91.0.15/24 assigned to VLAN 91.
* The default gateway is set to 10.91.0.254.
* Management protocols enabled: SSH (version 2), DHCP snooping, and ARP inspection.

### Access Control & Security

- **Console Access**: Configuration of console line: `login authentication console`
- **VTY Access**: Telnet/SSH configuration:
	+ Line configuration: `line vty 0 4 access-class MGMT-MGMT in`
	+ Access class restrictions: Applied ACL MGMT-MGMT
	+ Transport protocols allowed: SSH (version 2)
- **Enable Password**: Status and encryption level: The enable password is encrypted with a hash (`5 $1$mERr$Lwr5BSUyZULbT8G7d2fD90`).
- **AAA Configuration**: Authentication, Authorization, Accounting setup:
	+ `aaa new-model`
	+ `aaa authentication login console local`
	+ `aaa authentication login default group tacacs+ local`
	+ `aaa authorization exec default group tacacs+ local`
	+ `aaa accounting exec default start-stop group tacacs+`

### Login Banners

- **Login Banner**: The switch has a configured banner: `banner login ^CUnauthorized access prohibited.^C`

## VLANs

### VLAN Database
| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 1       | Vlan1 | Management VLAN     |
| 21      | server2_vlan | Server 2's VLAN    |
| 22      | server1_vlan | Server 1's VLAN    |
| 91      | Management SVI | Management VLAN   |

### VLAN Interfaces (SVIs)

* **VLAN 1 Interface**: `interface Vlan1 no ip address shutdown`
* **VLAN 21 Interface**:
	+ IP Address: Not explicitly set
	+ Description: server2_vlan
	+ DHCP Helper: Not configured
	+ HSRP/VRRP: Not configured
* **VLAN 22 Interface**:
	+ IP Address: Not explicitly set
	+ Description: server1_vlan
	+ DHCP Helper: Not configured
	+ HSRP/VRRP: Not configured
* **VLAN 91 Interface**: `interface Vlan91 ip address 10.91.0.15 255.255.255.0 mac-address 0001.43cb.9e01`

### VTP Configuration

- VTP Mode: Server (configured with `vtp domain` command, but the exact mode isn't specified)
- VTP Domain: Not explicitly mentioned in the configuration
- VTP Version: Not specified
- Analysis: The switch is configured to run VTP on VLAN 1. This allows for dynamic VLAN creation and deletion.

## Physical Interfaces

### Interface Summary
| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| FastEthernet0/1 | server2 | Access | 21        | Not specified | Up    | Port-security, Spanning-Tree, Storm-Control |
| FastEthernet0/2 | server1 | Access | 22        | Not specified | Up    | Port-security, Spanning-Tree, Storm-Control |
| FastEthernet0/3 | Admin-TACACS | Access | 91       | Not specified | Up    | Port-security, Spanning-Tree, Storm-Control |
| FastEthernet0/4 | Admin-NTP | Access | 91      | Not specified | Up   | Port-security, Spanning-Tree, Storm-Control |

### Detailed Interface Configurations

#### FastEthernet0/1
- **Description**: server2
- **Mode**: Access
- **Configuration Details**:
	+ `switchport access vlan 21`
	+ `switchport mode access`
	+ `switchport port-security`
	+ `switchport port-security mac-address sticky 00D0.97B5.5228`
	+ `switchport port-security aging time 3`

#### FastEthernet0/2
- **Description**: server1
- **Mode**: Access
- **Configuration Details**:
	+ `switchport access vlan 22`
	+ `switchport mode access`
	+ `switchport port-security`
	+ `switchport port-security mac-address sticky 0050.0F08.AD98`
	+ `switchport port-security aging time 3`

#### FastEthernet0/3
- **Description**: Admin-TACACS
- **Mode**: Access
- **Configuration Details**:
	+ `switchport access vlan 91`
	+ `switchport mode access`
	+ `switchport port-security`
	+ `switchport port-security mac-address sticky 0005.5E86.CE22`
	+ `switchport port-security aging time 3`

#### FastEthernet0/4
- **Description**: Admin-NTP
- **Mode**: Access
- **Configuration Details**:
	+ `switchport access vlan 91`
	+ `switchport mode access`
	+ `switchport port-security`
	+ `switchport port-security mac-address sticky 0030.F242.21A6`
	+ `switchport port-security aging time 3`

## Port-Channel / EtherChannel
There is no configuration for a Port-Channel or EtherChannel.

## Routing Configuration

### Routing Protocol
No routing protocol is configured on this switch.

### Static Routes
None are explicitly listed in the configuration.

### Default Route
None is explicitly set in the configuration.

### Inter-VLAN Routing
Not explicitly enabled.

## Spanning Tree Protocol

### STP Configuration
- **Mode**: PVST+ (configured with `spanning-tree mode pvst`)
- **Root Bridge**: Not specified, but PVST+ runs per-VLAN instance.
- **Priority**: The priority is set to 28672 for VLANs 21 and 22.

### STP Features

* **PortFast**: Enabled on access ports (`spanning-tree portfast`).
* **BPDU Guard**: Enabled on access ports (`spanning-tree bpduguard enable`).

## High Availability & Redundancy
No FHRP (Hot Standby Router Protocol) configuration is found in the given configuration.

## Quality of Service (QoS)
There's no QoS configuration in the provided switch configuration file.

## Security Features

### Port Security
- **Interfaces with port security enabled**: FastEthernet0/1, FastEthernet0/2, FastEthernet0/3, and FastEthernet0/4.
- **Maximum MAC addresses allowed**: 3 per interface.
- **Violation actions configured**: `switchport port-security violation restrict`.
- **Static MAC addresses (if configured)**: Each of these interfaces has a statically configured MAC address.

### DHCP Security
* **DHCP Snooping**: Enabled (`ip dhcp snooping`).
* **Trusted ports**: Not explicitly listed.

### Dynamic ARP Inspection (DAI)
- **Status**: Disabled.
- **Trusted interfaces**: None are specified in the configuration.

### IP Source Guard
Not configured.

### Storm Control
- **Configuration**: `storm-control broadcast level 1`.
- **Interfaces configured**: FastEthernet0/1, FastEthernet0/2, FastEthernet0/3, and FastEthernet0/4.

## Network Services

### DHCP Server/Relay
* **DHCP Server**: Not explicitly configured as a DHCP server.
* **DHCP Relay**: Helper addresses are not listed in the configuration.

### NTP (Network Time Protocol)
- **NTP Server(s)**: 10.91.0.123 (`ntp server 10.91.0.123 key 15`).
- **NTP Authentication**: `ntp authentication-key` is configured with an MD5 key.
- **Timezone**: Not explicitly set.

## CDP/LLDP
* **CDP**: Disabled globally (`no cdp run`) and per-interface (not applicable, as the interface configuration doesn't show any CDP-related commands).
* **LLDP**: The switch has `lldp` enabled globally, but no specific LLDP related configurations are found in this switch config.

## Best Practices Analysis

Based on the provided configuration:

### Good Practices Identified
- Port-security is enabled on all interfaces.
- Spanning Tree Protocol (PVST+) is running with a priority set for VLANs 21 and 22.
- DHCP snooping is enabled globally, which helps prevent attacks using spoofed MAC addresses.

### Potential Issues or Concerns
- There are no security concerns explicitly mentioned in the configuration.
- The switch uses the default VLAN 1 for management. It's recommended to use a separate VLAN for management access.
- No FHRP (HSRP/VRRP/GLBP) is configured, which might make the network more susceptible to single-point-of-failure issues.

### Recommendations for Improvement
1. Consider implementing FHRP (HSRP/VRRP/GLBP) for high availability and redundancy in the network.
2. Plan a separate VLAN for management access instead of using VLAN 1.
3. Regularly review and update the configuration to ensure that it remains aligned with security best practices.

## Configuration Summary

- **Total VLANs**: 4
- **Total Configured Interfaces**: 12 (active interfaces)
- **Routing**: Disabled
- **Spanning Tree**: PVST+ with a priority set for VLANs 21 and 22
- **Key Features Enabled**:
	+ Port-security on all active interfaces
	+ DHCP snooping globally
	+ Storm control configured on all active interfaces
- **Security Posture**: Generally secure, but consider implementing FHRP and planning separate management VLAN.
- **Overall Assessment**: The configuration appears to be well-maintained with some security best practices implemented. However, additional recommendations have been suggested for improvement.

## Appendix

### Uncommon or Complex Configurations
This section is intentionally left blank as the given switch configuration doesn't contain any unusual or highly complex configurations that need additional explanation beyond what's already provided in this document.

### Configuration Snippets
None are included here, but relevant configuration snippets would be added if necessary to explain complex sections of the configuration.