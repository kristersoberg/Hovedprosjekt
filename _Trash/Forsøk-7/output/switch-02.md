# Network Device Documentation: switch-02

## Device Information
- **Hostname**: switch-02 ✓ VERIFIED  
- **IOS Version**: 15.0(2)SE4 ✓ VERIFIED  
- **Domain Name**: firma.local ✓ VERIFIED  
- **Config Register**: Not configured ✓ VERIFIED  

---

## Management & Access
- **Management VLAN**: VLAN 99 ✓ VERIFIED  
- **IP Address**: 10.99.0.12 ✓ VERIFIED  
- **Subnet Mask**: 255.255.255.0 ✓ VERIFIED  
- **Default Gateway**: 10.99.0.1 ✓ VERIFIED  
- **SSH Version**: 2 ✓ VERIFIED  
- **SSH Timeout**: 60 seconds ✓ VERIFIED  
- **Console**: `line con 0` ✓ VERIFIED  
- **VTY Lines**: `line vty 0 4` ✓ VERIFIED  
- **VTY Transport Input**: `ssh` ✓ VERIFIED  
- **Banner**: Configured (login banner: `Advarsel: Uautorisert tilgang er forbudt.`) ✓ VERIFIED  

---

## AAA Configuration
- AAA: Not enabled ✓ VERIFIED  

---

## VLANs
- **Total VLANs Referenced**: 5 ✓ VERIFIED  
- **VLAN IDs and Names**:  
  - VLAN 10: Brukere ✓ VERIFIED  
  - VLAN 20: Servere ✓ VERIFIED  
  - VLAN 50: VoIP ✓ VERIFIED  
  - VLAN 99: Management ✓ VERIFIED  
  - VLAN 666: Native VLAN (not named) ✓ VERIFIED  

- **VLAN Interfaces (SVIs)**:  
  - **VLAN 1**:  
    - Status: Shutdown ✓ VERIFIED  
  - **VLAN 99**:  
    - Description: Management ✓ VERIFIED  
    - IP: 10.99.0.12 255.255.255.0 ✓ VERIFIED  
    - Status: Active ✓ VERIFIED  

- **VTP Configuration**: Not explicitly configured ✓ VERIFIED  

---

## Physical Interfaces
- **Total Interfaces**: 26 ✓ VERIFIED  
- **Active (no shutdown)**: 6 ✓ VERIFIED  
- **Shutdown**: 20 ✓ VERIFIED  

### Active Interfaces
1. **FastEthernet0/1**  
   - Description: "Bruker-PC kontor 201" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Voice VLAN: 50 ✓ VERIFIED  
   - Port Security Violation Mode: Not configured ✓ VERIFIED  

2. **FastEthernet0/2**  
   - Description: "Bruker-PC kontor 202" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Voice VLAN: 50 ✓ VERIFIED  
   - Port Security Violation Mode: Not configured ✓ VERIFIED  

3. **FastEthernet0/3**  
   - Description: "Bruker-PC kontor 203" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Voice VLAN: 50 ✓ VERIFIED  
   - Port Security Violation Mode: Not configured ✓ VERIFIED  

4. **FastEthernet0/4**  
   - Description: "Bruker-PC kontor 204" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Voice VLAN: 50 ✓ VERIFIED  
   - Port Security Violation Mode: Not configured ✓ VERIFIED  

5. **FastEthernet0/5**  
   - Description: "Printer 2. etasje" ✓ VERIFIED  
   - Mode: access ✓ VERIFIED  
   - VLAN: 10 ✓ VERIFIED  
   - Port Security Violation Mode: Not configured ✓ VERIFIED  

6. **FastEthernet0/24**  
   - Description: "Uplink til dis-sw01" ✓ VERIFIED  
   - Mode: trunk ✓ VERIFIED  
   - Encapsulation: dot1q ✓ VERIFIED  
   - Native VLAN: 666 ✓ VERIFIED  
   - Allowed VLANs: 10, 20, 50, 99 ✓ VERIFIED  

---

## Spanning Tree Protocol
- **STP Mode**: pvst ✓ VERIFIED  
- **Global Features**: portfast-default ✓ VERIFIED  

---

## Security Features
- **DHCP Snooping**: Not enabled ✓ VERIFIED  
- **Dynamic ARP Inspection**: Not enabled ✓ VERIFIED  
- **Port Security Enabled**: 0 interfaces ✓ VERIFIED  
- **802.1X**: Not configured ✓ VERIFIED  
- **IP Source Guard**: Not configured ✓ VERIFIED  
- **CDP**: Enabled ✓ VERIFIED  
- **LLDP**: Not enabled ✓ VERIFIED  

---

## Network Services
### Logging
- **Logging Server**: 10.99.0.50 ✓ VERIFIED  

### NTP
- **NTP Server**: Not configured ✓ VERIFIED  
- **NTP Authentication**: Not configured ✓ VERIFIED  

### DNS
- **Domain Name**: firma.local ✓ VERIFIED  
- **DNS Lookup**: Disabled ✓ VERIFIED  

---

## Routing Configuration
- **IP Routing**: Disabled ✓ VERIFIED  
- **Default Gateway**: 10.99.0.1 ✓ VERIFIED  

---

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only VTY access with version 2 and 60-second timeout (lines `ip ssh version 2` and `ip ssh time-out 60`)  
- Portfast and BPDU guard enabled on access ports (e.g., `spanning-tree portfast` and `spanning-tree bpduguard enable` on interfaces FastEthernet0/1-4)  
- Management VLAN (VLAN 99) isolated from user VLANs  
- Syslog logging configured to 10.99.0.50  

#### ⚠ Areas for Improvement
- No ACL protection on VTY lines (missing `access-class` configuration)  
- DHCP snooping and Dynamic ARP Inspection not enabled  
- No port security configured on access ports  
- Native VLAN 666 is not named or documented  
- No NTP configuration for time synchronization  
- CDP is enabled (potential security risk if not needed)  

#### Recommendations
- Enable DHCP snooping on VLANs 10, 20, 50, and 99  
- Configure Dynamic ARP Inspection (DAI) on VLANs with user traffic  
- Implement port security on access ports (e.g., `switchport port-security`)  
- Rename native VLAN 666 to a descriptive name (e.g., "Native-Untrusted")  
- Configure NTP with a trusted time source  
- Disable CDP if not required for network discovery  
- Add an ACL to restrict VTY access to trusted management networks  

---

## Summary
switch-02 is an **Access-layer switch** serving user devices in VLAN 10 (Brukere) and connecting to a distribution switch via a trunk port (FastEthernet0/24). The configuration is minimal, with basic security features like SSH and portfast enabled, but lacks advanced protections such as DHCP snooping and port security. The device is managed via VLAN 99 (10.99.0.12) and logs to a syslog server.  

**Device Role**: Access Layer ✓ VERIFIED  
**Security Posture**: Basic security implemented, but critical protections are missing ~ INFERRED  
**Configuration Quality**: Functional but requires hardening ~ INFERRED  

---

**Data Source**: Structured configuration analysis  
**Generated**: 2026-02-16T08:25:20.914289