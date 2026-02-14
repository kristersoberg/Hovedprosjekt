# Network Device Documentation: switch-03

## Device Information
- **Hostname**: switch-03 ✓ VERIFIED  
- **IOS Version**: 15.0(2)SE4 ✓ VERIFIED  
- **Domain Name**: intern.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

## Management & Access
- **Management VLAN**: 99 ✓ VERIFIED  
- **IP Address**: 10.99.1.3 ✓ VERIFIED  
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **VTY Transport Input**: ssh ✓ VERIFIED  
- **VTY Access Class**: MGMT-ACCESS (in) ✓ VERIFIED  
- **Console Access**: Line con 0, no authentication, logging synchronous enabled ✓ VERIFIED  

## AAA Configuration
- **AAA**: Not enabled ✓ VERIFIED  

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED  
- **VLAN IDs**: 10, 20, 30, 99, 666 ✓ VERIFIED  
- **VLAN Interfaces (SVIs)**: 2 configured ✓ VERIFIED  

### VLAN Interface Details
- **VLAN 1**  
  - Status: Shutdown ✓ VERIFIED  
- **VLAN 99**  
  - Description: Management SVI ✓ VERIFIED  
  - IP Address: 10.99.1.3 /24 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - ACL In: MGMT-ACCESS ✓ VERIFIED  

- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED  
- **Active (no shutdown)**: 8 ✓ VERIFIED  
- **Shutdown**: 18 ✓ VERIFIED  
- **Access Ports**: 6 ✓ VERIFIED  
- **Trunk Ports**: 2 ✓ VERIFIED  
- **Port Security Enabled**: 6 interfaces ✓ VERIFIED  

### Key Interface Configurations
- **FastEthernet0/1**  
  - Description: Ansatt-PC kontor A101  
  - Mode: access  
  - VLAN: 10  
  - Port-Sec: ✓  
  - Config Line: `switchport port-security`  
  - DHCP Snooping Rate Limit: 10  
  - Storm Control: Broadcast level 5  
  - PortFast: Enabled  
  - BPDU Guard: Enabled  

- **FastEthernet0/2**  
  - Description: Ansatt-PC kontor A102  
  - Mode: access  
  - VLAN: 10  
  - Port-Sec: ✓  
  - Config Line: `switchport port-security`  
  - DHCP Snooping Rate Limit: 10  
  - Storm Control: Broadcast level 5  
  - PortFast: Enabled  
  - BPDU Guard: Enabled  

- **FastEthernet0/3**  
  - Description: Ansatt-PC kontor A103  
  - Mode: access  
  - VLAN: 10  
  - Port-Sec: ✓  
  - Config Line: `switchport port-security`  
  - DHCP Snooping Rate Limit: 10  
  - Storm Control: Broadcast level 5  
  - PortFast: Enabled  
  - BPDU Guard: Enabled  

- **FastEthernet0/4**  
  - Description: Gjestenettverk moeterom B1  
  - Mode: access  
  - VLAN: 20  
  - Port-Sec: ✓  
  - Config Line: `switchport port-security`  
  - DHCP Snooping Rate Limit: 10  
  - Storm Control: Broadcast level 5  
  - PortFast: Enabled  
  - BPDU Guard: Enabled  

- **FastEthernet0/5**  
  - Description: Gjestenettverk moeterom B2  
  - Mode: access  
  - VLAN: 20  
  - Port-Sec: ✓  
  - Config Line: `switchport port-security`  
  - DHCP Snooping Rate Limit: 10  
  - Storm Control: Broadcast level 5  
  - PortFast: Enabled  
  - BPDU Guard: Enabled  

- **FastEthernet0/6**  
  - Description: Nettverksskriver 3. etasje  
  - Mode: access  
  - VLAN: 30  
  - Port-Sec: ✓  
  - Config Line: `switchport port-security`  
  - Port Security Violation: shutdown  
  - PortFast: Enabled  
  - BPDU Guard: Enabled  

- **FastEthernet0/23**  
  - Description: Uplink-1 dis-sw01 fa0/3  
  - Mode: trunk  
  - Native VLAN: 666  
  - Allowed VLANs: 10, 20, 30, 99  
  - Config Line: `switchport trunk allowed vlan 10,20,30,99`  
  - DHCP Snooping Trust: Enabled  
  - ARP Inspection Trust: Enabled  

- **FastEthernet0/24**  
  - Description: Uplink-2 dis-sw02 fa0/3  
  - Mode: trunk  
  - Native VLAN: 666  
  - Allowed VLANs: 10, 20, 30, 99  
  - Config Line: `switchport trunk allowed vlan 10,20,30,99`  
  - DHCP Snooping Trust: Enabled  
  - ARP Inspection Trust: Enabled  

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED  
- **Per-VLAN Priorities**:  
  - VLAN 10: 32768 ✓ VERIFIED  
  - VLAN 20: 32768 ✓ VERIFIED  
  - VLAN 30: 32768 ✓ VERIFIED  
  - VLAN 99: 32768 ✓ VERIFIED  

## Security Features
- **DHCP Snooping**: ✓ Enabled on VLANs 10, 20, 30 ✓ VERIFIED  
  - Information Option: Disabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: ✓ Enabled on VLANs 10, 20, 30 ✓ VERIFIED  
- **Port Security**: Enabled on 6 interfaces ✓ VERIFIED  
- **Access Control Lists (ACLs)**: 1 configured  
  - **Standard ACL 'MGMT-ACCESS'**:  
    - Permit 10.99.0.0/24  
    - Permit 10.99.1.0/24  
    - Deny any  
    - Applied on VLAN 99 (in) ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  
- **Logging Level**: Warnings ✓ VERIFIED  

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED  
- **NTP Authentication**: Disabled ✓ VERIFIED  

### Syslog
- **Syslog Enabled**: ✓  
- **Syslog Server**: 10.99.0.50 ✓ VERIFIED  

### SNMP
- **SNMP**: Not configured ✓ VERIFIED  

### DNS
- **DNS Domain Name**: intern.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  

## Configuration Quality Assessment

### Device Role
- **Device Role**: ~ INFERRED  
  - This is an **Access Layer** switch.  
  - Justification:  
    - High number of access ports (6) with port security  
    - No routing enabled  
    - VLAN interfaces (SVIs) are minimal and only used for management  
    - Trunk ports are used for uplink to distribution layer  

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a timeout of 60 seconds ✓ VERIFIED  
- Port security is enabled on 6 access ports ✓ VERIFIED  
- DHCP snooping is enabled on VLANs 10, 20, 30 ✓ VERIFIED  
- Dynamic ARP Inspection (DAI) is enabled on VLANs 10, 20, 30 ✓ VERIFIED  
- CDP is disabled, reducing potential attack surface ✓ VERIFIED  
- A standard ACL (`MGMT-ACCESS`) is applied to the management VLAN to restrict access ✓ VERIFIED  
- PortFast and BPDU Guard are enabled on access ports to prevent STP loops ✓ VERIFIED  

#### ⚠ Areas for Improvement
- AAA is not enabled, so there is no centralized authentication, authorization, or accounting ✓ VERIFIED  
- 802.1X is not configured, so port-based authentication is missing ✓ VERIFIED  
- IP Source Guard is not enabled, which could help prevent IP spoofing ✓ VERIFIED  
- SNMP is not configured, which limits monitoring and management capabilities ✓ VERIFIED  
- No password is set for the `line vty` or `line con 0`, allowing unauthenticated access (if not using AAA) ✓ VERIFIED  
- No password is set for the `enable` command (only `enable secret` is configured) ✓ VERIFIED  

#### Recommendations
- Enable AAA for centralized authentication and authorization  
- Implement 802.1X for port-based authentication  
- Enable IP Source Guard on VLANs 10, 20, 30 to prevent IP spoofing  
- Configure SNMP for monitoring and management  
- Set passwords for `line vty` and `line con 0` to enforce authentication  
- Enable NTP authentication to secure time synchronization  
- Consider enabling LLDP for network discovery and troubleshooting  
- Review and tighten the `MGMT-ACCESS` ACL to ensure only authorized networks can access the management VLAN  

## Summary

switch-03 is an **Access Layer** switch configured to provide network access to end devices such as employee PCs, guest devices, and printers. It is connected to a distribution layer via two trunk ports and has port security, DHCP snooping, and DAI enabled for security. The device is managed via VLAN 99 with SSH access restricted by an ACL. While the configuration includes several good security practices, it lacks centralized authentication (AAA), 802.1X, and IP Source Guard, which could be improved to enhance the security posture.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T10:02:38.715922