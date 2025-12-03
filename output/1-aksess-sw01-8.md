# Switch Configuration Documentation: 1-aksess-sw01-8.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: This switch appears to be a managed access layer switch, possibly part of an enterprise network.
- **Last Modified**: Not available in the configuration file.
- **Domain Name**: krister.local

## Device Information
- **Model**: Not available in the configuration file.
- **System Image**: Unknown IOS version.
- **Serial Number**: Not available in the configuration file.
- **Hardware Details**: The switch has multiple Gigabit Ethernet ports, including Gi0/1 and Fae0/2.

## Management & Access

### Management Interfaces
Document all management-related interface configurations:

*   Management VLAN: Vlan90 (10.90.0.11/255.255.255.0)
*   Default Gateway: 10.90.0.254
*   Management protocols enabled:
    *   SSH version 2
    *   NTP

### Access Control & Security
- **Console Access**: Configuration of console line:
    *   Authentication method: local
    *   Exec timeout: 10 minutes
- **VTY Access**: Telnet/SSH configuration:
    *   Line configuration: vty 0 4
    *   Authentication default: group tacacs+ and local
    *   Transport protocols allowed: SSH
*   Enable Password: Status and encryption level:
    *   Enable secret: 3NA8le$cret!=1 (encrypted)
*   AAA Configuration: Authentication, Authorization, Accounting setup using TACACS+ and local methods.
*   Login Banners: Unauthorized access prohibited.

### Management Access Lists
Document any ACLs applied to management access:

*   ACL MGMT-MGMT:
    *   Standard ACL
    *   Permit 10.90.0.0/24 and 10.91.0.0/24

## VLANs

### VLAN Database
Create a table of all configured VLANs:

| VLAN ID | Name         | Purpose/Description |
|---------|--------------|---------------------|
| 11      | Usergroup1-1 | Access layer for users |
| 12      | Usergroup1-2 | Access layer for users |
| 90      | Admin-Mgmt-LEFT | Management VLAN |
| 666     | native-trunk | Native trunk VLAN |

### VLAN Interfaces (SVIs)
For each VLAN interface:

*   **VLAN 11 Interface**
    *   IP Address: Not configured
    *   Description: Not available
    *   DHCP Helper: Not enabled
    *   HSRP/VRRP: Not configured
    *   Spanning Tree Protocol: Enabled (PVST+)
*   **VLAN 12 Interface**
    *   IP Address: Not configured
    *   Description: Not available
    *   DHCP Helper: Not enabled
    *   HSRP/VRRP: Not configured
    *   Spanning Tree Protocol: Enabled (PVST+)

### VTP Configuration
- **VTP Mode**: Client
- **VTP Domain**: Not available
- **VTP Version**: 1

## Physical Interfaces

### Interface Summary
Create a comprehensive table:

| Interface | Description        | Mode     | VLAN/Trunk | Speed/Duplex | Status      | Special Features          |
|-----------|--------------------|----------|------------|--------------|-------------|---------------------------|
| Gi0/1    | dis-venstre-sw01   | Trunk    | 11,12,90   | 1000 Mb/s   | Up          | None                      |
| Fae0/2   | PC5-Access port    | Access   | 12         | Auto        | Up          | Port Security Enabled     |
| Fae0/3   | Management-PC      | Access   | 90         | Auto        | Up          | Port Security Enabled     |

### Detailed Interface Configurations
For interfaces with complex configurations:

*   **Gi0/1**:
    *   Description: dis-venstre-sw01 gig0/1
    *   Switchport trunk encapsulation dot1q
    *   Switchport mode trunk
    *   Switchport nonegotiate
    *   Switchport trunk native vlan 666
    *   Switchport trunk allowed vlan 11,12,90
*   **Fae0/2**:
    *   Description: PC5-Access port
    *   Switchport mode access
    *   Switchport access vlan 12
    *   Port Security Enabled:
        + Maximum MAC addresses allowed: 1
        + Violation action: Restrict

## Routing Configuration

### Routing Protocol
No routing protocol is configured.

### Static Routes
No static routes are configured.

### Default Route
- **Configuration**: Not available.
- **Next-hop**: Not configured.

### Inter-VLAN Routing
- **Status**: Enabled (Router-on-a-stick method)
- **Method**: Router-on-a-stick

## Spanning Tree Protocol

### STP Configuration
- **Mode**: PVST+
- **Root Bridge**: This switch is the root bridge for VLANs 11, 12, and 90.

### STP Features
- **PortFast**: Enabled on Fae0/2 (PC5-Access port)
- **BPDU Guard**: Not enabled.
- **Root Guard**: Not configured.
- **Loop Guard**: Not configured.
- **UDLD**: Not enabled.

## High Availability & Redundancy

### FHRP Configuration
No FHRP configuration is available.

### Stack Configuration
This switch does not appear to be part of a stack.

### Redundant Links
No redundant link configurations are available.

## Quality of Service (QoS)

No QoS configurations are available.

## Security Features

### Port Security
- **Interfaces with port security enabled**:
    *   Fae0/2 (PC5-Access port)
*   Maximum MAC addresses allowed: 1
*   Violation action: Restrict

### DHCP Security
- **DHCP Snooping**: Enabled on VLANs 11, 12.
- **Trusted interfaces**: Gi0/1 (dis-venstre-sw01)

### Dynamic ARP Inspection (DAI)
- **Status**: Enabled
- **Trusted interfaces**: Gi0/1 (dis-venstre-sw01)

### IP Source Guard
- **Status**: Not enabled.

### Storm Control
- **Configuration**:
    *   Broadcast: 1.00
*   Interfaces configured: None

### Access Control Lists (ACLs)
Document all ACLs:

*   **ACL MGMT-MGMT**:
    *   Standard ACL
    *   Permit 10.90.0.0/24 and 10.91.0.0/24

## Network Services

### DHCP Server/Relay
- **DHCP Relay**: Not enabled.

### NTP (Network Time Protocol)
- **NTP Server(s)**: 10.91.0.123 (key 15)
- **NTP Authentication**: Enabled with key 15.

### SNMP (Simple Network Management Protocol)
No SNMP configuration is available.

### Syslog
- **Logging Level**: Not configured.
- **Logging Hosts**: None

### DNS Configuration
- **DNS Servers**: Not configured.
- **Domain name**: krister.local

## Best Practices Analysis

*   ✅ **Good Practices Identified**:
    *   Enable port security on access ports (e.g., Fae0/2)
    *   Use meaningful VLAN names and plan a numbering scheme
    *   Document VLAN assignments and user traffic on VLAN 1
*   ⚠️ **Potential Issues or Concerns**:
    *   No routing protocol configured, potentially causing routing issues
    *   No QoS configurations available for managing network traffic
    *   Port security not enabled on all access ports (e.g., Fae0/3)
*   💡 **Recommendations for Improvement**:
    1.  Configure a routing protocol to manage and advertise networks.
    2.  Implement QoS configurations to manage network traffic.
    3.  Enable port security on all access ports.

## Configuration Summary

-   **Total VLANs**: 4
-   **Total Configured Interfaces**: 5 active interfaces
-   **Routing**: Enabled (Router-on-a-stick method)
-   **Spanning Tree**: PVST+ mode, root bridge for VLANs 11, 12, and 90
-   **Key Features Enabled**:
    *   Port security on access ports (Fae0/2 and Fae0/3)
    *   DHCP snooping and DAI enabled
*   **Security Posture**: The switch has a moderate level of security with port security enabled, but lacks routing protocol and QoS configurations.
-   **Overall Assessment**: This switch appears to be part of an enterprise network, providing managed access layer connectivity for users. It has a basic level of security configuration but requires improvement in routing and QoS management.

## Appendix

### Uncommon or Complex Configurations
This configuration does not have any complex or unusual configurations that require additional explanation.

### Configuration Snippets
The following configuration snippets are relevant:

*   VLAN database:
    ```
vlan 11 
name Usergroup1-1

vlan 12 
name Usergroup1-2

vlan 90
name Admin-Mgmt-LEFT

vlan 666
name native-trunk
```

*   Port security on Fae0/2 (PC5-Access port):
    ```bash
interface FastEthernet0/2
 no shutdown
 description PC5-Access port
 switchport mode access 
 switchport access vlan 12
 switchport port-security
 switchport port-security maximum 1 
 switchport port-security violation restrict
 switchport port-security aging time 3
 switchport port-security mac-address sticky
```

*   DHCP snooping and DAI enabled:
    ```bash
ip dhcp snooping vlan 11,12
ip dhcp snooping verify mac-address
```