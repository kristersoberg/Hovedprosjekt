```markdown
# Device Configuration Summary for Cisco 2911 Router

## General Information
- **Device Name:** Cisco 2911/K9
- **Serial Number:** FTX15244012-
- **Software Version:** IOS (not explicitly mentioned in the configuration)

## Network Configuration
### Domain and DNS Settings
- **Domain Lookup Disabled:** `no ip domain-lookup`
- **Domain Name:** `krister.local`

### SSH Configuration
- **SSH Version:** 2 (`ip ssh version 2`)
- **Timeout:** 60 seconds (`ip ssh time-out 60`)

## Authentication and Authorization
### AAA Configuration
- **AAA New Model Enabled:** `aaa new-model`
- **Authentication:**
  - Console login authenticated locally: `aaa authentication login console local`
  - Default login authenticated via TACACS+ or locally if TACACS+ fails: `aaa authentication login default group tacacs+ local`
- **Authorization:**
  - Exec authorization via TACACS+: `aaa authorization exec default group tacacs+ local`
- **Accounting:**
  - Start-stop accounting for exec sessions via TACACS+: `aaa accounting exec default start-stop group tacacs+`

### TACACS+ Configuration
- **TACACS+ Server:** 
  - Host IP: `10.91.0.10`
  - Key: `KompleksNoekkel` (configured with `tacacs-server host 10.91.0.10 key KompleksNoekkel`)

## VLAN and Interface Configuration
### Interfaces
- **GigabitEthernet0/0:** 
  - No IP address, shutdown (`interface GigabitEthernet0/0 no ip address shutdown`)
- **GigabitEthernet0/1:**
  - Description: `dis-venstre-sw01 GIG0/2`
  - No IP address (`no ip address`), auto duplex and speed
- **GigabitEthernet0/1.11 (VLAN 11):**
  - Description: `Usergroup 1-1`
  - Encapsulation dot1Q, VLAN ID 11
  - IP Address: `192.168.11.254/24`
  - Access-list applied inbound: `USERS_TO_SERV21` (`ip access-group USERS_TO_SERV21 in`)
- **GigabitEthernet0/1.12 (VLAN 12):**
  - Description: `Usergroup 1-2`
  - Encapsulation dot1Q, VLAN ID 12
  - IP Address: `192.168.12.254/24`
  - Access-list applied inbound: `USERS_TO_SERV22` (`ip access-group USERS_TO_SERV22 in`)
- **GigabitEthernet0/1.90 (VLAN 90):**
  - Description: `Management LEFT SIDE`
  - Encapsulation dot1Q, VLAN ID 90
  - IP Address: `10.90.0.254/24`
  - Access-list applied inbound: `MGMT-LEFT` (`ip access-group MGMT-LEFT in`)
- **GigabitEthernet0/2:**
  - Description: `dis-hoyre-sw01 GIG0/2`
  - No IP address, auto duplex and speed
- **GigabitEthernet0/2.21 (VLAN 21):**
  - Description: `Usergroup 2-1`
  - Encapsulation dot1Q, VLAN ID 21
  - IP Address: `192.168.21.254/24`
- **GigabitEthernet0/2.22 (VLAN 22):**
  - Description: `Usergroup 2-2`
  - Encapsulation dot1Q, VLAN ID 22
  - IP Address: `192.168.22.254/24`
- **GigabitEthernet0/2.91 (VLAN 91):**
  - Description: `Management RIGHT-SIDE`
  - Encapsulation dot1Q, VLAN ID 91
  - IP Address: `10.91.0.254/24`
  - Access-list applied inbound: `MGMT-RIGHT` (`ip access-group MGMT-RIGHT in`)
- **VLAN1 (SVI):**
  - No IP address, shutdown

## Access Control Lists
### Standard ACLs
- **MGMT-MGMT:** 
  - Permits traffic from `10.90.0.0/24` and `10.91.0.0/24`, denies all other traffic (`ip access-list standard MGMT-MGMT permit 10.90.0.0 0.0.0.255 permit 10.91.0.0 0.0.0.255 deny any`)

### Extended ACLs
- **USERS_TO_SERV21:**
  - Permits DHCP traffic and specific IP ranges to hosts `192.168.21.211`, `192.168.21.212`, and DNS server `10.91.0.123` (`ip access-list extended USERS_TO_SERV21`)
- **USERS_TO_SERV22:**
  - Similar to `USERS_TO_SERV21` but for different IP ranges and hosts
- **MGMT-RIGHT:** 
  - Permits traffic from `10.91.0.0/24` to various subnets, permits DNS traffic (`ip access-list extended MGMT-RIGHT`)
- **MGMT-LEFT:**
  - Similar to `MGMT-RIGHT` but for different IP ranges

## Logging and NTP Configuration
### Logging
- **Logging Server:** 
  - Host IP: `10.91.0.10` (`logging 10.91.0.10`)
  
### NTP Configuration
- **NTP Authentication Key:** 
  - ID: `15`, key configured with `ntp authentication-key 15 <REDACTED> 080A43431915001C011F3C0539382B3A37`
- **NTP Authentication Enabled:** 
  - Key ID: `15` (`ntp authenticate`)
- **Trusted NTP Keys:** 
  - Key ID: `15` (`ntp trusted-key 15`)
- **NTP Server Configuration:** 
  - Host IP: `10.91.0.123`, key ID: `15` (`<REDACTED> server 10.91.0.123 key 15`)

## Line and Console Configuration
### Console Line
- **Logging Synchronous:** 
  - Enabled (`logging synchronous`)
- **Login Authentication:** 
  - Console authentication (`login authentication console`)

### VTY Lines (0-4)
- **Access-Class:**
  - `MGMT-MGMT` applied inbound (`access-class MGMT-MGMT in`)
- **Login Authentication:**
  - Default login authentication (`login authentication default`)
- **Transport Input:**
  - SSH only (`transport input ssh`)

## Banner
- **Login Banner:** 
  - Unauthorized access prohibited (`banner login ^CUnauthorized access prohibited.^C`)

---

### Device Role and Functionality
The device is configured as a Layer 3 switch/router, providing VLAN segmentation and routing between different user groups and management networks. It also handles AAA (Authentication, Authorization, Accounting) via TACACS+ for secure network access control.

### Recommendations
1. **Enable DHCP Snooping:** To prevent unauthorized DHCP servers.
2. **Implement Port Security:** On critical interfaces to restrict MAC addresses.
3. **Regularly Update Firmware:** Ensure the device is running the latest firmware for security patches and features.
4. **Monitor Access Logs:** Regularly review logs from TACACS+ and NTP for any suspicious activity.

---

This configuration summary provides a comprehensive overview of the Cisco 2911 router's setup, including its network interfaces, access control lists, AAA configurations, logging, and other critical settings.
```