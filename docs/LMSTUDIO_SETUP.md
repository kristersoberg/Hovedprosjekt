# Using LM Studio Instead of Ollama

## TL;DR - What Changes?

**Answer:** Only the `config.json` file. Everything else stays the same!

## Configuration Changes

### Ollama Configuration (Current)
```json
{
  "llm": {
    "endpoint": "http://localhost:11434/api/generate",
    "model": "llama3.1:8b",
    "max_tokens": 4000
  }
}
```

### LM Studio Configuration (New)
```json
{
  "llm": {
    "endpoint": "http://localhost:1234/v1/chat/completions",
    "model": "llama-3.1-8b-instruct",
    "max_tokens": 4000
  }
}
```

### What Changed?

| Setting | Ollama | LM Studio |
|---------|--------|-----------|
| `endpoint` | `http://localhost:11434/api/generate` | `http://localhost:1234/v1/chat/completions` |
| `model` | `llama3.1:8b` | Model name from LM Studio (varies) |
| Everything else | Same | Same |

## Step-by-Step Migration

### 1. Setup LM Studio

1. **Download and install** [LM Studio](https://lmstudio.ai/)
2. **Download a model** in LM Studio (e.g., Llama 3.1 8B Instruct)
3. **Start the local server**:
   - Click "Local Server" tab in LM Studio
   - Select your model
   - Click "Start Server"
   - Default port: `1234`

### 2. Find Your Model Name

In LM Studio's server tab, you'll see the model name. Common formats:
- `llama-3.1-8b-instruct`
- `mistral-7b-instruct-v0.2`
- `codellama-7b-instruct`

Copy the **exact name** shown.

### 3. Update config.json

**Option A: Replace your current config.json**

```json
{
  "llm": {
    "endpoint": "http://localhost:1234/v1/chat/completions",
    "model": "YOUR-MODEL-NAME-FROM-LMSTUDIO",
    "api_key": "",
    "temperature": 0.7,
    "max_tokens": 4000,
    "timeout": 300000
  },
  "mcp": {
    "server_path": "./mcp_server/server.py",
    "enabled": true,
    "max_prompt_size": 50000,
    "max_commands": 2,
    "max_features": 1
  },
  "git": {
    "enabled": true,
    "auto_push": false,
    "remote": "origin",
    "branch": "main"
  },
  "processing": {
    "auto_start_on_file_change": true,
    "delete_old_documentation": false
  }
}
```

**Option B: Use the pre-made config**

I created `config_lmstudio.json` for you. To use it:

```powershell
# Backup current config
Copy-Item config.json config_ollama.json

# Use LM Studio config
Copy-Item config_lmstudio.json config.json

# Edit to add your exact model name
notepad config.json
```

### 4. Test the Connection

```powershell
# Test with a simple config file
python automation/processor.py configs/TEST.txt
```

You should see:
```
✓ Sending request to Ollama:
   - Endpoint: http://localhost:1234/v1/chat/completions
   - Model: llama-3.1-8b-instruct
   - Prompt size: 25000 characters
   - Max tokens to generate: 4000
```

## What Stays the Same?

✅ **All Python code** - No changes needed
✅ **MCP integration** - Works identically
✅ **File watcher** - No changes
✅ **Documentation generation** - Same process
✅ **Git integration** - Same
✅ **All scripts** - No changes

## Differences to Know

### API Format

LM Studio uses **OpenAI-compatible API**, so the processor will automatically detect this and use the correct format:

- Sends `messages` array instead of `prompt` string
- Uses `choices[0].message.content` for response
- Fully compatible with the current code

### Model Performance

LM Studio and Ollama may give different results with the same model because:
- Different quantization methods
- Different sampling parameters
- Different context handling

**Recommendation:** Start with the same settings (temperature 0.7, max_tokens 4000) and adjust as needed.

## Switching Between Ollama and LM Studio

### Keep Both Configs

```powershell
# For Ollama
Copy-Item config_ollama.json config.json

# For LM Studio
Copy-Item config_lmstudio.json config.json
```

### Or Use Environment-Specific Configs

The processor always reads `config.json`, so you can:

1. Have multiple config files:
   - `config_ollama.json`
   - `config_lmstudio.json`
   - `config_openai.json` (if you want to use OpenAI API)

2. Copy the one you want to `config.json` when switching

## Testing

### Test MCP Integration with LM Studio

```powershell
# MCP works the same with LM Studio
python tests/test_mcp_integration.py
```

All tests should pass identically.

### Process a Config

```powershell
# Start the watcher
python automation/watcher.py

# Drop a config file in configs/
# Watch it get processed with LM Studio!
```

## Performance Comparison

| Feature | Ollama | LM Studio |
|---------|--------|-----------|
| Speed | Fast | Fast |
| GPU Support | Yes | Yes |
| CPU Fallback | Yes | Yes |
| Model Library | Built-in | Download manually |
| API Compatibility | Native + OpenAI | OpenAI-compatible |
| UI | CLI | GUI |
| Ease of Use | Simple | Very Simple |

## Common LM Studio Models

Popular models that work well:

```json
// Llama 3.1 8B (Recommended)
"model": "llama-3.1-8b-instruct"

// Mistral 7B
"model": "mistral-7b-instruct-v0.2"

// Qwen 2.5 7B (Good for technical docs)
"model": "qwen2.5-7b-instruct"

// CodeLlama 7B (Good for code analysis)
"model": "codellama-7b-instruct"
```

**Important:** Use the **exact name** shown in LM Studio's server tab!

## Troubleshooting

### "Connection refused" Error

**Problem:** LM Studio server not running

**Fix:**
1. Open LM Studio
2. Go to "Local Server" tab
3. Select a model
4. Click "Start Server"
5. Verify it shows "Server running on port 1234"

### "Model not found" Error

**Problem:** Model name doesn't match

**Fix:** Copy the exact model name from LM Studio's server tab and paste it into `config.json`

### Very Slow Generation

**Problem:** CPU mode or large model

**Fix:**
- Check LM Studio is using GPU (shows in UI)
- Use a smaller model (3B instead of 8B)
- Reduce `max_tokens` to 2000-3000

## Summary

**To switch from Ollama to LM Studio:**

1. ✅ Install LM Studio
2. ✅ Download a model in LM Studio
3. ✅ Start LM Studio's server
4. ✅ Change 2 lines in `config.json`:
   - `endpoint`: `http://localhost:1234/v1/chat/completions`
   - `model`: (exact name from LM Studio)
5. ✅ Done! Everything else works the same

**Code changes:** ZERO
**File changes:** ONE (`config.json`)
**Effort:** 2 minutes

---

**That's it!** The entire MCP integration, all automation, everything works identically with LM Studio.
