# Troubleshooting Guide

Common issues and their solutions for the Cisco Configuration Documentation System.

## Installation Issues

### ❌ "npm: command not found"

**Problem**: Node.js is not installed or not in PATH.

**Solution**:
1. Download and install Node.js from https://nodejs.org/ (version 18 or higher)
2. Restart your terminal
3. Verify: `node --version`

---

### ❌ "npm install fails with permission errors"

**Problem**: Permission denied during npm install.

**Solution (Linux/Mac)**:
```bash
# Don't use sudo! Instead, fix npm permissions:
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.profile
source ~/.profile

# Then retry:
npm install
```

**Solution (Windows)**:
- Run terminal as Administrator, or
- Install in a user directory (not Program Files)

---

## LLM Connection Issues

### ❌ "LLM API request failed: ECONNREFUSED"

**Problem**: Cannot connect to the LLM server.

**Diagnosis**:
```bash
# Check if LLM is running
curl http://localhost:11434/api/version  # For Ollama
```

**Solutions**:

**For Ollama**:
```bash
# Start Ollama
ollama serve

# Verify it's running
ollama list
```

**For LM Studio**:
1. Open LM Studio
2. Go to "Local Server" tab
3. Click "Start Server"
4. Note the port number (usually 1234)
5. Update `config.json`:
   ```json
   {
     "llm": {
       "endpoint": "http://localhost:1234/v1/chat/completions"
     }
   }
   ```

**For other LLMs**:
- Ensure the server is running
- Check firewall settings
- Verify the port in `config.json` matches your LLM

---

### ❌ "Error: Unexpected LLM response format"

**Problem**: LLM returned data in an unexpected format.

**Diagnosis**:
Check what your LLM actually returns:
```bash
curl -X POST http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.1:8b",
    "messages": [{"role": "user", "content": "test"}]
  }'
```

**Solution**:
Modify `automation/processor.js` around line 150 to match your LLM's response format:

```javascript
// Add your format here
if (response.data.your_llm_format) {
  content = response.data.your_llm_format.text;
}
```

---

### ❌ "Model 'llama3.1:8b' not found"

**Problem**: The specified model is not downloaded.

**Solution (Ollama)**:
```bash
# List available models
ollama list

# Pull the model
ollama pull llama3.1:8b

# Or use a different model that's already downloaded
# Update config.json with the model name from `ollama list`
```

**Solution (LM Studio)**:
1. Open LM Studio
2. Go to "Search" or "Discover"
3. Download a model (e.g., "llama-3.1-8b-instruct")
4. Update `config.json` with the exact model name shown in LM Studio

---

### ❌ "Request timeout"

**Problem**: LLM is taking too long to respond.

**Solutions**:
1. **Increase timeout** in `config.json`:
   ```json
   {
     "llm": {
       "timeout": 600000  // 10 minutes
     }
   }
   ```

2. **Use a smaller model**:
   ```bash
   ollama pull llama3.1:8b  # Instead of 70B
   ```

3. **Reduce max_tokens**:
   ```json
   {
     "llm": {
       "max_tokens": 4000  // Instead of 8000
     }
   }
   ```

4. **Enable GPU acceleration** (if available):
   - For Ollama: Automatically uses GPU if available
   - For LM Studio: Enable GPU in settings

---

## File Watcher Issues

### ❌ "Watcher not detecting new files"

**Problem**: Adding files to `configs/` doesn't trigger processing.

**Diagnosis**:
1. Is the watcher running?
   ```bash
   cd automation
   npm start
   # You should see: "✅ Watcher ready and monitoring for changes"
   ```

2. Are files in the correct location?
   ```bash
   # Files should be in:
   G:\Fagskolen Hovedfagsprosjekt Lokal\configs\*.txt
   ```

**Solutions**:
- Ensure watcher is running (`cd automation && npm start`)
- Verify file extension is `.txt` (not `.TXT` or `.config`)
- Check file permissions (must be readable)
- Try restarting the watcher

---

### ❌ "File is processed multiple times"

**Problem**: Same config generates multiple documentation files.

**Cause**: File is being modified multiple times (e.g., by auto-save).

**Solution**:
The watcher has debouncing built-in. If this still happens:
1. Copy files instead of editing them in place
2. Increase debounce time in `automation/watcher.js`:
   ```javascript
   awaitWriteFinish: {
     stabilityThreshold: 5000,  // 5 seconds instead of 2
     pollInterval: 100
   }
   ```

---

## Processing Issues

### ❌ "Error loading config.json"

**Problem**: `config.json` not found or invalid.

**Solutions**:
1. **Check file exists**:
   ```bash
   ls config.json
   ```

2. **Validate JSON syntax**:
   - Use a JSON validator: https://jsonlint.com/
   - Check for missing commas, quotes, brackets

3. **Reset to default**:
   ```bash
   # Backup your config
   cp config.json config.json.backup

   # Copy from template (create one if needed)
   ```

---

### ❌ "IOS version not detected"

**Problem**: Shows "IOS Version: Unknown" in output.

**Cause**: Version string format not recognized.

**Solution**:
Check your config file has a version line like:
```
version 15.2
```
or
```
Cisco IOS Software, Version 15.2(4)E7
```

If it's in a different format, modify `automation/processor.js`:
```javascript
extractIOSVersion(configContent) {
  const patterns = [
    /Cisco IOS Software.*Version ([0-9.()A-Z]+)/i,
    /IOS.*Version ([0-9.]+)/i,
    /version ([0-9.]+)/i,
    // Add your pattern here:
    /your-custom-pattern/i
  ];
  // ...
}
```

---

### ❌ "Documentation quality is poor"

**Problem**: Generated documentation is incomplete or inaccurate.

**Solutions**:

1. **Use a better model**:
   - Llama 3.1 70B instead of 8B
   - Mixtral 8x7B
   - Models specifically fine-tuned for technical text

2. **Adjust temperature** (in `config.json`):
   ```json
   {
     "llm": {
       "temperature": 0.3  // Lower = more consistent, less creative
     }
   }
   ```

3. **Improve the prompt** (`automation/prompts/analysis_template.txt`):
   - Add more specific instructions
   - Provide examples of good documentation
   - Break down into smaller sections

4. **Increase context**:
   ```json
   {
     "llm": {
       "max_tokens": 12000  // Allow longer responses
     }
   }
   ```

5. **Enable MCP** (if your LLM supports it):
   - Configure MCP in your LLM
   - Ensure `mcp.enabled: true` in `config.json`

---

## Git Issues

### ❌ "Git commit failed"

**Problem**: Errors when trying to commit documentation.

**Diagnosis**:
```bash
git status
git log
```

**Solutions**:

1. **Git not initialized**:
   ```bash
   git init
   ```

2. **Git user not configured**:
   ```bash
   git config user.name "Your Name"
   git config user.email "your@email.com"
   ```

3. **Nothing to commit** (not really an error):
   - Documentation hasn't changed
   - This is normal!

4. **Disable Git** if you don't need it:
   ```json
   {
     "git": {
       "enabled": false
     }
   }
   ```

---

### ❌ "Git push failed"

**Problem**: Auto-push to remote fails.

**Solutions**:

1. **Remote not configured**:
   ```bash
   git remote add origin https://github.com/yourusername/yourrepo.git
   ```

2. **Authentication failed**:
   - Set up SSH keys, or
   - Use personal access token, or
   - Disable auto-push:
     ```json
     {
       "git": {
         "auto_push": false
       }
     }
     ```

3. **Branch doesn't exist on remote**:
   ```bash
   git push -u origin main
   ```

---

## MCP Server Issues

### ❌ "MCP server not responding"

**Problem**: LLM cannot access Cisco documentation.

**Diagnosis**:
```bash
# Test MCP server manually
cd mcp-server
node server.js
# Server should start without errors
```

**Solutions**:

1. **Install dependencies**:
   ```bash
   cd mcp-server
   npm install
   ```

2. **Check Node version**:
   ```bash
   node --version  # Should be 18+
   ```

3. **Verify MCP configuration** in your LLM's settings

4. **Check if your LLM supports MCP**:
   - Not all local LLMs support MCP
   - Works with: Claude Desktop, some custom setups
   - May not work with: Basic Ollama, basic LM Studio

5. **System still works without MCP**:
   - Documentation will be generated
   - Just won't have Cisco doc lookups
   - Consider it optional for basic usage

---

### ❌ "Command not found in MCP cache"

**Problem**: MCP server returns "not found" for commands.

**Solution**:
Add the command to `docs_cache/basic_commands.json`:

```json
{
  "your-command": {
    "description": "What it does",
    "syntax": "command syntax",
    "examples": ["example 1", "example 2"]
  }
}
```

Or extend the MCP server to fetch from Cisco.com (advanced).

---

## Performance Issues

### ❌ "Processing is very slow"

**Problem**: Takes 5+ minutes to process a single config.

**Solutions**:

1. **Use GPU acceleration**:
   - Ollama: Install CUDA/ROCm drivers
   - LM Studio: Enable GPU in settings

2. **Use smaller model**:
   ```bash
   ollama pull llama3.1:8b  # Not 70B
   ```

3. **Reduce output length**:
   ```json
   {
     "llm": {
       "max_tokens": 4000
     }
   }
   ```

4. **Use quantized models**:
   - Q4_K_M (faster, less accurate)
   - Q5_K_M (balanced)
   - Q8_0 (slower, more accurate)

5. **Simplify prompt**:
   - Edit `automation/prompts/analysis_template.txt`
   - Remove less important sections

---

### ❌ "System runs out of memory"

**Problem**: OOM error or system freezes.

**Solutions**:

1. **Use smaller model**:
   - 7B instead of 13B or 70B

2. **Close other applications**

3. **Increase swap space** (Linux):
   ```bash
   sudo fallocate -l 8G /swapfile
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   sudo swapon /swapfile
   ```

4. **Use cloud-based LLM** (requires code modification):
   - OpenAI API
   - Anthropic Claude API
   - Note: This sends configs to external servers!

---

## Output Issues

### ❌ "No output files generated"

**Problem**: `output/` folder is empty.

**Diagnosis**:
Check the processor logs for errors:
```bash
cd automation
node processor.js ../configs/test.txt
# Read the error messages
```

**Common causes**:
- LLM connection failed → Fix LLM connection
- Config file unreadable → Check permissions
- Disk full → Free up space
- Invalid config.json → Validate JSON

---

### ❌ "Output is incomplete"

**Problem**: Generated markdown cuts off mid-sentence.

**Cause**: Hit `max_tokens` limit.

**Solution**:
Increase in `config.json`:
```json
{
  "llm": {
    "max_tokens": 12000  // Or higher
  }
}
```

Check your LLM's maximum context window:
- Llama 3.1: 128K tokens (but 8-16K is practical)
- Mistral: 32K tokens
- Mixtral: 32K tokens

---

## Windows-Specific Issues

### ❌ "Path errors on Windows"

**Problem**: Paths with spaces cause issues.

**Solution**:
Always use quotes:
```bash
node processor.js "C:\Program Files\configs\test.txt"
```

Or avoid spaces in paths entirely.

---

### ❌ "Permission denied on Windows"

**Problem**: Cannot create files or directories.

**Solutions**:
1. Run terminal as Administrator
2. Install project in user directory (not C:\Program Files)
3. Check antivirus isn't blocking

---

## Linux/Mac-Specific Issues

### ❌ "Permission denied (EACCES)"

**Problem**: Cannot execute scripts or access files.

**Solution**:
```bash
# Make scripts executable
chmod +x setup.js
chmod +x mcp-server/server.js

# Fix file permissions
chmod -R u+rw configs/ output/
```

---

## Getting Help

If you're still stuck:

1. **Check logs**: Read error messages carefully
2. **Search issues**: Look for similar problems online
3. **Minimal test**: Try the simplest possible case
4. **Isolate component**: Test each part separately:
   - LLM connection
   - MCP server
   - Processor script
   - Watcher

### Diagnostic Commands

```bash
# System info
node --version
npm --version
git --version

# Check LLM
curl http://localhost:11434/api/version  # Ollama

# Test processor
cd automation
node processor.js ../configs/SAMPLE-SWITCH.txt

# Test MCP server
cd mcp-server
node server.js

# Check Git
git status
git log --oneline -5

# List installed packages
cd automation && npm list
cd mcp-server && npm list
```

### Enable Debug Logging

Modify scripts to add verbose logging:

**In processor.js**:
```javascript
const DEBUG = true;

function debugLog(...args) {
  if (DEBUG) console.log('[DEBUG]', ...args);
}

// Use throughout code
debugLog('Config content:', configContent.substring(0, 100));
```

---

## Common Gotchas

1. **Config file format**: Must be plain text `.txt` file
2. **LLM must be running**: Start before running watcher
3. **JSON syntax**: config.json must be valid JSON (no trailing commas!)
4. **Node version**: Must be 18+ (check with `node --version`)
5. **Case sensitivity**: Linux/Mac care about file name case
6. **Network ports**: Default ports must be available (11434, 1234, etc.)
7. **Firewalls**: May block localhost connections
8. **Working directory**: Run commands from correct directory

---

## Still Having Issues?

1. Try the [QUICKSTART.md](QUICKSTART.md) guide from scratch
2. Review [ARCHITECTURE.md](ARCHITECTURE.md) to understand the system
3. Check your `config.json` matches the format in [README.md](README.md)
4. Test with the provided `configs/SAMPLE-SWITCH.txt` first