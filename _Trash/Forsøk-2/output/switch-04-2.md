# Network Device Documentation: dis-sw01

## Device Information
- **Hostname**: dis-sw01 ✓ VERIFIED  
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED  
- **Domain Name**: core.bedrift.no ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: 10 ✓ VERIFIED  
- **IP Address**: 10.10.0.2 ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **VTY Transport Input**: ssh ✓ VERIFIED  

---

## AAA Configuration
- **AAA**: ✓ Enabled ✓ VERIFIED  
  - **Authentication Lists**:
    - `aaa authentication login default local` ✓ VERIFIED  
    - `aaa authentication login CONSOLE local` ✓ VERIFIED  
  - **Authorization Lists**:
    - `aaa authorization exec default local` ✓ VERIFIED  
  - **Local Users**:
    - `netadmin` (privilege 15) ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 6 ✓ VERIFIED  
- **VLAN IDs**: 10, 20, 30, 50, 99, 666 ✓ VERIFIED  
- **VLAN Interfaces (SVIs)**: 6 configured ✓ VERIFIED  

### VLAN Details
- **VLAN 1**:
  - Status: Shutdown ✓ VERIFIED  
- **VLAN 10**:
  - Description: Ansatte Gateway ✓ VERIFIED  
  - IP: 10.10.0.2 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - HSRP: Configured ✓ VERIFIED  
- **VLAN 20**:
  - Description: Gjest Gateway ✓ VERIFIED  
  - IP: 10.20.0.2 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - HSRP: Configured ✓ VERIFIED  
- **VLAN 30**:
  - Description: Skrivere Gateway ✓ VERIFIED  
  - IP: 10.30.0.2 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - HSRP: Configured ✓ VERIFIED  
- **VLAN 50**:
  - Description: VoIP Gateway ✓ VERIFIED  
  - IP: 10.50.0.2 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - HSRP: Configured ✓ VERIFIED  
- **VLAN 99**:
  - Description: Management ✓ VERIFIED  
  - IP: 10.99.1.2 255.255.255.0 ✓ VERIFIED  
  - Status: Active ✓ VERIFIED  
  - ACL In: `MGMT-ACCESS` ✓ VERIFIED  

- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 6 ✓ VERIFIED  
- **Active (no shutdown)**: 4 ✓ VERIFIED  
- **Shutdown**: 2 ✓ VERIFIED  

### Key Interface Configurations
- **GigabitEthernet0/1**:
  - Description: Uplink til core-sw01 gig0/1 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
  - DHCP Snooping Trust: Enabled ✓ VERIFIED  
- **GigabitEthernet0/2**:
  - Description: Uplink til core-sw01 gig0/2 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
  - DHCP Snooping Trust: Enabled ✓ VERIFIED  
- **GigabitEthernet0/3**:
  - Description: Downlink aksess-sw03 fa0/23 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
- **GigabitEthernet0/4**:
  - Description: Downlink aksess-sw04 fa0/23 ✓ VERIFIED  
  - Mode: trunk ✓ VERIFIED  
  - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED  
  - Native VLAN: 666 ✓ VERIFIED  
- **GigabitEthernet0/5**:
  - Status: Shutdown ✓ VERIFIED  
- **GigabitEthernet0/6**:
  - Status: Shutdown ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: rapid-pvst ✓ VERIFIED  
- **Per-VLAN Priorities**:
  - VLAN 10: 4096 ✓ VERIFIED  
  - VLAN 20: 4096 ✓ VERIFIED  
  - VLAN 30: 4096 ✓ VERIFIED  
  - VLAN 50: 4096 ✓ VERIFIED  
  - VLAN 99: 4096 ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: ✓ Enabled on VLANs Not specified ✓ VERIFIED  
  - Information Option: Enabled ✓ VERIFIED  
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED  
- **Port Security**: Not configured on any interfaces ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **CDP**: Disabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  

### Access Control Lists (ACLs)
- **Standard ACL 'MGMT-ACCESS'**: 3 entries ✓ VERIFIED  
- **Extended ACL 'BLOCK-GUEST-INTERNAL'**: 5 entries ✓ VERIFIED  

---

## Network Services

### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  
- **Logging Level**: informational ✓ VERIFIED  

### NTP
- **NTP Server**: 10.99.0.1 ✓ VERIFIED  
- **NTP Authentication**: Disabled ✓ VERIFIED  

### Syslog
- **Syslog Enabled**: ✓ Enabled ✓ VERIFIED  

### SNMP
- **SNMP**: Not configured ✓ VERIFIED  

### DNS
- **DNS Domain Name**: core.bedrift.no ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Enabled ✓ VERIFIED  
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED  

### Static Routes
- **0.0.0.0 0.0.0.0 via 10.99.1.1** ✓ VERIFIED  

---

## Configuration Quality Assessment

### Device Role
- **Device Role**: ~ INFERRED  
  - This device is a **Distribution Layer** switch.  
  - Justification: It has multiple VLAN interfaces (SVIs) with IP addresses, inter-VLAN routing enabled, and trunk links to both core and access switches. It also has HSRP configured for redundancy.  

---

### Security Posture

#### ✓ Strengths
- SSH is configured with version 2 and a 60-second timeout, ensuring secure remote access.  
- AAA is enabled with local authentication and authorization, providing a baseline for access control.  
- DHCP snooping is enabled globally, helping prevent rogue DHCP servers.  
- CDP is disabled, reducing the risk of lateral discovery.  
- A standard ACL (`MGMT-ACCESS`) is applied to the management VLAN to restrict access.  
- An extended ACL (`BLOCK-GUEST-INTERNAL`) is configured to block traffic from the guest VLAN to internal networks.  

#### ⚠ Areas for Improvement
- **Dynamic ARP Inspection (DAI)** is not enabled, which could leave the network vulnerable to ARP spoofing.  
- **Port security** is not configured on any interfaces, which could allow unauthorized devices to connect.  
- **802.1X** is not enabled, which means there is no port-level authentication for wired devices.  
- **IP Source Guard** is not enabled, which could allow spoofed IP addresses to bypass ACLs.  
- **LLDP** is not enabled, which could limit visibility into connected devices.  
- **SNMP** is not configured, which limits monitoring and management capabilities.  
- **DHCP snooping** is enabled globally but not scoped to specific VLANs, which could reduce its effectiveness.  

#### Recommendations
- Enable **Dynamic ARP Inspection (DAI)** on VLANs 10, 20, 30, 50, and 99 to prevent ARP spoofing.  
- Configure **port security** on access ports to limit the number of MAC addresses allowed per port.  
- Enable **802.1X** for wired device authentication, especially on ports connected to user devices.  
- Enable **IP Source Guard** on VLANs to prevent IP address spoofing.  
- Enable **LLDP** to improve visibility into connected devices.  
- Configure **SNMP** with appropriate community strings and access controls for monitoring.  
- Scope **DHCP snooping** to specific VLANs (e.g., VLANs 10, 20, 30, 50, 99) to improve security.  

---

## Summary

dis-sw01 is a **Distribution Layer** switch running Cisco IOS 15.2(2)E9. It serves as an aggregation point between access switches and the core, with multiple VLAN interfaces and inter-VLAN routing enabled. The configuration includes basic security features such as SSH, AAA, and DHCP snooping, but lacks advanced protections like DAI, port security, and 802.1X. The device is well-documented and configured for redundancy with HSRP, but further hardening is recommended to improve its security posture.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-11T08:41:21.038348