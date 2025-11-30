# Fix: Context Window Overflow

## The Problem

```
context full, shifting: n_ctx = 4096, n_discarded_ctx_tokens = 227
```

Your prompt is larger than the model's context window (4096 tokens), causing LM Studio to discard parts of your Cisco config or MCP documentation.

## Solution 1: Increase Context in LM Studio (Best Fix)

### Step-by-Step:

1. **Open LM Studio**

2. **Go to "Local Server" tab**

3. **Click "Configure" or the settings icon** (⚙️)

4. **Find "Context Length" setting**

5. **Change from 4096 to 8192 or 16384:**
   ```
   Context Length: 8192   ← Recommended
   or
   Context Length: 16384  ← Better for large configs
   ```

6. **Stop and restart the server:**
   - Click "Stop Server"
   - Click "Start Server"
   - Server will reload with new context size

### Why This Works:
- 8192 tokens = ~6000 words
- Enough for your config (2000-3000 tokens) + MCP docs (1000-2000 tokens) + response (4000 tokens)
- No more discarded tokens!

## Solution 2: Reduce MCP Documentation (If Context Can't Be Increased)

Edit `config.json`:

```json
{
  "mcp": {
    "enabled": true,
    "max_prompt_size": 30000,    // Reduced from 50000
    "max_commands": 1,            // Reduced from 2
    "max_features": 1             // Keep at 1
  }
}
```

This reduces the amount of MCP documentation added, keeping the prompt smaller.

## Solution 3: Disable MCP for Large Configs

For very large switch configs (>500 lines), temporarily disable MCP:

```json
{
  "mcp": {
    "enabled": false    // Disable MCP enrichment
  }
}
```

Process the large config, then re-enable MCP for normal configs.

## How to Check If It's Fixed

After increasing context in LM Studio, process a config and check:

### ✅ Success - You Should See:
```
Sending request to LLM...
   - Prompt size: 35000 characters (~8750 tokens)
   - Max tokens to generate: 4000

[No context warnings in LM Studio console]
```

### ❌ Still Broken - You'll See:
```
context full, shifting: n_ctx = 4096, n_discarded_ctx_tokens = XXX
```

If still seeing this, LM Studio didn't reload with new context. Try:
1. Fully quit LM Studio
2. Restart LM Studio
3. Reload model
4. Start server again

## Understanding Token Counts

**Rough conversion:**
- 1 token ≈ 0.75 words (English)
- 1 token ≈ 4 characters
- 4096 tokens ≈ 16,000 characters ≈ 3000 words

**Your config file `1-aksess-sw01-2.txt`:**
- File size: ???? characters
- Estimated tokens: file_size ÷ 4
- If file is 8000 chars = ~2000 tokens

**MCP documentation added:**
- 2 commands × ~500 chars each = 1000 chars
- 1 feature × ~800 chars = 800 chars
- Total MCP: ~1800 chars = ~450 tokens

**Total prompt:**
- Config: 2000 tokens
- MCP: 450 tokens
- System prompts: 200 tokens
- **Total: 2650 tokens** (should fit in 4096!)

But if your config is larger (say 10,000 chars = 2500 tokens):
- Config: 2500 tokens
- MCP: 450 tokens
- System: 200 tokens
- **Total: 3150 tokens** (still fits in 4096)

If total exceeds 4096, you get the warning.

## Check Your Config File Size

```powershell
# Check file size
Get-Item configs\1-aksess-sw01-2.txt | Select-Object Name, Length

# Count lines
Get-Content configs\1-aksess-sw01-2.txt | Measure-Object -Line
```

If the file is:
- < 16,000 chars (< 4000 tokens): Should fit in 4096 context
- 16,000-32,000 chars: Need 8192 context
- 32,000-64,000 chars: Need 16384 context
- > 64,000 chars: Disable MCP or split file

## Recommended Settings

### For Small-Medium Configs (<500 lines)

**LM Studio:**
```
Context Length: 8192
GPU Layers: ALL (33/33)
```

**config.json:**
```json
{
  "mcp": {
    "enabled": true,
    "max_prompt_size": 50000,
    "max_commands": 2,
    "max_features": 1
  }
}
```

### For Large Configs (500-1000 lines)

**LM Studio:**
```
Context Length: 16384
GPU Layers: ALL (33/33)
```

**config.json:**
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

### For Very Large Configs (>1000 lines)

**LM Studio:**
```
Context Length: 16384 (or 32768 if available)
```

**config.json:**
```json
{
  "mcp": {
    "enabled": false    // Disable for very large configs
  },
  "llm": {
    "max_tokens": 6000  // Allow longer output
  }
}
```

## What Happens When Context Overflows?

### The Bad:
- ❌ Parts of your config get discarded (lost)
- ❌ MCP documentation gets truncated
- ❌ System prompts might be cut off
- ❌ Output quality suffers

### The Good:
- ✅ LM Studio tries to keep the most important parts
- ✅ Processing doesn't crash
- ✅ You still get output (just not as good)

But you **should fix it** to get full quality!

## Quick Action Steps

**Right now:**

1. **Open LM Studio** → Local Server tab → Settings
2. **Set Context Length: 8192** (or 16384)
3. **Stop Server** → **Start Server**
4. **Try processing again**

You should see no more context warnings!

## Monitor in Real-Time

Watch LM Studio's console output while processing. You should see:
- Model loading messages
- Context size confirmation
- Generation progress
- **NO "context full" warnings** ✓

---

**Bottom line:** Increase context to 8192 in LM Studio, restart server, problem solved!
