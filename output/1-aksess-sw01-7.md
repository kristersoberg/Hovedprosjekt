# Switch Configuration Documentation: 1-aksess-sw01-7.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown (based on the configuration)
- **Configuration Purpose**: This switch appears to be a core access layer device, providing Layer 2 connectivity for multiple VLANs and managing access control lists.
- **Last Modified**: Not specified in the configuration
- **Domain Name**: krister.local

## Device Information
- **Model**: Not explicitly mentioned in the configuration
- **System Image**: Unknown (due to lack of version information)
- **Serial Number**: Not available in the provided configuration
- **Hardware Details**: The switch has multiple Gigabit Ethernet ports, Fast Ethernet ports, and at least one console port.

## Management & Access

### Management Interfaces
The management interface is configured as follows:

*   Management VLAN: Vlan90 (with IP address 10.90.0.11/24)
*   Default gateway: 10.90.0.254
*   Management protocols: SSHv2, with timeout and authentication retries configured

### Access Control & Security
- **Console Access**: Console line is configured to use local authentication.
    *   Authentication method: Local authentication only.
- **VTY Access**: Telnet/SSH configuration:
    *   Line vty 0 4 uses default authentication for SSH access.
        +   Authentication method: TACACS+ with local fallback (default group).
- **Enable Password**: Enable secret is set to 3NA8le$cret!=1, encrypted.
    *   Encryption level: 15
- **AAA Configuration**: TACACS+ server is configured:
    *   Server host: 10.91.0.10 with a key of KompleksNoekkel.
        +   Authentication method: TACACS+ (default group).
- **Login Banners**: Unauthorized access prohibited banner is displayed for login attempts.

### Management Access Lists
An ACL named MGMT-MGMT restricts management access to the switch:

*   Standard ACL with permit and deny rules:
    *   Permit 10.90.0.0/24, 10.91.0.0/24.
    *   Deny any other IP address.

## VLANs

### VLAN Database
The following table lists all configured VLANs:

| VLAN ID | Name             | Purpose/Description          |
|---------|------------------|-------------------------------|
| 11      | Usergroup1-1     | Access for user group 1-1   |
| 12      | Usergroup1-2     | Access for user group 1-2   |
| 90      | Admin-Mgmt-LEFT  | Management VLAN            |
| 666     | native-trunk     | Native trunk VLAN           |

### VLAN Interfaces (SVIs)
VLAN interfaces are configured as follows:

*   Vlan90:
    *   IP address: 10.90.0.11/24.
    *   Description: Management SVI.
    *   DHCP helper is not configured.

## Physical Interfaces

### Interface Summary
The following table lists all physical interfaces:

| Interface | Description           | Mode      | VLAN/Trunk | Speed/Duplex | Status  | Special Features            |
|-----------|-----------------------|-----------|------------|--------------|---------|-----------------------------|
| GigabitEthernet0/1 | dis-venstre-sw01 gig0/1| trunk     | native vlan 666 | auto          | up      | Switchport nonegotiate, trunk allowed VLANs 11,12,90 |
| FastEthernet0/1   | PC4-Access port      | access    | vlan 11       | auto          | up      | Port-security, port-fast, bpduguard enabled     |
| FastEthernet0/2   | PC5-Access port      | access    | vlan 12       | auto          | up      | Port-security, port-fast, bpduguard enabled     |
| FastEthernet0/3   | Management-PC Access port | access    | vlan 90       | auto          | up      | Port-security, port-fast                        |

### Detailed Interface Configurations
The following interfaces have complex configurations:

*   GigabitEthernet0/1:
    *   Mode: trunk.
    *   Configuration details: switchport trunk encapsulation dot1q, native vlan 666, allowed VLANs 11,12,90.

## Port-Channel / EtherChannel

No port-channel configuration is present in the provided configuration.

## Routing Configuration

### Routing Protocol
No routing protocol is configured in this switch's configuration.

### Static Routes
No static routes are defined in the configuration.

### Default Route
A default route is not explicitly configured.

### Inter-VLAN Routing
Inter-vlan routing is likely enabled, but no specific method (router-on-a-stick or Layer 3 switching) can be determined from the provided configuration.

## Spanning Tree Protocol

### STP Configuration
The switch uses PVST+:

*   Mode: pvst.
*   Root bridge status: This device does not appear to be configured as a root bridge for any VLANs.

### STP Features
PortFast is enabled on several interfaces, and BPDU guard is also enabled. Loop guard is not mentioned in the configuration.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
No FHRP protocol is configured.

### Stack Configuration
This switch does not appear to be part of a stack.

## Quality of Service (QoS)

No QoS configuration is present in the provided switch configuration file.

## Security Features

### Port Security
Port-security is enabled on several interfaces:

*   FastEthernet0/1, 2 and 3 are configured with port-security.
    +   Maximum MAC addresses allowed: 1.
    +   Violation action: restrict.

### DHCP Security
DHCP snooping and ARP inspection are enabled for VLANs 11 and 12:

*   Status: Enabled for VLANs 11 and 12.
*   Trusted interfaces: GigabitEthernet0/1 (due to its trunk configuration).

### Dynamic ARP Inspection (DAI)
DAI is enabled for VLANs 11 and 12.

*   Status: Enabled.
*   Trusted interfaces: None (since no trusted ports are explicitly listed in the configuration).

### IP Source Guard
No IP source guard configuration is present.

### Storm Control
Storm control is configured to prevent broadcast storms:

*   Configuration: Broadcast level set to 1.00 on FastEthernet0/1, 2 and 3.
*   Interfaces configured: FastEthernet0/1, 2 and 3.

## Access Control Lists (ACLs)

An ACL named MGMT-MGMT restricts management access to the switch:

*   Standard ACL with permit and deny rules:
    *   Permit 10.90.0.0/24, 10.91.0.0/24.
    *   Deny any other IP address.

## Network Services

### DHCP Server/Relay
No DHCP server or relay configuration is present in the switch's configuration.

### NTP (Network Time Protocol)
NTP is configured with an authentication key:

*   Authentication key: 15 md5 KomplekstPassord.
*   Trusted key: 15.

### SNMP (Simple Network Management Protocol)
No SNMP version, community strings, or trap settings are mentioned in the configuration.

## Best Practices Analysis

Based on the analysis of the switch's configuration, several good practices have been identified:

- The use of a login banner to display unauthorized access prohibited.
- Configuration of port-security features to restrict MAC addresses on interfaces.
- Enforcement of spanning tree protocol for network loop prevention.
- Enablement of DHCP snooping and ARP inspection for VLANs 11 and 12.

However, several potential issues or concerns were identified:

- The switch does not have a clear default route configuration, which might cause connectivity problems if there are no other routing protocols configured.
- No QoS configuration is present in the provided switch configuration file, potentially leading to congestion on high-traffic interfaces.
- There is no explicit IP source guard configuration.

## Configuration Summary

*   **Total VLANs:** 4
*   **Total Configured Interfaces:** 7
*   **Routing:** Disabled (no routing protocol or static routes)
*   **Spanning Tree:** Enabled with PVST+ mode
*   **Key Features Enabled:**
    *   Port-security features
    *   DHCP snooping and ARP inspection for VLANs 11 and 12
    *   Storm control on FastEthernet0/1, 2 and 3 interfaces
*   **Security Posture:** Good practices identified; potential issues include missing QoS configuration and lack of explicit default route.
*   **Overall Assessment:** The switch's configuration appears to be focused on providing Layer 2 connectivity for multiple VLANs with secure access control features enabled.