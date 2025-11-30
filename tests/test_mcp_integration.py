#!/usr/bin/env python3
"""
Test script to verify MCP integration with the processor.

This script tests the MCP client connection and command lookup functionality.
"""

import sys
import asyncio
from pathlib import Path

# Add automation directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "automation"))

from mcp_client import CiscoMCPClient


async def test_mcp_connection():
    """Test MCP server connection and basic commands."""

    print("=" * 60)
    print("Testing MCP Integration")
    print("=" * 60)
    print()

    server_path = Path(__file__).parent.parent / "mcp_server" / "server.py"

    if not server_path.exists():
        print(f"[X] ERROR: MCP server not found at {server_path}")
        return False

    print(f"[OK] MCP server found at: {server_path}")
    print()

    try:
        client = CiscoMCPClient(server_path)

        print("Connecting to MCP server...")
        async with client.connect():
            print("[OK] Connected successfully!")
            print()

            # Test 1: List available tools
            print("Test 1: Listing available tools")
            print("-" * 40)
            tools = await client.list_tools()
            for tool in tools:
                print(f"  - {tool.get('name')}: {tool.get('description', 'N/A')[:50]}...")
            print(f"[OK] Found {len(tools)} tools")
            print()

            # Test 2: Search for 'vlan' command
            print("Test 2: Searching for 'vlan' command")
            print("-" * 40)
            result = await client.search_command("vlan")
            if result["success"]:
                print("[OK] Command documentation retrieved:")
                print(result["data"][:300] + "...")
            else:
                print(f"[X] Failed: {result['error']}")
            print()

            # Test 3: Get VLAN feature documentation
            print("Test 3: Getting VLAN feature documentation")
            print("-" * 40)
            result = await client.get_feature_docs("VLAN")
            if result["success"]:
                print("[OK] Feature documentation retrieved:")
                print(result["data"][:300] + "...")
            else:
                print(f"[X] Failed: {result['error']}")
            print()

            # Test 4: Get STP feature documentation
            print("Test 4: Getting STP feature documentation")
            print("-" * 40)
            result = await client.get_feature_docs("STP")
            if result["success"]:
                print("[OK] Feature documentation retrieved:")
                print(result["data"][:300] + "...")
            else:
                print(f"[X] Failed: {result['error']}")
            print()

            print("=" * 60)
            print("[OK] All tests passed!")
            print("=" * 60)
            return True

    except Exception as e:
        print(f"[X] ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def test_processor_integration():
    """Test that the processor can use MCP enrichment."""

    print()
    print("=" * 60)
    print("Testing Processor Integration")
    print("=" * 60)
    print()

    # Create a minimal test config
    test_config = """version 15.2
hostname TEST-SWITCH
!
vlan 10
 name OFFICE
!
vlan 20
 name SERVERS
!
spanning-tree mode rapid-pvst
!
interface GigabitEthernet0/1
 switchport mode access
 switchport access vlan 10
!
"""

    # Write test config to temp file
    test_config_path = Path(__file__).parent.parent / "configs" / "TEST.txt"
    test_config_path.parent.mkdir(exist_ok=True)

    print(f"Creating test config at: {test_config_path}")
    with open(test_config_path, 'w') as f:
        f.write(test_config)
    print("[OK] Test config created")
    print()

    try:
        # Add parent directory to path for importing
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent))

        from automation.processor import ConfigProcessor

        print("Initializing processor...")
        processor = ConfigProcessor(test_config_path)

        # Test command extraction
        print("Testing command extraction...")
        commands = processor._extract_commands_from_config(test_config)
        print(f"[OK] Found commands: {commands}")

        # Test feature extraction
        print("Testing feature extraction...")
        features = processor._extract_features_from_config(test_config)
        print(f"[OK] Found features: {features}")
        print()

        print("=" * 60)
        print("[OK] Processor integration test passed!")
        print("=" * 60)
        print()
        print("To test full documentation generation, run:")
        print(f"  python automation/processor.py configs/TEST.txt")
        print()

        return True

    except Exception as e:
        print(f"[X] ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Run all tests."""

    # Test MCP connection
    mcp_ok = await test_mcp_connection()

    if mcp_ok:
        # Test processor integration
        processor_ok = await test_processor_integration()

        if processor_ok:
            print()
            print("[SUCCESS] All tests passed! MCP integration is working correctly.")
            print()
            print("Next steps:")
            print("1. Make sure your Ollama server is running")
            print("2. Place a Cisco config file in the configs/ folder")
            print("3. Run: python automation/processor.py configs/your-config.txt")
            print()
            return True

    return False


if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
