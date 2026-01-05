"""
Structured Prompt Builder

Builds LLM prompts from pre-parsed structured configuration data.
This ensures the LLM receives accurate, factual data instead of having to parse raw configs.
"""

import json
from typing import Dict, Any, List
from datetime import datetime


class StructuredPromptBuilder:
    """Build LLM prompts from structured configuration data."""

    def __init__(self, structured_data: Dict[str, Any], mcp_docs: str = ""):
        """
        Initialize with structured config data.

        Args:
            structured_data: Parsed configuration data from config_parser.py
            mcp_docs: Optional MCP documentation to include
        """
        self.data = structured_data
        self.mcp_docs = mcp_docs

    def build_prompt(self) -> str:
        """Build complete prompt for LLM."""
        device_info = self.data.get("device_info", {})
        hostname = device_info.get("hostname") or "Unknown"
        ios_version = device_info.get("ios_version") or "Unknown"

        prompt = f"""You are an expert Cisco network engineer creating professional documentation.

You are provided with STRUCTURED, PRE-PARSED configuration data. This data has been extracted deterministically from a Cisco IOS configuration file, so all values are FACTUALLY CORRECT.

## CRITICAL RULES:

1. **USE THE PROVIDED DATA EXACTLY** - The structured data below contains factual information extracted from the configuration. Do NOT change these values.
2. **Example**: If structured_data shows `"hostname": "aksess-sw01"`, the hostname IS "aksess-sw01". Never change it to something else.
3. **MARK CONFIDENCE ACCURATELY**:
   - ✓ VERIFIED - Data directly from structured_data (hostname, IP addresses, VLANs, counts, etc.)
   - ~ INFERRED - Your analysis/interpretation (device role, security posture, recommendations)
   - ? UNCERTAIN - Information not available in the data

4. **NEVER HALLUCINATE** - If data is null or missing, write "Not configured" - do NOT invent values.

---

## STRUCTURED CONFIGURATION DATA

**Device**: {hostname}
**IOS Version**: {ios_version}

### Device Information (✓ ALL VERIFIED)
"""
        prompt += self._format_device_info()
        prompt += "\n\n### Management Configuration (✓ ALL VERIFIED)\n"
        prompt += self._format_management()
        prompt += "\n\n### AAA Configuration (✓ ALL VERIFIED)\n"
        prompt += self._format_aaa()
        prompt += "\n\n### VLAN Configuration (✓ ALL VERIFIED)\n"
        prompt += self._format_vlans()
        prompt += "\n\n### Interface Configuration (✓ ALL VERIFIED)\n"
        prompt += self._format_interfaces_summary()
        prompt += "\n\n### Routing Configuration (✓ ALL VERIFIED)\n"
        prompt += self._format_routing()
        prompt += "\n\n### Spanning Tree Configuration (✓ ALL VERIFIED)\n"
        prompt += self._format_stp()
        prompt += "\n\n### Security Features (✓ ALL VERIFIED)\n"
        prompt += self._format_security()
        prompt += "\n\n### Network Services (✓ ALL VERIFIED)\n"
        prompt += self._format_services()

        if self.mcp_docs:
            prompt += f"\n\n## CISCO DOCUMENTATION REFERENCE\n\n{self.mcp_docs}\n"

        prompt += "\n\n---\n\n"
        prompt += self._build_task_instructions()

        # Add raw config for reference
        prompt += f"\n\n### Raw Configuration (for config line citations)\n\n```\n{self.data.get('raw_config', '')}\n```\n"

        return prompt

    def _format_device_info(self) -> str:
        """Format device information section."""
        info = self.data.get("device_info", {})
        return f"""
- Hostname: {info.get('hostname') or 'Not configured'}
- IOS Version: {info.get('ios_version') or 'Unknown'}
- Domain Name: {info.get('domain_name') or 'Not configured'}
- Config Register: {info.get('config_register') or 'Not shown'}
"""

    def _format_management(self) -> str:
        """Format management configuration."""
        mgmt = self.data.get("management", {})

        output = "#### Management Interface\n"
        if mgmt.get("svi"):
            output += f"- Management VLAN: {mgmt['svi']}\n"
            output += f"- IP Address: {mgmt.get('ip_address', 'Not configured')}\n"
            output += f"- Subnet Mask: {mgmt.get('subnet_mask', 'Not configured')}\n"
            output += f"- Default Gateway: {mgmt.get('default_gateway', 'Not configured')}\n"
        else:
            output += "- No management SVI configured\n"

        output += "\n#### SSH Configuration\n"
        ssh = mgmt.get("ssh", {})
        if ssh:
            output += f"- SSH Version: {ssh.get('version', 'Not configured')}\n"
            output += f"- SSH Timeout: {ssh.get('timeout', 'Not configured')} seconds\n"
        else:
            output += "- SSH not explicitly configured\n"

        output += "\n#### Console Access\n"
        console = mgmt.get("console", {})
        if console:
            output += f"- Line: {console.get('range', 'con 0')}\n"
            output += f"- Authentication: {console.get('authentication', 'Not configured')}\n"
            output += f"- Logging Synchronous: {console.get('logging_synchronous', False)}\n"

        output += "\n#### VTY Access\n"
        vty = mgmt.get("vty", {})
        if vty:
            output += f"- Lines: {vty.get('range', 'Not configured')}\n"
            output += f"- Transport Input: {', '.join(vty.get('transport_input', []) or ['Not specified'])}\n"
            output += f"- Authentication: {vty.get('authentication', 'Not configured')}\n"
            acl = vty.get('access_class')
            if acl:
                output += f"- Access Class: {acl.get('acl')} ({acl.get('direction')})\n"
            else:
                output += "- Access Class: None (⚠ No ACL protection)\n"

        return output

    def _format_aaa(self) -> str:
        """Format AAA configuration."""
        aaa = self.data.get("aaa", {})

        if not aaa.get("enabled"):
            return "- AAA: Not enabled\n"

        output = "- AAA: ✓ Enabled\n\n"

        if aaa.get("authentication"):
            output += "**Authentication Lists:**\n"
            for auth in aaa["authentication"]:
                output += f"  - {auth}\n"

        if aaa.get("authorization"):
            output += "\n**Authorization Lists:**\n"
            for authz in aaa["authorization"]:
                output += f"  - {authz}\n"

        if aaa.get("accounting"):
            output += "\n**Accounting:**\n"
            for acct in aaa["accounting"]:
                output += f"  - {acct}\n"

        if aaa.get("tacacs_servers"):
            output += f"\n**TACACS+ Servers:** {', '.join(aaa['tacacs_servers'])}\n"

        if aaa.get("radius_servers"):
            output += f"\n**RADIUS Servers:** {', '.join(aaa['radius_servers'])}\n"

        if aaa.get("local_users"):
            output += "\n**Local Users:**\n"
            for user in aaa["local_users"]:
                priv = user.get("privilege", "not specified")
                output += f"  - {user['username']} (privilege {priv})\n"

        return output

    def _format_vlans(self) -> str:
        """Format VLAN configuration."""
        vlans = self.data.get("vlans", {})

        vlan_ids = vlans.get("vlan_ids", [])
        output = f"**Total VLANs Referenced:** {len(vlan_ids)}\n"
        output += f"**VLAN IDs:** {', '.join(map(str, vlan_ids)) if vlan_ids else 'None'}\n"

        svi_list = vlans.get("svi_interfaces", [])
        if svi_list:
            output += f"\n**VLAN Interfaces (SVIs):** {len(svi_list)} configured\n\n"
            for svi in svi_list:
                output += f"- **VLAN {svi['vlan_id']}**\n"
                if svi.get('description'):
                    output += f"  - Description: {svi['description']}\n"
                if svi.get('ip_address'):
                    output += f"  - IP: {svi['ip_address']} {svi.get('subnet_mask', '')}\n"
                output += f"  - Status: {'Shutdown' if svi.get('shutdown') else 'Active'}\n"
                if svi.get('acl_in'):
                    output += f"  - ACL In: {svi['acl_in']}\n"
                if svi.get('hsrp'):
                    output += f"  - HSRP: Configured\n"
                if svi.get('vrrp'):
                    output += f"  - VRRP: Configured\n"
                output += "\n"

        vtp = vlans.get("vtp", {})
        output += "**VTP Configuration:**\n"
        if vtp.get("mode"):
            output += f"  - Mode: {vtp['mode']}\n"
            output += f"  - Domain: {vtp.get('domain', 'Not set')}\n"
            output += f"  - Version: {vtp.get('version', 'Not set')}\n"
        else:
            output += "  - Not explicitly configured\n"

        return output

    def _format_interfaces_summary(self) -> str:
        """Format interface summary."""
        interfaces = self.data.get("interfaces", [])

        total = len(interfaces)
        active = sum(1 for i in interfaces if not i.get("shutdown"))
        shutdown = total - active
        access_ports = sum(1 for i in interfaces if i.get("mode") == "access")
        trunk_ports = sum(1 for i in interfaces if i.get("mode") == "trunk")
        port_sec_count = sum(1 for i in interfaces if i.get("port_security", {}).get("enabled"))

        output = f"""**Interface Statistics:**
- Total Interfaces: {total}
- Active (no shutdown): {active}
- Shutdown: {shutdown}
- Access Ports: {access_ports}
- Trunk Ports: {trunk_ports}
- Port Security Enabled: {port_sec_count} interfaces

**Detailed Interface List:**

"""
        # List first 5 active interfaces as examples
        active_intfs = [i for i in interfaces if not i.get("shutdown")][:5]
        for intf in active_intfs:
            output += f"- **{intf['name']}**"
            if intf.get('description'):
                output += f" - {intf['description']}"
            output += f" | Mode: {intf.get('mode', 'not set')}"
            if intf.get('access_vlan'):
                output += f" | VLAN: {intf['access_vlan']}"
            if intf.get('trunk_allowed_vlans'):
                vlans = intf['trunk_allowed_vlans']
                output += f" | Allowed VLANs: {vlans if isinstance(vlans, str) else ', '.join(map(str, vlans[:5]))}"
            if intf.get('port_security', {}).get('enabled'):
                output += " | Port-Sec: ✓"
            output += "\n"

        if len(interfaces) > 5:
            output += f"\n... and {len(interfaces) - 5} more interfaces (see raw config for details)\n"

        return output

    def _format_routing(self) -> str:
        """Format routing configuration."""
        routing = self.data.get("routing", {})

        output = f"- IP Routing: {'Enabled' if routing.get('ip_routing_enabled') else 'Disabled'}\n"

        if routing.get('default_gateway'):
            output += f"- Default Gateway: {routing['default_gateway']}\n"

        if routing.get('static_routes'):
            output += f"\n**Static Routes:** {len(routing['static_routes'])} configured\n"
            for route in routing['static_routes']:
                output += f"  - {route['network']} {route['mask']} via {route['next_hop']}\n"

        if routing.get('routing_protocols'):
            output += f"\n**Routing Protocols:** {', '.join(routing['routing_protocols'])}\n"

        return output

    def _format_stp(self) -> str:
        """Format spanning tree configuration."""
        stp = self.data.get("spanning_tree", {})

        output = f"- STP Mode: {stp.get('mode', 'Not configured')}\n"

        vlan_priorities = stp.get("vlan_priorities", {})
        if vlan_priorities:
            output += "\n**Per-VLAN Priorities:**\n"
            for vlan_id, priority in sorted(vlan_priorities.items()):
                output += f"  - VLAN {vlan_id}: {priority}\n"

        if stp.get("global_features"):
            output += f"\n**Global Features:** {', '.join(stp['global_features'])}\n"

        return output

    def _format_security(self) -> str:
        """Format security features."""
        security = self.data.get("security", {})

        output = ""

        # DHCP Snooping
        dhcp = security.get("dhcp_snooping", {})
        if dhcp.get("enabled"):
            vlans = ', '.join(map(str, dhcp.get('vlans', []))) if dhcp.get('vlans') else 'Not specified'
            output += f"- **DHCP Snooping:** ✓ Enabled on VLANs {vlans}\n"
            output += f"  - Information Option: {'Enabled' if dhcp.get('information_option', True) else 'Disabled'}\n"
        else:
            output += "- **DHCP Snooping:** Not enabled\n"

        # DAI
        dai = security.get("arp_inspection", {})
        if dai.get("enabled"):
            vlans = ', '.join(map(str, dai.get('vlans', []))) if dai.get('vlans') else 'Not specified'
            output += f"- **Dynamic ARP Inspection:** ✓ Enabled on VLANs {vlans}\n"
        else:
            output += "- **Dynamic ARP Inspection:** Not enabled\n"

        # ACLs
        acls = security.get("acls", [])
        if acls:
            output += f"\n**Access Control Lists:** {len(acls)} configured\n"
            for acl in acls:
                acl_id = acl.get('name') or acl.get('number')
                output += f"  - {acl['type'].capitalize()} ACL '{acl_id}': {len(acl.get('entries', []))} entries\n"

        # Other features
        output += f"\n- **CDP:** {'Disabled ✓' if not security.get('cdp_enabled', True) else 'Enabled'}\n"
        output += f"- **LLDP:** {'Enabled' if security.get('lldp_enabled') else 'Not enabled'}\n"
        output += f"- **802.1X:** {'Enabled' if security.get('dot1x_enabled') else 'Not configured'}\n"
        output += f"- **IP Source Guard:** {'Configured' if security.get('ip_source_guard') else 'Not configured'}\n"

        return output

    def _format_services(self) -> str:
        """Format network services."""
        services = self.data.get("services", {})

        output = ""

        # NTP
        ntp = services.get("ntp", {})
        if ntp.get("enabled"):
            servers = ', '.join(ntp.get('servers', [])) if ntp.get('servers') else 'None'
            output += f"- **NTP:** ✓ Enabled\n"
            output += f"  - Servers: {servers}\n"
            output += f"  - Authentication: {'Enabled' if ntp.get('authentication') else 'Disabled'}\n"
        else:
            output += "- **NTP:** Not configured\n"

        # Syslog
        syslog = services.get("syslog", {})
        if syslog.get("enabled"):
            servers = ', '.join(syslog.get('servers', [])) if syslog.get('servers') else 'None'
            output += f"- **Syslog:** ✓ Enabled\n"
            output += f"  - Servers: {servers}\n"
        else:
            output += "- **Syslog:** Not configured\n"

        # SNMP
        snmp = services.get("snmp", {})
        if snmp.get("enabled"):
            output += f"- **SNMP:** Enabled ({snmp.get('version', 'version unknown')})\n"
        else:
            output += "- **SNMP:** Not configured\n"

        # DNS
        dns = services.get("dns", {})
        output += f"- **DNS Domain Name:** {dns.get('domain_name', 'Not configured')}\n"
        output += f"- **DNS Lookup:** {'Enabled' if dns.get('domain_lookup', True) else 'Disabled'}\n"
        if dns.get('name_servers'):
            output += f"- **Name Servers:** {', '.join(dns['name_servers'])}\n"

        return output

    def _build_task_instructions(self) -> str:
        """Build task instructions for LLM."""
        device_info = self.data.get("device_info", {})
        hostname = device_info.get("hostname") or "Unknown"

        return f"""
## YOUR TASK:

Generate comprehensive Markdown documentation for this network device. Use the STRUCTURED DATA above as your PRIMARY source of truth.

### Critical Instructions:

1. **Trust the structured data** - All values in the "STRUCTURED CONFIGURATION DATA" section are factually correct. Use them EXACTLY as shown.

2. **Hostname is: {hostname}** - Use this exact hostname throughout the document. Do NOT change it.

3. **Mark confidence levels**:
   - ✓ VERIFIED - for any data from the structured data above
   - ~ INFERRED - for your analysis (device role, recommendations, security assessment)
   - ? UNCERTAIN - for anything not available in the data

4. **Device role determination** - Analyze the configuration to determine if this is an Access, Distribution, or Core layer switch:
   - Access layer: Many access ports, port security, no routing
   - Distribution layer: VLANs with IPs (SVIs), inter-VLAN routing, aggregation
   - Core layer: High-speed interfaces, routing protocols, minimal VLANs

5. **Security assessment** - Based on the structured data, identify:
   - Good practices (SSH-only access, DHCP snooping, port security, etc.)
   - Security gaps (missing features that should be configured)
   - Recommendations for improvement

6. **Include config line references** - When documenting features, cite the exact config lines from the raw configuration section

### Document Structure:

```markdown
# Network Device Documentation: {hostname}

## Device Information
[Use device_info from structured data]

## Management & Access
[Use management config from structured data]

## AAA Configuration
[Use aaa from structured data]

## VLANs
[Use vlans from structured data]

## Physical Interfaces
[Use interfaces from structured data - include summary statistics and key interfaces]

## Spanning Tree Protocol
[Use spanning_tree from structured data]

## Security Features
[Use security from structured data]

## Network Services
[Use services from structured data]

## Routing Configuration
[Use routing from structured data]

## Configuration Quality Assessment

### Security Posture

#### ✓ Strengths
[List good security practices found in configuration]

#### ⚠ Areas for Improvement
[List security gaps or concerns]

#### Recommendations
[Specific recommendations based on configuration analysis]

## Summary

[Provide 2-3 sentence summary of device purpose, role, and overall configuration quality]

---

**Data Source**: Structured configuration analysis
**Generated**: {datetime.now().isoformat()}
```

Generate this documentation now, ensuring you use the structured data accurately and mark confidence levels appropriately.
"""


if __name__ == "__main__":
    # Test the prompt builder
    import sys
    import codecs

    if len(sys.argv) < 2:
        print("Usage: python structured_prompt_builder.py <structured_json_file>")
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        data = json.load(f)

    builder = StructuredPromptBuilder(data)
    prompt = builder.build_prompt()

    # Write to stdout with UTF-8 encoding
    sys.stdout.reconfigure(encoding='utf-8')
    print(prompt)
