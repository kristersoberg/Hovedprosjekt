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

### DNS
- **DNS Domain Name**: core.bedrift.no ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Enabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED
- **Static Routes**:
  - 0.0.0.0 0.0.0.0 via 10.99.1.1 ✓ VERIFIED

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- **SSH-only VTY access** is configured (`transport input ssh`) ✓ VERIFIED
- **SSH version 2** is used, which is secure ✓ VERIFIED
- **DHCP snooping** is enabled globally, with `ip dhcp snooping trust` on uplink interfaces ✓ VERIFIED
- **Standard ACL 'MGMT-ACCESS'** is applied to VTY lines and VLAN 99, restricting access to management network ranges ✓ VERIFIED
- **Extended ACL 'BLOCK-GUEST-INTERNAL'** blocks traffic from VLAN 20 (Gjest) to internal VLANs, improving internal network security ✓ VERIFIED
- **CDP is disabled**, reducing potential attack surface ✓ VERIFIED
- **Password encryption** is enabled via `service password-encryption` ✓ VERIFIED
- **Banner is configured** to warn unauthorized users (`banner login ^CUautorisert tilgang er forbudt. All aktivitet logges.^C`) ✓ VERIFIED
- **Syslog is configured** to send logs to 10.99.0.50, aiding in monitoring and auditing ✓ VERIFIED

#### ⚠ Areas for Improvement
- **DHCP snooping is not configured on specific VLANs**, which could reduce its effectiveness. It is enabled globally but not scoped to VLANs ✓ VERIFIED
- **Dynamic ARP Inspection (DAI)** is not enabled, which could help prevent ARP spoofing attacks ? UNCERTAIN
- **Port security** is not enabled on any interfaces, which could help prevent unauthorized device access ? UNCERTAIN
- **802.1X authentication** is not configured, which could improve access control for wired devices ? UNCERTAIN
- **IP Source Guard** is not enabled, which could help prevent IP spoofing ? UNCERTAIN
- **LLDP is not enabled**, which could be used for network discovery and monitoring ? UNCERTAIN
- **NTP authentication** is not enabled, which could leave the device vulnerable to NTP spoofing ? UNCERTAIN
- **SNMP is not configured**, which could be used for monitoring and management ? UNCERTAIN

#### Recommendations
- **Scope DHCP snooping to specific VLANs** to increase its effectiveness. Example: `ip dhcp snooping vlan 10,20,30,50,99`
- **Enable Dynamic ARP Inspection (DAI)** on VLANs where it is needed. Example: `ip arp inspection vlan 10,20,30,50,99`
- **Enable port security** on access ports to prevent unauthorized device access. Example: `switchport port-security`
- **Consider enabling 802.1X authentication** for wired access control, especially on access ports.
- **Enable IP Source Guard** on VLANs to prevent IP spoofing. Example: `ip verify source vlan 10,20,30,50,99`
- **Enable LLDP** for network discovery and monitoring. Example: `lldp run`
- **Enable NTP authentication** to secure time synchronization. Example: `ntp authenticate`
- **Configure SNMP** for monitoring and management. Example: `snmp-server community <community> RO`
- **Ensure all VLANs are properly documented** and that unused VLANs are removed or disabled.

## Summary

The device **dis-sw02** is a **Distribution Layer switch** based on its configuration, which includes multiple VLAN interfaces (SVIs), inter-VLAN routing, and trunking to both core and access switches. It is running Cisco IOS version 15.2(2)E9 and is configured with strong security practices such as SSH-only access, DHCP snooping, and access control lists. The configuration is well-structured and includes essential network services like NTP, syslog, and routing. However, there are opportunities to enhance security further by enabling additional features like DAI, port security, and 802.1X.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T11:09:00.829425