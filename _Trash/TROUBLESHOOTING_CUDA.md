# Troubleshooting: CUDA Errors and Memory Issues

## Problem: Ollama CUDA Error (500 Internal Server Error)

### Error Message:
```
Exception: LLM API error: 500 - {"error":"llama runner process has terminated: CUDA error"}
```

### Cause:
The enriched prompt (config + MCP documentation) is too large for your GPU memory, causing Ollama to crash.

## Solutions

### Solution 1: Reduce MCP Documentation (Recommended)

The processor has been updated with automatic safeguards. Configure limits in `config.json`:

```json
{
  "mcp": {
    "enabled": true,
    "max_prompt_size": 100000,
    "max_commands": 3,
    "max_features": 2
  }
}
```

**Settings explained:**
- `max_prompt_size`: Maximum prompt size in characters (default: 100,000 = ~25k tokens)
- `max_commands`: How many commands to fetch docs for (default: 3)
- `max_features`: How many features to fetch docs for (default: 2)

**To reduce memory usage further:**
```json
{
  "mcp": {
    "max_prompt_size": 50000,   // Smaller limit
    "max_commands": 2,           // Fewer commands
    "max_features": 1            // Fewer features
  }
}
```

### Solution 2: Temporarily Disable MCP

If you're still having issues, disable MCP enrichment:

```json
{
  "mcp": {
    "enabled": false
  }
}
```

This will process configs without Cisco documentation context.

### Solution 3: Use a Smaller Model

Switch to a smaller Ollama model in `config.json`:

```json
{
  "llm": {
    "model": "llama3.1:8b"    // Current
    "model": "llama3.2:3b"    // Smaller, uses less GPU memory
  }
}
```

Download smaller model:
```bash
ollama pull llama3.2:3b
```

### Solution 4: Reduce max_tokens

Limit the response length to save memory:

```json
{
  "llm": {
    "max_tokens": 4000   // Reduced from 8000
  }
}
```

### Solution 5: Use CPU Mode

If your GPU is struggling, run Ollama in CPU mode:

```powershell
# Set environment variable before starting Ollama
$env:CUDA_VISIBLE_DEVICES=""
ollama serve
```

**Note:** CPU mode is much slower but won't have CUDA errors.

## Automatic Safeguards (Built-in)

The processor now automatically:

1. ✅ **Limits documentation** - Only fetches top 3 commands + 2 features
2. ✅ **Trims docs** - Each doc limited to ~500-800 characters
3. ✅ **Checks prompt size** - Warns if prompt exceeds max_prompt_size
4. ✅ **Falls back gracefully** - Uses original prompt if enriched is too large
5. ✅ **Prints diagnostics** - Shows prompt size in characters

## Monitoring Prompt Size

When processing, watch for these messages:

```
✓ Enriching with Cisco documentation from MCP server...
   Found 5 commands and 2 features
   Connected to MCP server
   Fetching docs for command: vlan
   Fetching docs for command: interface
   Fetching docs for feature: VLAN
   Added 4 documentation sections to prompt
   Total prompt size: 45000 characters    <- Check this!
```

**Safe ranges:**
- ✅ < 50,000 chars: Safe for most models
- ⚠️ 50,000-100,000 chars: May work, watch for errors
- ❌ > 100,000 chars: Likely to cause CUDA errors

## Testing with Reduced Settings

Try processing with minimal MCP enrichment:

```json
{
  "mcp": {
    "enabled": true,
    "max_prompt_size": 30000,
    "max_commands": 1,
    "max_features": 1
  }
}
```

Then gradually increase if successful.

## Verify Ollama Status

Check if Ollama is running properly:

```powershell
# Check Ollama service
ollama list

# Test a simple prompt
ollama run llama3.1:8b "Say hello"
```

If this fails, restart Ollama:
```powershell
# Stop all Ollama processes
taskkill /F /IM ollama.exe

# Restart
ollama serve
```

## GPU Memory Check

Check your GPU memory:

```powershell
# If you have nvidia-smi
nvidia-smi
```

Look for:
- **Total memory**: How much GPU RAM you have
- **Used memory**: How much is in use
- **Free memory**: What's available

**Typical requirements:**
- 3B model: ~4GB GPU RAM
- 8B model: ~8-12GB GPU RAM
- 8B model + large context: 12-16GB GPU RAM

## Quick Fix Script

Create `fix_cuda_error.bat`:

```batch
@echo off
echo Fixing CUDA error by reducing MCP limits...

REM Kill Ollama
taskkill /F /IM ollama.exe

REM Wait a moment
timeout /t 2

REM Restart Ollama
start ollama serve

echo Ollama restarted. Now try processing again.
pause
```

## Alternative: Process Without Watcher

If the watcher is giving you trouble, process files manually with reduced load:

```powershell
# Process one file at a time
python automation/processor.py configs/your-file.txt
```

This gives you more control and visibility over what's happening.

## Summary of Fixes

| Issue | Fix | Impact |
|-------|-----|--------|
| CUDA error | Reduce `max_commands` to 2 | Less documentation context |
| Prompt too large | Set `max_prompt_size` to 50000 | Smaller prompts |
| Out of memory | Use smaller model (3b instead of 8b) | Faster, less accurate |
| Slow processing | Disable MCP (`enabled: false`) | No Cisco docs context |
| GPU unavailable | Run Ollama in CPU mode | Much slower |

## Best Configuration for 8GB GPU

```json
{
  "llm": {
    "model": "llama3.1:8b",
    "max_tokens": 4000
  },
  "mcp": {
    "enabled": true,
    "max_prompt_size": 10000,
    "max_commands": 2,
    "max_features": 1
  }
}
```

## Best Configuration for 4GB GPU

```json
{
  "llm": {
    "model": "llama3.2:3b",
    "max_tokens": 3000
  },
  "mcp": {
    "enabled": true,
    "max_prompt_size": 30000,
    "max_commands": 1,
    "max_features": 1
  }
}
```

---

**Status:** The system now has built-in protections against CUDA errors. If you still encounter issues, use the reduced configuration settings above.
