# Switch Configuration Documentation: 1-aksess-sw01-5.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: This switch appears to be a managed access layer device, providing network connectivity and security features for users.
- **Last Modified**: Not specified in the configuration file
- **Domain Name**: krister.local

## Device Information
- **Model**: Not explicitly stated in the configuration; however, based on the hardware description, it might be a Cisco 3750 or similar model
- **System Image**: Not specified in the configuration file
- **Serial Number**: Not specified in the configuration file
- **Hardware Details**: This switch has multiple Gigabit Ethernet ports and FastEthernet ports.

## Management & Access

### Management Interfaces
The management interface is configured with the following settings:
- **Management VLAN**: 90 (named Admin-Mgmt-LEFT)
- **IP Address**: 10.90.0.11/24
- **Default Gateway**: 10.90.0.254
- **Management Protocols**:
  - SSH version 2 enabled with a timeout of 60 seconds and authentication-retries set to 3

### Access Control & Security
- **Console Access**: The console line is configured for local authentication, with the enable secret password encrypted.
- **VTY Access**: Telnet/SSH access is enabled on lines vty 0 through 4. Authentication is performed using the default group (tacacs+ and local) for login. SSH version 2 is enabled, and access-class MGMT-MGMT (a standard ACL) restricts management access.
- **Enable Password**: The enable secret password is encrypted.
- **AAA Configuration**:
  - AAA new-model is enabled.
  - TACACS server host 10.91.0.10 with key KompleksNoekkel
  - Authentication for console and vty lines using local and tacacs+ as methods.
  - Authorization for exec sessions using group tacacs+ and local.
- **Login Banners**: The login banner displays a message stating "Unauthorized access prohibited."

### Management Access Lists
The following ACLs are applied to management access:
- `MGMT-MGMT`: A standard ACL that permits traffic from networks 10.90.0.0/24 and 10.91.0.0/24, while denying all other traffic.

## VLANs

### VLAN Database

| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      | Usergroup1-1 | Access VLAN for users |
| 12      | Usergroup1-2 | Access VLAN for users |
| 90      | Admin-Mgmt-LEFT | Management and admin VLAN |
| 666     | native-trunk | Native trunk VLAN |

### VLAN Interfaces (SVIs)

#### VLAN 11 Interface
- **VLAN ID**: 11
- **Name**: Usergroup1-1
- **IP Address**: Not configured
- **Description**: Access VLAN for users

#### VLAN 12 Interface
- **VLAN ID**: 12
- **Name**: Usergroup1-2
- **IP Address**: Not configured
- **Description**: Access VLAN for users

#### VLAN 90 Interface
- **VLAN ID**: 90
- **Name**: Admin-Mgmt-LEFT
- **IP Address**: 10.90.0.11/24
- **Description**: Management and admin VLAN

### VTP Configuration
- **Mode**: Not explicitly stated; however, it's likely in transparent mode since there are no VTP server or client configurations.
- **Domain Name**: Not configured
- **VTP Version**: Not specified

## Physical Interfaces

### Interface Summary

| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| GigabitEthernet0/1 | dis-venstre-sw01 gig0/1 | Trunk | 11,12,90 | Auto Negotiation | Up | Switchport trunk native vlan 666, switchport trunk allowed vlan 11,12,90 |
| FastEthernet0/1 | PC4-Access port | Access | 11 | Auto Negotiation | Up | Port-security enabled with maximum MAC addresses set to 1, spanning-tree portfast and bpduguard enabled |
| FastEthernet0/2 | PC5-Access port | Access | 12 | Auto Negotiation | Up | Port-security enabled with maximum MAC addresses set to 1, spanning-tree portfast and bpduguard enabled |
| FastEthernet0/3 | Management-PC Access port | Access | 90 | Auto Negotiation | Up | Port-security enabled with maximum MAC addresses set to 1 |

### Detailed Interface Configurations

#### GigabitEthernet0/1
- **Description**: dis-venstre-sw01 gig0/1
- **Mode**: Trunk
- **Configuration Details**:
  - Switchport trunk encapsulation dot1q
  - Switchport mode trunk
  - Switchport nonegotiate
  - Switchport trunk native vlan 666
  - Switchport trunk allowed vlan 11,12,90
  - Ip dhcp snooping trust and ip arp inspection trust enabled

#### FastEthernet0/1
- **Description**: PC4-Access port
- **Mode**: Access
- **Configuration Details**:
  - Port-security enabled with maximum MAC addresses set to 1
  - Spanning-tree portfast and bpduguard enabled
  - Storm-control broadcast level set to 1.00

#### FastEthernet0/2
- **Description**: PC5-Access port
- **Mode**: Access
- **Configuration Details**:
  - Port-security enabled with maximum MAC addresses set to 1
  - Spanning-tree portfast and bpduguard enabled
  - Storm-control broadcast level set to 1.00

#### FastEthernet0/3
- **Description**: Management-PC Access port
- **Mode**: Access
- **Configuration Details**:
  - Port-security enabled with maximum MAC addresses set to 1
  - Spanning-tree portfast and bpduguard enabled

### Unused Interfaces
- There are two unused interfaces: FastEthernet0/4 through FastEthernet0/24 and GigabitEthernet0/2.

## Routing Configuration

### Static Routes
No static routes configured.

### Default Route
- **Configuration**: Not present in the configuration file.

### Inter-Vlan Routing
- **Status**: Enabled (using router-on-a-stick method).
- **Method**: Router-on-a-stick is used for inter-vlan routing, with VLANs 11 and 12 routed through a subinterface on GigabitEthernet0/1.

## Spanning Tree Protocol

### STP Configuration
- **Mode**: PVST+ (based on the configuration of spanning-tree vlan priority).
- **Root Bridge**: This switch is not configured as the root bridge.
- **Priority**: The spanning tree priority for VLANs 11, 12, and 90 is set to 61440.

### STP Features
- **PortFast**: Enabled on FastEthernet0/1 through FastEthernet0/3 interfaces.
- **BPDU Guard**: Not explicitly configured; however, it might be enabled globally (by default).
- **Root Guard**: Not configured.
- **Loop Guard**: Not configured.
- **UDLD**: Not configured.

## Best Practices Analysis

### Good Practices Identified
- Port-security is enabled on access ports to prevent unauthorized devices from connecting.
- Spanning-tree portfast and bpduguard are enabled on access ports to improve convergence time and prevent loops.
- SSH version 2 is enabled with a timeout of 60 seconds and authentication-retries set to 3 for secure remote management.

### Potential Issues or Concerns
- The VTP configuration mode is not explicitly stated, which might indicate it's in transparent mode; however, there are no server or client configurations, which could cause issues if the network requires dynamic VLAN assignment.
- There are no static routes configured, and the default route is not present in the configuration file.

### Recommendations for Improvement
1. Configure a default route to ensure connectivity between networks.
2. Consider implementing VTP server or client configurations depending on your network requirements.
3. Use meaningful VLAN names and descriptions for better management.
4. Document any complex configurations, such as inter-vlan routing using router-on-a-stick.

## Configuration Summary

- **Total VLANs**: 4
- **Total Configured Interfaces**: 6 active interfaces (GigabitEthernet0/1, FastEthernet0/1 through FastEthernet0/3, and the management interface)
- **Routing**: Enabled (using router-on-a-stick method for inter-vlan routing).
- **Spanning Tree**: PVST+ mode with a root priority of 61440 for VLANs 11, 12, and 90.
- **Key Features Enabled**:
  - SSH version 2
  - Port-security on access ports
  - Spanning-tree portfast and bpduguard on access ports
  - Inter-vlan routing using router-on-a-stick
- **Security Posture**: The switch has a good security posture due to the use of SSH, port-security, spanning-tree portfast and bpduguard, and inter-vlan routing.
- **Overall Assessment**: This configuration is well-structured with good practices for access layer management. However, it lacks a default route, and there are some concerns regarding VTP configurations.

## Appendix

### Uncommon or Complex Configurations
The router-on-a-stick method is used for inter-vlan routing; this might be considered an uncommon configuration.
This configuration does not have any complex or unusual settings beyond the use of router-on-a-stick.

### Configuration Snippets
None