# Switch Configuration Documentation: router-0.txt

## Overview
- **Hostname**: sentral-router-01
- **IOS Version**: 15.1
- **Configuration Purpose**: The configuration suggests a multi-VLAN switch with various interfaces connected to different networks and devices.
- **Last Modified**: Not available in the provided configuration.
- **Domain Name**: krister.local

## Device Information
- **Model**: CISCO2911/K9 (Extracted from license udi)
- **System Image**: IOS version 15.1 (Extracted from `version` command)
- **Serial Number**: FTX15244012- (Extracted from license udi)
- **Hardware Details**: The device is a Cisco 2911 router, which supports multiple interfaces and features.

## Management & Access

### Management Interfaces
The switch has several management-related interface configurations:
- **Management VLAN and IP addressing**:
  - `interface GigabitEthernet0/0` is not configured.
  - `ip ssh version 2`, `ip ssh time-out 60`, and `no ip domain-lookup` suggest that SSH is enabled, and the switch is not looking up external DNS for its own hostname.
- **Default gateway configuration**: Not explicitly configured in this section.
- **Management protocols enabled**:
  - SSH v2 with a timeout of 60 seconds.

### Access Control & Security
- **Console Access**: The `line con 0` command has been executed, configuring console line settings.
- **VTY Access**: Telnet/SSH configuration is as follows:
  - **Line configuration**: `login authentication default` and `transport input ssh`.
  - **Access class restrictions**: None explicitly configured in this section.
  - **Transport protocols allowed**: Only SSH is enabled.
- **Enable Password**: The enable secret password is encrypted, indicating that the password is secure.
- **AAA Configuration**: Authentication, Authorization, and Accounting (AAA) services are configured as follows:
  - `aaa new-model` enables AAA services.
  - `aaa authentication login console local` specifies that local authentication should be used for console connections.
  - `aaa authentication login default group tacacs+ local` specifies that TACACS+ authentication should be used as the default, with local authentication as a fallback.
  - `aaa authorization exec default group tacacs+ local` specifies that TACACS+ authorization should be used for EXEC access, with local authorization as a fallback.
  - `aaa accounting exec default start-stop group tacacs+` specifies that TACACS+ accounting should be used for EXEC access.
- **Login Banners**: A login banner is configured to display an unauthorized access message.

### Management Access Lists
An ACL named MGMT-MGMT has been applied to inbound VTY connections:
- `ip access-list standard MGMT-MGMT`: This ACL permits traffic from the 10.90.0.0/24 and 10.91.0.0/24 networks, and denies all other traffic.

## VLANs

### VLAN Database
The following table lists the configured VLANs:

| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      | Usergroup 1-1 | For user group 1-1 traffic.|
| 12      | Usergroup 1-2 | For user group 1-2 traffic.|
| 21      | Usergroup 2-1 | For user group 2-1 traffic.|
| 22      | Usergroup 2-2 | For user group 2-2 traffic.|
| 90      | Management LEFT SIDE | For management traffic on the left side. |
| 91      | Management RIGHT-SIDE | For management traffic on the right side. |

### VLAN Interfaces (SVIs)
The following table lists the SVI configurations:

| VLAN ID | Interface | Description | IP Address | DHCP Helper | HSRP/VRRP |
|---------|-----------|-------------|------------|-------------|----------|
| 11      | GigabitEthernet0/1.11 | Usergroup 1-1 | 192.168.11.254/24 | None       | None     |
| 12      | GigabitEthernet0/1.12 | Usergroup 1-2 | 192.168.12.254/24 | None       | None     |
| 21      | GigabitEthernet0/2.21 | Usergroup 2-1 | 192.168.21.254/24 | None       | None     |
| 22      | GigabitEthernet0/2.22 | Usergroup 2-2 | 192.168.22.254/24 | None       | None     |
| 90      | GigabitEthernet0/1.90 | Management LEFT SIDE | 10.90.0.254/24 | None       | None     |
| 91      | GigabitEthernet0/2.91 | Management RIGHT-SIDE | 10.91.0.254/24 | None       | None     |

### VTP Configuration
- **VTP Mode**: Not explicitly configured.
- **VTP Domain**: Not explicitly configured.
- **VTP Version**: Not explicitly configured.

## Physical Interfaces

### Interface Summary
The following table lists the physical interface configurations:

| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| GigabitEthernet0/0 | Management interface | Access |  |  | Shutdown |  |
| GigabitEthernet0/1 | dis-venstre-sw01 GIG0/2 | Trunk | 90,91 | Auto/Auto | Up |  |
| GigabitEthernet0/1.11 | Usergroup 1-1 | Trunk | 11 |  | Up |  |
| GigabitEthernet0/1.12 | Usergroup 1-2 | Trunk | 12 |  | Up |  |
| GigabitEthernet0/1.90 | Management LEFT SIDE | Trunk | 90 |  | Up |  |
| GigabitEthernet0/2 | dis-hoyre-sw01 GIG0/2 | Trunk | 21,22,91 | Auto/Auto | Up |  |
| GigabitEthernet0/2.21 | Usergroup 2-1 | Trunk | 21 |  | Up |  |
| GigabitEthernet0/2.22 | Usergroup 2-2 | Trunk | 22 |  | Up |  |
| GigabitEthernet0/2.91 | Management RIGHT-SIDE | Trunk | 91 |  | Up |  |

### Detailed Interface Configurations
The following interfaces have complex configurations:

#### GigabitEthernet0/1
- **Description**: dis-venstre-sw01 GIG0/2
- **Mode**: Trunk
- **Configuration Details**:
  - `description` sets the interface description.
  - `duplex auto` and `speed auto` set the duplex and speed settings to auto-negotiate.

#### GigabitEthernet0/1.11
- **Description**: Usergroup 1-1
- **Mode**: Trunk
- **Configuration Details**:
  - `encapsulation dot1Q 11` sets the VLAN encapsulation type.
  - `ip address 192.168.11.254 255.255.255.0` sets the IP address and subnet mask for the interface.
  - `ip access-group USERS_TO_SERV21 in` applies an access list to the interface.

#### GigabitEthernet0/2
- **Description**: dis-hoyre-sw01 GIG0/2
- **Mode**: Trunk
- **Configuration Details**:
  - `duplex auto` and `speed auto` set the duplex and speed settings to auto-negotiate.

## Port-Channel / EtherChannel

### Port-Channel [ID]
No port-channel configurations are present in this configuration.

## Routing Configuration

### Routing Protocol
No routing protocols are configured in this configuration.

### Static Routes
No static routes are defined in this configuration.

### Default Route
No default route is configured in this configuration.

### Inter-VLAN Routing
No inter-vlan routing is enabled or configured in this configuration.

## Spanning Tree Protocol

### STP Configuration
- **Mode**: PVST (Per VLAN Spanning Tree)
- **Root Bridge**: Not explicitly configured.
- **Priority**: Not explicitly configured.

### STP Features
- **PortFast**: No PortFast configurations are present.
- **BPDU Guard**: No BPDU Guard configurations are present.
- **Root Guard**: No Root Guard configurations are present.
- **Loop Guard**: No Loop Guard configurations are present.
- **UDLD**: No UDLD (Unidirectional Link Detection) configurations are present.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
No HSRP, VRRP, or GLBP configurations are present in this configuration.

### Stack Configuration
This device is not part of a stack.

### Redundant Links
No redundant link configurations are present in this configuration.

## Quality of Service (QoS)

No QoS configurations are present in this configuration.

## Security Features

### Port Security
- **Interfaces with port security enabled**: None.
- **Maximum MAC addresses allowed**: Not configured.
- **Violation actions configured**: Not configured.
- **Static MAC addresses (if configured)**: Not configured.

### DHCP Security
- **DHCP Snooping**: Disabled, as indicated by the absence of `ip dhcp snooping` configuration statements.
- **DHCP Snooping Database**: No configurations are present for a DHCP snooping database.

### Dynamic ARP Inspection (DAI)
- **Status**: Enabled.
- **Trusted interfaces**: None explicitly configured, but all interfaces are implicitly trusted due to the lack of any explicit untrusted interface designations.
- **VLANs protected**: All VLANs, as indicated by the absence of any `ip dhcp snooping vlan` configuration statements.

### IP Source Guard
- **Status and configuration**: Not configured.

### Storm Control
- **Configuration**: None explicitly configured.
- **Interfaces configured**: None.

## Access Control Lists (ACLs)

The following ACLs are present:

| ACL # | Type | Purpose | Rules |
|-------|------|---------|-------|
| MGMT-MGMT | Standard | Allow management traffic from 10.90.0.0/24 and 10.91.0.0/24 | permit 10.90.0.0 0.0.0.255, permit 10.91.0.0 0.0.0.255 |
| USERS_TO_SERV21 | Extended | Allow user traffic from 192.168.11.0/24 to servers on VLAN 21 | permit udp any any eq bootps, permit udp any any eq bootpc, permit ip 192.168.11.0 0.0.0.255 host 192.168.21.211, permit ip 192.168.11.0 0.0.0.255 host 192.168.21.212, permit udp 192.168.11.0 0.0.0.255 host 10.91.0.123 eq domain, permit tcp 192.168.11.0 0.0.0.255 host 10.91.0.123 eq domain |
| USERS_TO_SERV22 | Extended | Allow user traffic from 192.168.12.0/24 to servers on VLAN 22 | permit udp any any eq bootps, permit udp any any eq bootpc, permit ip 192.168.12.0 0.0.0.255 host 192.168.22.221, permit ip 192.168.12.0 0.0.0.255 host 192.168.22.222, permit udp 192.168.12.0 0.0.0.255 host 10.91.0.123 eq domain, permit tcp 192.168.12.0 0.0.0.255 host 10.91.0.123 eq domain |
| MGMT-RIGHT | Extended | Allow management traffic from 10.91.0.0/24 to VLANs 11, 12, 21, and 22 | permit ip 10.91.0.0 0.0.0.255 192.168.11.0 0.0.0.255, permit ip 10.91.0.0 0.0.0.255 192.168.12.0 0.0.0.255, permit ip 10.91.0.0 0.0.0.255 192.168.21.0 0.0.0.255, permit ip 10.91.0.0 0.0.0.255 192.168.22.0 0.0.0.255 |
| MGMT-LEFT | Extended | Allow management traffic from 10.90.0.0/24 to VLANs 11, 12, 21, and 22 | permit ip 10.90.0.0 0.0.0.255 192.168.11.0 0.0.0.255, permit ip 10.90.0.0 0.0.0.255 192.168.12.0 0.0.0.255, permit ip 10.90.0.0 0.0.0.255 192.168.21.0 0.0.0.255, permit ip 10.90.0.0 0.0.0.255 192.168.22.0 0.0.0.255 |

## Best Practices Analysis

### Good Practices Identified
- The configuration uses meaningful VLAN names.
- Access lists are used to restrict traffic to specific VLANs and networks.

### Potential Issues or Concerns
- Security:
  - The configuration lacks any form of encryption for sensitive information like passwords and keys.
  - SSH is enabled, but it's recommended to use a stronger version (e.g., SSHv2) with key-based authentication.
- Configuration and Management:
  - There are no explicit configurations for VTP mode, domain name, or version.
  - The absence of configuration commands could indicate potential security risks if the switch were to be compromised.

### Recommendations for Improvement
1. Implement secure password encryption using `enable secret`.
2. Configure SSH with key-based authentication and a stronger version (e.g., SSHv2).
3. Set up VTP mode, domain name, and version configurations.
4. Enable DHCP snooping on all VLANs to prevent malicious ARP attacks.

## Configuration Summary

- **Total VLANs**: 6
- **Total Configured Interfaces**: 9 active interfaces
- **Routing**: No routing protocols are configured; inter-vlan routing is not enabled or configured.
- **Spanning Tree**: PVST (Per VLAN Spanning Tree) mode with no explicit root bridge configuration and unconfigured priority values.
- **Key Features Enabled**: SSH, DHCP excluded addresses, IP cef, NTP authentication-key, ntp authenticate, and ntp trusted-key 15.
- **Security Posture**: The configuration lacks any form of encryption for sensitive information like passwords and keys.
- **Overall Assessment**: This switch configuration has some security concerns due to the lack of secure password storage and SSH key-based authentication.