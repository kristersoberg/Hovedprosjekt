# Network Device Documentation: dis-sw02

## Device Information
- **Hostname**: dis-sw02 ✓ VERIFIED
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED
- **Domain Name**: core.bedrift.no ✓ VERIFIED
- **Config Register**: Not configured ✓ VERIFIED

## Management & Access
- **Management VLAN**: 10 ✓ VERIFIED
- **IP Address**: 10.10.0.3 ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED
- **SSH Version**: 2 ✓ VERIFIED
- **SSH Timeout**: 60 seconds ✓ VERIFIED
- **VTY Transport Input**: ssh ✓ VERIFIED
- **VTY Access Class**: MGMT-ACCESS (in) ✓ VERIFIED

## AAA Configuration
- **AAA Enabled**: ✓ VERIFIED
- **Authentication Login Default**: local ✓ VERIFIED
- **Authentication Login CONSOLE**: local ✓ VERIFIED
- **Authorization Exec Default**: local ✓ VERIFIED
- **Local Users**: netadmin (privilege 15) ✓ VERIFIED

## VLANs
- **Total VLANs Referenced**: 6 ✓ VERIFIED
- **VLAN IDs**: 10, 20, 30, 50, 99, 666 ✓ VERIFIED
- **VLAN Interfaces (SVIs)**: 6 configured ✓ VERIFIED

### VLAN Details
- **VLAN 1**:
  - Status: Shutdown ✓ VERIFIED
- **VLAN 10**:
  - Description: Ansatte Gateway ✓ VERIFIED
  - IP: 10.10.0.3 255.255.255.0 ✓ VERIFIED
  - Status: Active ✓ VERIFIED
  - HSRP: Configured ✓ VERIFIED
- **VLAN 20**:
  - Description: Gjest Gateway ✓ VERIFIED
  - IP: 10.20.0.3 255.255.255.0 ✓ VERIFIED
  - Status: Active ✓ VERIFIED
  - HSRP: Configured ✓ VERIFIED
- **VLAN 30**:
  - Description: Skrivere Gateway ✓ VERIFIED
  - IP: 10.30.0.3 255.255.255.0 ✓ VERIFIED
  - Status: Active ✓ VERIFIED
  - HSRP: Configured ✓ VERIFIED
- **VLAN 50**:
  - Description: VoIP Gateway ✓ VERIFIED
  - IP: 10.50.0.3 255.255.255.0 ✓ VERIFIED
  - Status: Active ✓ VERIFIED
  - HSRP: Configured ✓ VERIFIED
- **VLAN 99**:
  - Description: Management ✓ VERIFIED
  - IP: 10.99.1.3 255.255.255.0 ✓ VERIFIED
  - Status: Active ✓ VERIFIED
  - ACL In: MGMT-ACCESS ✓ VERIFIED

- **VTP Configuration**: Not explicitly configured ✓ VERIFIED

## Physical Interfaces
- **Total Interfaces**: 6 ✓ VERIFIED
- **Active (no shutdown)**: 4 ✓ VERIFIED
- **Shutdown**: 2 ✓ VERIFIED
- **Access Ports**: 0 ✓ VERIFIED
- **Trunk Ports**: 4 ✓ VERIFIED
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED

### Detailed Interface List
- **GigabitEthernet0/1** - Uplink til core-sw01 gig0/3 | Mode: trunk | Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED
- **GigabitEthernet0/2** - Uplink til core-sw01 gig0/4 | Mode: trunk | Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED
- **GigabitEthernet0/3** - Downlink aksess-sw03 fa0/24 | Mode: trunk | Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED
- **GigabitEthernet0/4** - Downlink aksess-sw04 fa0/24 | Mode: trunk | Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED
- **GigabitEthernet0/5** - Shutdown ✓ VERIFIED
- **GigabitEthernet0/6** - Shutdown ✓ VERIFIED

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED
- **Per-VLAN Priorities**:
  - VLAN 10: 8192 ✓ VERIFIED
  - VLAN 20: 8192 ✓ VERIFIED
  - VLAN 30: 8192 ✓ VERIFIED
  - VLAN 50: 8192 ✓ VERIFIED
  - VLAN 99: 8192 ✓ VERIFIED

## Security Features
- **DHCP Snooping**: ✓ Enabled on VLANs Not specified ✓ VERIFIED
  - Information Option: Enabled ✓ VERIFIED
- **Dynamic ARP Inspection**: Not enabled ✓ VERIFIED
- **Access Control Lists**:
  - Standard ACL 'MGMT-ACCESS': 3 entries ✓ VERIFIED
  - Extended ACL 'BLOCK-GUEST-INTERNAL': 5 entries ✓ VERIFIED
- **CDP**: Disabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED
- **802.1X**: Not configured ✓ VERIFIED
- **IP Source Guard**: Not configured ✓ VERIFIED

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED
- **Logging Level**: informational ✓ VERIFIED (from `logging trap informational`)

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED
- **NTP Authentication**: Disabled ✓ VERIFIED

### Syslog
- **Syslog Enabled**: ✓ VERIFIED
- **Syslog Server**: 10.99.0.50 ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

### DNS
- **DNS Domain Name**: core.bedrift.no ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Enabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED
- **Static Routes**:
  - 0.0.0.0 0.0.0.0 via 10.99.1.1 ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, ensuring secure remote access. (Config line: `ip ssh version 2`, `ip ssh time-out 60`)
- AAA is enabled with local authentication for console and VTY access, ensuring user accountability. (Config lines: `aaa new-model`, `aaa authentication login default local`, `aaa authentication login CONSOLE local`)
- DHCP snooping is enabled globally, helping prevent rogue DHCP servers. (Config line: `ip dhcp snooping`)
- A standard ACL (`MGMT-ACCESS`) is applied to VTY lines to restrict remote access to trusted subnets. (Config line: `access-class MGMT-ACCESS in`)
- CDP is explicitly disabled, reducing the risk of network discovery attacks. (Config line: `no cdp run`)
- A banner is configured to warn unauthorized users. (Config line: `banner login ^CUautorisert tilgang er forbudt. All aktivitet logges.^C`)
- Syslog is enabled with a remote server, providing centralized logging. (Config line: `logging 10.99.0.50`)
- NTP is configured for time synchronization. (Config line: `ntp server 10.99.0.1`)

#### ⚠ Areas for Improvement
- **DHCP Snooping VLANs**: DHCP snooping is enabled globally but not restricted to specific VLANs. It is recommended to specify VLANs to limit scope and improve security.
- **Dynamic ARP Inspection (DAI)**: Not enabled. DAI should be configured to prevent ARP spoofing attacks.
- **Port Security**: Not enabled on any interfaces. Port security should be implemented on access ports to prevent unauthorized device connections.
- **IP Source Guard**: Not enabled. IP Source Guard should be used in conjunction with DHCP snooping to prevent IP spoofing.
- **802.1X**: Not configured. If the network supports it, 802.1X should be implemented for secure port-based authentication.
- **NTP Authentication**: NTP is configured without authentication. Enabling NTP authentication would prevent time spoofing attacks.
- **LLDP**: Not enabled. LLDP could be used for network discovery and documentation, but it is not a security concern in this context.
- **VLAN 1**: VLAN 1 is still in use (SVI is configured and shutdown). It is best practice to disable VLAN 1 and use a different VLAN for native traffic.
- **Native VLAN Mismatch**: The native VLAN on trunk ports is set to 666, but it is not used in any VLAN configuration. This could lead to VLAN mismatch issues. It is recommended to use a non-default VLAN for native traffic and ensure consistency across the network.

#### Recommendations
- **Enable DAI** on VLANs where DHCP snooping is active.
- **Enable IP Source Guard** on VLANs with DHCP snooping.
- **Implement port security** on access ports to prevent unauthorized device connections.
- **Enable 802.1X** if the network supports it for secure port-based authentication.
- **Enable NTP authentication** to prevent time spoofing.
- **Specify VLANs for DHCP snooping** to limit scope and improve security.
- **Disable VLAN 1** and use a different VLAN for native traffic.
- **Ensure native VLAN consistency** across trunk ports to prevent VLAN mismatch issues.
- **Enable LLDP** if network discovery and documentation are required.
- **Review and tighten ACLs** to ensure they are as restrictive as possible without impacting legitimate traffic.

## Summary

The device `dis-sw02` is a **Distribution Layer switch** based on its configuration, which includes multiple VLAN interfaces (SVIs), inter-VLAN routing, and trunk ports connecting to both core and access switches. It is running Cisco IOS version 15.2(2)E9 and is configured with a strong baseline of security features such as SSH, AAA, and DHCP snooping. However, there are several areas for improvement, particularly in the areas of dynamic ARP inspection, port security, and VLAN management. The configuration is generally well-structured and follows best practices, but additional hardening measures are recommended to enhance security and operational reliability.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-10T21:44:18.371777