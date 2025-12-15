# Switch Configuration Documentation: 1-aksess-sw01-14.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: This configuration appears to be for a network device, possibly a Cisco switch, with various settings and features enabled.
- **Last Modified**: Not available in the provided configuration file
- **Domain Name**: krister.local

## Device Information
- **Model**: Not available in the provided configuration file
- **System Image**: Boot image information not available
- **Serial Number**: Not available in the provided configuration file
- **Hardware Details**: No specific hardware details are mentioned in the configuration.

## Management & Access

### Management Interfaces
- The management VLAN is configured as VLAN 90 with IP address 10.90.0.11/24.
- The default gateway for this switch is set to 10.90.0.254.
- SSH version 2 is enabled, and a timeout of 60 seconds has been set.

### Access Control & Security
- **Console Access**: Console access is restricted with the console line configured to authenticate locally using the "console" authentication method.
- **VTY Access**: VTY (Virtual Terminal) access is allowed for SSH connections on ports 0 through 4. The default login method for these lines is set to "default," which uses TACACS+ as a primary source and local authentication as a secondary source. Only the management VLAN has been restricted with an ACL.
- **Enable Password**: An enable secret password, encrypted with a level of 3, is configured.
- **AAA Configuration**: The switch uses AAA (Authentication, Authorization, and Accounting) for access control, with TACACS+ as a primary source and local authentication as a secondary source. Authentication occurs on the console line using a locally stored username called "emergency-admin" with privilege level 15. 
- **Login Banners**: A login banner is configured to display when users log in.

### Management Access Lists
A standard access list named MGMT-MGMT has been applied to restrict management traffic, allowing only specific IP addresses from subnets 10.90.0.0/24 and 10.91.0.0/24.

## VLANs

### VLAN Database
| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      | Usergroup1-1 | A user VLAN, possibly for a specific group or application    |
| 12      | Usergroup1-2 | Another user VLAN for another group or application   |
| 90      | Admin-Mgmt-LEFT | The management VLAN, used for administrative access and other purposes  |
| 666     | native-trunk | A special VLAN configured as the native VLAN for trunk links    |

### VLAN Interfaces (SVIs)
For each VLAN interface:

* **VLAN 11 Interface**:
	+ IP Address: Not configured
	+ Description: Usergroup1-1
	+ DHCP Helper: Not configured
	+ HSRP/VRRP: Not configured
* **VLAN 12 Interface**:
	+ IP Address: Not configured
	+ Description: Usergroup1-2
	+ DHCP Helper: Not configured
	+ HSRP/VRRP: Not configured
* **VLAN 90 Interface (Management SVI)**:
	+ IP Address: 10.90.0.11/24
	+ Description: Management SVI
	+ DHCP Helper: Not configured
	+ HSRP/VRRP: Not configured

### VTP Configuration
- The switch is not in VTP server mode, as the VTP domain is not set.
- VTP version is also not explicitly set.

## Physical Interfaces

### Interface Summary
| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| GigabitEthernet0/1 | dis-venstre-sw01 gig0/1 | Trunk | 11,12,90 | Not set | Up | Port security enabled |
| FastEthernet0/1 | PC4-Access port | Access | 11 | Not set | Up | Storm control enabled, port fast enabled, bpduguard enabled |
| FastEthernet0/2 | PC5-Access port | Access | 12 | Not set | Up | Storm control enabled, port fast enabled, bpduguard enabled |
| FastEthernet0/3 | Management-PC Access port | Access | 90 | Not set | Up | Storm control enabled, port fast enabled |

### Detailed Interface Configurations

#### GigabitEthernet0/1
* **Description**: dis-venstre-sw01 gig0/1
* **Mode**: Trunk
* **Configuration Details**:
	+ Trunk encapsulation is set to dot1q.
	+ Native VLAN 666 is configured.
	+ Port security is enabled.
	+ The switchport port-security maximum command has been set to 1.

#### FastEthernet0/1
* **Description**: PC4-Access port
* **Mode**: Access
* **Configuration Details**:
	+ This interface is configured for access mode with VLAN 11.
	+ Storm control is enabled, and the threshold level is set to 1.00% for broadcast packets.

#### FastEthernet0/2
* **Description**: PC5-Access port
* **Mode**: Access
* **Configuration Details**:
	+ This interface is configured for access mode with VLAN 12.
	+ Storm control is enabled, and the threshold level is set to 1.00% for broadcast packets.

#### FastEthernet0/3
* **Description**: Management-PC Access port
* **Mode**: Access
* **Configuration Details**:
	+ This interface is configured for access mode with VLAN 90.
	+ Storm control is enabled, and the threshold level is set to 1.00% for broadcast packets.

### Unused Interfaces
- The interfaces in the range FastEthernet0/4-24 are shutdown.
- GigabitEthernet0/2 is also shutdown.

## Port-Channel / EtherChannel

No port-channel or EtherChannel configurations have been found in this configuration.

## Routing Configuration

### Routing Protocol
No routing protocols are configured in this switch, suggesting that inter-VLAN routing might be handled by a different device (such as a router).

### Static Routes
No static routes are explicitly configured.

### Default Route
A default route is not configured.

### Inter-VLAN Routing
Inter-VLAN routing appears to be disabled on this switch.

## Spanning Tree Protocol

### STP Configuration
The switch uses PVST+ with Rapid Spanning Tree enabled. The root bridge for VLANs 11, 12, and 90 has been manually set as secondary.

### STP Features
- **PortFast**: Enabled on interfaces FastEthernet0/1, FastEthernet0/2, and FastEthernet0/3.
- **BPDU Guard**: Enabled on these access ports.
- **Root Guard**: Not explicitly configured but is enabled by default for all trunk interfaces due to the use of PVST+ with Rapid Spanning Tree.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
No HSRP or VRRP configurations have been found in this switch configuration, suggesting that these protocols might be handled by a different device (such as routers).

### Stack Configuration
This switch is not configured to be part of a stack.

## Quality of Service (QoS)

No QoS configurations are present in the provided switch configuration.

## Security Features

### Port Security
- **Port Security**: Enabled on FastEthernet0/1, FastEthernet0/2, and FastEthernet0/3.
- **Maximum MAC addresses allowed**: 1 per port.
- **Violation actions configured**: The command "switchport port-security violation restrict" has been used.

### DHCP Security
- **DHCP Snooping**: Enabled with trusted ports set to GigabitEthernet0/1 and FastEthernet0/1, FastEthernet0/2. 
- **Trusted interfaces**: These are the only trusted interfaces for this feature.
- **VLANs protected**: VLANs 11, 12.

### Dynamic ARP Inspection (DAI)
- Status: Enabled
- **Trusted interfaces**: GigabitEthernet0/1 and FastEthernet0/1, FastEthernet0/2. 
- **VLANs protected**: VLANs 11, 12

## Network Services

### DHCP Server/Relay
- No DHCP server configurations are present in this switch.
- A DHCP relay agent might be used to forward DHCP requests.

### NTP (Network Time Protocol)
An NTP configuration is present with the following settings:
- **NTP Server(s)**: 10.91.0.123.
- **NTP Authentication**: Enabled using a key of 15 and MD5 encryption with password KomplekstPassord.
- **Timezone**: Not set.

### SNMP (Simple Network Management Protocol)
The switch uses SNMP version 3, but no community strings are provided in the configuration.

### Syslog
Logging has been configured to:
- **Logging Level**: The default level is used.
- **Logging Hosts**: A remote syslog server at IP address 10.91.0.10 has been specified.
- **Logging Buffer**: The buffer size and settings have not been explicitly changed from their defaults.

### DNS Configuration
A domain name krister.local has been set, but no DNS servers are configured in the provided switch configuration.

## Best Practices Analysis

Based on this analysis, here's an evaluation of the configuration against Cisco best practices:

- **Good Practices Identified**:
  - Port security is enabled and restricted to one MAC address per port.
  - Storm control is implemented with a threshold level set for broadcast packets.
  - BPDU guard has been configured on access ports.
  - The switch uses PVST+ with Rapid Spanning Tree, which provides fast convergence in case of a link failure.

- **Potential Issues or Concerns**:
  - There are no HSRP or VRRP configurations to ensure high availability and redundancy for Layer 3 protocols like IP routing.
  - No QoS policies have been implemented to manage traffic flows and prioritize critical applications.
  - Although DHCP snooping is enabled, it only protects VLANs 11 and 12. Other VLANs might not be protected against rogue devices or MAC spoofing attacks.

- **Recommendations for Improvement**:
  1. Implement HSRP or VRRP to ensure high availability and redundancy for Layer 3 protocols like IP routing.
  2. Configure QoS policies to manage traffic flows, prioritize critical applications, and prevent bandwidth congestion.
  3. Extend DHCP snooping protection to all VLANs on the switch.

## Configuration Summary

- **Total VLANs**: 4 (11, 12, 90, 666)
- **Total Configured Interfaces**: All interfaces except for FastEthernet0/4-24 and GigabitEthernet0/2 are active.
- **Routing**: Inter-VLAN routing is likely handled by a different device (such as routers).
- **Spanning Tree**: PVST+ with Rapid Spanning Tree is enabled, providing fast convergence in case of link failures.
- **Key Features Enabled**:
  - Port security
  - Storm control
  - BPDU guard
  - DHCP snooping
  - DAI
  - NTP configuration
  - SNMP version 3 (without community strings)
- **Security Posture**: The switch has a moderate level of security enabled, but potential vulnerabilities exist.
- **Overall Assessment**: This configuration provides a basic level of network functionality and security features. However, it lacks certain high availability mechanisms like HSRP/VRRP and QoS policies to manage traffic flows.