#!/usr/bin/env python3
"""
MCP Client for Cisco Documentation Server

Provides interface to communicate with the MCP server and retrieve
Cisco IOS documentation for commands and features.
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Optional, Dict, Any, List
from contextlib import asynccontextmanager

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class CiscoMCPClient:
    """Client for interacting with the Cisco Documentation MCP Server."""

    def __init__(self, server_path: Path, debug: bool = False):
        """
        Initialize the MCP client.

        Args:
            server_path: Path to the MCP server script (server.py)
            debug: Enable debug logging on the MCP server
        """
        self.server_path = Path(server_path)
        self.debug = debug
        self.session: Optional[ClientSession] = None
        self._read_stream = None
        self._write_stream = None

    @asynccontextmanager
    async def connect(self):
        """Connect to the MCP server."""
        import os

        # Build environment variables for the server
        # Always copy environment, then add MCP_DEBUG if needed
        env = os.environ.copy()
        if self.debug:
            env["MCP_DEBUG"] = "true"
            # Optional: Set log file path for server output
            log_dir = Path(__file__).parent.parent / "logs"
            log_dir.mkdir(exist_ok=True)
            env["MCP_LOG_FILE"] = str(log_dir / "mcp_server.log")

        server_params = StdioServerParameters(
            command=sys.executable,  # Use the current Python interpreter
            args=[str(self.server_path)],
            env=env
        )

        async with stdio_client(server_params) as (read_stream, write_stream):
            self._read_stream = read_stream
            self._write_stream = write_stream

            async with ClientSession(read_stream, write_stream) as session:
                self.session = session

                # Initialize the session
                await session.initialize()

                yield self

    async def search_command(self, command: str, ios_version: Optional[str] = None) -> Dict[str, Any]:
        """
        Search for Cisco IOS command documentation.

        Args:
            command: The command to search for (e.g., 'interface', 'vlan')
            ios_version: Optional IOS version

        Returns:
            Dictionary containing command documentation
        """
        if not self.session:
            raise RuntimeError("Client not connected. Use 'async with client.connect()' first.")

        try:
            result = await self.session.call_tool(
                name="search_command",
                arguments={
                    "command": command,
                    **({"ios_version": ios_version} if ios_version else {})
                }
            )

            # Extract text content from result
            if result.content and len(result.content) > 0:
                return {"success": True, "data": result.content[0].text}
            else:
                return {"success": False, "error": "No content returned"}

        except Exception as e:
            return {"success": False, "error": str(e)}

    async def get_feature_docs(self, feature: str, ios_version: Optional[str] = None) -> Dict[str, Any]:
        """
        Get documentation for a Cisco feature.

        Args:
            feature: The feature to look up (e.g., 'VLAN', 'OSPF', 'STP')
            ios_version: Optional IOS version

        Returns:
            Dictionary containing feature documentation
        """
        if not self.session:
            raise RuntimeError("Client not connected. Use 'async with client.connect()' first.")

        try:
            result = await self.session.call_tool(
                name="get_feature_docs",
                arguments={
                    "feature": feature,
                    **({"ios_version": ios_version} if ios_version else {})
                }
            )

            if result.content and len(result.content) > 0:
                return {"success": True, "data": result.content[0].text}
            else:
                return {"success": False, "error": "No content returned"}

        except Exception as e:
            return {"success": False, "error": str(e)}

    async def validate_syntax(self, command: str, context: Optional[str] = None) -> Dict[str, Any]:
        """
        Validate Cisco IOS command syntax.

        Args:
            command: The command to validate
            context: Configuration context (e.g., 'global', 'interface')

        Returns:
            Dictionary containing validation results
        """
        if not self.session:
            raise RuntimeError("Client not connected. Use 'async with client.connect()' first.")

        try:
            result = await self.session.call_tool(
                name="validate_syntax",
                arguments={
                    "command": command,
                    **({"context": context} if context else {})
                }
            )

            if result.content and len(result.content) > 0:
                return {"success": True, "data": result.content[0].text}
            else:
                return {"success": False, "error": "No content returned"}

        except Exception as e:
            return {"success": False, "error": str(e)}

    async def explain_config_section(self, config_block: str) -> Dict[str, Any]:
        """
        Get explanation for a configuration section.

        Args:
            config_block: The configuration block to explain

        Returns:
            Dictionary containing explanation
        """
        if not self.session:
            raise RuntimeError("Client not connected. Use 'async with client.connect()' first.")

        try:
            result = await self.session.call_tool(
                name="explain_config_section",
                arguments={"config_block": config_block}
            )

            if result.content and len(result.content) > 0:
                return {"success": True, "data": result.content[0].text}
            else:
                return {"success": False, "error": "No content returned"}

        except Exception as e:
            return {"success": False, "error": str(e)}

    async def list_tools(self) -> List[Dict[str, Any]]:
        """
        List available tools from the MCP server.

        Returns:
            List of available tools
        """
        if not self.session:
            raise RuntimeError("Client not connected. Use 'async with client.connect()' first.")

        try:
            result = await self.session.list_tools()
            return [{"name": tool.name, "description": tool.description} for tool in result.tools]
        except Exception as e:
            return [{"error": str(e)}]


# Convenience functions for synchronous usage
def run_async(coro):
    """Run an async coroutine synchronously."""
    return asyncio.run(coro)


async def quick_search_command(server_path: Path, command: str, ios_version: Optional[str] = None) -> Dict[str, Any]:
    """
    Quick helper to search for a command without managing client lifecycle.

    Args:
        server_path: Path to MCP server script
        command: Command to search for
        ios_version: Optional IOS version

    Returns:
        Command documentation
    """
    client = CiscoMCPClient(server_path)
    async with client.connect():
        return await client.search_command(command, ios_version)


async def quick_get_feature_docs(server_path: Path, feature: str, ios_version: Optional[str] = None) -> Dict[str, Any]:
    """
    Quick helper to get feature docs without managing client lifecycle.

    Args:
        server_path: Path to MCP server script
        feature: Feature to look up
        ios_version: Optional IOS version

    Returns:
        Feature documentation
    """
    client = CiscoMCPClient(server_path)
    async with client.connect():
        return await client.get_feature_docs(feature, ios_version)


if __name__ == "__main__":
    # Test the client
    import sys

    async def test():
        server_path = Path(__file__).parent.parent / "mcp_server" / "server.py"

        print("Testing MCP Client...")
        print(f"Server path: {server_path}")
        print()

        client = CiscoMCPClient(server_path)

        async with client.connect():
            print("Connected to MCP server!")
            print()

            # List available tools
            print("Available tools:")
            tools = await client.list_tools()
            for tool in tools:
                print(f"  - {tool.get('name')}: {tool.get('description')}")
            print()

            # Test search_command
            print("Testing search_command('vlan')...")
            result = await client.search_command("vlan")
            if result["success"]:
                print(f"Result: {result['data'][:200]}...")
            else:
                print(f"Error: {result['error']}")
            print()

            # Test get_feature_docs
            print("Testing get_feature_docs('VLAN')...")
            result = await client.get_feature_docs("VLAN")
            if result["success"]:
                print(f"Result: {result['data'][:200]}...")
            else:
                print(f"Error: {result['error']}")

    asyncio.run(test())
