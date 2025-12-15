## Switch Configuration Documentation: 15-commands-10-features.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: This switch is likely used as a management or access switch based on the configuration, possibly providing connectivity to PCs and other devices within a VLAN.
- **Last Modified**: Not explicitly stated in the configuration file. However, it can be inferred that this configuration was generated recently due to the presence of modern features like SSHv2 and DHCP Snooping.
- **Domain Name**: krister.local

## Device Information
- **Model**: Unknown (not specified in the configuration)
- **System Image**: Not provided
- **Serial Number**: Not available
- **Hardware Details**: The switch is equipped with Gigabit Ethernet interfaces, FastEthernet interfaces, and a CPU.

## Management & Access

### Management Interfaces
- Management VLAN: Vlan90 is configured as the management VLAN.
- IP Addressing: 10.90.0.11/24 is assigned to interface Vlan90.
- Default Gateway: 10.90.0.254 is set as the default gateway for the switch.
- Management Protocols:
  - SSHv2 is enabled and configured with a timeout of 60 seconds and 3 authentication retries.
  - TACACS+ is configured as an authentication server, but it's not clear if this is used for AAA or just for access control.

### Access Control & Security
- **Console Access**: The console line (Line Console 0) has login authentication set to "console."
- **VTY Access**: Telnet/SSH configuration:
  - Line VTY 0-4 has login authentication set to "default" and supports SSHv2.
  - Transport input is restricted to SSHv2, which is a good practice for security.
- **Enable Password**: The enable secret password is encrypted with the value "3NA8le$cret!=1."
- **AAA Configuration**: An AAA model is enabled, but no explicit AAA configuration commands are present. This indicates that default settings might be used.
- **Login Banners**: A login banner is configured to display a warning about unauthorized access.

### Management Access Lists
A management ACL named MGMT-MGMT has been created with the following rules:

| Rule # | Protocol | Source | Destination | Action |
|--------|----------|--------|-------------|--------|
| 1      | IP       | any    | 10.90.0.0/24 | permit |
| 2      | IP       | any    | 10.91.0.0/24 | permit |
| 3      | IP       | any    | any          | deny   |

## VLANs

### VLAN Database
The following table lists the configured VLANs:

| VLAN ID | Name         | Purpose/Description |
|---------|--------------|--------------------|
| 11      | Usergroup1-1 | Access layer for user traffic. |
| 12      | Usergroup1-2 | Another access layer for user traffic. |
| 90      | Admin-Mgmt-LEFT | Management VLAN used by the switch itself (e.g., management IP address). |
| 666     | native-trunk | Native VLAN for trunking between switches. |

### VLAN Interfaces (SVIs)
- **VLAN 11 Interface**: No SVI configured.
- **VLAN 12 Interface**: No SVI configured.
- **VLAN 90 Interface**:
  - IP Address: 10.90.0.11/24
  - Description: Management SVI
  - DHCP Helper: Not configured
  - HSRP/VRRP: Not configured

### VTP Configuration
The switch is in "transparent" mode, meaning it doesn't originate or respond to VTP advertisements.

## Physical Interfaces

### Interface Summary
| Interface | Description          | Mode    | VLAN/Trunk | Speed/Duplex | Status  | Special Features |
|-----------|----------------------|---------|------------|--------------|--------|------------------|
| Gi0/1     | dis-venstre-sw01 gig0/1 | trunk   | 11,12,90    | -           | up      | none              |
| Fa0/1     | PC4-Access port    | access  | 11         | -           | up      | Port Security     |
| Fa0/2     | PC5-Access port    | access  | 12         | -           | up      | Port Security     |
| Fa0/3     | Management-PC Access port  | access  | 90         | -           | up      | none              |

### Detailed Interface Configurations
#### GigabitEthernet0/1
- **Description**: dis-venstre-sw01 gig0/1
- **Mode**: Trunk
- **Configuration Details**:
  - Switchport trunk encapsulation is set to dot1q.
  - Switchport mode is set to trunk.
  - Switchport nonegotiate and switchport trunk native vlan 666 are configured.
  - IP DHCP snooping trust and IP ARP inspection trust are enabled.

#### FastEthernet0/1
- **Description**: PC4-Access port
- **Mode**: Access
- **Configuration Details**:
  - Switchport access VLAN is set to 11.
  - Port Security is enabled with the following settings: maximum 1, violation restrict, aging time 3, and sticky MAC addresses.

#### FastEthernet0/2
- **Description**: PC5-Access port
- **Mode**: Access
- **Configuration Details**:
  - Switchport access VLAN is set to 12.
  - Port Security is enabled with the same settings as Fa0/1.

#### FastEthernet0/3
- **Description**: Management-PC Access port
- **Mode**: Access
- **Configuration Details**:
  - Switchport access VLAN is set to 90.
  - No additional security features are configured.

### Unused Interfaces
There are two unused interfaces (Fa0/4-Fa0/24 and Gi0/2) in shutdown state.

## Port-Channel / EtherChannel

No port-channel or etherchannel configurations are present.

## Routing Configuration

### Routing Protocol
No routing protocols are explicitly configured. However, IP routing is disabled globally.

### Static Routes
No static routes are defined.

### Default Route
The default route (0.0.0.0/0) points to the next-hop address 10.90.0.254.

### Inter-VLAN Routing
Inter-VLAN routing is not enabled.

## Spanning Tree Protocol

### STP Configuration
- **Mode**: Rapid-PVST+ is running.
- **Root Bridge**: The root bridge for VLANs 11, 12, and 90 has a priority of 61440 (a non-standard value).

### STP Features
- **PortFast**: Enabled on Fa0/1 and Fa0/2.
- **BPDU Guard**: Not explicitly configured, but enabled by default in PVST+ mode.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
No HSRP or VRRP configurations are present. However, GLBP is not supported on this switch platform.

### Stack Configuration
This switch does not appear to be part of a stack.

## Quality of Service (QoS)

No QoS configuration is present.

## Security Features

### Port Security
Port security is enabled on Fa0/1 and Fa0/2 with the following settings: maximum 1, violation restrict, aging time 3, and sticky MAC addresses.

### DHCP Security
- **DHCP Snooping**: Enabled for VLANs 11 and 12.
- **DHCP Snooping Database**: The switch maintains a database of authorized DHCP servers for these VLANs.

### Dynamic ARP Inspection (DAI)
- Status: Disabled for all VLANs.
- Trusted interfaces: None configured.

### IP Source Guard
- Status: Not configured or enabled.

### Storm Control
- Configuration: Broadcast, multicast, and unicast thresholds are set to 1.00 on Fa0/1 and Fa0/2.

### Access Control Lists (ACLs)
An ACL named MGMT-MGMT is defined for management traffic.

### 802.1X / Network Access Control
No 802.1x or network access control configurations are present.

## Network Services

### DHCP Server/Relay
- **DHCP Server**: No DHCP server configuration is present.
- **DHCP Relay**: The switch acts as a DHCP relay for VLANs 11 and 12, with the helper address set to its own IP address (10.90.0.11).

### NTP (Network Time Protocol)
An NTP server at 10.91.0.123 is configured.

### SNMP (Simple Network Management Protocol)
- **SNMP Version**: v2c is supported.
- No community strings are explicitly configured, but it's recommended to set them for security purposes.

## Best Practices Analysis

### ✅ Good Practices Identified
- SSHv2 is enabled and configured correctly.
- Port Security is enabled on access ports with reasonable settings.
- DHCP Snooping is enabled for VLANs 11 and 12.
- BPDU Guard is implicitly enabled due to the PVST+ mode.

### ⚠️ Potential Issues or Concerns
- The root bridge priority value (61440) seems non-standard and might need adjustment.
- PortFast is enabled on access ports, which can introduce security risks if not properly configured.
- DHCP Snooping database maintenance might be required for authorized servers.

### 💡 Recommendations for Improvement
1. Adjust the root bridge priority to a standard value (e.g., 4096).
2. Review and adjust the PortFast configuration to ensure it's secure.
3. Configure community strings for SNMP access.
4. Enable DAI on VLANs where DHCP Snooping is enabled.

## Configuration Summary

- **Total VLANs**: 4
- **Total Configured Interfaces**: 7 (active interfaces)
- **Routing**: Disabled globally
- **Spanning Tree**: Rapid-PVST+ with implicit BPDU Guard
- **Key Features Enabled**: SSHv2, DHCP Snooping, Port Security, Storm Control
- **Security Posture**: The switch configuration has some good security practices in place but may benefit from further analysis and optimization.
- **Overall Assessment**: This is a basic network switch configuration that could be improved with additional security features, QoS settings, and possibly some adjustments to the STP configuration.