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
- **RADIUS Servers**: 10.99.0.30, 10.99.0.31 ✓ VERIFIED  
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
  - Description: 802.1X-port kontor C301 ✓ VERIFIED  
  - Mode: access ✓ VERIFIED  
  - VLAN: 10 ✓ VERIFIED  
  - Port-Sec: ✓ VERIFIED  
- **FastEthernet0/2**:
  - Description: 802.1X-port kontor C302 ✓ VERIFIED  
  - Mode: access ✓ VERIFIED  
  - VLAN: 10 ✓ VERIFIED  
  - Port-Sec: ✓ VERIFIED  
- **FastEthernet0/3**:
  - Description: 802.1X-port kontor C303 ✓ VERIFIED  
  - Mode: access ✓ VERIFIED  
  - VLAN: 10 ✓ VERIFIED  
  - Port-Sec: ✓ VERIFIED  
- **FastEthernet0/4**:
  - Description: 802.1X-port kontor C304 ✓ VERIFIED  
  - Mode: access ✓ VERIFIED  
  - VLAN: 10 ✓ VERIFIED  
  - Port-Sec: ✓ VERIFIED  
- **FastEthernet0/23**:
  - Description: Uplink-1 dis-sw01 gig0/5 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 99, 999 ✓ VERIFIED  
- **FastEthernet0/24**:
  - Description: Uplink-2 dis-sw02 gig0/5 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 99, 999 ✓ VERIFIED  

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
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  

## Network Services
### Logging
- **Syslog Enabled**: ✓ VERIFIED  
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  
- **Logging Trap Level**: informational ✓ VERIFIED  

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
  - 3 entries ✓ VERIFIED  
  - `permit 10.99.0.0 0.0.0.255` ✓ VERIFIED  
  - `permit 10.99.1.0 0.0.0.255` ✓ VERIFIED  
  - `deny any` ✓ VERIFIED  

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- **SSH-only VTY access** with timeout and authentication-retries configured (lines `ip ssh version 2`, `ip ssh time-out 60`, `ip ssh authentication-retries 2`) ✓ VERIFIED  
- **Port security** enabled on 4 access ports (e.g., `switchport port-security`, `switchport port-security maximum 3`) ✓ VERIFIED  
- **802.1X authentication** enabled with RADIUS integration (lines `dot1x system-auth-control`, `aaa authentication dot1x default group radius`) ✓ VERIFIED  
- **DHCP snooping** enabled on VLANs 10 and 20 (line `ip dhcp snooping vlan 10,20`) ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)** enabled on VLANs 10 and 20 (line `ip arp inspection vlan 10,20`) ✓ VERIFIED  
- **CDP is disabled** (line `no cdp run`) ✓ VERIFIED  
- **Local emergency admin user** with privilege 15 (line `username emergency-admin privilege 15 secret 5 <REDACTED>`) ✓ VERIFIED  
- **Syslog logging** configured to 10.99.0.50 with informational level (lines `logging 10.99.0.50`, `logging trap informational`) ✓ VERIFIED  

#### ⚠ Areas for Improvement
- **NTP is not configured**, which could impact time-sensitive operations and log correlation.  
- **SNMP is not configured**, which limits monitoring and management capabilities.  
- **IP Source Guard** is not enabled, which could leave the network vulnerable to IP spoofing.  
- **LLDP is not enabled**, which could hinder network discovery and troubleshooting.  
- **No VTP configuration** is present, which may be intentional but should be documented.  
- **No VLAN 1 is used**, but it is still defined and active as an SVI. It should be shut down or removed if not in use.  

#### Recommendations
- **Enable NTP** with at least one NTP server to ensure accurate time synchronization.  
- **Enable SNMP** with appropriate community strings and access control for monitoring.  
- **Enable IP Source Guard** on VLANs 10 and 20 to prevent IP spoofing.  
- **Enable LLDP** to improve network visibility and troubleshooting.  
- **Shut down VLAN 1** if it is not in use to reduce attack surface.  
- **Document VTP configuration status** to clarify whether it is intentionally disabled or not required.  
- **Consider enabling port security violation shutdown** instead of `restrict` to prevent unauthorized devices from connecting.  

## Summary

This device, **switch-06**, is an **Access layer switch** based on its configuration, which includes multiple access ports with 802.1X authentication, port security, and VLAN-based services. It is not performing routing and is connected to a distribution layer via trunk links. The configuration is generally secure, with SSH-only access, AAA with RADIUS, and security features like DHCP snooping and DAI enabled. However, there are opportunities to improve by enabling NTP, SNMP, and IP Source Guard.  

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T15:35:11.098326