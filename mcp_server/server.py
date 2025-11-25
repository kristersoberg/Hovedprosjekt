#!/usr/bin/env python3
"""
Cisco Documentation MCP Server

Provides Cisco IOS command and feature documentation to LLMs via the Model Context Protocol.
"""

import json
import sys
import asyncio
from pathlib import Path
from typing import Any, Dict, List

from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    CallToolResult,
)


class CiscoDocsMCPServer:
    """MCP Server for Cisco IOS documentation."""

    def __init__(self):
        self.server = Server("cisco-docs-server")
        self.docs_cache_dir = Path(__file__).parent.parent / "docs_cache"
        self.basic_commands_path = self.docs_cache_dir / "basic_commands.json"

        # Ensure cache directory exists
        self.docs_cache_dir.mkdir(exist_ok=True)

        # Initialize basic documentation
        asyncio.create_task(self._initialize_basic_docs())

        # Register handlers
        self._setup_handlers()

    async def _initialize_basic_docs(self):
        """Initialize basic Cisco command documentation if not exists."""
        if not self.basic_commands_path.exists():
            basic_docs = {
                "interface": {
                    "description": "Configures an interface and enters interface configuration mode",
                    "syntax": "interface <type> <number>",
                    "examples": ["interface GigabitEthernet0/1", "interface Vlan10"],
                    "parameters": {
                        "type": "Interface type (e.g., GigabitEthernet, FastEthernet, Vlan, Loopback)",
                        "number": "Interface number or ID"
                    }
                },
                "ip address": {
                    "description": "Sets a primary or secondary IP address for an interface",
                    "syntax": "ip address <ip-address> <subnet-mask> [secondary]",
                    "examples": ["ip address 192.168.1.1 255.255.255.0"],
                    "parameters": {
                        "ip-address": "IP address in dotted decimal notation",
                        "subnet-mask": "Network mask in dotted decimal notation",
                        "secondary": "Optional keyword to specify a secondary address"
                    }
                },
                "switchport": {
                    "description": "Sets interface as a Layer 2 switched interface",
                    "syntax": "switchport mode <mode>",
                    "modes": ["access", "trunk", "dynamic auto", "dynamic desirable"],
                    "examples": ["switchport mode access", "switchport mode trunk"]
                },
                "vlan": {
                    "description": "Configures a VLAN and enters VLAN configuration mode",
                    "syntax": "vlan <vlan-id>",
                    "examples": ["vlan 10", "vlan 100"],
                    "parameters": {
                        "vlan-id": "VLAN number (1-4094)"
                    }
                },
                "spanning-tree": {
                    "description": "Configures Spanning Tree Protocol",
                    "syntax": "spanning-tree <options>",
                    "examples": ["spanning-tree mode rapid-pvst", "spanning-tree portfast"],
                    "modes": ["pvst", "rapid-pvst", "mst"]
                },
                "router": {
                    "description": "Enables a routing process and enters router configuration mode",
                    "syntax": "router <protocol> [autonomous-system]",
                    "examples": ["router ospf 1", "router eigrp 100", "router bgp 65000"],
                    "protocols": ["ospf", "eigrp", "bgp", "rip"]
                },
                "access-list": {
                    "description": "Configures a standard or extended access list",
                    "syntax": "access-list <number> <permit|deny> <source> [wildcard]",
                    "examples": ["access-list 10 permit 192.168.1.0 0.0.0.255"],
                    "ranges": {
                        "standard": "1-99, 1300-1999",
                        "extended": "100-199, 2000-2699"
                    }
                },
                "line": {
                    "description": "Configures a line and enters line configuration mode",
                    "syntax": "line <type> <number>",
                    "examples": ["line vty 0 4", "line console 0"],
                    "types": ["console", "vty", "aux"]
                },
                "enable secret": {
                    "description": "Sets the encrypted privileged EXEC mode password",
                    "syntax": "enable secret <password>",
                    "examples": ["enable secret MySecurePassword123"]
                },
                "hostname": {
                    "description": "Sets the system hostname",
                    "syntax": "hostname <name>",
                    "examples": ["hostname CORE-SWITCH-01"]
                },
                "trunk": {
                    "description": "Configures trunk-specific parameters",
                    "commands": {
                        "switchport trunk allowed vlan": "Specifies VLANs allowed on trunk",
                        "switchport trunk native vlan": "Sets native VLAN for 802.1Q trunk",
                        "switchport trunk encapsulation": "Sets trunk encapsulation (dot1q or isl)"
                    }
                },
                "channel-group": {
                    "description": "Assigns interface to an EtherChannel group",
                    "syntax": "channel-group <number> mode <mode>",
                    "modes": ["on", "active", "passive", "auto", "desirable"],
                    "examples": ["channel-group 1 mode active"]
                }
            }

            with open(self.basic_commands_path, 'w') as f:
                json.dump(basic_docs, f, indent=2)

    def _setup_handlers(self):
        """Set up MCP request handlers."""

        @self.server.list_tools()
        async def handle_list_tools() -> List[Tool]:
            """List available tools."""
            return [
                Tool(
                    name="search_command",
                    description="Search for Cisco IOS command documentation by command name or keyword",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "command": {
                                "type": "string",
                                "description": "The Cisco IOS command to search for (e.g., 'interface', 'ip address', 'vlan')"
                            },
                            "ios_version": {
                                "type": "string",
                                "description": "Optional: Specific IOS version (e.g., '15.2', '12.2')"
                            }
                        },
                        "required": ["command"]
                    }
                ),
                Tool(
                    name="get_feature_docs",
                    description="Get documentation for a specific Cisco feature or technology",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "feature": {
                                "type": "string",
                                "description": "The feature to look up (e.g., 'VLAN', 'OSPF', 'STP', 'VTP', 'EtherChannel')"
                            },
                            "ios_version": {
                                "type": "string",
                                "description": "Optional: Specific IOS version"
                            }
                        },
                        "required": ["feature"]
                    }
                ),
                Tool(
                    name="validate_syntax",
                    description="Validate Cisco IOS command syntax",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "command": {
                                "type": "string",
                                "description": "The full command line to validate"
                            },
                            "context": {
                                "type": "string",
                                "description": "Configuration context (e.g., 'global', 'interface', 'router')"
                            }
                        },
                        "required": ["command"]
                    }
                ),
                Tool(
                    name="explain_config_section",
                    description="Get explanation for a configuration section or block",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "config_block": {
                                "type": "string",
                                "description": "The configuration block to explain"
                            }
                        },
                        "required": ["config_block"]
                    }
                )
            ]

        @self.server.call_tool()
        async def handle_call_tool(name: str, arguments: dict) -> List[TextContent]:
            """Handle tool calls."""
            if name == "search_command":
                return await self._search_command(arguments)
            elif name == "get_feature_docs":
                return await self._get_feature_docs(arguments)
            elif name == "validate_syntax":
                return await self._validate_syntax(arguments)
            elif name == "explain_config_section":
                return await self._explain_config_section(arguments)
            else:
                raise ValueError(f"Unknown tool: {name}")

    async def _search_command(self, args: dict) -> List[TextContent]:
        """Search for command documentation."""
        command = args.get("command", "").lower().strip()
        ios_version = args.get("ios_version")

        try:
            with open(self.basic_commands_path, 'r') as f:
                docs = json.load(f)

            # Search for exact or partial match
            result = docs.get(command)

            if not result:
                # Try partial match
                matches = [key for key in docs.keys()
                          if command in key or key in command]
                if matches:
                    result = docs[matches[0]]
                    result["matched_command"] = matches[0]

            if result:
                version_note = f"\n\nNote: Documentation requested for IOS version {ios_version}. " \
                              f"The information provided is generally applicable across IOS versions, " \
                              f"but verify specific syntax for your version." if ios_version else ""

                return [TextContent(
                    type="text",
                    text=f"Command: {command}\n\n{json.dumps(result, indent=2)}{version_note}"
                )]
            else:
                return [TextContent(
                    type="text",
                    text=f'Command "{command}" not found in local cache. This may be a valid Cisco command, '
                         f'but documentation is not available locally. Consider adding it to the documentation '
                         f'cache or consulting Cisco\'s official documentation.'
                )]

        except Exception as e:
            return [TextContent(
                type="text",
                text=f"Error searching for command: {str(e)}"
            )]

    async def _get_feature_docs(self, args: dict) -> List[TextContent]:
        """Get feature documentation."""
        feature = args.get("feature", "")
        ios_version = args.get("ios_version")

        feature_docs = {
            "VLAN": {
                "description": "Virtual Local Area Networks (VLANs) are logical broadcast domains that can span multiple physical LAN segments",
                "key_concepts": [
                    "VLANs segment networks at Layer 2",
                    "Default VLAN is VLAN 1",
                    "VLAN range: 1-4094 (1-1005 normal range, 1006-4094 extended)",
                    "VLANs 1, 1002-1005 are reserved and cannot be deleted"
                ],
                "common_commands": [
                    "vlan <id> - Create/enter VLAN configuration",
                    "name <name> - Assign VLAN name",
                    "switchport access vlan <id> - Assign port to VLAN",
                    "show vlan brief - Display VLAN information"
                ],
                "best_practices": [
                    "Use meaningful VLAN names",
                    "Document VLAN assignments",
                    "Avoid using VLAN 1 for user traffic",
                    "Plan VLAN numbering scheme"
                ]
            },
            "OSPF": {
                "description": "Open Shortest Path First - Link-state routing protocol",
                "key_concepts": [
                    "Uses Dijkstra's algorithm",
                    "Supports VLSM and CIDR",
                    "Fast convergence",
                    "Hierarchical design with areas",
                    "Area 0 is the backbone area"
                ],
                "common_commands": [
                    "router ospf <process-id>",
                    "network <address> <wildcard> area <area-id>",
                    "router-id <id>",
                    "passive-interface <interface>",
                    "show ip ospf neighbor",
                    "show ip ospf database"
                ],
                "best_practices": [
                    "Always configure router-id manually",
                    "Use passive-interface for security",
                    "Summarize routes at area boundaries",
                    "Keep area 0 contiguous"
                ]
            },
            "STP": {
                "description": "Spanning Tree Protocol prevents Layer 2 loops in redundant network topologies",
                "key_concepts": [
                    "Prevents broadcast storms",
                    "Elects root bridge based on lowest bridge ID",
                    "Port states: Blocking, Listening, Learning, Forwarding",
                    "PVST+ runs per-VLAN instance",
                    "RSTP (Rapid STP) provides faster convergence"
                ],
                "common_commands": [
                    "spanning-tree mode <pvst|rapid-pvst|mst>",
                    "spanning-tree vlan <id> root primary|secondary",
                    "spanning-tree portfast",
                    "spanning-tree bpduguard enable",
                    "show spanning-tree",
                    "show spanning-tree summary"
                ],
                "best_practices": [
                    "Enable PortFast on access ports",
                    "Use BPDU Guard on access ports",
                    "Manually configure root bridge",
                    "Use Root Guard on specific ports"
                ]
            },
            "EtherChannel": {
                "description": "Link aggregation technology that bundles multiple physical links into one logical link",
                "key_concepts": [
                    "Increases bandwidth and provides redundancy",
                    "Load balances traffic across member links",
                    "Can bundle 2-8 links",
                    "All links must have same speed and duplex",
                    "Protocols: PAgP (Cisco), LACP (IEEE 802.3ad), Static"
                ],
                "common_commands": [
                    "interface range <interface-range>",
                    "channel-group <number> mode <on|active|passive|auto|desirable>",
                    "interface port-channel <number>",
                    "show etherchannel summary",
                    "show etherchannel port-channel"
                ],
                "modes": {
                    "on": "Forces EtherChannel without negotiation",
                    "active": "LACP - actively negotiate",
                    "passive": "LACP - passive negotiate",
                    "auto": "PAgP - passive negotiate",
                    "desirable": "PAgP - actively negotiate"
                },
                "best_practices": [
                    "Use LACP (active/passive) for standard compliance",
                    "Ensure all member interfaces have identical configuration",
                    "Configure both physical interfaces and port-channel",
                    "Verify with show etherchannel summary"
                ]
            },
            "VTP": {
                "description": "VLAN Trunking Protocol - Cisco proprietary protocol for propagating VLAN configuration",
                "key_concepts": [
                    "Synchronizes VLAN database across switches",
                    "Three modes: Server, Client, Transparent",
                    "VTP advertisements sent over trunk links",
                    "Domain name must match for synchronization"
                ],
                "common_commands": [
                    "vtp mode <server|client|transparent>",
                    "vtp domain <name>",
                    "vtp password <password>",
                    "vtp version <1|2|3>",
                    "show vtp status"
                ],
                "best_practices": [
                    "Use VTP transparent mode or disable VTP in most modern networks",
                    "Always set VTP mode before connecting new switch",
                    "Use VTP password for security",
                    "Document VTP configuration carefully"
                ]
            }
        }

        feature_key = next((k for k in feature_docs.keys()
                           if k.lower() == feature.lower()), None)

        if feature_key:
            version_note = f"\n\nDocumentation context: IOS version {ios_version}" if ios_version else ""
            return [TextContent(
                type="text",
                text=f"Feature: {feature_key}\n\n{json.dumps(feature_docs[feature_key], indent=2)}{version_note}"
            )]
        else:
            available = ", ".join(feature_docs.keys())
            return [TextContent(
                type="text",
                text=f'Feature "{feature}" documentation not found in cache. Available features: {available}'
            )]

    async def _validate_syntax(self, args: dict) -> List[TextContent]:
        """Validate command syntax."""
        command = args.get("command", "")
        context = args.get("context", "unknown")

        validation = {
            "command": command,
            "context": context,
            "is_valid": True,
            "warnings": [],
            "suggestions": []
        }

        # Basic validation rules
        if "  " in command:
            validation["warnings"].append("Command contains double spaces")

        # Check IP address format
        import re
        if re.search(r'\d+\.\d+\.\d+\.\d+', command):
            if 'ip address' in command and not re.search(r'\d+\.\d+\.\d+\.\d+\s+\d+\.\d+\.\d+\.\d+', command):
                validation["warnings"].append("IP address command typically requires both IP and subnet mask")

        return [TextContent(
            type="text",
            text=json.dumps(validation, indent=2)
        )]

    async def _explain_config_section(self, args: dict) -> List[TextContent]:
        """Explain configuration section."""
        config_block = args.get("config_block", "")

        return [TextContent(
            type="text",
            text=f"Configuration block analysis:\n\n{config_block}\n\n"
                 f"This tool provides context about the configuration section. "
                 f"Use search_command for specific command details."
        )]

    async def run(self):
        """Run the MCP server."""
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="cisco-docs-server",
                    server_version="1.0.0",
                    capabilities=self.server.get_capabilities(
                        notification_options=NotificationOptions(),
                        experimental_capabilities={}
                    )
                )
            )


async def main():
    """Main entry point."""
    server = CiscoDocsMCPServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())