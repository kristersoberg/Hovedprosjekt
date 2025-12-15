# Switch Configuration Documentation: [Extract hostname from config]

## Overview

| Field | Value | Confidence |
|-------|-------|------------|
| **Hostname** | [from config] | ✓ |
| **IOS Version** | [from config] | ✓ |
| **Domain Name** | [from config or "Not configured"] | |
| **Device Role** | [Access/Distribution/Core] | [~ INFERRED with evidence] |
| **Configuration Date** | [if available or "Not available"] | |

### Device Role Analysis

**Determined Role**: [Access/Distribution/Core] Layer Switch

**Supporting Evidence:**
- Evidence 1: [specific config line or feature]
- Evidence 2: [specific config line or feature]
- Evidence 3: [specific config line or feature]

**Confidence**: [High/Medium/Low]

## Management & Access

### Management Interface

| Setting | Value | Config Reference |
|---------|-------|------------------|
| Management VLAN | | |
| IP Address | | |
| Subnet Mask | | |
| Default Gateway | | |

**Config Lines:**
```
[paste exact config lines]
```

### Remote Access Configuration

#### Console Access
- **Authentication**: [method] ✓
- **Config**: `[exact line]`

#### VTY Access  
- **Lines Configured**: [range]
- **Transport Input**: [protocols allowed]
- **Access Control**: [ACL name if applied]
- **Authentication**: [method]

**Config Lines:**
```
[paste exact config lines]
```

#### SSH Configuration
| Setting | Value | Config Reference |
|---------|-------|------------------|
| SSH Version | | |
| SSH Timeout | | |

### AAA Configuration

**Status**: [Configured/Not Configured]

If configured:
- **Authentication Methods**: 
- **Authorization Methods**:
- **Accounting Methods**:
- **TACACS+/RADIUS Servers**:

**Config Lines:**
```
[paste exact config lines]
```

### Login Banner

**Status**: [Configured/Not Configured]

If configured, describe purpose (do not reproduce full banner text if lengthy).

### Management Access Lists

For each ACL applied to management access:

**ACL Name**: [name]
**Applied To**: [vty lines, management interface, etc.]
**Purpose**: [brief description]
**Rules Summary**:
| Action | Source | Description |
|--------|--------|-------------|
| | | |

**Config Lines:**
```
[paste exact config lines]
```

## VLANs

### VLAN Summary

**Total VLANs Referenced in Config**: [count - verify manually]

| VLAN ID | Name | Purpose | Config Reference |
|---------|------|---------|------------------|
| | | | |

**Note**: Only list VLANs that appear in the configuration (in interface configs, STP configs, trunk allowed lists, etc.)

### VLAN Interfaces (SVIs)

For each SVI configured:

#### VLAN [ID] Interface

| Setting | Value | Config Reference |
|---------|-------|------------------|
| IP Address | | |
| Subnet Mask | | |
| Description | | |
| Status | | |
| DHCP Helper | | |
| HSRP/VRRP | | |
| ACL Applied | | |

**Config Lines:**
```
[paste exact config lines]
```

### VTP Configuration

**Status**: [Configured/Not Configured/Disabled]

If configured:
| Setting | Value | Config Reference |
|---------|-------|------------------|
| VTP Mode | | |
| VTP Domain | | |
| VTP Version | | |

If not explicitly configured, state: "VTP not explicitly configured in running-config. Device may be using defaults (mode: server) or VTP may be disabled."

## Physical Interfaces

### Interface Summary

**Total Interfaces**: [count]
**Active Interfaces**: [count] 
**Shutdown Interfaces**: [count]
**Trunk Interfaces**: [count]
**Access Interfaces**: [count]

| Interface | Description | Mode | VLAN(s) | Status | Security Features |
|-----------|-------------|------|---------|--------|-------------------|
| | | | | | |

**Verification**: Ensure counts match the table entries.

### Detailed Interface Configurations

Document each interface with non-default configuration:

#### [Interface Name]

**Description**: [from config or "None"]
**Operational Mode**: [Access/Trunk/Dynamic]
**Admin Status**: [No shutdown/Shutdown]

| Configuration | Value | Config Line |
|---------------|-------|-------------|
| | | |

**Full Config Block:**
```
[paste complete interface config]
```

**Analysis**: [Brief explanation of this interface's purpose and configuration]

### Trunk Port Configuration

For each trunk port:

#### [Interface Name] - Trunk

| Setting | Value | Config Line |
|---------|-------|-------------|
| Encapsulation | | |
| Native VLAN | | |
| Allowed VLANs | | |
| DTP Mode | | |

**Security Considerations**: [Note if native VLAN is default, if DTP is enabled, etc.]

### Unused Interfaces

**Count**: [number] interfaces in shutdown state

**Shutdown Interfaces**: [list or range, e.g., F0/4-F0/24, G0/2]

**Security Assessment**: [Are unused ports properly secured?]

## Port-Channel / EtherChannel

**Status**: [Configured/Not Configured]

If configured, for each port-channel:

#### Port-Channel [ID]

| Setting | Value | Config Reference |
|---------|-------|------------------|
| Member Interfaces | | |
| Mode | | |
| Load Balance Method | | |

## Routing Configuration

### Layer 3 Capability

**Inter-VLAN Routing**: [Enabled/Disabled]
**Routing Protocol**: [None/OSPF/EIGRP/RIP/BGP/Static Only]

### Default Gateway

| Setting | Value | Config Line |
|---------|-------|-------------|
| Default Gateway | | |

### Static Routes

**Status**: [Configured/Not Configured]

If configured:
| Destination | Mask | Next-Hop | Config Line |
|-------------|------|----------|-------------|
| | | | |

### Dynamic Routing

**Status**: [Not Configured] or document fully if present

## Spanning Tree Protocol

### STP Configuration

| Setting | Value | Config Reference |
|---------|-------|------------------|
| STP Mode | | |
| Priority | | |
| Root Bridge | | |

**Config Lines:**
```
[paste STP config lines]
```

### STP Security Features

| Feature | Status | Interfaces | Config Reference |
|---------|--------|------------|------------------|
| PortFast | | | |
| BPDU Guard | | | |
| Root Guard | | | |
| Loop Guard | | | |

### Per-VLAN STP Settings

If non-default priorities or settings exist:

| VLAN | Priority | Root Status |
|------|----------|-------------|
| | | |

## Security Features

### Port Security

**Status**: [Configured/Not Configured]

If configured:

**Interfaces with Port Security**: [list]

| Interface | Max MACs | Violation Action | Sticky MACs | Aging | Config Reference |
|-----------|----------|------------------|-------------|-------|------------------|
| | | | | | |

**Note**: If max MACs not specified, default is 1.

**Config Lines:**
```
[paste port-security config lines]
```

### DHCP Security

#### DHCP Snooping

**Status**: [Enabled/Disabled]

If enabled:
| Setting | Value | Config Reference |
|---------|-------|------------------|
| Protected VLANs | | |
| Trusted Ports | | |
| Rate Limiting | | |

**Config Lines:**
```
[paste exact config lines]
```

#### Dynamic ARP Inspection (DAI)

**Status**: [Enabled/Disabled]

If enabled:
| Setting | Value | Config Reference |
|---------|-------|------------------|
| Protected VLANs | | |
| Trusted Ports | | |

**Config Lines:**
```
[paste exact config lines]
```

### Storm Control

**Status**: [Configured/Not Configured]

If configured:
| Interface | Broadcast Level | Multicast Level | Unicast Level |
|-----------|-----------------|-----------------|---------------|
| | | | |

### Access Control Lists

For each ACL:

#### ACL: [Name/Number]

**Type**: [Standard/Extended]
**Purpose**: [describe based on where it's applied]
**Applied To**: [interfaces, VTY lines, etc.]

| Seq | Action | Source | Destination | Protocol/Port |
|-----|--------|--------|-------------|---------------|
| | | | | |

**Config Lines:**
```
[paste exact ACL config]
```

### 802.1X Configuration

**Status**: [Configured/Not Configured]

### Additional Security Features

| Feature | Status | Config Reference |
|---------|--------|------------------|
| CDP | | |
| LLDP | | |
| IP Source Guard | | |
| UDLD | | |

## Network Services

### NTP Configuration

**Status**: [Configured/Not Configured]

If configured:
| Setting | Value | Config Reference |
|---------|-------|------------------|
| NTP Server(s) | | |
| NTP Authentication | | |
| Timezone | | |

### Syslog Configuration

**Status**: [Configured/Not Configured]

If configured:
| Setting | Value | Config Reference |
|---------|-------|------------------|
| Logging Host(s) | | |
| Logging Level | | |
| Buffer Size | | |

### SNMP Configuration

**Status**: [Configured/Not Configured]

If configured, document settings (do not expose community strings).

### DNS Configuration

| Setting | Value | Config Reference |
|---------|-------|------------------|
| Domain Name | | |
| Domain Lookup | | |
| Name Servers | | |

### Other Services

| Service | Status | Config Reference |
|---------|--------|------------------|
| HTTP Server | | |
| HTTPS Server | | |
| CDP | | |
| LLDP | | |

## Configuration Quality Assessment

### Security Posture

#### Strengths (Good Practices Identified)
List configurations that follow security best practices:

1. [Practice]: [Config evidence]
2. [Practice]: [Config evidence]

#### Concerns (Potential Issues)
List security concerns or misconfigurations:

1. **[Issue]**: [Description]
   - Config: `[relevant line]`
   - Risk: [explain risk]
   - Recommendation: [how to fix]

#### Missing Security Features
List recommended security features that are not configured:

1. [Feature]: [Why it should be considered]

### Operational Recommendations

1. **[Recommendation]**: [Explanation and justification]
2. **[Recommendation]**: [Explanation and justification]

## Summary

| Metric | Value |
|--------|-------|
| Total VLANs | |
| Active Interfaces | |
| Shutdown Interfaces | |
| Trunk Ports | |
| Device Role | |
| STP Mode | |
| Layer 3 Routing | |
| Port Security | |
| DHCP Snooping | |
| DAI | |

### Overall Assessment

[2-4 sentences describing the overall configuration quality, purpose of this switch in the network, and any critical items requiring attention]

## Verification Checklist

Before finalizing this documentation, verify:

- [ ] All VLAN counts match actual VLANs in config
- [ ] All interface counts match actual interfaces
- [ ] Every security feature documented has a config line reference
- [ ] Device role determination includes specific evidence
- [ ] No features are documented that don't exist in the config
- [ ] Trusted ports for DHCP snooping and DAI are correctly identified
- [ ] All ACLs are documented with their application points

### Items Requiring Human Review

List any items marked with ? UNCERTAIN or where you could not verify information:

| Item | Reason for Uncertainty |
|------|------------------------|
| | |

### MCP Tools Used

List the MCP tool calls made during this analysis:

| Tool | Query | Result Summary |
|------|-------|------------------|
| | | |

---

*Documentation generated from running-config analysis*
*Configuration File: [filename]*
*Analysis Date: [current date]*