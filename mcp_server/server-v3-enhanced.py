#!/usr/bin/env python3
"""
Cisco Documentation MCP Server - v3 Enhanced with Multi-File Support

Provides Cisco IOS command and feature documentation from multiple JSON files.
Supports air-gapped operation with locally cached documentation.
"""

import json
import sys
import asyncio
import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    CallToolResult,
)

# Configure logging
DEBUG = os.getenv("MCP_DEBUG", "false").lower() == "true"
log_level = logging.DEBUG if DEBUG else logging.INFO

log_file = os.getenv("MCP_LOG_FILE")
handlers = []

if log_file:
    handlers.append(logging.FileHandler(log_file, mode='a', encoding='utf-8'))
else:
    handlers.append(logging.StreamHandler(sys.stderr))

logging.basicConfig(
    level=log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=handlers
)

logger = logging.getLogger("cisco-docs-mcp-v3")


class EnhancedCiscoDocsMCPServer:
    """Enhanced MCP Server with multi-file documentation support."""

    def __init__(self):
        logger.info("=" * 60)
        logger.info("Initializing Enhanced Cisco Documentation MCP Server v3")
        logger.info("=" * 60)

        self.server = Server("cisco-docs-server-enhanced")
        self.docs_cache_dir = Path(__file__).parent.parent / "docs_cache"

        # Multiple documentation sources
        self.doc_files = {
            "basic_commands": self.docs_cache_dir / "basic_commands.json",
            "enhanced_commands": self.docs_cache_dir / "cisco_ios_commands_enhanced.json",
            "interface_commands": self.docs_cache_dir / "cisco_ios_interface_commands.json",
        }

        # Loaded documentation
        self.commands = {}
        self.features = {}
        self.command_index = {}  # For fast lookups

        logger.info(f"Cache directory: {self.docs_cache_dir}")
        logger.info(f"Documentation files configured: {len(self.doc_files)}")

        # Ensure cache directory exists
        if not self.docs_cache_dir.exists():
            logger.info(f"Creating cache directory: {self.docs_cache_dir}")
            self.docs_cache_dir.mkdir(exist_ok=True)

        # Load all documentation
        logger.info("Loading documentation from cache...")
        asyncio.create_task(self._load_all_documentation())

        # Register handlers
        logger.info("Setting up request handlers...")
        self._setup_handlers()
        logger.info("Server initialization complete")

    async def _load_all_documentation(self):
        """Load documentation from all configured JSON files."""
        logger.info("=" * 60)
        logger.info("Loading Documentation Database")
        logger.info("=" * 60)

        total_commands = 0
        total_features = 0

        for doc_name, doc_path in self.doc_files.items():
            if doc_path.exists():
                logger.info(f"Loading {doc_name} from {doc_path.name}")
                try:
                    with open(doc_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    # Load commands if present
                    if "commands" in data:
                        for cmd_name, cmd_data in data["commands"].items():
                            # Store with source information
                            cmd_data["_source"] = doc_name
                            cmd_data["_source_file"] = doc_path.name
                            self.commands[cmd_name.lower()] = cmd_data

                            # Build index for partial matching
                            self.command_index[cmd_name.lower()] = cmd_name

                        cmd_count = len(data["commands"])
                        total_commands += cmd_count
                        logger.info(f"  Loaded {cmd_count} commands from {doc_name}")

                    # Load features if present
                    if "features" in data:
                        for feature_name, feature_data in data["features"].items():
                            feature_data["_source"] = doc_name
                            self.features[feature_name.upper()] = feature_data

                        feature_count = len(data["features"])
                        total_features += feature_count
                        logger.info(f"  Loaded {feature_count} features from {doc_name}")

                except Exception as e:
                    logger.error(f"  Failed to load {doc_name}: {e}")
            else:
                logger.warning(f"Documentation file not found: {doc_path}")

        logger.info("=" * 60)
        logger.info(f"Documentation loading complete!")
        logger.info(f"Total commands loaded: {total_commands}")
        logger.info(f"Total features loaded: {total_features}")
        logger.info("=" * 60)

        if total_commands > 0:
            logger.debug(f"Available commands: {', '.join(sorted(list(self.commands.keys())[:20]))}...")

    def _setup_handlers(self):
        """Set up MCP request handlers."""

        @self.server.list_tools()
        async def handle_list_tools() -> List[Tool]:
            """List available tools."""
            logger.info("Received list_tools request")
            tools = [
                Tool(
                    name="search_command",
                    description="Search for Cisco IOS command documentation. Returns detailed syntax, parameters, examples, best practices, and security considerations.",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "command": {
                                "type": "string",
                                "description": "The Cisco IOS command to search for (e.g., 'interface', 'ip address', 'switchport mode')"
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
                    description="Get comprehensive documentation for a Cisco feature or technology",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "feature": {
                                "type": "string",
                                "description": "The feature to look up (e.g., 'VLAN', 'OSPF', 'STP', 'EtherChannel')"
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
                    name="list_available_commands",
                    description="List all commands available in the documentation database. Useful for discovering what documentation is available.",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "category": {
                                "type": "string",
                                "description": "Optional: Filter by category (e.g., 'interface', 'security', 'routing')"
                            }
                        }
                    }
                ),
                Tool(
                    name="get_best_practices",
                    description="Get security and configuration best practices for a command or feature",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "topic": {
                                "type": "string",
                                "description": "Command or feature name to get best practices for"
                            }
                        },
                        "required": ["topic"]
                    }
                )
            ]
            logger.info(f"Returning {len(tools)} available tools")
            return tools

        @self.server.call_tool()
        async def handle_call_tool(name: str, arguments: dict) -> List[TextContent]:
            """Handle tool calls."""
            logger.info(f"Received tool call: {name}")
            logger.debug(f"Arguments: {json.dumps(arguments, indent=2)}")

            try:
                if name == "search_command":
                    return await self._search_command(arguments)
                elif name == "get_feature_docs":
                    return await self._get_feature_docs(arguments)
                elif name == "list_available_commands":
                    return await self._list_available_commands(arguments)
                elif name == "get_best_practices":
                    return await self._get_best_practices(arguments)
                else:
                    logger.error(f"Unknown tool: {name}")
                    raise ValueError(f"Unknown tool: {name}")

            except Exception as e:
                logger.error(f"Tool {name} failed: {e}", exc_info=True)
                raise

    async def _search_command(self, args: dict) -> List[TextContent]:
        """Search for command documentation with enhanced matching."""
        command = args.get("command", "").lower().strip()
        ios_version = args.get("ios_version")

        logger.info(f"Searching for command: '{command}'" + (f" (IOS {ios_version})" if ios_version else ""))

        # Direct match
        if command in self.commands:
            cmd_data = self.commands[command]
            logger.info(f"Found exact match: '{command}'")
            return [TextContent(
                type="text",
                text=self._format_command_documentation(command, cmd_data, ios_version)
            )]

        # Partial match
        matches = [key for key in self.commands.keys()
                  if command in key or key in command]

        if matches:
            best_match = matches[0]
            cmd_data = self.commands[best_match]
            logger.info(f"Found partial match: '{best_match}' for query '{command}'")

            response = f"**Note:** No exact match for '{command}'. Showing documentation for '{best_match}'.\n\n"
            response += self._format_command_documentation(best_match, cmd_data, ios_version)

            if len(matches) > 1:
                response += f"\n\n**Other possible matches:** {', '.join(matches[1:6])}"

            return [TextContent(type="text", text=response)]

        # No match found
        logger.warning(f"No documentation found for: '{command}'")

        # Suggest similar commands
        suggestions = [key for key in self.commands.keys()
                      if any(word in key for word in command.split())]

        response = f"**Command '{command}' not found in documentation database.**\n\n"

        if suggestions:
            response += f"**Similar commands available:**\n"
            for suggestion in suggestions[:10]:
                response += f"  - {suggestion}\n"
        else:
            response += f"**Available command categories:**\n"
            response += f"  - Interface commands: interface, switchport, description\n"
            response += f"  - Security commands: aaa, tacacs-server, username\n"
            response += f"  - Use 'list_available_commands' tool to see all {len(self.commands)} commands\n"

        return [TextContent(type="text", text=response)]

    def _format_command_documentation(self, command: str, cmd_data: dict, ios_version: Optional[str] = None) -> str:
        """Format command documentation for LLM consumption."""

        output = [f"# Command: {command}\n"]

        # Source information
        if "_source" in cmd_data:
            output.append(f"*Source: {cmd_data['_source_file']}*\n")

        # Basic info
        output.append(f"## Syntax")
        output.append(f"```\n{cmd_data.get('syntax', 'N/A')}\n```\n")

        output.append(f"## Description")
        output.append(f"{cmd_data.get('description', 'No description available')}\n")

        # Configuration mode
        if "modes" in cmd_data:
            output.append(f"## Configuration Mode")
            output.append(f"{', '.join(cmd_data['modes'])}\n")

        # Prerequisites
        if "prerequisites" in cmd_data:
            output.append(f"## Prerequisites")
            for prereq in cmd_data['prerequisites']:
                output.append(f"  - {prereq}")
            output.append("")

        # Parameters
        if "parameters" in cmd_data and cmd_data["parameters"]:
            output.append(f"## Parameters")
            for param_name, param_info in cmd_data["parameters"].items():
                output.append(f"### {param_name}")
                if isinstance(param_info, dict):
                    for key, value in param_info.items():
                        if key not in ["_source", "_source_file"]:
                            output.append(f"  - **{key}**: {value}")
                else:
                    output.append(f"  {param_info}")
            output.append("")

        # Examples
        if "examples" in cmd_data:
            output.append(f"## Examples")
            for idx, example in enumerate(cmd_data["examples"], 1):
                if isinstance(example, dict):
                    output.append(f"### Example {idx}")
                    output.append(f"```\n{example.get('command', '')}\n```")
                    if "description" in example:
                        output.append(f"{example['description']}")
                    if "context" in example:
                        output.append(f"*Context: {example['context']}*")
                else:
                    output.append(f"  - {example}")
            output.append("")

        # Best practices
        if "best_practices" in cmd_data:
            output.append(f"## Best Practices")
            for practice in cmd_data["best_practices"]:
                output.append(f"  - {practice}")
            output.append("")

        # Security considerations
        if "security_considerations" in cmd_data:
            output.append(f"## Security Considerations")
            for consideration in cmd_data["security_considerations"]:
                output.append(f"  - ⚠️ {consideration}")
            output.append("")

        # Common mistakes
        if "common_mistakes" in cmd_data:
            output.append(f"## Common Mistakes to Avoid")
            for mistake in cmd_data["common_mistakes"]:
                output.append(f"  - ❌ {mistake}")
            output.append("")

        # Related commands
        if "related_commands" in cmd_data:
            output.append(f"## Related Commands")
            output.append(f"{', '.join(cmd_data['related_commands'])}\n")

        # IOS version note
        if ios_version:
            output.append(f"\n*Documentation provided for IOS version {ios_version} context*")

        return "\n".join(output)

    async def _get_feature_docs(self, args: dict) -> List[TextContent]:
        """Get feature documentation."""
        feature = args.get("feature", "").upper().strip()
        ios_version = args.get("ios_version")

        logger.info(f"Retrieving feature documentation: '{feature}'")

        if feature in self.features:
            feature_data = self.features[feature]
            logger.info(f"Found feature: '{feature}'")

            output = [f"# Feature: {feature}\n"]
            output.append(f"## Description")
            output.append(f"{feature_data.get('description', 'No description available')}\n")

            if "key_concepts" in feature_data:
                output.append(f"## Key Concepts")
                for concept in feature_data["key_concepts"]:
                    output.append(f"  - {concept}")
                output.append("")

            if "common_commands" in feature_data:
                output.append(f"## Common Commands")
                for cmd in feature_data["common_commands"]:
                    output.append(f"  - `{cmd}`")
                output.append("")

            if "best_practices" in feature_data:
                output.append(f"## Best Practices")
                for practice in feature_data["best_practices"]:
                    output.append(f"  - ✓ {practice}")
                output.append("")

            if ios_version:
                output.append(f"\n*Feature documentation for IOS version {ios_version}*")

            return [TextContent(type="text", text="\n".join(output))]
        else:
            available = ", ".join(self.features.keys())
            return [TextContent(
                type="text",
                text=f"Feature '{feature}' not found.\n\nAvailable features: {available}"
            )]

    async def _list_available_commands(self, args: dict) -> List[TextContent]:
        """List all available commands in the database."""
        category = args.get("category", "").lower()

        logger.info(f"Listing available commands" + (f" for category: {category}" if category else ""))

        if not self.commands:
            return [TextContent(
                type="text",
                text="No commands loaded in documentation database."
            )]

        output = [f"# Available Commands ({len(self.commands)} total)\n"]

        # Group commands by source if no category specified
        if not category:
            commands_by_source = {}
            for cmd_name, cmd_data in self.commands.items():
                source = cmd_data.get("_source", "unknown")
                if source not in commands_by_source:
                    commands_by_source[source] = []
                commands_by_source[source].append(cmd_name)

            for source, commands in sorted(commands_by_source.items()):
                output.append(f"## {source} ({len(commands)} commands)")
                output.append(", ".join(sorted(commands)))
                output.append("")
        else:
            # Filter by category (simple keyword matching)
            matching = [cmd for cmd in self.commands.keys() if category in cmd]
            if matching:
                output.append(f"## Commands matching '{category}' ({len(matching)})")
                output.append(", ".join(sorted(matching)))
            else:
                output.append(f"No commands found matching category '{category}'")

        return [TextContent(type="text", text="\n".join(output))]

    async def _get_best_practices(self, args: dict) -> List[TextContent]:
        """Get best practices for a command or feature."""
        topic = args.get("topic", "").lower().strip()

        logger.info(f"Retrieving best practices for: '{topic}'")

        # Check commands first
        if topic in self.commands:
            cmd_data = self.commands[topic]
            output = [f"# Best Practices: {topic}\n"]

            if "best_practices" in cmd_data:
                output.append("## Configuration Best Practices")
                for practice in cmd_data["best_practices"]:
                    output.append(f"  ✓ {practice}")
                output.append("")

            if "security_considerations" in cmd_data:
                output.append("## Security Considerations")
                for consideration in cmd_data["security_considerations"]:
                    output.append(f"  ⚠️ {consideration}")
                output.append("")

            if "common_mistakes" in cmd_data:
                output.append("## Common Mistakes to Avoid")
                for mistake in cmd_data["common_mistakes"]:
                    output.append(f"  ❌ {mistake}")

            return [TextContent(type="text", text="\n".join(output))]

        # Check features
        topic_upper = topic.upper()
        if topic_upper in self.features:
            feature_data = self.features[topic_upper]
            output = [f"# Best Practices: {topic_upper}\n"]

            if "best_practices" in feature_data:
                for practice in feature_data["best_practices"]:
                    output.append(f"  ✓ {practice}")

            return [TextContent(type="text", text="\n".join(output))]

        return [TextContent(
            type="text",
            text=f"No best practices documentation found for '{topic}'"
        )]

    async def run(self):
        """Run the MCP server."""
        logger.info("=" * 60)
        logger.info("Starting Enhanced MCP server...")
        logger.info("=" * 60)

        try:
            async with stdio_server() as (read_stream, write_stream):
                logger.info("Client connected!")
                await self.server.run(
                    read_stream,
                    write_stream,
                    InitializationOptions(
                        server_name="cisco-docs-server-enhanced",
                        server_version="3.0.0",
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
    logger.info("Starting Cisco Documentation MCP Server v3 (Enhanced)")
    logger.info(f"Debug mode: {'ENABLED' if DEBUG else 'DISABLED'}")

    try:
        server = EnhancedCiscoDocsMCPServer()
        await server.run()
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt, shutting down...")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
