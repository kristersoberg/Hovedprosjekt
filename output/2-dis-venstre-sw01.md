# Switch Configuration Documentation: 2-dis-venstre-sw01.txt

## Overview
- **Hostname**: dis-venstre-sw01
- **IOS Version**: Unknown (not specified)
- **Configuration Purpose**: This switch appears to be a core layer device for network management and access, with features such as AAA, SSH, DHCP Snooping, and DAI.
- **Last Modified**: Not available
- **Domain Name**: krister.local

## Device Information
- **Model**: Not explicitly mentioned in the configuration (use `show version` command to determine model)
- **System Image**: Unknown (not specified)
- **Serial Number**: Not available
- **Hardware Details**: This switch has at least two Gigabit Ethernet interfaces.

## Management & Access

### Management Interfaces
The management VLAN is configured as VLAN 90:

*   **Management VLAN and IP Addressing**:
    *   `Vlan90` interface with an IP address of `10.90.0.12/24`.
*   **Default Gateway Configuration**: The default gateway for this switch is set to `10.90.0.254`.

### Access Control & Security

#### Console Access
The console line configuration includes:

*   **Console Line**:
    *   Authentication method: Local.
    *   Exec-timeout: 10 minutes.

#### VTY Access
Telnet and SSH are both disabled by default on this switch, but the following VTY configurations were found:

*   **VTY Configuration**:
    *   Login authentication method is set to `default` (which in turn uses tacacs+).
    *   Transport input is restricted to `ssh`.

#### Enable Password
The enable secret password is configured with a strength of 8 characters.

#### AAA Configuration
AAA is enabled globally, and the following configurations were found:

*   **TACACS Server Configuration**: The TACACS server is set to `10.91.0.10` with a key of `KompleksNoekkel`.
*   **Local Authentication Configuration**: Local authentication on the console line is enabled.
*   **Authorization and Accounting Configuration**: Authorization using tacacs+ is configured, while accounting also uses tacacs+.

#### Login Banners
A login banner prohibits unauthorized access to the switch.

### Management Access Lists

The following ACLs were found:

*   `MGMT-MGMT`: A standard ACL that allows traffic from two specific subnets (`10.90.0.0/24` and `10.91.0.0/24`) while denying all other traffic.

## VLANs

### VLAN Database
Below is a table summarizing the configured VLANs:

| VLAN ID | Name        | Purpose/Description |
|---------|-------------|---------------------|
| 11      | Usergroup1-1|                     |
| 12      | Usergroup1-2|                     |
| 90      | Admin-Mgmt-LEFT|Management SVI      |
| 666     | native-trunk|Trunking VLAN       |

### VLAN Interfaces (SVIs)

The following VLAN interfaces were found:

*   **VLAN 11 Interface**: Not configured.
*   **VLAN 12 Interface**: Not configured.
*   **VLAN 90 Interface**: This interface is used for management and has an IP address of `10.90.0.12/24`.
*   **VLAN 666 Interface**: Not configured.

### VTP Configuration
VTP is not explicitly enabled in this configuration, but given the presence of multiple VLANs, it's likely that VTP is running on a global level with default settings.

## Physical Interfaces

### Interface Summary

Below is a comprehensive table summarizing all interfaces:

| Interface | Description    | Mode  | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|----------------|-------|------------|--------------|--------|------------------|
| G0/1     | aksess-sw01   | trunk | 11,12,90   | auto         | up     | STP, UDLD        |
| G0/2     | sentral-router-01|trunk | 11,12,90   | auto         | up     | STP               |

### Detailed Interface Configurations

The following interfaces have complex configurations:

*   **GigabitEthernet0/1**:
    *   **Description**: aksess-sw01 gig0/1
    *   **Mode**: trunk
    *   **Configuration Details**:
        + `switchport trunk encapsulation dot1q` - Sets the trunking encapsulation method to 802.1Q.
        + `switchport mode trunk` - Enables trunk mode on this interface.
        + `switchport nonegotiate` - Prevents dynamic negotiation of DTP (Dynamic Trunking Protocol).
        + `switchport trunk native vlan 666` - Sets the native VLAN for trunking to VLAN 666.
        + `switchport trunk allowed vlan 11,12,90` - Specifies which VLANs are allowed on this trunk interface.
        + `ip dhcp snooping limit rate 15` - Configures DHCP snooping with a rate limit of 15 packets per second.
        + `ip arp inspection trust` - Enables IP ARP inspection and sets the trust state to trusted.
        + `spanning-tree guard root` - Enables STP root guard on this interface.

*   **GigabitEthernet0/2**:
    *   **Description**: sentral-router-01 gig0/1
    *   **Mode**: trunk
    *   **Configuration Details**:
        + `switchport trunk encapsulation dot1q` - Sets the trunking encapsulation method to 802.1Q.
        + `switchport mode trunk` - Enables trunk mode on this interface.
        + `switchport nonegotiate` - Prevents dynamic negotiation of DTP (Dynamic Trunking Protocol).
        + `switchport trunk native vlan 666` - Sets the native VLAN for trunking to VLAN 666.
        + `switchport trunk allowed vlan 11,12,90` - Specifies which VLANs are allowed on this trunk interface.
        + `ip dhcp snooping trust` - Enables DHCP snooping and sets the trust state to trusted.
        + `ip arp inspection trust` - Enables IP ARP inspection and sets the trust state to trusted.

### Unused Interfaces
There are 24 unused interfaces (FastEthernet0/1-24) in shutdown state. Their default configuration is as follows:

*   **Interface Configuration**:
    *   `shutdown` - Places this interface into a shutdown state.
    *   `no ip address` - Removes any IP address assignments from this interface.

## Port-Channel / EtherChannel

No port-channel or etherchannel configurations are explicitly mentioned in the provided configuration file. However, interfaces GigabitEthernet0/1 and GigabitEthernet0/2 do have trunk configurations that might be part of a larger setup for load balancing or redundancy purposes.

## Routing Configuration

### Routing Protocol
No routing protocols (OSPF, EIGRP, RIP, BGP) are configured in the provided configuration file. However, the switch does have IP routing disabled (`no ip routing`), which implies that it is not functioning as a router at this time.

### Static Routes
There are no static routes configured.

### Default Route
No default route is explicitly configured.

### Inter-VLAN Routing
Inter-vlan routing is likely enabled through the use of VLAN interfaces (SVIs) with IP addresses assigned to them, but there's no explicit configuration indicating this.

## Spanning Tree Protocol

### STP Configuration
The spanning tree protocol is operating in Rapid-PVST mode (`spanning-tree vlan <vlan-id> mode mstp` is not directly stated, however it can be inferred from the `mst region-name` command which is used below).

*   **Rapid-PVST Mode**:
    *   The configuration implies that the switch operates in Rapid-PVST mode, as indicated by the presence of MST regions and instances.

### STP Features
The following STP features are configured:

*   **PortFast**: Not explicitly mentioned.
*   **BPDU Guard**: Not explicitly mentioned.
*   **Root Guard**: Enabled on interface GigabitEthernet0/1 (`spanning-tree guard root`).
*   **Loop Guard**: Not explicitly mentioned.
*   **UDLD**: Not enabled.

### Per-VLAN STP Status
The spanning tree status for VLANs 11, 12, and 90 are configured to have a priority of 4096 and the switch is configured as the primary root bridge (`spanning-tree vlan <vlan-id> root primary`).

## Quality of Service (QoS)

No QoS configurations are explicitly mentioned in the provided configuration file.

## Security Features

### Port Security
Port security is enabled on interface GigabitEthernet0/1, which has a maximum number of MAC addresses allowed and violation actions configured:

*   **Maximum MAC Addresses**: 8.
*   **Violation Actions**: Shutdown (`switchport port-security violation shutdown`).

### DHCP Security
The following DHCP security features are configured:

*   **DHCP Snooping**: Enabled for VLANs 11, 12, and the global configuration is set to verify MAC addresses on received DHCP packets (`ip dhcp snooping vlan <vlan-id>`).
*   **DHCP Snooping Database**: Not explicitly mentioned.
*   **IP Source Guard**: Not enabled.

### Dynamic ARP Inspection (DAI)
Dynamic ARP inspection (DAI) is enabled for VLANs 11, 12:

*   **Trusted Interfaces**: GigabitEthernet0/1 and GigabitEthernet0/2 (`ip arp inspection vlan <vlan-id>`).

### IP Source Guard
IP source guard is not explicitly mentioned.

### Storm Control
Storm control is not explicitly mentioned.

### Access Control Lists (ACLs)
The following ACLs are configured:

*   **MGMT-MGMT**: A standard access list that permits traffic from networks 10.90.0.0/24 and 10.91.0.0/24 (`ip access-list standard MGMT-MGMT`).

## Network Services

### DHCP Server/Relay
No DHCP server configurations are explicitly mentioned; however, the global configuration is set to trust interface GigabitEthernet0/1 for ARP inspection on received DHCP packets.

### NTP (Network Time Protocol)
NTP authentication is enabled:

*   **Authentication Key**: 15.
*   **Trusted Keys**: Only key 15 (`ntp authenticate`).

### SNMP (Simple Network Management Protocol)
SNMP version and community strings are not explicitly mentioned; however, the global configuration is set to allow SNMP traps.

### Syslog
The following syslog configurations are explicitly mentioned:

*   **Logging Level**: Informational.
*   **Logging Hosts**: 10.91.0.10 (`logging host <host>`).

### DNS Configuration
DNS servers and domain name are not explicitly mentioned.

### CDP/LLDP
CDP is disabled globally; however, the interface configuration for GigabitEthernet0/1 has it enabled:

*   **CDP Mode**: Enabled on a per-interface basis.
*   **LLDP Status**: Disabled (`no lldp run`).

## Best Practices Analysis

The following are good practices that were identified in this configuration:

*   The switch has a unique hostname and IP address for the management interface.
*   A login banner is configured to deter unauthorized access.
*   Port security is enabled on GigabitEthernet0/1, which prevents MAC spoofing attacks.
*   DHCP snooping and dynamic ARP inspection are enabled, which protects against rogue devices and man-in-the-middle attacks.
*   The switch has an NTP configuration that ensures accurate timekeeping.

The following potential issues or concerns were identified:

*   The enable secret password is set to a weak value.
*   The management interface IP address (10.90.0.12) may be vulnerable to IP spoofing attacks if not properly secured.
*   There are no ACLs configured on the interfaces, which leaves them open to unauthorized access.
*   The switch has a default gateway of 10.90.0.254, but there is no BGP or OSPF configuration that would allow for dynamic routing.

The following recommendations were made for improvement:

1.  Change the enable secret password to a stronger value and consider using a passphrase instead of a simple password.
2.  Configure ACLs on the interfaces to restrict unauthorized access.
3.  Consider implementing a more robust authentication mechanism, such as RADIUS or TACACS+.
4.  Ensure that the management interface IP address is properly secured with a strong password and/or additional security features.

## Configuration Summary

*   **Total VLANs**: 5
*   **Total Configured Interfaces**: 2 (GigabitEthernet0/1, GigabitEthernet0/2)
*   **Routing**: Disabled
*   **Spanning Tree**: Spanning-Tree Protocol is enabled, and the switch is configured as a root bridge for VLANs 11, 12, and 90.
*   **Key Features Enabled**: DHCP snooping, dynamic ARP inspection, NTP authentication, and port security on GigabitEthernet0/1.
*   **Security Posture**: The switch has a good security posture due to the configuration of features such as DHCP snooping, dynamic ARP inspection, and port security. However, there are some potential issues that need to be addressed.

## Appendix

### Uncommon or Complex Configurations
There is no complex or uncommon configuration in this switch configuration.

### Configuration Snippets
The following configuration snippets may be helpful for understanding the configuration:

```markdown
vlan 11
 name Usergroup1-1

vlan 12
 name Usergroup1-2

vlan 90
 name Admin-Mgmt-LEFT

interface Vlan90
 no shutdown
 description Management SVI
 ip address 10.90.0.12 255.255.255.0
 ip access-group MGMT-MGMT in
 no shutdown
```

This configuration snippet shows the creation of VLANs and the configuration of the management interface (VLAN 90).