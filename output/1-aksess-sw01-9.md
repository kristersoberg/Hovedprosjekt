# Switch Configuration Documentation: 1-aksess-sw01-9.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown (from file name)
- **Configuration Purpose**: Management switch with access ports for users and management PC, uplink trunk to another switch, and VLAN database configuration.
- **Last Modified**: Not found in config
- **Domain Name**: krister.local

## Device Information
- **Model**: Not extracted from config, requires manual lookup or access to the device's serial number
- **System Image**: Boot image information not provided in the config file
- **Serial Number**: Not available
- **Hardware Details**: The switch appears to be a Cisco Catalyst 2960 series based on the configuration commands used.

## Management & Access

### Management Interfaces
The management VLAN and IP addressing are configured as follows:

*   **Management VLAN Interface**:
    *   **VLAN ID**: 90 (configured as native-trunk)
    *   **IP Address**: 10.90.0.11/255.255.255.0 (configured on VLAN 90 interface)
    *   **Default Gateway**: 10.90.0.254

### Access Control & Security
- **Console Access**:
    *   The console line is configured with authentication set to `console` and an exec-timeout of 10 minutes.
- **VTY Access**:
    *   Telnet/SSH access class restrictions are applied using the `access-class MGMT-MGMT in` command.
    *   Only SSH version 2 is enabled, with a timeout of 60 seconds.
- **Enable Password**: The enable secret password is set to `3NA8le$cret!=1`.
- **AAA Configuration**:
    *   AAA authentication for login and exec are configured using TACACS+ with a local fallback.
    *   Authorization for exec commands uses TACACS+ with a local fallback.

### Login Banners
A login banner is set to display "Unauthorized access prohibited." when users log in to the switch.

### Management Access Lists
The following ACLs are applied to management access:

*   **MGMT-MGMT**:
    *   Permits traffic from 10.90.0.0/255.255.255.255 and 10.91.0.0/255.255.255.255.
    *   Denies all other traffic.

## VLANs

### VLAN Database
The following table lists the configured VLANs:

| VLAN ID | Name | Purpose/Description |
|---------|------|---------------------|
| 11      | Usergroup1-1 | User group 1, VLAN 1 |
| 12      | Usergroup1-2 | User group 1, VLAN 2 |
| 90      | Admin-Mgmt-LEFT | Management VLAN for left side admin |
| 666     | native-trunk | Native trunk VLAN |

### VLAN Interfaces (SVIs)
The management VLAN interface is configured as follows:

*   **VLAN 90 Interface**
    *   IP Address: 10.90.0.11/255.255.255.0
    *   Description: Management SVI
    *   No DHCP helper address or HSRP/VRRP configurations are found.

### VTP Configuration
The switch is configured in transparent mode, which means it does not participate in VTP domain management.

## Physical Interfaces

### Interface Summary

| Interface | Description | Mode | VLAN/Trunk | Speed/Duplex | Status | Special Features |
|-----------|-------------|------|------------|--------------|--------|------------------|
| GigabitEthernet0/1   | dis-venstre-sw01 gig0/1 | trunk  | dot1q, native vlan 666, allowed vlans 11,12,90 | auto    | not shut     | ip dhcp snooping trust, ip arp inspection trust |
| FastEthernet0/1      | PC4-Access port   | access | VLAN 11          | auto    | not shut     | port-security, storm-control broadcast level 1.00 |
| FastEthernet0/2      | PC5-Access port   | access | VLAN 12          | auto    | not shut     | port-security, storm-control broadcast level 1.00 |
| FastEthernet0/3      | Management-PC Access port  | access | VLAN 90          | auto    | not shut     | spanning-tree portfast, spanning-tree bpduguard enable |

### Detailed Interface Configurations
The following are detailed interface configurations:

#### GigabitEthernet0/1
*   **Description**: dis-venstre-sw01 gig0/1
*   **Mode**: Trunk
*   **Configuration Details**:
    *   `switchport trunk encapsulation dot1q`
    *   `switchport mode trunk`
    *   `switchport nonegotiate`
    *   `switchport trunk native vlan 666`
    *   `switchport trunk allowed vlan 11,12,90`
    *   `ip dhcp snooping trust` and `ip arp inspection trust`

#### FastEthernet0/1
*   **Description**: PC4-Access port
*   **Mode**: Access
*   **Configuration Details**:
    *   `switchport mode access`
    *   `switchport access vlan 11`
    *   `switchport port-security` and `port-security maximum 1`
    *   `ip dhcp snooping limit rate 15`

#### FastEthernet0/2
*   **Description**: PC5-Access port
*   **Mode**: Access
*   **Configuration Details**:
    *   `switchport mode access`
    *   `switchport access vlan 12`
    *   `switchport port-security` and `port-security maximum 1`

#### FastEthernet0/3
*   **Description**: Management-PC Access port
*   **Mode**: Access
*   **Configuration Details**:
    *   `switchport mode access`
    *   `switchport access vlan 90`
    *   `spanning-tree portfast` and `spanning-tree bpduguard enable`

## Port-Channel / EtherChannel

No port-channel configurations are found.

## Routing Configuration
### Routing Protocol
No routing protocols (OSPF, EIGRP, RIP, BGP) are configured.

### Static Routes
The following static routes are configured:

*   Destination: 10.90.0.0/255.255.255.0 → Next-hop: 10.90.0.254

### Default Route
No default route is explicitly configured.

## Spanning Tree Protocol
### STP Configuration
The switch uses Rapid PVST+ mode and has a bridge priority of 61440 for VLANs 11,12,90.

## High Availability & Redundancy

### FHRP Configuration (HSRP/VRRP/GLBP)
No FHRP configurations are found.

## Quality of Service (QoS)

QoS is not configured.

## Security Features
### Port Security
Port security is enabled on the following interfaces:

*   `FastEthernet0/1`
*   `FastEthernet0/2`

### DHCP Security
DHCP snooping and IP source guard are not explicitly configured but DHCP snooping trust is applied to interface GigabitEthernet0/1.

## Network Services

### DHCP Server/Relay
No DHCP server configurations are found, but a DHCP relay helper address is used on the switch.

### NTP (Network Time Protocol)
The following NTP servers and authentication keys are configured:

*   `ntp authentication-key 15 md5 KomplekstPassord`
*   `ntp trusted-key 15`

## Best Practices Analysis

### Good Practices Identified
None

### Potential Issues or Concerns
- Missing descriptions for some interfaces.
- Enable secret password should be longer than 8 characters and not reused.

### Recommendations for Improvement
1. Consider implementing a stronger enable secret password.
2. Add meaningful descriptions to all interfaces.
3. Implement QoS policies as per network requirements.
4. Configure the switch for high availability by setting up FHRP or other redundancy mechanisms.
5. Plan and implement an NTP server on the network.

## Configuration Summary
- **Total VLANs**: 4
- **Total Configured Interfaces**: 7 (active)
- **Routing**: Static routing using a default route.
- **Spanning Tree**: Rapid PVST+ mode with bridge priority for VLANs 11,12,90 set to 61440.
- **Key Features Enabled**: Port security on FastEthernet0/1 and FastEthernet0/2, DHCP snooping trust on GigabitEthernet0/1, NTP authentication key 15 md5 KomplekstPassord with trusted-key 15.

## Appendix

### Uncommon or Complex Configurations
No uncommon configurations found.