# Switch Configuration Documentation: 1-aksess-sw01-6.txt

## Overview
- **Hostname**: aksess-sw01
- **IOS Version**: Unknown
- **Configuration Purpose**: This switch is likely a network access layer device, providing connectivity to various departments and users within the organization.
- **Last Modified**: Not specified in the configuration file.
- **Domain Name**: krister.local

## Device Information
- **Model**: Not specified in the configuration file. To determine this information, you would need to refer to the actual switch model or consult with the manufacturer/distributor.
- **System Image**: The boot image is not explicitly mentioned in the provided configuration, but it can be found by running the `show version` command on the device.
- **Serial Number**: Not specified in the configuration file. To determine this information, you would need to refer to the actual switch or consult with the manufacturer/distributor.
- **Hardware Details**: The hardware details are not explicitly mentioned in the provided configuration.

## Management & Access

### Management Interfaces
The management interface is configured as follows:

*   The management VLAN and IP addressing: `Vlan90` is used for the management SVI, which has an IP address of `10.90.0.11/24`.
*   Default gateway configuration: The default gateway is set to `10.90.0.254`.
*   Management protocols enabled: SSH version 2 and HTTPS are likely enabled due to the presence of the `ip ssh` commands.

```markdown
### Management VLAN and IP Addressing

| VLAN ID | Name       | Purpose            |
|---------|------------|--------------------|
| 90      | Admin-Mgmt-LEFT | Management SVI     |

### Default Gateway Configuration

*   Default gateway: `10.90.0.254`

### Management Protocols Enabled

*   SSH version 2: Enabled
*   HTTPS: Likely enabled (not explicitly configured)
```

### Access Control & Security

#### Console Access

The console access is configured with:

*   Authentication method: Local authentication
*   Authentication timeout: 10 minutes (configurable)

```markdown
### Console Access Configuration

*   Authentication method: local
*   Authentication timeout: 10 minutes
```

#### VTY Access

VTY access is configured as follows:

*   Line configuration: `line vty 0 4`
*   Authentication method: Default group (`tacacs+`), with local authentication fallback.
*   Access class restrictions: The `access-class MGMT-MGMT in` command restricts SSH access to the management network.

```markdown
### VTY Access Configuration

*   Line configuration: `line vty 0 4`
*   Authentication method: Default group (`tacacs+`) with local fallback
*   Access class restrictions: `access-class MGMT-MGMT in`
```

#### Enable Password

The enable password is configured as follows:

*   Enable secret: `3NA8le$cret!=1` (encrypted)

```markdown
### Enable Password Configuration

*   Enable secret: `3NA8le$cret!=1`
```

#### AAA Configuration

AAA configuration includes:

*   TACACS+ server: `tacacs-server host 10.91.0.10 key KompleksNoekkel`
*   Authentication methods for login and exec services
*   Accounting method for exec services

```markdown
### AAA Configuration

*   TACACS+ server: `tacacs-server host 10.91.0.10 key KompleksNoekkel`
*   Authentication methods:
    *   Login authentication: Default group (`tacacs+`) with local fallback
    *   Exec authentication: Default group (`tacacs+`) with local fallback
*   Accounting method: Default group (`tacacs+`)
```

#### Login Banners

A login banner is configured to display the following message:

`^CUnauthorized access prohibited.^C`

```markdown
### Login Banner Configuration

*   Login banner: `^CUnauthorized access prohibited.^C`
```

### Management Access Lists

The management ACL (`MGMT-MGMT`) restricts SSH access from any source IP address.

```markdown
### Management ACL Configuration

| Seq # | Action    | Protocol  | Source          | Destination              |
|-------|-----------|-----------|-----------------|----------------------------|
| 1     | permit    | icmp      | 10.90.0.0/24    | 10.90.0.0/24             |
| 2     | permit    | tcp       | 10.91.0.0/24    | 10.91.0.0/24             |

*   SSH access restricted from any source IP address
```

## VLANs

### VLAN Database

The following table lists the configured VLANs:

| VLAN ID | Name                  | Purpose                               |
|---------|------------------------|---------------------------------------|
| 11      | Usergroup1-1           | User group 1 (VLAN 11)                |
| 12      | Usergroup1-2           | User group 2 (VLAN 12)                |
| 90      | Admin-Mgmt-LEFT        | Management VLAN                      |
| 666     | native-trunk           | Native trunk VLAN                     |

```markdown
### VLAN Database

| VLAN ID | Name                  | Purpose                               |
|---------|------------------------|---------------------------------------|
| 11      | Usergroup1-1           | User group 1 (VLAN 11)                |
| 12      | Usergroup1-2           | User group 2 (VLAN 12)                |
| 90      | Admin-Mgmt-LEFT        | Management VLAN                      |
| 666     | native-trunk           | Native trunk VLAN                     |

```

### VLAN Interfaces (SVIs)

The following table lists the VLAN interface configurations:

| VLAN ID | Interface  | IP Address    | Description       |
|---------|------------|----------------|--------------------|
| 90      | Vlan90     | 10.90.0.11/24  | Management SVI     |

```markdown
### VLAN Interfaces

| VLAN ID | Interface  | IP Address    | Description       |
|---------|------------|----------------|--------------------|
| 90      | Vlan90     | 10.90.0.11/24  | Management SVI     |

```

## Physical Interfaces

### Interface Summary

The following table lists the physical interfaces and their configurations:

| Interface | Description    | Mode   | VLAN/Trunk | Speed/Duplex | Status   |
|-----------|----------------|--------|------------|--------------|----------|
| Gig 0/1   | dis-venstre-sw01| Trunk  | Dot1q      | Auto         | Up       |
| Fast 0/1  | PC4-Access port| Access | None       | Auto         | Up       |
| Fast 0/2  | PC5-Access port| Access | None       | Auto         | Up       |
| Fast 0/3  | Management-PC| Access| None        | Auto          | Up       |

```markdown
### Interface Summary

| Interface | Description    | Mode   | VLAN/Trunk | Speed/Duplex | Status   |
|-----------|----------------|--------|------------|--------------|----------|
| Gig 0/1   | dis-venstre-sw01| Trunk  | Dot1q      | Auto         | Up       |
| Fast 0/1  | PC4-Access port| Access | None       | Auto         | Up       |
| Fast 0/2  | PC5-Access port| Access | None       | Auto         | Up       |
| Fast 0/3  | Management-PC| Access| None        | Auto          | Up       |

```

### Detailed Interface Configurations

#### GigabitEthernet0/1

*   Description: dis-venstre-sw01 gig0/1
*   Mode: Trunk
*   Configuration Details:
    *   `switchport trunk encapsulation dot1q`
    *   `switchport mode trunk`
    *   `switchport nonegotiate`
    *   `switchport trunk native vlan 666`
    *   `switchport trunk allowed vlan 11,12,90`

```markdown
### Detailed Interface Configurations: GigabitEthernet0/1

*   Description: dis-venstre-sw01 gig0/1
*   Mode: Trunk
*   Configuration Details:
    *   switchport trunk encapsulation dot1q
    *   switchport mode trunk
    *   switchport nonegotiate
    *   switchport trunk native vlan 666
    *   switchport trunk allowed vlan 11,12,90

```

## Port-Channel / EtherChannel

No port-channel configurations are present in the provided configuration.

## Routing Configuration

### Routing Protocol

No routing protocols are configured in the provided configuration.

## Spanning Tree Protocol

### STP Configuration

The following table lists the spanning tree protocol settings:

| Mode  | VLANs            |
|-------|------------------|
| PVST+ | 11,12,90        |

```markdown
### Spanning Tree Protocol Settings

| Mode  | VLANs            |
|-------|------------------|
| PVST+ | 11,12,90        |

```

## Quality of Service (QoS)

No QoS configurations are present in the provided configuration.

## Security Features

### Port Security

The following table lists the port security settings:

| Interface | Maximum MAC addresses | Violation action |
|-----------|----------------------|------------------|
| Fast 0/1  | 1                    | Restrict        |
| Fast 0/2  | 1                    | Restrict        |
| Fast 0/3  | 1                    | Restrict        |

```markdown
### Port Security Settings

| Interface | Maximum MAC addresses | Violation action |
|-----------|----------------------|------------------|
| Fast 0/1  | 1                    | Restrict        |
| Fast 0/2  | 1                    | Restrict        |
| Fast 0/3  | 1                    | Restrict        |

```

## Network Services

### DHCP Server/Relay

No DHCP server or relay configurations are present in the provided configuration.

## NTP (Network Time Protocol)

The following table lists the NTP settings:

| Server       | Key          |
|--------------|--------------|
| 10.91.0.123  | 15           |

```markdown
### NTP Settings

| Server       | Key          |
|--------------|--------------|
| 10.91.0.123  | 15           |

```

## Syslog

The following table lists the syslog settings:

| Level    | Host(s)     |
|----------|-------------|
| Info     | 10.91.0.10  |

```markdown
### Syslog Settings

| Level    | Host(s)     |
|----------|-------------|
| Info     | 10.91.0.10  |

```

## Best Practices Analysis

The analysis of the configuration against Cisco best practices is as follows:

### ✅ Good Practices Identified

*   The enable secret password is encrypted.
*   TACACS+ server authentication is configured for login and exec services.
*   Port security is enabled on access ports to prevent MAC address spoofing.

### ⚠️ Potential Issues or Concerns

*   No routing protocols are configured, which may cause issues with inter-VLAN routing or network connectivity.
*   No QoS configurations are present in the provided configuration, which may lead to poor network performance.
*   The span-tree configuration is set for PVST+, but there are no VLAN IDs specified for this protocol.

### 💡 Recommendations for Improvement

1.  Configure a routing protocol (such as OSPF or EIGRP) for inter-VLAN routing and network connectivity.
2.  Implement QoS configurations to ensure proper traffic prioritization and shaping.
3.  Review the span-tree configuration to ensure it is properly set up for the specific VLANs in use.

## Configuration Summary

The following table provides a high-level summary of the switch configuration:

| Category     | Description                                         |
|--------------|------------------------------------------------------|
| Total VLANs   | 4 (11, 12, 90, 666)                                |
| Total Configured Interfaces  | 10 (Gig 0/1, Fast 0/1-3, Vlan90)                 |
| Routing       | Disabled (no routing protocols configured)        |
| Spanning Tree | PVST+ (configured for VLANs 11,12,90)            |
| Key Features Enabled:      | Port security on access ports, TACACS+ authentication for login and exec services
| Security Posture:   | Good practice of encrypting the enable secret password and enabling port security
| Overall Assessment: The configuration is mostly complete but lacks routing protocols, QoS configurations, and proper span-tree settings

## Appendix

### Uncommon or Complex Configurations

No uncommon or complex configurations are present in the provided configuration.

### Configuration Snippets

No additional configuration snippets are necessary for this analysis.