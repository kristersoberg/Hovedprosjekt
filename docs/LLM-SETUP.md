# Using LM Studio Instead of Ollama

## TL;DR - What Changes?

**Answer:** Only the `config.json` file. Everything else stays the same!

## Configuration Changes

### Ollama Configuration 
```json
{
  "llm": {
    "endpoint": "http://localhost:11434/api/generate",
    "model": "llama3.1:8b",
    "max_tokens": 4000
  }
}
```

### LM Studio Configuration 
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

## Step-by-Step Migration from Ollama to LM Studio

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

Replace your current `config.json` with:

```json
{
  "llm": {
    "endpoint": "http://localhost:1234/v1/chat/completions",
    "model": "YOUR-MODEL-NAME-FROM-LMSTUDIO",
    "api_key": "",
    "temperature": 0.1,
    "max_tokens": 16000,
    "top_p": 0.9,
    "num_ctx": 32768
  },
  "logging": {
    "enabled": true,
    "log_dir": "./logs",
    "verbose": false,
    "debug": false
  },
  "git": {
    "enabled": true,
    "auto_push": false,
    "remote": "origin",
    "branch": "master"
  },
  "processing": {
    "auto_start_on_file_change": true,
    "delete_old_documentation": false
  },
  "validation": {
    "enabled": true,
    "save_reports": true
  },
  "security": {
    "sanitize_secrets": true,
    "redact_passwords": true,
    "redact_snmp_communities": true,
    "redact_tacacs_keys": true
  }
}
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

The processor always reads `config.json`. A simple way to switch is to keep a backup for each setup:

```powershell
# Save your current Ollama config
Copy-Item config.json config_ollama.json

# Save your LM Studio config
Copy-Item config.json config_lmstudio.json

# Switch by copying the one you want
Copy-Item config_ollama.json config.json
Copy-Item config_lmstudio.json config.json
```

## Testing

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

**That's it!** All automation, file watching, Git integration, and validation work identically with LM Studio.
