# Network Device Documentation: switch-06

## Device Information
- **Hostname**: switch-06 ✓ VERIFIED
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED
- **Domain Name**: secure.bedrift.no ✓ VERIFIED
- **Config Register**: Not configured ✓ VERIFIED

## Management & Access
- **Management VLAN**: 99 ✓ VERIFIED
- **IP Address**: 10.99.1.6 ✓ VERIFIED
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED
- **SSH Version**: 2 ✓ VERIFIED
- **SSH Timeout**: 60 seconds ✓ VERIFIED
- **VTY Transport Input**: ssh ✓ VERIFIED
- **VTY Authentication**: None ✓ VERIFIED
- **VTY Access Class**: MGMT-ACCESS (in) ✓ VERIFIED
- **Console Authentication**: CONSOLE ✓ VERIFIED
- **Console Logging Synchronous**: True ✓ VERIFIED

## AAA Configuration
- **AAA Enabled**: ✓ VERIFIED
- **Authentication Methods**:
  - `aaa authentication login default group radius local` ✓ VERIFIED
  - `aaa authentication login CONSOLE local` ✓ VERIFIED
  - `aaa authentication dot1x default group radius` ✓ VERIFIED
- **Authorization Methods**:
  - `aaa authorization network default group radius` ✓ VERIFIED
- **Accounting Methods**:
  - `aaa accounting dot1x default start-stop group radius` ✓ VERIFIED
- **RADIUS Servers**:
  - 10.99.0.30 ✓ VERIFIED
  - 10.99.0.31 ✓ VERIFIED
- **Local Users**:
  - `emergency-admin` (privilege 15) ✓ VERIFIED

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED
- **VLAN IDs**: 10, 20, 99, 666, 999 ✓ VERIFIED
- **VLAN Interfaces (SVIs)**:
  - **VLAN 1**:
    - Status: Shutdown ✓ VERIFIED
  - **VLAN 99**:
    - Description: Management SVI ✓ VERIFIED
    - IP: 10.99.1.6 255.255.255.0 ✓ VERIFIED
    - Status: Active ✓ VERIFIED
    - ACL In: MGMT-ACCESS ✓ VERIFIED
- **VTP Configuration**: Not explicitly configured ✓ VERIFIED

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED
- **Active (no shutdown)**: 6 ✓ VERIFIED
- **Shutdown**: 20 ✓ VERIFIED
- **Access Ports**: 4 ✓ VERIFIED
- **Trunk Ports**: 2 ✓ VERIFIED
- **Port Security Enabled**: 4 interfaces ✓ VERIFIED

### Key Active Interfaces
- **FastEthernet0/1**:
  - Description: 802.1X-port kontor C301
  - Mode: access
  - VLAN: 10
  - Port-Sec: ✓
- **FastEthernet0/2**:
  - Description: 802.1X-port kontor C302
  - Mode: access
  - VLAN: 10
  - Port-Sec: ✓
- **FastEthernet0/3**:
  - Description: 802.1X-port kontor C303
  - Mode: access
  - VLAN: 10
  - Port-Sec: ✓
- **FastEthernet0/4**:
  - Description: 802.1X-port kontor C304
  - Mode: access
  - VLAN: 10
  - Port-Sec: ✓
- **FastEthernet0/23**:
  - Description: Uplink-1 dis-sw01 gig0/5
  - Mode: trunk
  - Allowed VLANs: 10, 20, 99, 999
- **FastEthernet0/24**:
  - Description: Uplink-2 dis-sw02 gig0/5
  - Mode: trunk
  - Allowed VLANs: 10, 20, 99, 999

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED
- **Per-VLAN Priorities**:
  - VLAN 10: 32768 ✓ VERIFIED
  - VLAN 20: 32768 ✓ VERIFIED
  - VLAN 99: 32768 ✓ VERIFIED

## Security Features
- **DHCP Snooping**: ✓ Enabled on VLANs 10, 20 ✓ VERIFIED
  - Information Option: Disabled ✓ VERIFIED
- **Dynamic ARP Inspection (DAI)**: ✓ Enabled on VLANs 10, 20 ✓ VERIFIED
- **Port Security**: ✓ Enabled on 4 interfaces ✓ VERIFIED
- **802.1X**: ✓ Enabled ✓ VERIFIED
- **CDP**: ✓ Disabled ✓ VERIFIED
- **LLDP**: ? UNCERTAIN (Not enabled) ✓ VERIFIED
- **IP Source Guard**: ? UNCERTAIN (Not configured) ✓ VERIFIED

## Network Services
### Logging
- **Syslog Enabled**: ✓ VERIFIED
- **Logging Server**: 10.99.0.50 ✓ VERIFIED
- **Logging Level**: informational ✓ VERIFIED

### NTP
- **NTP Server**: Not configured ✓ VERIFIED
- **NTP Authentication**: Not configured ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

### DNS
- **DNS Domain Name**: secure.bedrift.no ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED

## Access Control Lists
- **Standard ACL 'MGMT-ACCESS'**:
  - Permit 10.99.0.0/24
  - Permit 10.99.1.0/24
  - Deny any
  - Applied on VLAN 99 (in) ✓ VERIFIED

## Configuration Quality Assessment

### Device Role
- **Device Role**: ~ INFERRED - **Access Layer Switch**
  - Justification: The device has multiple access ports with port security, 802.1X authentication, and no routing enabled. It connects end-user devices and uplinks to a distribution switch.

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, preventing weak authentication methods.
- AAA is enabled with RADIUS authentication for login and 802.1X, ensuring centralized authentication.
- DHCP snooping and Dynamic ARP Inspection (DAI) are enabled on VLANs 10 and 20, mitigating spoofing and ARP poisoning attacks.
- Port security is enabled on 4 access ports, limiting unauthorized device access.
- CDP is disabled, reducing the risk of network discovery and lateral movement.
- A standard ACL (`MGMT-ACCESS`) is applied to the management VLAN, restricting access to trusted subnets.
- A banner is configured to warn unauthorized users and log access attempts.

#### ⚠ Areas for Improvement
- **NTP is not configured**, which could lead to time synchronization issues and affect log correlation.
- **SNMP is not configured**, which may limit monitoring and management capabilities.
- **LLDP is not enabled**, which could be useful for network discovery and documentation.
- **IP Source Guard is not configured**, which could help prevent IP spoofing on VLANs with DHCP snooping.
- **VLAN 1 is not used** and is shut down, which is good, but it's still referenced in the configuration. Consider removing it if not needed.
- **VLAN 666 and 999 are referenced but not described**, which could be a security concern if they are not properly documented or used.

#### Recommendations
- **Enable NTP** with at least one NTP server to ensure accurate timekeeping.
- **Enable SNMP** with appropriate community strings and access controls for monitoring.
- **Enable LLDP** to assist with network discovery and documentation.
- **Enable IP Source Guard** on VLANs 10 and 20 to prevent IP spoofing.
- **Document VLAN 666 and 999** to ensure they are used as intended and are not misconfigured.
- **Remove VLAN 1 configuration** if it is not needed, to reduce attack surface.
- **Consider enabling IP Source Guard** on all VLANs with DHCP snooping.
- **Ensure RADIUS servers are monitored and redundant**, to avoid authentication outages.

## Summary

The device `switch-06` is an **Access Layer Switch** operating in a secure enterprise environment. It provides 802.1X authentication, port security, and DHCP snooping on VLANs 10 and 20. The device is managed via SSH and a dedicated management VLAN (VLAN 99), with access restricted by a standard ACL. The configuration is well-structured and includes several strong security features. However, there are opportunities to improve monitoring and time synchronization by enabling NTP and SNMP.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T15:22:19.716952