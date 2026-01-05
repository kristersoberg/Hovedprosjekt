# Quick Start Guide

Get your Cisco Configuration Documentation System running in 5 minutes!

## Prerequisites

- ✅ Python 3.8+ installed
- ✅ A local LLM (Ollama, LM Studio, or similar)
- ✅ Git (optional, for version control features)

---

## Step 1: Install Dependencies

```bash
# Option 1: Use the automated setup script
python setup.py

# Option 2: Manual installation
pip install -r requirements.txt
```

**Recommended:** Use a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Step 2: Start Your Local LLM

Choose one option:

### Option A: Using Ollama (Recommended)

```bash
# Install Ollama from https://ollama.ai

# Pull a recommended model
ollama pull llama3.1:8b

# Start Ollama (runs automatically on http://localhost:11434)
ollama serve
```

### Option B: Using LM Studio

1. Download LM Studio from https://lmstudio.ai
2. Download a model (e.g., Llama 3.1 8B)
3. Start the local server on port 1234

See [LMSTUDIO_SETUP.md](LMSTUDIO_SETUP.md) for detailed LM Studio configuration.

### Option C: Using Text Generation WebUI

1. Install from https://github.com/oobabooga/text-generation-webui
2. Load your model
3. Enable the API in settings
4. Start the server

---

## Step 3: Configure the System

Edit [config.json](../config.json) to match your LLM setup:

**For Ollama:**
```json
{
  "llm": {
    "endpoint": "http://localhost:11434/v1/chat/completions",
    "model": "llama3.1:8b",
    "api_key": "",
    "temperature": 0.7,
    "max_tokens": 8000
  },
  "mcp": {
    "server_path": "./mcp_server/server-v2.py",
    "enabled": true
  },
  "git": {
    "enabled": true,
    "auto_push": false
  }
}
```

**For LM Studio:**
```json
{
  "llm": {
    "endpoint": "http://localhost:1234/v1/chat/completions",
    "model": "llama-3.1-8b-instruct",
    "api_key": "",
    "temperature": 0.7,
    "max_tokens": 8000
  }
}
```

---

## Step 4: Test the System

### Run the Test Suite

Verify everything is working:

```bash
# Run MCP integration tests
python tests/test_mcp_integration.py

# Or use the test runner
# Windows:
tests\run_tests.bat
# Linux/Mac:
bash tests/run_tests.sh
```

You should see: `[SUCCESS] All tests passed!`

### Create a Test Configuration

Use the sample config or add your own:
- Sample config is already in `configs/` folder
- Or create a file `configs/test-switch.txt` with Cisco `show running-config` output

---

## Step 5: Start Processing

### Option 1: Automatic Processing (Recommended)

Start the file watcher to automatically process new configs:

```bash
python automation/watcher.py
```

You should see:
```
🔍 Starting Cisco Config Watcher...
📁 Monitoring directory: configs/
───────────────────────────────────────
✅ Watcher ready and monitoring for changes
```

Now drop `.txt` files into the `configs/` folder and they'll be processed automatically!

### Option 2: Manual Processing

Process a single file on-demand:

```bash
python automation/processor.py configs/your-switch.txt
```

---

## Step 6: View the Results

Check the `output/` folder for your generated markdown documentation!

**Example:**
- Input: `configs/CORE-SW-01.txt`
- Output: `output/CORE-SW-01.md`

---

## What You'll See During Processing

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
✓ Documentation generated: output/CORE-SW-01.md
✓ Git commit created (if enabled)
```

---

## Features

✅ **MCP Integration** - Automatic Cisco documentation lookup
✅ **Local LLM** - Privacy-first, no cloud services
✅ **Auto-detection** - Finds IOS version, commands, and features automatically
✅ **Git Integration** - Auto-commits documentation changes
✅ **Watch Mode** - Processes files as they're added
✅ **Structured Output** - Clean, readable markdown documentation

---

## Troubleshooting

### "LLM API request failed: ECONNREFUSED"

**Cause:** LLM server is not running

**Fix:**
- ✅ Check if your LLM server is running
- ✅ Verify the endpoint URL in `config.json`
- ✅ Test manually:
  ```bash
  # For Ollama:
  curl http://localhost:11434/api/version

  # For LM Studio:
  curl http://localhost:1234/v1/models
  ```

### "Module not found" or Import Errors

**Cause:** Dependencies not installed or not in virtual environment

**Fix:**
- ✅ Ensure you installed dependencies: `pip install -r requirements.txt`
- ✅ Verify Python version: `python --version` (should be 3.8+)
- ✅ Make sure virtual environment is activated:
  ```bash
  # Windows:
  venv\Scripts\activate
  # Linux/Mac:
  source venv/bin/activate
  ```

### "Git commit failed"

**Cause:** Git not initialized or configured

**Fix:**
- ✅ Initialize Git: `git init`
- ✅ Configure Git user:
  ```bash
  git config user.name "Your Name"
  git config user.email "your@email.com"
  ```
- ✅ Or disable Git in `config.json`: `"git.enabled": false`

### MCP Server Not Working

**Cause:** MCP server not starting or LLM not connecting to it

**Fix:**
- ✅ Run tests to diagnose: `python tests/test_mcp_integration.py`
- ✅ Check `logs/mcp_server.log` for errors
- ✅ Verify `config.json` has correct MCP server path
- ✅ You can disable MCP temporarily: `"mcp.enabled": false`

### Processing is Very Slow

**Cause:** Model too large or insufficient hardware

**Fix:**
- ✅ Use a smaller model (e.g., 7B instead of 70B)
- ✅ Reduce `max_tokens` in `config.json` (try 4000)
- ✅ Lower temperature for faster processing (try 0.3)
- ✅ Ensure your computer has enough RAM/VRAM for the model

### Poor Documentation Quality

**Cause:** Model not powerful enough or incorrect settings

**Fix:**
- ✅ Use a larger/better model (Llama 3.1 8B minimum recommended)
- ✅ Increase `max_tokens` for more detailed output
- ✅ Lower temperature for more consistent output (0.3-0.5)
- ✅ Ensure MCP server is enabled and working

---

## Common Use Cases

### Daily Network Documentation

Run the watcher continuously to auto-document config changes:
```bash
python automation/watcher.py
# Leave running in background or terminal
```

### One-Time Batch Processing

Process multiple existing configs manually:
```bash
python automation/processor.py configs/switch1.txt
python automation/processor.py configs/switch2.txt
python automation/processor.py configs/switch3.txt
```

### Scheduled Documentation

Set up automated processing:

**Windows (Task Scheduler):**
- Create a task that runs `python automation/watcher.py` on startup

**Linux/Mac (cron):**
```bash
# Add to crontab:
0 2 * * * cd /path/to/project && /usr/bin/python3 automation/watcher.py
```

---

## Next Steps

Once your system is running:

1. **Customize the prompt template**: Edit [automation/prompts/analysis_template.txt](../automation/prompts/analysis_template.txt)
2. **Add more Cisco documentation**: Edit `docs_cache/` JSON files
3. **Configure Git remote**: Push documentation to a repository
4. **Process your network**: Add all your switch configs to `configs/`
5. **Explore MCP features**: See [MCP_INTEGRATION_GUIDE.md](MCP_INTEGRATION_GUIDE.md)

---

## Quick Reference Commands

```bash
# Test the system
python tests/test_mcp_integration.py

# Start automatic watcher
python automation/watcher.py

# Process single file
python automation/processor.py configs/CONFIG.txt

# Check Ollama status
ollama list
curl http://localhost:11434/api/version

# View configuration
cat config.json  # Linux/Mac
type config.json  # Windows
```

---

## File Structure

```
Hovedprosjekt/
├── configs/              # Input: Drop Cisco configs here (.txt files)
├── output/               # Output: Generated documentation (.md files)
├── automation/           # Processing scripts
│   ├── watcher.py       # Automatic file watcher
│   ├── processor.py     # Main processing engine
│   └── mcp_client.py    # MCP client interface
├── mcp_server/          # Cisco documentation server
│   └── server-v2.py     # Active MCP server
├── docs_cache/          # Cached Cisco documentation
├── tests/               # Test scripts
├── logs/                # System logs
└── config.json          # Main configuration file
```

---

## Getting More Help

- **Complete documentation**: [README.md](README.md)
- **System architecture**: [ARCHITECTURE.md](ARCHITECTURE.md)
- **Detailed workflows**: [WORKFLOW.md](WORKFLOW.md)
- **Troubleshooting guide**: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **MCP integration**: [MCP_INTEGRATION_GUIDE.md](MCP_INTEGRATION_GUIDE.md)
- **LM Studio setup**: [LMSTUDIO_SETUP.md](LMSTUDIO_SETUP.md)

---

## Example Workflow

1. Export Cisco configuration: `show running-config`
2. Save as `configs/CORE-SW-01.txt`
3. System auto-processes (if watcher is running)
4. Review generated documentation: `output/CORE-SW-01.md`
5. Documentation is auto-committed to Git (if enabled)
6. Share documentation with your team!

---

**Status:** ✅ You're all set!

**Need help?** Run `python tests/test_mcp_integration.py` to verify your setup.

Drop a Cisco configuration file in the `configs/` folder and watch the magic happen! 🎉
