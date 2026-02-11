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
- **VLAN 1**
  - Status: Shutdown ✓ VERIFIED

- **VLAN 10**
  - Description: Ansatte Gateway ✓ VERIFIED
  - IP: 10.10.0.3 255.255.255.0 ✓ VERIFIED
  - Status: Active ✓ VERIFIED
  - HSRP: Configured ✓ VERIFIED

- **VLAN 20**
  - Description: Gjest Gateway ✓ VERIFIED
  - IP: 10.20.0.3 255.255.255.0 ✓ VERIFIED
  - Status: Active ✓ VERIFIED
  - HSRP: Configured ✓ VERIFIED

- **VLAN 30**
  - Description: Skrivere Gateway ✓ VERIFIED
  - IP: 10.30.0.3 255.255.255.0 ✓ VERIFIED
  - Status: Active ✓ VERIFIED
  - HSRP: Configured ✓ VERIFIED

- **VLAN 50**
  - Description: VoIP Gateway ✓ VERIFIED
  - IP: 10.50.0.3 255.255.255.0 ✓ VERIFIED
  - Status: Active ✓ VERIFIED
  - HSRP: Configured ✓ VERIFIED

- **VLAN 99**
  - Description: Management ✓ VERIFIED
  - IP: 10.99.1.3 255.255.255.0 ✓ VERIFIED
  - Status: Active ✓ VERIFIED
  - ACL In: MGMT-ACCESS ✓ VERIFIED

- **VTP Configuration**: Not explicitly configured ✓ VERIFIED

## Physical Interfaces
- **Total Interfaces**: 6 ✓ VERIFIED
- **Active (no shutdown)**: 4 ✓ VERIFIED
- **Shutdown**: 2 ✓ VERIFIED

### Active Interfaces
- **GigabitEthernet0/1** - Uplink til core-sw01 gig0/3 | Mode: trunk | Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED
- **GigabitEthernet0/2** - Uplink til core-sw01 gig0/4 | Mode: trunk | Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED
- **GigabitEthernet0/3** - Downlink aksess-sw03 fa0/24 | Mode: trunk | Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED
- **GigabitEthernet0/4** - Downlink aksess-sw04 fa0/24 | Mode: trunk | Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED

### Per-VLAN Priorities
- **VLAN 10**: 8192 ✓ VERIFIED
- **VLAN 20**: 8192 ✓ VERIFIED
- **VLAN 30**: 8192 ✓ VERIFIED
- **VLAN 50**: 8192 ✓ VERIFIED
- **VLAN 99**: 8192 ✓ VERIFIED

## Security Features
- **DHCP Snooping**: ✓ Enabled on VLANs Not specified ✓ VERIFIED
  - Information Option: Enabled ✓ VERIFIED
- **Dynamic ARP Inspection**: Not enabled ✓ VERIFIED
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED
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

### DNS
- **DNS Domain Name**: core.bedrift.no ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Enabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED

### Static Routes
- **0.0.0.0 0.0.0.0 via 10.99.1.1** ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, providing secure remote access. (Config lines: `ip ssh version 2`, `ip ssh time-out 60`)
- AAA is enabled with local authentication for console and VTY access, ensuring user accountability. (Config lines: `aaa new-model`, `aaa authentication login default local`, `aaa authentication login CONSOLE local`)
- DHCP snooping is enabled globally, helping prevent rogue DHCP servers. (Config line: `ip dhcp snooping`)
- A standard ACL (`MGMT-ACCESS`) is applied to VTY lines, restricting remote access to trusted subnets. (Config lines: `access-class MGMT-ACCESS in`, `ip access-list standard MGMT-ACCESS`)
- CDP is explicitly disabled, reducing the risk of network discovery attacks. (Config line: `no cdp run`)
- A banner is configured to warn unauthorized users. (Config line: `banner login ^CUautorisert tilgang er forbudt. All aktivitet logges.^C`)
- A guest VLAN (VLAN 20) is isolated from internal VLANs using an extended ACL (`BLOCK-GUEST-INTERNAL`). (Config line: `ip access-list extended BLOCK-GUEST-INTERNAL`)

#### ⚠ Areas for Improvement
- **Dynamic ARP Inspection (DAI)** is not enabled, which could leave the network vulnerable to ARP spoofing attacks.
- **Port security** is not enabled on any interfaces, which could allow unauthorized devices to connect to the network.
- **802.1X authentication** is not configured, which could leave the network open to unauthorized access.
- **IP Source Guard** is not enabled, which could allow spoofed IP addresses to be used on the network.
- **DHCP snooping** is enabled globally but not restricted to specific VLANs, which could allow rogue DHCP servers to operate in untrusted VLANs.
- **LLDP** is not enabled, which could limit network visibility and troubleshooting capabilities.
- **SNMP** is not configured, which could limit monitoring and management capabilities.

#### Recommendations
- Enable **Dynamic ARP Inspection (DAI)** on VLANs where it is needed to prevent ARP spoofing.
- Enable **port security** on access ports to prevent unauthorized devices from connecting to the network.
- Consider implementing **802.1X authentication** for secure user and device authentication.
- Enable **IP Source Guard** to prevent IP address spoofing.
- Specify **DHCP snooping VLANs** to limit the scope of trusted DHCP servers.
- Enable **LLDP** to improve network visibility and troubleshooting.
- Configure **SNMP** to enable monitoring and management of the device.

## Summary

dis-sw02 is a **Distribution Layer** switch, as evidenced by the presence of multiple VLAN interfaces (SVIs), inter-VLAN routing, and trunk links to both core and access switches. The device is configured with a strong baseline of security features, including SSH, AAA, and ACLs, but lacks some advanced security mechanisms such as DAI and port security. The configuration is well-structured and includes essential network services such as NTP, syslog, and routing. The device plays a central role in aggregating traffic between access switches and the core, and its configuration reflects a professional, enterprise-grade setup.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T02:38:59.015521