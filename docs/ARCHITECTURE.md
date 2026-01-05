# System Architecture

This document explains how the Cisco Configuration Documentation System works.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Cisco Config Documentation System                 │
└─────────────────────────────────────────────────────────────────────┘

┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│   configs/   │      │  automation/ │      │   output/    │
│              │─────▶│              │─────▶│              │
│  *.txt files │      │  Processing  │      │  *.md files  │
└──────────────┘      └──────────────┘      └──────────────┘
                             │
                             │
                    ┌────────┴────────┐
                    │                 │
                    ▼                 ▼
            ┌───────────────┐  ┌──────────────┐
            │  Local LLM    │  │  MCP Server  │
            │               │◀─│              │
            │  (Ollama,     │  │  Cisco Docs  │
            │   LM Studio)  │  │              │
            └───────────────┘  └──────────────┘
                    │
                    ▼
            ┌───────────────┐
            │  Git Repo     │
            │  (Version     │
            │   Control)    │
            └───────────────┘
```

## Component Details

### 1. File Watcher ([automation/watcher.py](../automation/watcher.py))

**Purpose**: Monitor the `configs/` directory for new or changed configuration files.

**Technology**: `watchdog` (Python file system monitoring library)

**Behavior**:
- Watches `*.txt` files in `configs/`
- Debounces file changes (2-second cooldown to avoid duplicate processing)
- Prevents duplicate processing using a lock mechanism
- Spawns processor subprocess for each detected file

**Flow**:
```
File Added/Changed
    ↓
Cooldown Check (2 seconds)
    ↓
Check if already processing (lock)
    ↓
Spawn: python processor.py <file_path>
    ↓
Monitor completion
```

**Implementation**:
- Uses `watchdog.observers.Observer` for cross-platform file monitoring
- `FileSystemEventHandler` handles `on_created` and `on_modified` events
- Subprocess spawning with `subprocess.Popen()`
- Processing lock prevents duplicate runs

### 2. Configuration Processor ([automation/processor.py](../automation/processor.py))

**Purpose**: Process a single configuration file and generate documentation.

**Main Classes and Functions**:
1. **`ConfigProcessor`** class - Main processing orchestrator
2. **`read_config_file()`** - Load the configuration file
3. **`extract_ios_version()`** - Parse IOS version from config text
4. **`build_prompt()`** - Load template and inject config content
5. **`call_llm()`** - Send HTTP request to local LLM API
6. **`save_documentation()`** - Write markdown to output/
7. **`commit_to_git()`** - Commit changes with metadata

**Processing Pipeline**:
```
Input: configs/SWITCH-01.txt
    ↓
Extract IOS Version (regex: "Version 15.2")
    ↓
Load Prompt Template (analysis_template.txt)
    ↓
Extract Commands & Features from config
    ↓
Fetch Cisco Docs via MCP Client
    ↓
Enrich Prompt with {{CISCO_DOCS}}
    ↓
Replace {{CONFIG_CONTENT}}, {{IOS_VERSION}}, {{FILENAME}}
    ↓
Send HTTP POST to LLM API (requests library)
    ↓
Receive Markdown Documentation
    ↓
Save to output/SWITCH-01.md
    ↓
Git Add + Commit (GitPython)
    ↓
Output: Generated documentation
```

**Key Dependencies**:
- `requests` - HTTP client for LLM API
- `GitPython` - Git integration
- `pathlib` - Path manipulation
- `re` - Regular expressions for parsing

### 3. MCP Client ([automation/mcp_client.py](../automation/mcp_client.py))

**Purpose**: Interface between processor and MCP server.

**Class**: `CiscoMCPClient`

**Main Methods**:
- `fetch_command_docs()` - Get documentation for Cisco commands
- `fetch_feature_docs()` - Get documentation for Cisco features
- `enrich_prompt()` - Add fetched docs to LLM prompt

**Communication**:
```
Processor ←─ Python API ─→ MCP Client
                              ↕
                      [Fetch commands,
                       Fetch features]
                              ↕
                         MCP Server
                              ↕
                      docs_cache/*.json
```

### 4. MCP Server ([mcp_server/server-v2.py](../mcp_server/server-v2.py))

**Purpose**: Provide the LLM and processor with access to Cisco IOS documentation.

**Protocol**: Model Context Protocol (MCP)

**Technology**: Python-based MCP server using `mcp` SDK

**Available Tools**:

| Tool | Purpose | Example |
|------|---------|---------|
| `search_cisco_command` | Look up command documentation | `interface`, `ip address` |
| `get_cisco_feature` | Get feature explanations | `VLAN`, `OSPF`, `STP` |
| `list_available_commands` | List all cached commands | Returns command inventory |
| `list_available_features` | List all cached features | Returns feature inventory |

**Data Sources**:
- `docs_cache/cisco_ios_commands_enhanced.json` - Enhanced command docs
- `docs_cache/cisco_ios_interface_commands.json` - Interface-specific commands
- `docs_cache/basic_commands.json` - Basic command reference

**Communication**:
```
MCP Client ←─ stdio/API ─→ MCP Server
                              ↕
                    [Search, Lookup,
                     List, Explain]
                              ↕
                    docs_cache/*.json
```

### 5. Local LLM

**Supported Platforms**:
- **Ollama**: Recommended, easy setup, CLI-based
- **LM Studio**: GUI-based, user-friendly
- **Text Generation WebUI**: Advanced users
- **Any OpenAI-compatible API**

**Requirements**:
- Minimum 8GB VRAM (for 7B models)
- 16GB VRAM recommended (for better models)
- Context window: 8K+ tokens (larger is better)
- Supports `/v1/chat/completions` endpoint

**API Format**:
```json
POST /v1/chat/completions
{
  "model": "llama3.1:8b",
  "messages": [
    {"role": "system", "content": "You are a Cisco expert..."},
    {"role": "user", "content": "Analyze this config..."}
  ],
  "temperature": 0.1,
  "max_tokens": 4000
}
```

**Python Implementation**:
```python
import requests

response = requests.post(
    config['llm']['endpoint'],
    json={
        'model': config['llm']['model'],
        'messages': messages,
        'temperature': config['llm']['temperature'],
        'max_tokens': config['llm']['max_tokens']
    },
    timeout=config['llm']['timeout'] / 1000
)
```

### 6. Git Integration

**Purpose**: Version control for generated documentation.

**Technology**: `GitPython` library

**Features**:
- Automatic repository initialization
- Commits per documentation update
- Detailed commit messages with metadata
- Optional auto-push to remote

**Commit Format**:
```
Update documentation: aksess-sw01.txt

Generated from: aksess-sw01.txt
Timestamp: 2025-01-05T14:30:00.000Z
Auto-generated by Cisco Config Documentation System
```

**Python Implementation**:
```python
from git import Repo

repo = Repo(project_root)
repo.index.add([output_file])
repo.index.commit(commit_message)
if config['git']['auto_push']:
    origin = repo.remote(name=config['git']['remote'])
    origin.push()
```

## Data Flow

### Complete Processing Flow

```
1. User adds file: configs/CORE-SW-01.txt
                           ↓
2. Watcher detects change (watchdog event)
                           ↓
3. Watcher spawns: python processor.py configs/CORE-SW-01.txt
                           ↓
4. Processor reads config file (pathlib.read_text())
                           ↓
5. Processor extracts IOS version: "15.2" (regex)
                           ↓
6. Processor loads prompt template
                           ↓
7. Processor extracts commands/features from config
                           ↓
8. MCP Client fetches Cisco docs from MCP Server
                           ↓
9. Processor enriches prompt with {{CISCO_DOCS}}
                           ↓
10. Processor builds final prompt with config content
                           ↓
11. Processor sends HTTP POST to LLM API (requests)
                           ↓
12. LLM receives prompt and generates documentation
                           ↓
13. Processor receives LLM response (JSON)
                           ↓
14. Processor saves: output/CORE-SW-01.md
                           ↓
15. Processor commits to Git (GitPython):
    - git add output/CORE-SW-01.md
    - git commit -m "Update documentation: CORE-SW-01.txt"
                           ↓
16. Process complete! ✅
```

## Configuration Flow

### config.json Structure

```json
{
  "llm": {
    "endpoint": "URL of local LLM API",
    "model": "Model name to use",
    "temperature": "Creativity level (0-1)",
    "max_tokens": "Maximum response length",
    "timeout": "Request timeout in milliseconds"
  },
  "mcp": {
    "server_path": "./mcp_server/server-v2.py",
    "enabled": "Use MCP server for docs",
    "debug": "Enable debug logging",
    "max_prompt_size": "Maximum prompt size",
    "max_commands": "Max commands to fetch docs for",
    "max_features": "Max features to fetch docs for"
  },
  "git": {
    "enabled": "Enable version control",
    "auto_push": "Push commits automatically",
    "remote": "Git remote name",
    "branch": "Git branch name"
  },
  "processing": {
    "auto_start_on_file_change": "Auto-process when files change",
    "delete_old_documentation": "Delete old docs before generating"
  }
}
```

### Prompt Template Flow

```
automation/prompts/analysis_template.txt
              ↓
    [Read template file]
              ↓
    [Extract commands/features from config]
              ↓
    [Fetch Cisco docs via MCP]
              ↓
    [Replace placeholders]
    - {{CONFIG_CONTENT}} → Actual config text
    - {{IOS_VERSION}} → Detected version
    - {{FILENAME}} → Config filename
    - {{CISCO_DOCS}} → MCP-fetched documentation
              ↓
    [Send to LLM as prompt]
```

## Error Handling

### File Watcher Errors
- File access denied → Skip and log error to console
- File too large → Process anyway (LLM will handle)
- Duplicate processing → Blocked by cooldown and lock mechanism
- Subprocess failure → Log error and continue monitoring

### Processor Errors
- Config file not found → Exit with error code 1
- IOS version not found → Continue with "Unknown"
- LLM connection failed → Exit with detailed error message
- Git commit failed → Log warning but continue (non-critical)
- MCP fetch failed → Continue without enrichment

### MCP Server Errors
- Command not found → Return empty result
- Documentation missing → Return "not in cache" message
- JSON parse error → Log error and return empty docs
- Server crash → Processor continues without MCP enrichment

## Scalability Considerations

### Single Configuration
- Processing time: 30-120 seconds (depending on model and config size)
- Memory usage: Depends on LLM model size and Python process
- Typical memory: 100-500MB for processor + LLM VRAM

### Batch Processing
- File watcher processes sequentially (prevents resource overload)
- Lock mechanism prevents duplicate processing
- Each file is independent (parallel processing possible with modifications)
- Can use multiprocessing module for parallel processing if needed

### Large Configurations
- Configurations up to ~4000 lines are handled well
- Larger configs may require:
  - Increased `max_tokens` in config.json (up to model limit)
  - Larger context window in LLM
  - Potential splitting into sections
  - MCP `max_prompt_size` limit to avoid prompt overflow

## Extension Points

### 1. Add More Documentation

Edit JSON files in `docs_cache/`:
```json
{
  "new_command": {
    "description": "...",
    "syntax": "...",
    "examples": [...]
  }
}
```

### 2. Add New MCP Tools

Edit `mcp_server/server-v2.py`:
```python
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="new_tool",
            description="...",
            inputSchema={...}
        )
    ]
```

### 3. Customize Output Format

Edit `automation/prompts/analysis_template.txt` to change:
- Section order
- Level of detail
- Markdown formatting
- Analysis criteria

### 4. Add Pre/Post Processing

Modify `processor.py`:
```python
def preprocess_config(self, config_text):
    # Add preprocessing before LLM call
    return processed_text

def postprocess_documentation(self, docs):
    # Add postprocessing after LLM response
    return enhanced_docs
```

### 5. Integrate with External Systems

Add to `processor.py`:
```python
def notify_completion(self, output_file):
    # Send notifications (email, Slack, Teams)
    pass

def upload_to_portal(self, docs):
    # Upload to documentation portal
    pass
```

## Security Considerations

### Sensitive Data
- Configurations may contain:
  - Passwords (even encrypted)
  - IP addresses
  - Network topology information
- Keep repository private
- Review output before sharing
- Use `.gitignore` for sensitive files

### MCP Server
- Runs locally (no external calls)
- Only reads from local cache
- Can be extended to fetch from Cisco (add rate limiting)
- Runs in isolated process

### Git Commits
- May commit sensitive config data
- Use `.gitignore` for sensitive files
- Consider using private repository
- Review commits before pushing

### LLM
- All processing is **local** (no data sent to cloud)
- Ensure LLM is properly secured
- No API keys needed for local LLMs
- Data stays on your network

## Performance Optimization

### Speed Up Processing
1. Use smaller LLM model (7B instead of 70B)
2. Reduce `max_tokens` in config.json
3. Lower temperature for faster, more deterministic output
4. Use GPU acceleration for LLM
5. Disable Git integration if not needed
6. Reduce `max_commands` and `max_features` in MCP config

### Reduce Resource Usage
1. Use quantized models (Q4, Q5)
2. Limit concurrent processing (already done)
3. Clean up `docs_cache` periodically
4. Use Python's `gc.collect()` for memory management
5. Monitor with `psutil` for resource tracking

## Monitoring and Debugging

### Logs
- **Watcher logs**: Console output when running `python automation/watcher.py`
- **Processor logs**: Detailed step-by-step progress to stdout
- **MCP Server logs**: Logged to `logs/mcp_server.log`
- **Git logs**: `git log` for commit history

### Debug Mode
Enable debug logging in config.json:
```json
{
  "mcp": {
    "debug": true
  }
}
```

Or modify scripts:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Testing Components

**Test MCP Server**:
```bash
python mcp_server/server-v2.py
# Server starts and shows available tools
```

**Test Processor Manually**:
```bash
python automation/processor.py configs/aksess-sw01.txt
# Processes single file and generates output
```

**Test MCP Integration**:
```bash
python tests/test_mcp_integration.py
# Runs comprehensive MCP tests
```

**Test LLM Connection**:
```bash
curl -X POST http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"llama3.1:8b","messages":[{"role":"user","content":"test"}]}'
```

**Test Watcher**:
```bash
python automation/watcher.py
# Add a file to configs/ - should auto-process
```

---

## Technology Stack

### Core Technologies
- **Python 3.8+** - Main programming language
- **requests** - HTTP client for LLM API calls
- **watchdog** - File system monitoring
- **GitPython** - Git version control integration
- **mcp** - Model Context Protocol SDK

### Optional/Development
- **python-dotenv** - Environment variable management
- **pytest** - Testing framework
- **logging** - Debug and error logging

### External Services
- **Local LLM** (Ollama, LM Studio) - AI analysis
- **Git** - Version control
- **Cisco IOS Documentation** - Cached locally in JSON

---

## Summary

This system combines:
- **Python** for scripting and orchestration
- **File watching** (watchdog) for automation
- **Local LLM** for intelligent analysis
- **MCP protocol** for documentation access
- **Git** (GitPython) for version control

All components work together to transform raw Cisco configurations into comprehensive, readable documentation automatically.

**Key Advantages**:
- **Privacy**: All processing happens locally
- **Automation**: Minimal human intervention required
- **Accuracy**: MCP provides authoritative Cisco documentation
- **Version Control**: Git tracks all documentation changes
- **Extensibility**: Easy to add new features and integrations
