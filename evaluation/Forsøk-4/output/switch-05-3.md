# Network Device Documentation: dis-sw02

## Device Information
- **Hostname**: dis-sw02 ✓ VERIFIED
- **IOS Version**: 15.2(2)E9 ✓ VERIFIED
- **Domain Name**: core.bedrift.no ✓ VERIFIED
- **Config Register**: Not configured ✓ VERIFIED

---

## Management & Access
- **Management VLAN**: 10 ✓ VERIFIED
- **IP Address**: 10.10.0.3 ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED
- **SSH Version**: 2 ✓ VERIFIED
- **SSH Timeout**: 60 seconds ✓ VERIFIED
- **VTY Transport Input**: ssh ✓ VERIFIED
- **VTY Access Class**: MGMT-ACCESS (in) ✓ VERIFIED
- **Console Authentication**: CONSOLE ✓ VERIFIED
- **Console Logging Synchronous**: Enabled ✓ VERIFIED

---

## AAA Configuration
- **AAA Enabled**: ✓ VERIFIED
- **Authentication Methods**:
  - `aaa authentication login default local` ✓ VERIFIED
  - `aaa authentication login CONSOLE local` ✓ VERIFIED
- **Authorization Methods**:
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

---

## Physical Interfaces
- **Total Interfaces**: 6 ✓ VERIFIED
- **Active (no shutdown)**: 4 ✓ VERIFIED
- **Shutdown**: 2 ✓ VERIFIED
- **Access Ports**: 0 ✓ VERIFIED
- **Trunk Ports**: 4 ✓ VERIFIED
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED

### Detailed Interface List
- **GigabitEthernet0/1**:
  - Description: Uplink til core-sw01 gig0/3 ✓ VERIFIED
  - Mode: trunk ✓ VERIFIED
  - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED
  - Native VLAN: 666 ✓ VERIFIED
  - DHCP Snooping Trust: Enabled ✓ VERIFIED
- **GigabitEthernet0/2**:
  - Description: Uplink til core-sw01 gig0/4 ✓ VERIFIED
  - Mode: trunk ✓ VERIFIED
  - Allowed VLANs: 10, 20, 30, 50, 99 ✓ VERIFIED
  - Native VLAN: 666 ✓ VERIFIED
  - DHCP Snooping Trust: Enabled ✓ VERIFIED
- **GigabitEthernet0/3**:
  - Description: Downlink aksess-sw03 fa0/24 ✓ VERIFIED
  - Mode: trunk ✓ VERIFIED
  - Allowed VLANs: 10, 20, 30, 99 ✓ VERIFIED
  - Native VLAN: 666 ✓ VERIFIED
- **GigabitEthernet0/4**:
  - Description: Downlink aksess-sw04 fa0/24 ✓ VERIFIED
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
  - VLAN 10: 8192 ✓ VERIFIED
  - VLAN 20: 8192 ✓ VERIFIED
  - VLAN 30: 8192 ✓ VERIFIED
  - VLAN 50: 8192 ✓ VERIFIED
  - VLAN 99: 8192 ✓ VERIFIED

---

## Security Features
- **DHCP Snooping**: ✓ Enabled on VLANs Not specified ✓ VERIFIED
  - Information Option: Enabled ✓ VERIFIED
- **Dynamic ARP Inspection (DAI)**: Not enabled ✓ VERIFIED
- **Port Security**: Not enabled on any interfaces ✓ VERIFIED
- **802.1X**: Not configured ✓ VERIFIED
- **IP Source Guard**: Not configured ✓ VERIFIED
- **CDP**: Disabled ✓ VERIFIED
- **LLDP**: Not enabled ✓ VERIFIED

### Access Control Lists
- **Standard ACL 'MGMT-ACCESS'**: 3 entries ✓ VERIFIED
- **Extended ACL 'BLOCK-GUEST-INTERNAL'**: 5 entries ✓ VERIFIED

---

## Network Services

### Logging
- **Syslog Enabled**: ✓ VERIFIED
- **Logging Server**: 10.99.0.50 ✓ VERIFIED
- **Logging Level**: informational ✓ VERIFIED

### NTP
- **NTP Enabled**: ✓ VERIFIED
- **NTP Server**: 10.99.0.1 ✓ VERIFIED
- **NTP Authentication**: Disabled ✓ VERIFIED

### DNS
- **DNS Domain Name**: core.bedrift.no ✓ VERIFIED
- **DNS Lookup**: Disabled ✓ VERIFIED

### SNMP
- **SNMP**: Not configured ✓ VERIFIED

---

## Routing Configuration
- **IP Routing**: Enabled ✓ VERIFIED
- **Default Gateway**: 10.99.1.1 ✓ VERIFIED

### Static Routes
- **0.0.0.0 0.0.0.0 via 10.99.1.1** ✓ VERIFIED

---

## Configuration Quality Assessment

### Device Role
- **Role**: Distribution Layer Switch ~ INFERRED
  - Justification: The device has multiple VLAN interfaces (SVIs), inter-VLAN routing enabled, and trunk ports connecting to access switches and a core switch. It also has HSRP configured for redundancy, which is typical of a distribution layer device.

---

### Security Posture

#### ✓ Strengths
- SSH is enabled with version 2 and a 60-second timeout, preventing weak authentication methods. (Config lines: `ip ssh version 2`, `ip ssh time-out 60`)
- AAA is enabled with local authentication for console and VTY access, ensuring user accountability. (Config lines: `aaa new-model`, `aaa authentication login default local`, `aaa authentication login CONSOLE local`)
- DHCP snooping is enabled globally, helping prevent rogue DHCP servers. (Config line: `ip dhcp snooping`)
- CDP is explicitly disabled, reducing the risk of network discovery attacks. (Config line: `no cdp run`)
- A standard ACL (`MGMT-ACCESS`) is applied to the management VLAN to restrict access to trusted subnets.
- An extended ACL (`BLOCK-GUEST-INTERNAL`) is configured to block traffic from the guest VLAN to internal VLANs, improving internal network security.
- A banner is configured to warn unauthorized users. (Config line: `banner login ^CUautorisert tilgang er forbudt. All aktivitet logges.^C`)

#### ⚠ Areas for Improvement
- **Dynamic ARP Inspection (DAI)** is not enabled, which could leave the network vulnerable to ARP spoofing attacks.
- **Port security** is not enabled on any interfaces, which could allow unauthorized devices to connect to the network.
- **802.1X** is not configured, which means there is no port-level authentication for wired devices.
- **IP Source Guard** is not enabled, which could allow spoofed IP addresses to be used on the network.
- **LLDP** is not enabled, which could limit network visibility and troubleshooting capabilities.
- **VTP** is not configured, which may complicate VLAN management across the network.
- **SNMP** is not configured, which limits monitoring and management capabilities.

#### Recommendations
- Enable **Dynamic ARP Inspection (DAI)** on VLANs where it is needed to prevent ARP spoofing.
- Enable **port security** on access ports to prevent unauthorized device access.
- Consider implementing **802.1X** for wired device authentication.
- Enable **IP Source Guard** to prevent IP address spoofing.
- Enable **LLDP** to improve network visibility and troubleshooting.
- Consider configuring **VTP** if VLAN management across multiple switches is required.
- Configure **SNMP** to enable monitoring and management of the device.
- Consider enabling **DAI** and **IP Source Guard** on VLANs where they are needed to enhance security.

---

## Summary

The device `dis-sw02` is a **distribution layer switch** operating in a multi-VLAN environment with inter-VLAN routing enabled. It connects to access switches and a core switch via trunk ports and provides gateway services for VLANs 10, 20, 30, 50, and 99. The configuration includes strong security practices such as SSH, AAA, and ACLs, but lacks some advanced security features like DAI and port security. The configuration is well-structured and includes essential network services like NTP, syslog, and DNS.

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-14T14:49:45.423506