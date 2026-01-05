# Cisco Documentation MCP Server v2 (Verbose Edition)

## Overview

The Cisco Documentation MCP Server v2 is an enhanced version of the original MCP server that provides comprehensive logging and visibility into server operations. This server exposes Cisco IOS command and feature documentation to LLMs via the Model Context Protocol (MCP).

## What's New in v2

- **Comprehensive Logging**: All server operations are logged to stderr for visibility
- **Debug Mode**: Optional verbose debugging with the `MCP_DEBUG` environment variable
- **Execution Timing**: Performance metrics for each tool call
- **Detailed Request Tracking**: See every incoming request and its parameters
- **Cache Operations Visibility**: Know when documentation is loaded or created
- **Error Tracking**: Full exception details with stack traces

## Features

### Available Tools

The server provides four main tools for Cisco IOS documentation:

1. **search_command** - Search for Cisco IOS command documentation
2. **get_feature_docs** - Get documentation for Cisco features (VLAN, OSPF, STP, etc.)
3. **validate_syntax** - Validate Cisco IOS command syntax
4. **explain_config_section** - Get explanations for configuration blocks

### Built-in Documentation

The server includes documentation for:

**Commands:**
- interface, ip address, switchport, vlan, spanning-tree
- router, access-list, line, enable secret, hostname
- trunk, channel-group

**Features:**
- VLAN (Virtual Local Area Networks)
- OSPF (Open Shortest Path First)
- STP (Spanning Tree Protocol)
- EtherChannel (Link Aggregation)
- VTP (VLAN Trunking Protocol)

## Installation

### Prerequisites

```bash
pip install mcp
```

### File Structure

```
mcp_server/
├── server-v2.py          # Enhanced verbose server
├── server.py             # Original silent server
└── SERVER-V2-README.md   # This file

docs_cache/
└── basic_commands.json   # Auto-generated documentation cache
```

## Usage

### Starting the Server

#### Normal Mode (INFO level logging)

```bash
python mcp_server/server-v2.py
```

#### Debug Mode (DEBUG level logging)

```bash
# Windows
set MCP_DEBUG=true
python mcp_server/server-v2.py

# Linux/Mac
MCP_DEBUG=true python mcp_server/server-v2.py
```

### Using with MCP Clients

#### Standalone Usage (Claude Desktop, etc.)

Add to your MCP client configuration (e.g., Claude Desktop):

```json
{
  "mcpServers": {
    "cisco-docs": {
      "command": "python",
      "args": ["c:/Git-lokalt/Hovedprosjekt/mcp_server/server-v2.py"]
    }
  }
}
```

For debug mode:

```json
{
  "mcpServers": {
    "cisco-docs": {
      "command": "python",
      "args": ["c:/Git-lokalt/Hovedprosjekt/mcp_server/server-v2.py"],
      "env": {
        "MCP_DEBUG": "true"
      }
    }
  }
}
```

#### Integrated Usage (via config.json)

This project includes a config.json that controls the MCP server integration. To enable debug mode, edit `config.json`:

```json
{
  "mcp": {
    "server_path": "./mcp_server/server-v2.py",
    "enabled": true,
    "debug": true,  // ← Set to true to enable verbose logging
    "max_prompt_size": 50000,
    "max_commands": 2,
    "max_features": 1
  }
}
```

**Debug Options:**
- `"debug": false` (default) - INFO level logging, shows key operations
- `"debug": true` - DEBUG level logging, shows detailed request parameters and internal operations

When debug mode is enabled in config.json, the MCP client automatically passes the `MCP_DEBUG=true` environment variable to the server.

## How It Works

### Architecture

1. **MCP Protocol Communication**
   - Uses stdio (stdin/stdout) for MCP protocol communication
   - All logging goes to stderr to avoid protocol interference

2. **Documentation Cache**
   - First run creates `docs_cache/basic_commands.json`
   - Subsequent runs load from cache
   - Cache can be manually edited to add custom documentation

3. **Request Handling**
   - Client sends tool requests via MCP protocol
   - Server logs the request details
   - Tool executes and returns results
   - Execution time is tracked and logged

### Logging Levels

**INFO Level (Default):**
- Server startup and shutdown
- Tool requests received
- Search results and matches
- Cache operations
- Warnings and errors

**DEBUG Level (MCP_DEBUG=true):**
- All INFO level logs
- Detailed request arguments
- Cache file paths
- Available commands/features
- Search algorithm details
- Configuration block previews

### Tool Operations

#### search_command

Searches for Cisco IOS command documentation:

```python
# Example request
{
  "command": "interface",
  "ios_version": "15.2"  # Optional
}
```

**Logging output:**
```
INFO - Searching for command: 'interface'
INFO - Successfully found documentation for command: 'interface'
```

#### get_feature_docs

Retrieves feature documentation:

```python
# Example request
{
  "feature": "VLAN",
  "ios_version": "15.2"  # Optional
}
```

**Logging output:**
```
INFO - Retrieving feature documentation: 'VLAN'
DEBUG - Available features: VLAN, OSPF, STP, EtherChannel, VTP
INFO - Found feature documentation: 'VLAN'
```

#### validate_syntax

Validates command syntax:

```python
# Example request
{
  "command": "ip address 192.168.1.1",
  "context": "interface"  # Optional
}
```

**Logging output:**
```
INFO - Validating syntax for command: 'ip address 192.168.1.1' in context: 'interface'
DEBUG - IP address command missing subnet mask
INFO - Validation complete: valid=True, warnings=1
```

#### explain_config_section

Explains configuration blocks:

```python
# Example request
{
  "config_block": "interface GigabitEthernet0/1\n switchport mode access\n switchport access vlan 10"
}
```

**Logging output:**
```
INFO - Explaining configuration section (87 chars)
DEBUG - Config block preview: interface GigabitEthernet0/1...
```

## Example Output

### Startup Sequence

```
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Starting Cisco Documentation MCP Server v2 (Verbose Edition)
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Debug mode: DISABLED
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Set MCP_DEBUG=true environment variable for debug logging
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - ------------------------------------------------------------
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - ============================================================
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Initializing Cisco Documentation MCP Server v2
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - ============================================================
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Server name: cisco-docs-server
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Cache directory: c:\Git-lokalt\Hovedprosjekt\docs_cache
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Basic commands file: c:\Git-lokalt\Hovedprosjekt\docs_cache\basic_commands.json
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Cache directory already exists
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Scheduling basic documentation initialization...
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Setting up request handlers...
2025-12-03 14:23:45 - cisco-docs-mcp - DEBUG - Registering list_tools handler...
2025-12-03 14:23:45 - cisco-docs-mcp - DEBUG - Registering call_tool handler...
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Registered 2 handlers: list_tools, call_tool
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Server initialization complete
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - ============================================================
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Starting MCP server with stdio transport...
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - ============================================================
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Server is now ready to accept connections
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Waiting for client to connect...
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Checking for basic commands documentation...
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Basic commands file exists, loading...
2025-12-03 14:23:45 - cisco-docs-mcp - INFO - Loaded 12 commands from cache
```

### Tool Request

```
2025-12-03 14:24:12 - cisco-docs-mcp - INFO - Client connected! Server is now active
2025-12-03 14:24:15 - cisco-docs-mcp - INFO - Received list_tools request
2025-12-03 14:24:15 - cisco-docs-mcp - INFO - Returning 4 available tools: search_command, get_feature_docs, validate_syntax, explain_config_section
2025-12-03 14:24:20 - cisco-docs-mcp - INFO - Received call_tool request: search_command
2025-12-03 14:24:20 - cisco-docs-mcp - DEBUG - Arguments: {
  "command": "vlan"
}
2025-12-03 14:24:20 - cisco-docs-mcp - INFO - Searching for command: 'vlan'
2025-12-03 14:24:20 - cisco-docs-mcp - DEBUG - Reading from cache file: c:\Git-lokalt\Hovedprosjekt\docs_cache\basic_commands.json
2025-12-03 14:24:20 - cisco-docs-mcp - INFO - Successfully found documentation for command: 'vlan'
2025-12-03 14:24:20 - cisco-docs-mcp - INFO - Tool search_command completed in 0.023s
```

## Troubleshooting

### Server Not Starting

**Issue:** Server exits immediately
- **Solution:** Check that MCP dependencies are installed: `pip install mcp`

### No Log Output

**Issue:** Terminal shows no output
- **Solution:** Ensure you're looking at stderr. Some terminals separate stdout/stderr

### Cache Not Created

**Issue:** basic_commands.json not appearing
- **Solution:** Check write permissions in the parent directory

### Debug Logs Not Showing

**Issue:** Still seeing only INFO logs with MCP_DEBUG=true
- **Solution:** Verify environment variable is set:
  ```bash
  # Windows
  echo %MCP_DEBUG%

  # Linux/Mac
  echo $MCP_DEBUG
  ```

## Extending the Server

### Adding New Commands

Edit `docs_cache/basic_commands.json`:

```json
{
  "new-command": {
    "description": "Command description",
    "syntax": "new-command <parameters>",
    "examples": ["new-command example"],
    "parameters": {
      "param1": "Parameter description"
    }
  }
}
```

### Adding New Features

Edit the `feature_docs` dictionary in `_get_feature_docs()` method:

```python
feature_docs = {
    "NEW_FEATURE": {
        "description": "Feature description",
        "key_concepts": ["Concept 1", "Concept 2"],
        "common_commands": ["command 1", "command 2"],
        "best_practices": ["Practice 1", "Practice 2"]
    }
}
```

### Custom Logging

Add additional log statements:

```python
logger.info("Your info message")
logger.debug("Your debug message")
logger.warning("Your warning message")
logger.error("Your error message", exc_info=True)
```

## Performance Considerations

- **Cache Loading**: Documentation loaded once at startup
- **Tool Execution**: Typically completes in < 50ms
- **Memory Usage**: Minimal (~10MB with full cache)
- **Logging Overhead**: Negligible for INFO level, slightly higher for DEBUG

## Security Notes

- Server only reads local documentation files
- No network connections made
- No external API calls
- Documentation cache is read-only during operation
- All tool inputs are logged (be careful with sensitive data in DEBUG mode)

## Version Information

- **Version**: 2.0.0
- **Based on**: server.py (1.0.0)
- **MCP Version**: Compatible with MCP SDK
- **Python**: 3.7+

## Differences from v1

| Feature | v1 (server.py) | v2 (server-v2.py) |
|---------|----------------|-------------------|
| Logging | None | Comprehensive to stderr |
| Debug Mode | No | Yes (MCP_DEBUG) |
| Performance Metrics | No | Yes (execution timing) |
| Request Visibility | No | Yes (all requests logged) |
| Error Details | Basic | Full stack traces |
| Startup Info | Silent | Detailed banner |

## Support

For issues or questions:
1. Check the logs in DEBUG mode
2. Verify MCP client configuration
3. Ensure documentation cache is properly created
4. Review this README for common solutions

## License

Same as parent project.
