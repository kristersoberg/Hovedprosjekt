# Quick Start Guide

Get your Cisco Configuration Documentation System running in 5 minutes!

## Step 1: Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt

# Or use the setup script
python setup.py
```

## Step 2: Start Your Local LLM

Choose one option:

### Option A: Using Ollama (Recommended)

```bash
# Install Ollama from https://ollama.ai

# Pull a recommended model
ollama pull llama3.1:8b

# Ollama runs automatically on http://localhost:11434
```

### Option B: Using LM Studio

1. Download LM Studio from https://lmstudio.ai
2. Download a model (e.g., Llama 3.1 8B)
3. Start the local server on port 1234

### Option C: Using Text Generation WebUI

1. Install from https://github.com/oobabooga/text-generation-webui
2. Load your model
3. Enable the API in settings
4. Start the server

## Step 3: Configure the System

Edit [config.json](config.json) to match your LLM:

**For Ollama:**
```json
{
  "llm": {
    "endpoint": "http://localhost:11434/v1/chat/completions",
    "model": "llama3.1:8b",
    "api_key": ""
  }
}
```

**For LM Studio:**
```json
{
  "llm": {
    "endpoint": "http://localhost:1234/v1/chat/completions",
    "model": "llama-3.1-8b-instruct",
    "api_key": ""
  }
}
```

## Step 4: Test the System

### Create a Test Configuration

Create a file `configs/test-switch.txt` with a sample Cisco configuration, or use your own.

### Start the Watcher

```bash
python automation/watcher.py
```

You should see:
```
🔍 Starting Cisco Config Watcher...
📁 Monitoring directory: G:\Fagskolen Hovedfagsprosjekt Lokal\configs
───────────────────────────────────────
✅ Watcher ready and monitoring for changes
```

### Add a Configuration File

Either:
1. Copy a Cisco `show running-config` output to `configs/your-switch.txt`, or
2. Create a new `.txt` file in the `configs/` folder

The system will automatically:
1. Detect the new file
2. Extract the IOS version
3. Send to LLM for analysis
4. Generate documentation in `output/`
5. Commit to Git (if enabled)

## Step 5: View the Results

Check the `output/` folder for your generated markdown documentation!

## Troubleshooting

### "LLM API request failed"
- ✅ Check if your LLM server is running
- ✅ Verify the endpoint URL in `config.json`
- ✅ Test manually: `curl http://localhost:11434/api/version` (for Ollama)

### "Module not found"
- ✅ Ensure you installed dependencies: `pip install -r requirements.txt`
- ✅ Verify Python version: `python --version` (should be 3.8+)
- ✅ Consider using a virtual environment

### "Git commit failed"
- ✅ Initialize Git: `git init`
- ✅ Configure Git user:
  ```bash
  git config user.name "Your Name"
  git config user.email "your@email.com"
  ```
- ✅ Or disable Git in `config.json`: `"git.enabled": false`

### Processing is slow
- ✅ Use a smaller model (e.g., 7B instead of 70B)
- ✅ Reduce `max_tokens` in `config.json`
- ✅ Ensure your computer has enough RAM for the model

## Next Steps

1. **Customize the prompt**: Edit [automation/prompts/analysis_template.txt](automation/prompts/analysis_template.txt)
2. **Add more Cisco docs**: Edit `docs_cache/basic_commands.json`
3. **Configure MCP in your LLM**: See [README.md](README.md) for LLM-specific instructions
4. **Set up Git remote**: Push documentation to a repository
5. **Process multiple configs**: Add all your switch configs to `configs/`

## Testing MCP Server Manually

To test the MCP server independently:

```bash
python mcp_server/server.py
```

Then in another terminal, send a test request (if your LLM supports it).

## Common Use Cases

### Daily Network Documentation
Run the watcher continuously to auto-document config changes:
```bash
python automation/watcher.py
# Leave running in background
```

### One-Time Batch Processing
Process existing configs manually:
```bash
python automation/processor.py configs/switch1.txt
python automation/processor.py configs/switch2.txt
python automation/processor.py configs/switch3.txt
```

### Scheduled Documentation
Set up a cron job or scheduled task to run the processor periodically.

**Linux/Mac (cron):**
```bash
# Add to crontab:
0 2 * * * cd /path/to/project && /usr/bin/python3 automation/processor.py configs/*.txt
```

**Windows (Task Scheduler):**
- Create a task that runs `python automation/watcher.py` on startup

---

## Virtual Environment (Recommended)

For better dependency management, use a virtual environment:

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

# Run the system
python automation/watcher.py
```

---

**You're all set! 🎉**

Drop a Cisco configuration file in the `configs/` folder and watch the magic happen.