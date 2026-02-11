```markdown
# Configuration Summary for Device: `CISCO2911/K9`

## General Information

- **Device Name:** CISCO2911/K9
- **Serial Number:** FTX15244012-
- **Domain Name:** krister.local
- **Spanning Tree Mode:** PVST

## Device Configuration Details

### Domain and SSH Settings
- **IP Domain Name:** `krister.local`
- **SSH Version:** 2
- **SSH Time-out:** 60 seconds
- **No IP Domain Lookup:**

```plaintext
ip domain-name krister.local
no ip domain-lookup
ip ssh version 2
ip ssh time-out 60
```

### AAA Configuration
- **AAA New Model Enabled**
- **Authentication Login Console Local**
- **Authentication Default Group TACACS+ Local**
- **Authorization Exec Default Group TACACS+ Local**
- **Accounting Exec Start-stop Group TACACS+**

```plaintext
aaa new-model
aaa authentication login console local 
aaa authentication login default group tacacs+ local 
aaa authorization exec default group tacacs+ local
aaa accounting exec default start-stop group tacacs+
```

### User Accounts and TACACS+
- **Username:** `emergency-admin` with privilege level 15
- **TACACS+ Server Host:** `10.91.0.10`
- **Key:** `KompleksNoekkel`

```plaintext
username emergency-admin privilege 15 secret 5 <REDACTED>
tacacs-server host 10.91.0.10 key KompleksNoekkel
```

### Interfaces Configuration

#### GigabitEthernet Interfaces
- **GigabitEthernet0/0:** Shutdown
- **GigabitEthernet0/1:** Description `dis-venstre-sw01 GIG0/2`
- **GigabitEthernet0/2:** Description `dis-hoyre-sw01 GIG0/2`

```plaintext
interface GigabitEthernet0/0
 no ip address
 duplex auto
 speed auto
 shutdown

interface GigabitEthernet0/1
 description dis-venstre-sw01 GIG0/2
 no ip address
 duplex auto
 speed auto

interface GigabitEthernet0/2
 description dis-hoyre-sw01 GIG0/2
 no ip address
 duplex auto
 speed auto
```

#### Subinterfaces Configuration
- **GigabitEthernet0/1.11:** VLAN 11, IP `192.168.11.254`
- **GigabitEthernet0/1.12:** VLAN 12, IP `192.168.12.254`
- **GigabitEthernet0/1.90:** VLAN 90, IP `10.90.0.254`
- **GigabitEthernet0/2.21:** VLAN 21, IP `192.168.21.254`
- **GigabitEthernet0/2.22:** VLAN 22, IP `192.168.22.254`
- **GigabitEthernet0/2.91:** VLAN 91, IP `10.91.0.254`

```plaintext
interface GigabitEthernet0/1.11
 description Usergroup 1-1
 encapsulation dot1Q 11
 ip address 192.168.11.254 255.255.255.0
 ip access-group USERS_TO_SERV21 in

interface GigabitEthernet0/1.12
 description Usergroup 1-2
 encapsulation dot1Q 12
 ip address 192.168.12.254 255.255.255.0
 ip access-group USERS_TO_SERV22 in

interface GigabitEthernet0/1.90
 description Management LEFT SIDE
 encapsulation dot1Q 90
 ip address 10.90.0.254 255.255.255.0
 ip access-group MGMT-LEFT in

interface GigabitEthernet0/2.21
 description Usergroup 2-1
 encapsulation dot1Q 21
 ip address 192.168.21.254 255.255.255.0

interface GigabitEthernet0/2.22
 description Usergroup 2-2
 encapsulation dot1Q 22
 ip address 192.168.22.254 255.255.255.0

interface GigabitEthernet0/2.91
 description Management RIGHT-SIDE
 encapsulation dot1Q 91
 ip address 10.91.0.254 255.255.255.0
 ip access-group MGMT-RIGHT in
```

### Access Control Lists (ACLs)
- **Standard ACL:** `MGMT-MGMT`
- **Extended ACLs:**
  - `USERS_TO_SERV21`
  - `USERS_TO_SERV22`
  - `MGMT-RIGHT`
  - `MGMT-LEFT`

```plaintext
ip access-list standard MGMT-MGMT
 permit 10.90.0.0 0.0.0.255
 permit 10.91.0.0 0.0.0.255
 deny any

ip access-list extended USERS_TO_SERV21
 permit udp any any eq bootps
 permit udp any any eq bootpc
 permit ip 192.168.11.0 0.0.0.255 host 192.168.21.211
 permit ip 192.168.11.0 0.0.0.255 host 192.168.21.212
 permit udp 192.168.11.0 0.0.0.255 host 10.91.0.123 eq domain
 permit tcp 192.168.11.0 0.0.0.255 host 10.91.0.123 eq domain
 deny ip any any

ip access-list extended USERS_TO_SERV22
 permit udp any any eq bootps
 permit udp any any eq bootpc
 permit ip 192.168.12.0 0.0.0.255 host 192.168.22.221
 permit ip 192.168.12.0 0.0.0.255 host 192.168.22.222
 permit udp 192.168.12.0 0.0.0.255 host 10.91.0.123 eq domain
 permit tcp 192.168.12.0 0.0.0.255 host 10.91.0.123 eq domain
 deny ip any any

ip access-list extended MGMT-RIGHT
 permit ip 10.91.0.0 0.0.0.255 192.168.11.0 0.0.0.255
 permit ip 10.91.0.0 0.0.0.255 192.168.12.0 0.0.0.255
 permit ip 10.91.0.0 0.0.0.255 192.168.21.0 0.0.0.255
 permit ip 10.91.0.0 0.0.0.255 192.168.22.0 0.0.0.255
 permit ip 10.91.0.0 0.0.0.255 10.91.0.0 0.0.0.255
 permit ip 10.91.0.0 0.0.0.255 10.90.0.0 0.0.0.255
 permit udp 10.91.0.0 0.0.0.255 host 10.91.0.123 eq domain
 permit tcp 10.91.0.0 0.0.0.255 host 10.91.0.123 eq domain
 deny ip any any

ip access-list extended MGMT-LEFT
 permit ip 10.90.0.0 0.0.0.255 192.168.11.0 0.0.0.255
 permit ip 10.90.0.0 0.0.0.255 192.168.12.0 0.0.0.255
 permit ip 10.90.0.0 0.0.0.255 192.168.21.0 0.0.0.255
 permit ip 10.90.0.0 0.0.0.255 192.168.22.0 0.0.0.255
 permit ip 10.90.0.0 0.0.0.255 10.91.0.0 0.0.0.255
 permit udp 10.90.0.0 0.0.0.255 host 10.91.0.123 eq domain
 permit tcp 10.90.0.0 0.0.0.255 host 10.91.0.123 eq domain
 deny ip any any
```

### Logging and Monitoring
- **Logging Host:** `10.91.0.1`
- **Syslog Facility:** Local7

```plaintext
logging host 10.91.0.1
logging facility local7
```

## Line Configuration
- **Console Line:**
  - Login with password
  - Transport input none
  
- **VTY Lines (0-4):**
  - Login with password
  - Transport input SSH

```plaintext
line con 0
 login
 transport input none

line vty 0 4
 login
 transport input ssh
```

## NTP Configuration
- **NTP Server:** `10.91.0.2`
  
```plaintext
ntp server 10.91.0.2
```

### Summary of Key Points:
- The device is configured with TACACS+ for AAA services.
- Multiple VLANs and subinterfaces are defined, each with specific IP addresses and ACLs.
- SSH access is enabled on VTY lines.
- NTP synchronization is set up to ensure accurate timekeeping.

This configuration ensures secure remote management, proper network segmentation, and robust security measures.
```
```