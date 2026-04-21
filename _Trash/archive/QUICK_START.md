# Quick Start Guide

## MCP-Enhanced Cisco Documentation Generator

Generate detailed Cisco switch documentation using your local Ollama LLM with integrated Cisco documentation context.

## Prerequisites

- ✅ Python 3.8+ with virtual environment
- ✅ Ollama running locally
- ✅ Git (optional, for auto-commits)

## Setup (One-Time)

1. **Activate virtual environment:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. **Install dependencies (if not already done):**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Test the system:**
   ```powershell
   # Option 1: Double-click run_tests.bat
   # Option 2: Run manually
   python tests/test_mcp_integration.py
   ```

   You should see: `[SUCCESS] All tests passed!`

## Usage

### Option 1: Automatic Processing (Recommended)

1. **Start the watcher:**
   ```powershell
   python automation/watcher.py
   ```

2. **Drop config files** into the `configs/` folder
   - Files will be processed automatically
   - Documentation appears in `output/` folder

### Option 2: Manual Processing

```powershell
python automation/processor.py configs/your-switch-config.txt
```

## What You'll See

```
✓ Reading configuration file...
✓ Extracting IOS version...
   Detected IOS version: 15.2
✓ Loading prompt template...
✓ Enriching with Cisco documentation from MCP server...
   Found 5 commands and 2 features
   Connected to MCP server
   Fetching docs for command: vlan
   Fetching docs for command: interface
   Fetching docs for feature: VLAN
   Fetching docs for feature: STP
   Added 4 documentation sections to prompt
✓ Sending to LLM for analysis...
✓ Documentation generated: output/your-switch-config.md
```

## Configuration

Edit `config.json` to customize:

```json
{
  "llm": {
    "endpoint": "http://localhost:11434/api/generate",
    "model": "llama3.1:8b",
    "temperature": 0.7
  },
  "mcp": {
    "enabled": true  // Set false to disable MCP enrichment
  },
  "git": {
    "enabled": true,
    "auto_push": false
  }
}
```

## Output Location

- **Input:** `configs/SWITCH-01.txt`
- **Output:** `output/SWITCH-01.md`

## Features

✅ **MCP Integration** - Automatic Cisco documentation lookup
✅ **Local LLM** - Uses your Ollama instance
✅ **Auto-detection** - Finds commands and features automatically
✅ **Git Integration** - Auto-commits documentation changes
✅ **Watch Mode** - Processes files as they're added

## Troubleshooting

### Ollama not running
```
Error: LLM API request failed: ECONNREFUSED
```
**Fix:** Start Ollama: `ollama serve`

### MCP not working
**Fix:** Run tests to diagnose:
```powershell
python tests/test_mcp_integration.py
```

### Import errors
**Fix:** Make sure you're in the venv:
```powershell
.\venv\Scripts\Activate.ps1
```

## Quick Commands

```powershell
# Test MCP integration
python tests/test_mcp_integration.py

# Process single file
python automation/processor.py configs/CONFIG.txt

# Start auto-watcher
python automation/watcher.py

# Check Ollama models
ollama list

# Check config
type config.json
```

## File Structure

```
configs/          <- Put Cisco configs here (.txt files)
output/           <- Generated documentation appears here (.md files)
automation/       <- Processing scripts
mcp_server/       <- Cisco documentation server
tests/            <- Test scripts
config.json       <- Configuration file
```

## Getting Help

- **Detailed guide:** [MCP_INTEGRATION_GUIDE.md](MCP_INTEGRATION_GUIDE.md)
- **Integration info:** [INTEGRATION_COMPLETE.md](INTEGRATION_COMPLETE.md)
- **Architecture:** [ARCHITECTURE.md](ARCHITECTURE.md)

## Example Workflow

1. Export Cisco config: `show running-config`
2. Save as `configs/CORE-SW-01.txt`
3. System auto-processes (if watcher running)
4. Read documentation: `output/CORE-SW-01.md`
5. Documentation auto-committed to Git (if enabled)

---

**Status:** ✅ Ready to use!

**Need help?** Run `python tests/test_mcp_integration.py` to verify setup.
