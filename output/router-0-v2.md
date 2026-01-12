```markdown
# Device Configuration Summary for Cisco 2911 Router

## General Information
- **Device Name:** Cisco 2911/K9
- **Serial Number:** FTX15244012-
- **Software Version:** IOS (not explicitly mentioned in the configuration)

## Network Configuration
### Domain and DNS Settings
- **Domain Name:** krister.local
- **DNS Lookup Disabled:** `no ip domain-lookup`

### SSH Configuration
- **SSH Version:** 2
- **Timeout:** 60 seconds

### Spanning Tree Protocol (STP)
- **Mode:** PVST (Per-VLAN Spanning Tree)

## Interfaces
### Physical Interfaces
1. **GigabitEthernet0/0**
   - **Status:** Shutdown
   - **Description:** Not specified
2. **GigabitEthernet0/1**
   - **Description:** dis-venstre-sw01 GIG0/2
3. **GigabitEthernet0/2**
   - **Description:** dis-hoyre-sw01 GIG0/2

### Subinterfaces (VLANs)
1. **GigabitEthernet0/1.11**
   - **Description:** Usergroup 1-1
   - **VLAN ID:** 11
   - **IP Address:** 192.168.11.254/24
   - **Access Control List (ACL):** USERS_TO_SERV21

2. **GigabitEthernet0/1.12**
   - **Description:** Usergroup 1-2
   - **VLAN ID:** 12
   - **IP Address:** 192.168.12.254/24
   - **Access Control List (ACL):** USERS_TO_SERV22

3. **GigabitEthernet0/1.90**
   - **Description:** Management LEFT SIDE
   - **VLAN ID:** 90
   - **IP Address:** 10.90.0.254/24
   - **Access Control List (ACL):** MGMT-LEFT

4. **GigabitEthernet0/2.21**
   - **Description:** Usergroup 2-1
   - **VLAN ID:** 21
   - **IP Address:** 192.168.21.254/24

5. **GigabitEthernet0/2.22**
   - **Description:** Usergroup 2-2
   - **VLAN ID:** 22
   - **IP Address:** 192.168.22.254/24

6. **GigabitEthernet0/2.91**
   - **Description:** Management RIGHT-SIDE
   - **VLAN ID:** 91
   - **IP Address:** 10.91.0.254/24
   - **Access Control List (ACL):** MGMT-RIGHT

### VLAN Interface
- **Vlan1**
  - **Status:** Shutdown
  - **Description:** Not specified

## Access Control Lists (ACLs)
1. **Standard ACL: MGMT-MGMT**
   ```plaintext
   permit 10.90.0.0 0.0.0.255
   permit 10.91.0.0 0.0.0.255
   deny any
   ```

2. **Extended ACL: USERS_TO_SERV21**
   ```plaintext
   permit udp any any eq bootps
   permit udp any any eq bootpc
   permit ip 192.168.11.0 0.0.0.255 host 192.168.21.211
   permit ip 192.168.11.0 0.0.0.255 host 192.168.21.212
   permit udp 192.168.11.0 0.0.0.255 host 10.91.0.123 eq domain
   permit tcp 192.168.11.0 0.0.0.255 host 10.91.0.123 eq domain
   deny ip any any
   ```

3. **Extended ACL: USERS_TO_SERV22**
   ```plaintext
   permit udp any any eq bootps
   permit udp any any eq bootpc
   permit ip 192.168.12.0 0.0.0.255 host 192.168.22.221
   permit ip 192.168.12.0 0.0.0.255 host 192.168.22.222
   permit udp 192.168.12.0 0.0.0.255 host 10.91.0.123 eq domain
   permit tcp 192.168.12.0 0.0.0.255 host 10.91.0.123 eq domain
   deny ip any any
   ```

4. **Extended ACL: MGMT-RIGHT**
   ```plaintext
   permit ip 10.91.0.0 0.0.0.255 192.168.11.0 0.0.0.255
   permit ip 10.91.0.0 0.0.0.255 192.168.12.0 0.0.0.255
   permit ip 10.91.0.0 0.0.0.255 192.168.21.0 0.0.0.255
   permit ip 10.91.0.0 0.0.0.255 192.168.22.0 0.0.0.255
   permit ip 10.91.0.0 0.0.0.255 10.91.0.0 0.0.0.255
   permit ip 10.91.0.0 0.0.0.255 10.90.0.0 0.0.0.255
   permit udp 10.91.0.0 0.0.0.255 host 10.91.0.123 eq domain
   permit tcp 10.91.0.0 0.0.0.255 host 10.91.0.123 eq domain
   deny ip any any
   ```

5. **Extended ACL: MGMT-LEFT**
   ```plaintext
   permit ip 10.90.0.0 0.0.0.255 192.168.11.0 0.0.0.255
   permit ip 10.90.0.0 0.0.0.255 192.168.12.0 0.0.0.255
   permit ip 10.90.0.0 0.0.0.255 192.168.21.0 0.0.0.255
   permit ip 10.90.0.0 0.0.0.255 192.168.22.0 0.0.0.255
   permit ip 10.90.0.0 0.0.0.255 10.91.0.0 0.0.0.255
   permit ip 10.90.0.0 0.0.0.255 10.90.0.0 0.0.0.255
   permit udp 10.90.0.0 0.0.0.255 host 10.91.0.123 eq domain
   permit tcp 10.90.0.0 0.0.0.255 host 10.91.0.123 eq domain
   deny ip any any
   ```

## Authentication and Authorization
- **AAA Configuration:**
  - **Authentication:** 
    ```plaintext
    aaa authentication login console local
    aaa authentication login default group tacacs+ local
    ```
  - **Authorization:**
    ```plaintext
    aaa authorization exec default group tacacs+ local
    ```
  - **Accounting:**
    ```plaintext
    aaa accounting exec default start-stop group tacacs+
    ```

- **TACACS Server Configuration:**
  ```plaintext
  tacacs-server host <server_ip>
  tacacs-server key <key>
  ```

## Logging and Monitoring
- **Syslog Configuration:** Not explicitly configured in the provided configuration.
- **NTP Configuration:** Not explicitly configured in the provided configuration.

## Security Settings
- **Login Banner:**
  ```plaintext
  login on-success log
  login on-failure log
  ```
  
- **SSH Access Control List (ACL):** 
  - Applied to VTY lines for secure remote access.
  
## Network Services
- **Flow Export:** Not explicitly configured in the provided configuration.

## Summary of Key Points
1. The device is a Cisco 2911 router with multiple VLANs and subinterfaces.
2. SSH version 2 is enabled with a timeout of 60 seconds.
3. TACACS+ authentication and authorization are configured for secure access control.
4. Multiple ACLs are defined to manage traffic flow between different network segments.
5. The device acts as a router for multiple VLANs, providing connectivity between user groups and management networks.

This configuration ensures that the router provides secure and controlled network services while maintaining proper segmentation and security policies.
```markdown
```

This summary covers all key aspects of the provided configuration, including interfaces, ACLs, AAA settings, and other relevant details. It also includes a brief explanation for each section to help understand the purpose and functionality of the configurations. If you need any further customization or additional information, please let me know!```markdown
```