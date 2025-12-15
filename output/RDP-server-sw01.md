# Switch Configuration Documentation: RDP-server-sw01.txt

## Overview
- **Hostname**: RDP-server-sw01
- **IOS Version**: 12.2(37)SE1
- **Configuration Purpose**: This switch is likely a network access layer device managing user traffic, providing trunk connections to other switches or routers, and maintaining network services such as DHCP, NTP, and DNS.
- **Last Modified**: Not specified in the configuration file
- **Domain Name**: krister.local

## Device Information
- **Model**: Not specified in the configuration file
- **System Image**: IOS Version 12.2(37)SE1
- **Serial Number**: Not available
- **Hardware Details**: Not available

## Management & Access

### Management Interfaces
Document all management-related interface configurations:
- Management VLAN: Vlan91 with IP address 10.91.0.15/24
- Default gateway configuration: ip default-gateway 10.91.0.254
- Management protocols enabled:
  * SSH version 2, time-out set to 60 seconds

### Access Control & Security
- **Console Access**: Configuration of console line, login authentication is set to "console" using local database.
- **VTY Access**: Telnet/SSH configuration, access class restrictions are applied (MGMT-MGMT), transport protocols allowed for SSH only.
- **Enable Password**: Enable secret password is set with a hash value ($1$mERr$Lwr5BSUyZULbT8G7d2fD90).
- **AAA Configuration**: Authentication, Authorization, and Accounting setup using TACACS+ protocol. 
  * AAA authentication login default group tacacs+ local
  * aaa authorization exec default group tacacs+ local
  * aaa accounting exec default start-stop group tacacs+
- **Login Banners**: Unauthorized access is prohibited (banner login ^CUnauthorized access prohibited.^C).

### Management Access Lists
Document any ACLs applied to management access.
- MGMT-MGMT: Standard IP ACL, permits traffic from networks 10.90.0.0/24 and 10.91.0.0/24.

## VLANs

### VLAN Database
| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 1       | Vlan1 | Management VLAN for switch itself, no IP address configured. |
| 11      |        | No description available. |
| 12      |        | No description available. |
| 21      |        | No description available. |
| 22      |        | No description available. |
| 91      | Management SVI | Management VLAN with IP address 10.91.0.15/24, used for switch management access. |

### VLAN Interfaces (SVIs)
- **VLAN 1 Interface**: Not configured.
- **VLAN 11 Interface**: Not configured.
- **VLAN 12 Interface**: Not configured.
- **VLAN 21 Interface**: Not configured.
- **VLAN 22 Interface**: Not configured.
- **VLAN 91 Interface**:
  * IP Address: 10.91.0.15/24
  * Description: Management SVI
  * DHCP Helper: Not configured
  * HSRP/VRRP: Not configured

### VTP Configuration
- VTP Mode: Server (configured, but no VTP domain specified).
- VTP Domain: Not configured.
- VTP Version: Not configured.
- Analysis: The switch is configured as a VTP server with no domain set, which can lead to configuration inconsistencies across the network if not managed correctly.

## Physical Interfaces

### Interface Summary
| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| FastEthernet0/1 | server2 | Access | 21         | Not specified | Up     | Port security enabled, storm control configured. |
| FastEthernet0/2 | server1 | Access | 22         | Not specified | Up     | Port security enabled, storm control configured. |
| FastEthernet0/3 | Admin-TACACS | Access | 91         | Not specified | Up     | Port security enabled, storm control configured. |
| FastEthernet0/4 | Admin-NTP | Access | 91         | Not specified | Up     | Port security enabled, storm control configured. |
| GigabitEthernet0/1 | dist-hoyre-sw01 FA0/2 | Trunk | 666 (Native VLAN) | 1000 Full-Duplex | Up     | Trust for ARP inspection and DHCP snooping enabled. |
| FastEthernet0/5 to FastEthernet0/24 | Shutdown |        |              |                | Down   | Unused interfaces |

### Detailed Interface Configurations
- **FastEthernet0/1**:
  * Description: server2
  * Mode: Access
  * Configuration Details:
    + Port security enabled with sticky MAC addresses, restrict mode on violation.
    + Storm control configured for broadcast packets.
    + Spanning tree portfast and BPDU guard enabled.
- **FastEthernet0/2**:
  * Description: server1
  * Mode: Access
  * Configuration Details:
    + Port security enabled with sticky MAC addresses, restrict mode on violation.
    + Storm control configured for broadcast packets.
    + Spanning tree portfast and BPDU guard enabled.
- **GigabitEthernet0/1**:
  * Description: dist-hoyre-sw01 FA0/2
  * Mode: Trunk
  * Configuration Details:
    + Port trunk encapsulation set to dot1q.
    + Native VLAN configured as 666, but no specific VLANs allowed or denied.
    + Storm control not configured.

### Unused Interfaces
- There are 12 unused interfaces (FastEthernet0/5 to FastEthernet0/24) in shutdown state. Their default configurations would allow for various settings such as auto-negotiation and duplex mode.

## Port-Channel / EtherChannel

No configuration available for port-channel or etherchannel.

## Routing Configuration

### Routing Protocol
No routing protocol configured (OSPF, EIGRP, RIP, BGP).

### Static Routes
None configured.

### Default Route
- Configuration: ip default-gateway 10.91.0.254
- Next-hop: 10.91.0.254

### Inter-VLAN Routing
- Status: Enabled.
- Method: Router-on-a-stick (configured with subinterfaces on trunk ports).

## Spanning Tree Protocol

### STP Configuration
- **Mode**: PVST+ (configured).
- **Root Bridge**: Not specified as the root bridge, but VLAN 91 is likely to be configured for management traffic.
- **Priority**: Root priority set to 28672.

### STP Features
- **PortFast**: Enabled on FastEthernet0/1 to FastEthernet0/4 interfaces.
- **BPDU Guard**: Enabled on all access ports (FastEthernet0/1 to FastEthernet0/4).
- **Root Guard**: Not configured.
- **Loop Guard**: Not configured.

### Per-VLAN STP Status
Not applicable since PVST+ is used in this configuration.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
No high availability features such as HSRP, VRRP or GLBP are configured on the interfaces.

### Stack Configuration
This switch does not appear to be part of a stack.

### Redundant Links
- No redundant link configurations specified in this configuration file.

## Quality of Service (QoS)

No QoS configuration available.

## Security Features

### Port Security
Port security is enabled on all access ports with maximum MAC addresses set to 3. Sticky MAC addresses are configured for each port, and restrict mode is applied on port security violations.

### DHCP Security
- **DHCP Snooping**: Enabled on VLANs 11 and 12.
- **DHCP Snooping Database**: Not explicitly configured.

### Dynamic ARP Inspection (DAI)
- Status: Disabled.
- Trusted interfaces: None.
- VLANs protected: None.

### IP Source Guard
Not configured or applicable in this context.

### Storm Control
Storm control is configured on all access ports for broadcast packets.

### Access Control Lists (ACLs)
MGMT-MGMT ACL has been applied to VTY lines for management traffic filtering. 

## Network Services

### DHCP Server/Relay
- **DHCP Server**: Not configured as a server.
- **DHCP Relay**: No helper addresses are specified.

### NTP (Network Time Protocol)
NTP is enabled with one server IP address (10.91.0.123) and authentication key 15.

### SNMP (Simple Network Management Protocol)
SNMP version v2c is not configured.

### Syslog
Logging level for console messages set to "default" and logging host set to 10.91.0.10.

### DNS Configuration
DNS servers are specified with IP addresses 10.90.0.20, 10.90.0.30, but no domain name is provided.

## Best Practices Analysis

- **Good Practices Identified**:
  * Port security and storm control enabled on access ports for network stability.
  * SSH version 2 configured with a reasonable timeout of 60 seconds for better security.
  * HSRP or VRRP could be used to enhance network redundancy.
- **Potential Issues or Concerns**:
  * The switch is not part of any stack, which could be an issue if high availability is required.
  * No redundant links are specified in the configuration file. 
  * No QoS configuration is available, which may lead to poor performance during heavy traffic periods.

## Configuration Summary

- **Total VLANs**: 6
- **Total Configured Interfaces**: 4 active interfaces (access ports).
- **Routing**: Enabled with inter-VLAN routing.
- **Spanning Tree**: PVST+ configured as the STP mode.
- **Key Features Enabled**:
  * Port security and storm control on access ports
  * SSH version 2 for secure management
  * Inter-VLAN routing using router-on-a-stick method
- **Security Posture**: The switch has a moderate to high security posture due to port security, storm control, and SSH configuration.
- **Overall Assessment**:
The overall configuration appears well-maintained with standard features such as port security, storm control, and SSH configured. However, it lacks some advanced features like QoS, HSRP or VRRP for redundancy, which could be considered for a more robust network architecture.