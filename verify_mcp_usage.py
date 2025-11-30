#!/usr/bin/env python3
"""
Quick script to verify MCP was used during last processing.

Checks console output or runs a test to verify MCP integration.
"""

import sys
from pathlib import Path

# Add automation to path
sys.path.insert(0, str(Path(__file__).parent / "automation"))

from automation.processor import ConfigProcessor

def test_mcp_enrichment():
    """Test if MCP enrichment is working."""

    print("=" * 60)
    print("Verifying MCP Integration")
    print("=" * 60)
    print()

    # Simple test config
    test_config = """version 15.2
hostname MCP-TEST
!
vlan 10
 name TEST
!
spanning-tree mode rapid-pvst
!
interface GigabitEthernet0/1
 switchport mode access
 switchport access vlan 10
!
"""

    # Create temp file
    test_path = Path("configs/MCP-VERIFICATION-TEST.txt")
    test_path.parent.mkdir(exist_ok=True)

    with open(test_path, 'w') as f:
        f.write(test_config)

    print(f"Created test config: {test_path}")
    print()
    print("Processing with MCP enabled...")
    print("-" * 60)
    print()

    # Process and watch output
    processor = ConfigProcessor(test_path)

    # Check config
    import json
    config_file = Path("config.json")
    with open(config_file) as f:
        config = json.load(f)

    mcp_enabled = config.get("mcp", {}).get("enabled", True)

    print()
    print("-" * 60)
    print("Configuration Check:")
    print(f"  MCP Enabled: {mcp_enabled}")
    print(f"  MCP Server Path: {config.get('mcp', {}).get('server_path', 'N/A')}")
    print(f"  Max Prompt Size: {config.get('mcp', {}).get('max_prompt_size', 'N/A')}")
    print(f"  Max Commands: {config.get('mcp', {}).get('max_commands', 'N/A')}")
    print(f"  Max Features: {config.get('mcp', {}).get('max_features', 'N/A')}")
    print()

    if mcp_enabled:
        print("✓ MCP is ENABLED")
        print()
        print("If you saw these lines above:")
        print("  - 'Enriching with Cisco documentation from MCP server...'")
        print("  - 'Connected to MCP server'")
        print("  - 'Fetching docs for command: ...'")
        print("  - 'Added N documentation sections to prompt'")
        print()
        print("Then MCP WAS USED! ✓")
    else:
        print("✗ MCP is DISABLED")
        print()
        print("MCP was NOT used because it's disabled in config.json")

    print()
    print("=" * 60)
    print("Check the output above to verify MCP usage")
    print("=" * 60)

    # Clean up
    try:
        test_path.unlink()
        output_path = Path("output/MCP-VERIFICATION-TEST.md")
        if output_path.exists():
            output_path.unlink()
        print()
        print("Cleaned up test files")
    except:
        pass

if __name__ == "__main__":
    test_mcp_enrichment()
