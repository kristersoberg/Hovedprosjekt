# LM Studio Optimization Guide

## How to Verify MCP Was Used

### Method 1: Check Console Output (Best Method)

When processing a config file, look for these specific lines:

```
✓ Enriching with Cisco documentation from MCP server...
   Found 5 commands and 2 features          ← MCP detected commands
   Connected to MCP server                   ← MCP server running
   Fetching docs for command: vlan          ← Getting Cisco docs
   Fetching docs for command: interface     ← Getting more docs
   Fetching docs for feature: VLAN          ← Getting feature docs
   Added 4 documentation sections to prompt  ← Docs added!
   Total prompt size: 35000 characters      ← Shows enriched size
```

**If you see these lines = MCP WAS USED ✓**

**If you DON'T see these lines:**
- MCP is disabled in config.json
- MCP server failed to start
- No commands/features detected in config

### Method 2: Run Verification Script

```powershell
python verify_mcp_usage.py
```

This will:
- Show your MCP configuration
- Process a test file with verbose output
- Tell you if MCP was used

### Method 3: Compare Prompt Sizes

**Without MCP:**
```
✓ Sending to LLM for analysis...
   Prompt size: 8000 characters   ← Small prompt
```

**With MCP:**
```
✓ Sending to LLM for analysis...
   Prompt size: 35000 characters  ← Larger (includes docs)
```

### Method 4: Check Documentation Quality

MCP-enriched documentation should include:
- ✅ Accurate Cisco command syntax
- ✅ VLAN range information (1-4094)
- ✅ Best practices specific to Cisco
- ✅ Proper technical terminology
- ✅ Feature explanations (e.g., "Rapid-PVST", "Layer 2 broadcast domains")

Your TEST-03.md shows good technical detail, suggesting MCP was likely used!

## LM Studio Configuration & Optimization

### Essential Settings in LM Studio

#### 1. Model Selection Tab

**Recommended Models:**
- `meta-llama-3.1-8b-instruct` (Your current - Good choice!)
- `mistral-7b-instruct-v0.2` (Faster, slightly less accurate)
- `qwen2.5-7b-instruct` (Good for technical content)

**Model Format:**
- Use GGUF format
- Quantization: Q4_K_M or Q5_K_M (balance of speed/quality)
- For your 8B model: Q4_K_M is fine

#### 2. Server Settings Tab

Click "Server Options" in LM Studio:

```
✓ Enable CORS (already on)
✓ Port: 1234 (default)
✓ Context Length: 8192 (or higher if available)
✓ GPU Offload: 100% (use all layers on GPU)
```

**Important Settings:**

| Setting | Recommended | Why |
|---------|-------------|-----|
| Context Length | 8192-16384 | Allows larger configs + MCP docs |
| Temperature | 0.7 | Good balance (already in config.json) |
| Top P | 0.9 | Better coherence |
| Top K | 40 | Standard setting |
| Max Tokens | 4000 | Set in config.json ✓ |
| GPU Layers | ALL (33/33 for 8B) | Maximum speed |

#### 3. Advanced Settings

In LM Studio's "Advanced" section:

**Context & Attention:**
```
✓ Context Length: 8192 minimum
✓ Enable Flash Attention: ON (if available)
✓ Rope Scaling: Auto
```

**Performance:**
```
✓ Batch Size: 512 (or auto)
✓ Threads: Auto (let LM Studio decide)
✓ GPU Layers: 33 (all layers for 8B model)
```

**Sampling:**
```
Temperature: 0.7  (set in config.json)
Top P: 0.9
Top K: 40
Repeat Penalty: 1.1
Min P: 0.05
```

### Optimal config.json for LM Studio

```json
{
  "llm": {
    "endpoint": "http://192.168.56.1:1234/v1/chat/completions",
    "model": "meta-llama-3.1-8b-instruct",
    "api_key": "",
    "temperature": 0.7,
    "max_tokens": 4000,    // Good for detailed docs
    "timeout": 300000      // 5 minutes
  },
  "mcp": {
    "server_path": "./mcp_server/server.py",
    "enabled": true,              // ← Make sure this is true!
    "max_prompt_size": 50000,     // Safe for 8k context
    "max_commands": 2,            // Balance detail/size
    "max_features": 1             // Most important feature only
  }
}
```

### Performance Tuning

#### For Speed (Fast Processing)

```json
{
  "llm": {
    "model": "mistral-7b-instruct-v0.2",  // Faster model
    "temperature": 0.5,                    // More deterministic
    "max_tokens": 3000                     // Shorter responses
  },
  "mcp": {
    "max_commands": 1,                     // Minimal docs
    "max_features": 1
  }
}
```

**LM Studio:** Use Q4_K_M quantization

#### For Quality (Best Documentation)

```json
{
  "llm": {
    "model": "meta-llama-3.1-8b-instruct",
    "temperature": 0.7,
    "max_tokens": 6000                     // Longer, detailed
  },
  "mcp": {
    "max_prompt_size": 80000,              // Allow more docs
    "max_commands": 3,
    "max_features": 2
  }
}
```

**LM Studio:** Use Q5_K_M or Q6_K quantization, context 16384

#### For Large Configs (Big Switches)

```json
{
  "llm": {
    "max_tokens": 8000                     // Allow very long output
  },
  "mcp": {
    "enabled": false                       // Disable to save space
    // Or keep enabled with small limits:
    "max_prompt_size": 30000,
    "max_commands": 1,
    "max_features": 0
  }
}
```

**LM Studio:** Context 16384, ensure GPU has enough RAM

### Monitoring Performance

#### Check GPU Usage

In LM Studio's server tab, you'll see:
```
GPU: NVIDIA RTX 3060 (100%)  ← Should be high
RAM: 4.2 GB / 12 GB          ← Model loaded
Tokens/sec: 25-40            ← Speed (higher = better)
```

**Good performance:**
- GPU usage: 80-100%
- Tokens/sec: >20 for generation
- Response time: 30-120 seconds for full doc

**Poor performance:**
- GPU usage: <50% (might be using CPU)
- Tokens/sec: <10
- Response time: >5 minutes

**Fix:** Ensure all GPU layers are loaded in LM Studio

#### Monitor in config.json logs

Watch for:
```
Sending request to LLM...
   - Prompt size: 35000 characters     ← Input size
   - Max tokens to generate: 4000      ← Output limit

LLM response length: 3200 characters   ← Actual output
```

**Timing:**
- Prompt processing: ~5-10 seconds
- Generation: 1-3 minutes
- Total: 1.5-4 minutes typically

### Troubleshooting

#### Slow Generation

**Problem:** Takes >5 minutes

**Solutions:**
1. Check GPU layers in LM Studio (should be 33/33 for 8B)
2. Reduce `max_tokens` to 3000
3. Use faster model (Mistral 7B)
4. Reduce MCP limits

#### Context Length Error

**Problem:** "Context length exceeded"

**Solutions:**
1. Increase context in LM Studio (8192 → 16384)
2. Reduce `max_prompt_size` in config.json
3. Disable MCP temporarily
4. Use smaller config files

#### Poor Quality Output

**Problem:** Documentation is generic or inaccurate

**Solutions:**
1. **Enable MCP!** (Check config.json)
2. Increase temperature to 0.8
3. Increase `max_tokens` to 6000
4. Use better quantization (Q5_K_M instead of Q4_K_M)
5. Try different model (Qwen2.5 for technical docs)

#### Memory Errors

**Problem:** LM Studio crashes or OOM

**Solutions:**
1. Use smaller model (3B instead of 8B)
2. Reduce context length to 4096
3. Use lower quantization (Q4_K_S instead of Q4_K_M)
4. Close other applications
5. Reduce `max_prompt_size` to 30000

### Best Practices

#### 1. Start Simple, Then Optimize

Initial config:
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

If working well, gradually increase limits.

#### 2. Test Different Models

Try these in order:
1. `meta-llama-3.1-8b-instruct` (balanced)
2. `qwen2.5-7b-instruct` (technical)
3. `mistral-7b-instruct-v0.2` (fast)
4. `mixtral-8x7b-instruct` (quality, if you have 24GB+ RAM)

#### 3. Monitor Output Quality

Process the same config with different settings:
- MCP enabled vs disabled
- Different max_tokens values
- Different temperatures

Compare which produces best docs.

#### 4. Use Batch Processing

For many configs:
```powershell
# Process during off-hours
python automation/watcher.py
# Leave running overnight
```

LM Studio will process them one by one.

## Summary

### To Verify MCP Usage:
✅ Look for "Enriching with Cisco documentation" in console
✅ Run `python verify_mcp_usage.py`
✅ Check prompt size (>30k = likely has MCP docs)

### Optimal LM Studio Settings:
✅ Context: 8192 minimum (16384 better)
✅ GPU Layers: ALL (33/33 for 8B model)
✅ Quantization: Q4_K_M (speed) or Q5_K_M (quality)
✅ Temperature: 0.7 (in config.json)

### Best config.json:
```json
{
  "llm": {
    "endpoint": "http://192.168.56.1:1234/v1/chat/completions",
    "model": "meta-llama-3.1-8b-instruct",
    "max_tokens": 4000
  },
  "mcp": {
    "enabled": true,
    "max_prompt_size": 50000,
    "max_commands": 2,
    "max_features": 1
  }
}
```

Your current setup looks good! The output quality suggests everything is working well.
