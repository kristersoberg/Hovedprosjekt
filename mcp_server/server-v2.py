#!/usr/bin/env python3
"""
Cisco Documentation MCP Server - v2 (Verbose Edition)

Provides Cisco IOS command and feature documentation to LLMs via the Model Context Protocol.
This version includes comprehensive logging to stderr for better visibility into server operations.
"""

import json
import sys
import asyncio
import logging
import os
from pathlib import Path
from typing import Any, Dict, List
from datetime import datetime

from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    CallToolResult,
)

# Configure logging to stderr (stdout is reserved for MCP protocol)
DEBUG = os.getenv("MCP_DEBUG", "false").lower() == "true"
log_level = logging.DEBUG if DEBUG else logging.INFO

# Check if log file path is specified
log_file = os.getenv("MCP_LOG_FILE")
handlers = []

if log_file:
    # Log to file when specified
    handlers.append(logging.FileHandler(log_file, mode='a', encoding='utf-8'))
else:
    # Default: log to stderr
    handlers.append(logging.StreamHandler(sys.stderr))

logging.basicConfig(
    level=log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=handlers
)

logger = logging.getLogger("cisco-docs-mcp")


class CiscoDocsMCPServer:
    """MCP Server for Cisco IOS documentation."""

    def __init__(self):
        logger.info("=" * 60)
        logger.info("Initializing Cisco Documentation MCP Server v2")
        logger.info("=" * 60)

        self.server = Server("cisco-docs-server")
        self.docs_cache_dir = Path(__file__).parent.parent / "docs_cache"
        self.basic_commands_path = self.docs_cache_dir / "basic_commands.json"

        logger.info(f"Server name: cisco-docs-server")
        logger.info(f"Cache directory: {self.docs_cache_dir}")
        logger.info(f"Basic commands file: {self.basic_commands_path}")

        # Ensure cache directory exists
        if not self.docs_cache_dir.exists():
            logger.info(f"Creating cache directory: {self.docs_cache_dir}")
            self.docs_cache_dir.mkdir(exist_ok=True)
        else:
            logger.debug(f"Cache directory already exists")

        # Initialize basic documentation
        logger.info("Scheduling basic documentation initialization...")
        asyncio.create_task(self._initialize_basic_docs())

        # Register handlers
        logger.info("Setting up request handlers...")
        self._setup_handlers()
        logger.info("Server initialization complete")

    async def _initialize_basic_docs(self):
        """Initialize basic Cisco command documentation if not exists."""
        logger.info("Checking for basic commands documentation...")

        if not self.basic_commands_path.exists():
            logger.warning(f"Basic commands file not found, creating new one...")
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

            logger.info(f"Writing {len(basic_docs)} basic commands to cache...")
            with open(self.basic_commands_path, 'w') as f:
                json.dump(basic_docs, f, indent=2)
            logger.info(f"Successfully created basic commands file with {len(basic_docs)} entries")
        else:
            logger.info(f"Basic commands file exists, loading...")
            try:
                with open(self.basic_commands_path, 'r') as f:
                    docs = json.load(f)
                logger.info(f"Loaded {len(docs)} commands from cache")
                logger.debug(f"Available commands: {', '.join(docs.keys())}")
            except Exception as e:
                logger.error(f"Failed to load basic commands: {e}")

    def _setup_handlers(self):
        """Set up MCP request handlers."""

        logger.debug("Registering list_tools handler...")

        @self.server.list_tools()
        async def handle_list_tools() -> List[Tool]:
            """List available tools."""
            logger.info("Received list_tools request")
            tools = [
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
            logger.info(f"Returning {len(tools)} available tools: {', '.join(t.name for t in tools)}")
            return tools

        logger.debug("Registering call_tool handler...")

        @self.server.call_tool()
        async def handle_call_tool(name: str, arguments: dict) -> List[TextContent]:
            """Handle tool calls."""
            logger.info(f"Received call_tool request: {name}")
            logger.debug(f"Arguments: {json.dumps(arguments, indent=2)}")

            start_time = datetime.now()

            try:
                if name == "search_command":
                    result = await self._search_command(arguments)
                elif name == "get_feature_docs":
                    result = await self._get_feature_docs(arguments)
                elif name == "validate_syntax":
                    result = await self._validate_syntax(arguments)
                elif name == "explain_config_section":
                    result = await self._explain_config_section(arguments)
                else:
                    logger.error(f"Unknown tool requested: {name}")
                    raise ValueError(f"Unknown tool: {name}")

                elapsed = (datetime.now() - start_time).total_seconds()
                logger.info(f"Tool {name} completed in {elapsed:.3f}s")
                return result

            except Exception as e:
                elapsed = (datetime.now() - start_time).total_seconds()
                logger.error(f"Tool {name} failed after {elapsed:.3f}s: {e}", exc_info=True)
                raise

        logger.info(f"Registered 2 handlers: list_tools, call_tool")

    async def _search_command(self, args: dict) -> List[TextContent]:
        """Search for command documentation."""
        command = args.get("command", "").lower().strip()
        ios_version = args.get("ios_version")

        logger.info(f"Searching for command: '{command}'" + (f" (IOS {ios_version})" if ios_version else ""))

        try:
            logger.debug(f"Reading from cache file: {self.basic_commands_path}")
            with open(self.basic_commands_path, 'r') as f:
                docs = json.load(f)

            # Search for exact or partial match
            result = docs.get(command)

            if not result:
                logger.debug(f"No exact match for '{command}', trying partial match...")
                # Try partial match
                matches = [key for key in docs.keys()
                          if command in key or key in command]
                if matches:
                    logger.info(f"Found partial match: '{matches[0]}' for query '{command}'")
                    result = docs[matches[0]]
                    result["matched_command"] = matches[0]
                else:
                    logger.warning(f"No matches found for command: '{command}'")

            if result:
                logger.info(f"Successfully found documentation for command: '{command}'")
                version_note = f"\n\nNote: Documentation requested for IOS version {ios_version}. " \
                              f"The information provided is generally applicable across IOS versions, " \
                              f"but verify specific syntax for your version." if ios_version else ""

                return [TextContent(
                    type="text",
                    text=f"Command: {command}\n\n{json.dumps(result, indent=2)}{version_note}"
                )]
            else:
                logger.info(f"Command '{command}' not found in local cache")
                return [TextContent(
                    type="text",
                    text=f'Command "{command}" not found in local cache. This may be a valid Cisco command, '
                         f'but documentation is not available locally. Consider adding it to the documentation '
                         f'cache or consulting Cisco\'s official documentation.'
                )]

        except Exception as e:
            logger.error(f"Error searching for command '{command}': {e}", exc_info=True)
            return [TextContent(
                type="text",
                text=f"Error searching for command: {str(e)}"
            )]

    async def _get_feature_docs(self, args: dict) -> List[TextContent]:
        """Get feature documentation."""
        feature = args.get("feature", "")
        ios_version = args.get("ios_version")

        logger.info(f"Retrieving feature documentation: '{feature}'" + (f" (IOS {ios_version})" if ios_version else ""))

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

        logger.debug(f"Available features: {', '.join(feature_docs.keys())}")
        feature_key = next((k for k in feature_docs.keys()
                           if k.lower() == feature.lower()), None)

        if feature_key:
            logger.info(f"Found feature documentation: '{feature_key}'")
            version_note = f"\n\nDocumentation context: IOS version {ios_version}" if ios_version else ""
            return [TextContent(
                type="text",
                text=f"Feature: {feature_key}\n\n{json.dumps(feature_docs[feature_key], indent=2)}{version_note}"
            )]
        else:
            logger.warning(f"Feature '{feature}' not found in documentation cache")
            available = ", ".join(feature_docs.keys())
            return [TextContent(
                type="text",
                text=f'Feature "{feature}" documentation not found in cache. Available features: {available}'
            )]

    async def _validate_syntax(self, args: dict) -> List[TextContent]:
        """Validate command syntax."""
        command = args.get("command", "")
        context = args.get("context", "unknown")

        logger.info(f"Validating syntax for command: '{command}' in context: '{context}'")

        validation = {
            "command": command,
            "context": context,
            "is_valid": True,
            "warnings": [],
            "suggestions": []
        }

        # Basic validation rules
        if "  " in command:
            logger.debug("Detected double spaces in command")
            validation["warnings"].append("Command contains double spaces")

        # Check IP address format
        import re
        if re.search(r'\d+\.\d+\.\d+\.\d+', command):
            logger.debug("Command contains IP address pattern")
            if 'ip address' in command and not re.search(r'\d+\.\d+\.\d+\.\d+\s+\d+\.\d+\.\d+\.\d+', command):
                logger.debug("IP address command missing subnet mask")
                validation["warnings"].append("IP address command typically requires both IP and subnet mask")

        warnings_count = len(validation["warnings"])
        logger.info(f"Validation complete: valid={validation['is_valid']}, warnings={warnings_count}")

        return [TextContent(
            type="text",
            text=json.dumps(validation, indent=2)
        )]

    async def _explain_config_section(self, args: dict) -> List[TextContent]:
        """Explain configuration section."""
        config_block = args.get("config_block", "")

        logger.info(f"Explaining configuration section ({len(config_block)} chars)")
        logger.debug(f"Config block preview: {config_block[:100]}..." if len(config_block) > 100 else f"Config block: {config_block}")

        return [TextContent(
            type="text",
            text=f"Configuration block analysis:\n\n{config_block}\n\n"
                 f"This tool provides context about the configuration section. "
                 f"Use search_command for specific command details."
        )]

    async def run(self):
        """Run the MCP server."""
        logger.info("=" * 60)
        logger.info("Starting MCP server with stdio transport...")
        logger.info("=" * 60)
        logger.info("Server is now ready to accept connections")
        logger.info("Waiting for client to connect...")

        try:
            async with stdio_server() as (read_stream, write_stream):
                logger.info("Client connected! Server is now active")
                await self.server.run(
                    read_stream,
                    write_stream,
                    InitializationOptions(
                        server_name="cisco-docs-server",
                        server_version="2.0.0",
                        capabilities=self.server.get_capabilities(
                            notification_options=NotificationOptions(),
                            experimental_capabilities={}
                        )
                    )
                )
        except Exception as e:
            logger.error(f"Server error: {e}", exc_info=True)
            raise
        finally:
            logger.info("Server shutting down...")


async def main():
    """Main entry point."""
    logger.info("Starting Cisco Documentation MCP Server v2 (Verbose Edition)")
    logger.info(f"Debug mode: {'ENABLED' if DEBUG else 'DISABLED'}")
    if log_file:
        logger.info(f"Logging to file: {log_file}")
    else:
        logger.info(f"Logging to stderr")
    logger.info(f"Set MCP_DEBUG=true environment variable for debug logging")
    logger.info("-" * 60)

    try:
        server = CiscoDocsMCPServer()
        await server.run()
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt, shutting down gracefully...")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
