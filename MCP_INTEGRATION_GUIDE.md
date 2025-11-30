# MCP Integration Guide

## Overview

The Cisco Configuration Documentation System now directly integrates with the MCP (Model Context Protocol) server to enrich documentation with accurate Cisco IOS command and feature documentation.

## How It Works

```
┌─────────────────┐
│  Config File    │
│  (configs/)     │
└────────┬────────┘
         │
         ↓
┌─────────────────────────────────────┐
│  Processor (automation/processor.py) │
│                                      │
│  1. Reads config file               │
│  2. Extracts commands & features    │
│  3. Connects to MCP server ────────┐│
│  4. Fetches Cisco documentation    ││
│  5. Enriches prompt with docs      ││
│  6. Sends enriched prompt to LLM   ││
└─────────────────┬───────────────────┘│
                  │                    │
                  ↓                    ↓
         ┌────────────────┐   ┌──────────────┐
         │  Ollama (LLM)  │   │  MCP Server  │
         │                │   │ (server.py)  │
         │  Generates     │   │              │
         │  Documentation │   │  Provides    │
         └────────┬───────┘   │  Cisco Docs  │
                  │           └──────────────┘
                  ↓
         ┌────────────────┐
         │  Documentation │
         │  (output/)     │
         └────────────────┘
```

## Key Components

### 1. MCP Client (`automation/mcp_client.py`)
- Communicates with the MCP server via stdio
- Provides async methods to query Cisco documentation
- Tools available:
  - `search_command()` - Look up command syntax
  - `get_feature_docs()` - Get feature documentation
  - `validate_syntax()` - Validate command syntax
  - `explain_config_section()` - Explain config blocks

### 2. Enhanced Processor (`automation/processor.py`)
- Automatically extracts commands and features from configs
- Connects to MCP server to fetch relevant documentation
- Enriches the LLM prompt with Cisco documentation context
- Sends enriched prompt to Ollama for better analysis

### 3. MCP Server (`mcp_server/server.py`)
- Provides Cisco IOS documentation via MCP protocol
- Runs as a subprocess when needed
- Contains documentation for common commands and features

## Setup & Installation

### 1. Install Dependencies

Make sure you're in your virtual environment:

```powershell
# Activate venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 2. Verify Installation

Run the test script to verify MCP integration:

```powershell
python tests/test_mcp_integration.py

# Or simply double-click one of these files:
# - run_tests.bat (Windows batch file)
# - run_tests.ps1 (PowerShell script)
```

You should see:
- ✓ MCP server connection successful
- ✓ Command lookups working
- ✓ Feature documentation retrieval working

## Usage

### Automatic Processing (Recommended)

1. **Start the file watcher**:
   ```powershell
   cd automation
   python watcher.py
   ```

2. **Drop a config file** in the `configs/` folder

3. **Watch the magic happen**:
   - Processor detects the file
   - Extracts commands and features
   - Connects to MCP server
   - Fetches Cisco documentation
   - Enriches prompt
   - Sends to Ollama
   - Generates enhanced documentation

### Manual Processing

Process a single config file:

```powershell
python automation/processor.py configs/your-switch-config.txt
```

You'll see output like:
```
✓ Reading configuration file...
✓ Extracting IOS version...
   Detected IOS version: 15.2
✓ Loading prompt template...
✓ Enriching with Cisco documentation from MCP server...
   Found 6 commands and 3 features
   Connected to MCP server
   Fetching docs for command: vlan
   Fetching docs for command: interface
   Fetching docs for feature: VLAN
   Fetching docs for feature: STP
   Added 5 documentation sections to prompt
✓ Sending to LLM for analysis...
✓ Saving documentation...
✓ Documentation generated: output/your-switch-config.md
```

## Configuration

In `config.json`:

```json
{
  "mcp": {
    "server_path": "./mcp_server/server.py",
    "enabled": true
  }
}
```

- **enabled**: Set to `true` to use MCP enrichment, `false` to skip
- **server_path**: Path to the MCP server script (relative to project root)

## How Documentation is Enriched

### Before MCP Integration:
The LLM only sees the raw configuration file.

### After MCP Integration:
The LLM receives:
1. The configuration file
2. **Plus** relevant Cisco documentation for:
   - Commands found in the config (e.g., `vlan`, `interface`, `spanning-tree`)
   - Features detected (e.g., VLAN, STP, OSPF, EtherChannel)
   - Syntax examples
   - Best practices
   - Parameter explanations

This results in **more accurate, detailed, and technically correct documentation**.

## Example Output Enhancement

**Without MCP:**
> "VLAN 10 is configured with name OFFICE"

**With MCP:**
> "VLAN 10 is configured with the name 'OFFICE'. VLANs are Layer 2 broadcast domains that segment network traffic. This VLAN uses the normal range (1-1005). Best practice: Document VLAN assignments and use meaningful names like 'OFFICE' for easier network management."

## Troubleshooting

### MCP Server Connection Failed

**Error**: `Failed to connect to MCP server`

**Solution**:
- Check that `mcp_server/server.py` exists
- Verify Python dependencies are installed: `pip install mcp>=0.9.0`
- Try running the test: `python test_mcp_integration.py`

### No Documentation Retrieved

**Warning**: `No documentation retrieved, using original prompt`

This is normal if the config doesn't contain recognized commands. The processor will continue with the original prompt.

### Import Error for mcp_client

**Error**: `ModuleNotFoundError: No module named 'mcp_client'`

**Solution**:
- Make sure you're running from the project root
- Check that `automation/mcp_client.py` exists
- The processor imports from the same directory

## Disabling MCP Integration

If you want to process configs without MCP enrichment, set in `config.json`:

```json
{
  "mcp": {
    "enabled": false
  }
}
```

The processor will skip MCP enrichment and send configs directly to Ollama.

## Adding More Documentation

To extend the Cisco documentation available via MCP:

1. Edit `docs_cache/basic_commands.json` for command documentation
2. Edit `mcp_server/server.py` to add feature documentation
3. Restart the processor (MCP server auto-restarts each run)

## Benefits of Direct Integration

✅ **No manual configuration** - Works automatically
✅ **Offline operation** - Documentation cached locally
✅ **Accurate context** - LLM gets precise Cisco docs
✅ **Better output** - More detailed and technically correct
✅ **Portable** - No external services needed
✅ **Fast** - Documentation fetched in seconds

## Performance

- MCP connection: ~1-2 seconds
- Documentation fetch per item: ~100-200ms
- Total enrichment time: ~3-5 seconds for typical config
- Negligible impact on overall processing time

---

**Ready to go!** Drop a config file in `configs/` and see the enhanced documentation. 🚀
