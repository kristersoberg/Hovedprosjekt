# Network Device Documentation: aksess-sw01

## Device Information

The device is a Cisco switch with the hostname `aksess-sw01` and running IOS version `12.2(37)SE1`. The domain name is set to `krister.local`.

## Management & Access

Management access is configured on VLAN 90, which has an IP address of `10.90.0.11/24` with a default gateway of `10.90.0.254`. SSH version 2 is enabled with a timeout of 60 seconds.

### SSH Configuration
SSH is the only allowed transport input method for VTY access.

### Console Access
Console access is configured on line con 0, which requires authentication using the console method.

## AAA Configuration

AAA (Authentication, Authorization, and Accounting) is enabled on this device. The following authentication lists are defined:

- `console`: authenticates users against the local database.
- `default`: authenticates users against a TACACS+ server and then the local database if the TACACS+ server fails.

The following authorization list is defined:

- `exec`: authorizes users to execute commands on the device, using a TACACS+ server and then the local database if the TACACS+ server fails.

Accounting is enabled for exec sessions, with accounting information sent to a TACACS+ server.

### TACACS+ Servers
A single TACACS+ server is configured at IP address `10.91.0.10`.

### Local Users
One local user account exists: `emergency-admin` with privilege level 15.

## VLANs

There are four VLANs referenced in the configuration:

- VLAN 11
- VLAN 12
- VLAN 90 (management VLAN)
- VLAN 666 (native VLAN for trunk ports)

Two SVIs (Switched Virtual Interfaces) are configured:

- **VLAN 1**: Shutdown.
- **VLAN 90**: Active, with an IP address of `10.90.0.11/24`, a description of "Management SVI", and an ACL named `MGMT-MGMT` applied for incoming traffic.

## Physical Interfaces

There are 26 interfaces on this device:

- 22 shutdown
- 4 active (no shutdown)
- 3 access ports with port security enabled:
  - **FastEthernet0/1**: PC4-access port, VLAN 11.
  - **FastEthernet0/2**: PC5-access port, VLAN 12.
  - **FastEthernet0/3**: Management-PC access port, VLAN 90.

## Spanning Tree Protocol

STP (Spanning Tree Protocol) is enabled with PVST (Per-VLAN Spanning Tree) mode. The root bridge priority for VLANs 11 and 12 is set to 28672.

### Per-VLAN Priorities
The following per-VLAN priorities are configured:

- VLAN 11: 28672
- VLAN 12: 28672
- VLAN 90: 28672

## Security Features

Several security features are enabled on this device:

- **DHCP Snooping**: Enabled on VLANs 11 and 12.
- **Dynamic ARP Inspection (DAI)**: Enabled on VLANs 11 and 12.

### Access Control Lists
One standard ACL named `MGMT-MGMT` is configured with three entries.

## Network Services

The following network services are enabled:

- **NTP**: Enabled, with a single NTP server at IP address `10.91.0.123`.
- **Syslog**: Enabled, with a single syslog server at IP address `10.91.0.10`.

### DNS Domain Name
The DNS domain name is set to `krister.local`.

## Routing Configuration

IP routing is disabled on this device.

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
- SSH-only access for VTY access.
- DHCP snooping and DAI enabled on VLANs 11 and 12.
- Port security enabled on three access ports.

#### ⚠ Areas for Improvement
- No firewall configuration (e.g., ACLs).
- No IP source guard configured.
- No 802.1X authentication configured.

#### Recommendations
- Implement a firewall to restrict incoming traffic.
- Configure IP source guard to prevent MAC spoofing.
- Enable 802.1X authentication on access ports.

## Summary

This device appears to be an access layer switch, with many access ports and port security enabled. The management VLAN is configured for secure access. However, there are areas for improvement in terms of security posture, including the lack of a firewall and IP source guard configuration.

**Data Source**: Structured configuration analysis
**Generated**: 2026-01-05T14:12:10.411010