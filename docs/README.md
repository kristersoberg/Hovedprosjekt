# Cisco Configuration Documentation System

An automated system that uses a local LLM with MCP (Model Context Protocol) integration to interpret Cisco switch configurations and generate comprehensive, human-readable documentation with version control.

## Features

- 🤖 **Automated Processing**: File watcher automatically detects new/changed configuration files
- 📚 **MCP Server Integration**: Provides LLM access to Cisco IOS documentation for accurate interpretation
- 🔍 **IOS Version Detection**: Automatically extracts IOS version from configurations
- 📝 **Structured Documentation**: Generates detailed markdown documentation following best practices
- 🔄 **Version Control**: Automatic Git commits for documentation changes
- 🎯 **Best Practices Analysis**: Evaluates configurations against Cisco recommendations
- 🔒 **Privacy-First**: All processing happens locally - no cloud services required

## Project Structure

```
Hovedprosjekt/
├── configs/              # Input: Place Cisco running-config .txt files here
├── output/               # Output: Generated markdown documentation
├── docs_cache/           # Cached Cisco IOS documentation (JSON files)
├── mcp_server/           # MCP server for Cisco documentation access
│   ├── server-v2.py      # Active MCP server implementation
│   └── __init__.py
├── automation/           # Main automation scripts
│   ├── watcher.py        # File monitoring service
│   ├── processor.py      # Configuration processor
│   ├── mcp_client.py     # MCP client interface
│   └── prompts/          # LLM prompt templates
│       └── analysis_template.txt
├── tests/                # Test scripts
│   ├── test_mcp_integration.py
│   ├── test_llm.py
│   └── verify_mcp_usage.py
├── docs/                 # Documentation
│   ├── README.md         # This file
│   ├── QUICKSTART.md     # Quick start guide
│   ├── ARCHITECTURE.md   # System architecture
│   └── ...
├── logs/                 # System logs
├── config.json           # System configuration
├── requirements.txt      # Python dependencies
├── setup.py              # Setup script
└── .gitignore
```

## Prerequisites

- **Python** 3.8 or higher
- **Local LLM** (e.g., Ollama, LM Studio, etc.)
- **Git** (optional, for version control features)

## Installation

### 1. Install Python Dependencies

**Option 1: Use the setup script (recommended)**
```bash
python setup.py
```

**Option 2: Manual installation**
```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Required Python packages:**
- `requests` - HTTP client for LLM API calls
- `watchdog` - File system monitoring
- `GitPython` - Git integration
- `mcp` - Model Context Protocol SDK

### 2. Configure Your LLM

Edit `config.json` to match your local LLM setup:

```json
{
  "llm": {
    "endpoint": "http://192.168.1.211:1234/v1/chat/completions",
    "model": "meta-llama-3.1-8b-instruct",
    "api_key": "",
    "temperature": 0.1,
    "max_tokens": 4000,
    "timeout": 300000
  },
  "mcp": {
    "server_path": "./mcp_server/server-v2.py",
    "enabled": true,
    "debug": true,
    "max_prompt_size": 50000,
    "max_commands": 15,
    "max_features": 10
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

**Common LLM Endpoints:**
- **Ollama**: `http://localhost:11434/v1/chat/completions`
- **LM Studio**: `http://localhost:1234/v1/chat/completions`
- **Text Generation WebUI**: `http://localhost:5000/v1/chat/completions`

## Usage

### Starting the System

1. **Start your local LLM**:
   ```bash
   # For Ollama:
   ollama serve

   # For LM Studio: Start the server in the GUI
   ```

2. **Start the file watcher**:
   ```bash
   python automation/watcher.py
   ```

3. **Add or modify configuration files**:
   - Place `.txt` files containing Cisco `show running-config` output in the `configs/` folder
   - The system will automatically detect and process them

### Manual Processing

To process a single configuration file manually:

```bash
python automation/processor.py configs/your-config.txt
```

### Output

Generated documentation will be saved in the `output/` folder as markdown files with the same name as the input configuration file.

Example:
- Input: `configs/CORE-SW-01.txt`
- Output: `output/CORE-SW-01.md`

## Configuration Options

### config.json Settings

**LLM Configuration:**
- `endpoint` - Your local LLM API endpoint URL
- `model` - The model name to use
- `api_key` - API key if required (leave empty for most local LLMs)
- `temperature` - LLM creativity (0.0-1.0, lower = more deterministic)
- `max_tokens` - Maximum response length
- `timeout` - Request timeout in milliseconds

**MCP Configuration:**
- `server_path` - Path to MCP server script (server-v2.py)
- `enabled` - Enable/disable MCP server integration
- `debug` - Enable debug logging
- `max_prompt_size` - Maximum size for enriched prompts
- `max_commands` - Maximum number of commands to fetch docs for
- `max_features` - Maximum number of features to fetch docs for

**Git Configuration:**
- `enabled` - Enable/disable Git integration
- `auto_push` - Automatically push commits to remote
- `remote` - Git remote name
- `branch` - Git branch to commit to

**Processing Configuration:**
- `auto_start_on_file_change` - Auto-process when files change
- `delete_old_documentation` - Delete old docs before generating new ones

## MCP Server

The MCP (Model Context Protocol) server provides the LLM with access to Cisco IOS documentation, enabling more accurate and detailed analysis.

### How It Works

1. The processor extracts commands and features from the Cisco configuration
2. The MCP client requests documentation for these commands/features
3. The MCP server looks up documentation from cached JSON files
4. Documentation is injected into the LLM prompt
5. LLM generates more accurate documentation using official Cisco docs

### Available Tools

The MCP server (`mcp_server/server-v2.py`) provides these tools:

1. **search_cisco_command**: Look up Cisco IOS command documentation
2. **get_cisco_feature**: Get documentation for Cisco features (VLAN, STP, etc.)
3. **list_available_commands**: List all cached commands
4. **list_available_features**: List all cached features

### Extending Documentation

To add more command documentation, edit files in `docs_cache/`:
- `cisco_ios_commands_enhanced.json` - Command documentation
- `cisco_ios_interface_commands.json` - Interface-specific commands
- `basic_commands.json` - Basic command reference

## Workflow

1. **File Detection**: Watcher detects new/changed `.txt` file in `configs/`
2. **IOS Version Extraction**: System extracts IOS version from configuration
3. **Command/Feature Extraction**: Identifies Cisco commands and features
4. **MCP Documentation Lookup**: Fetches relevant Cisco documentation
5. **Prompt Enrichment**: Adds documentation to the analysis prompt
6. **LLM Analysis**: LLM analyzes configuration with documentation context
7. **Documentation Generation**: LLM generates structured markdown documentation
8. **Save Output**: Documentation saved to `output/` folder
9. **Git Commit**: Changes automatically committed (if Git enabled)

## Customizing Documentation Format

Edit the prompt template to customize the output:
```
automation/prompts/analysis_template.txt
```

The template uses placeholders:
- `{{CONFIG_CONTENT}}` - The configuration file content
- `{{IOS_VERSION}}` - Detected IOS version
- `{{FILENAME}}` - Configuration filename
- `{{CISCO_DOCS}}` - MCP-fetched Cisco documentation

## Troubleshooting

### LLM Connection Issues

**Problem**: "LLM API request failed: Connection refused"

**Solution**:
- Ensure your LLM server is running
- Verify the endpoint URL in `config.json`
- Check if the port is correct
- Test manually: `curl http://localhost:11434/api/version` (for Ollama)

### MCP Server Not Working

**Problem**: Documentation quality is poor or LLM doesn't use Cisco docs

**Solution**:
- Run tests: `python tests/test_mcp_integration.py`
- Check MCP server logs in `logs/mcp_server.log`
- Verify `mcp.enabled: true` in `config.json`
- Ensure documentation cache files exist in `docs_cache/`

### File Watcher Not Detecting Changes

**Problem**: New files in `configs/` are not processed

**Solution**:
- Ensure the watcher is running: `python automation/watcher.py`
- Check file extension is `.txt`
- Verify file permissions
- Check for error messages in console output

### Git Errors

**Problem**: Git commits failing

**Solution**:
- Initialize Git repository: `git init`
- Configure Git user:
  ```bash
  git config user.name "Your Name"
  git config user.email "your@email.com"
  ```
- Or disable Git in `config.json`: `"git.enabled": false`

### Import Errors

**Problem**: "ModuleNotFoundError" when running scripts

**Solution**:
- Activate virtual environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
- Install dependencies: `pip install -r requirements.txt`
- Verify Python version: `python --version` (should be 3.8+)

## Recommended LLM Models

For best results, use models with:
- Good instruction following
- Support for long context (8K+ tokens)
- Technical knowledge
- Function/tool calling capabilities (optional but helpful)

**Recommended models:**
- Llama 3.1 (8B or 70B)
- Mistral (7B or larger)
- Mixtral 8x7B
- Qwen 2.5
- DeepSeek Coder

## Performance Tips

1. **Use appropriate model size**: Larger models provide better analysis but are slower
2. **Adjust max_tokens**: Reduce for faster processing, increase for detailed docs
3. **Configure temperature**: Lower (0.1-0.3) for more consistent, factual output
4. **Enable MCP**: Provides better accuracy with Cisco documentation context
5. **Batch processing**: Process multiple configs during off-hours
6. **Use GPU acceleration**: Significantly faster than CPU-only inference

## Version Control

The system automatically creates Git commits for each documentation update:

```
commit 3a8f4b2
Author: System
Date:   Mon Nov 25 14:30:00 2024

    Update documentation: aksess-sw01.txt

    Generated from: aksess-sw01.txt
    Timestamp: 2024-11-25T14:30:00.000Z
    Auto-generated by Cisco Configuration Documentation System
```

To enable automatic pushing to a remote repository:
```json
{
  "git": {
    "enabled": true,
    "auto_push": true,
    "remote": "origin",
    "branch": "main"
  }
}
```

## Security Considerations

- Configuration files may contain sensitive information (passwords, IP addresses)
- Keep this repository private if it contains production configurations
- Review generated documentation before sharing
- Consider using `enable secret` instead of `enable password` in your configs
- The system will note security concerns in the "Configuration Quality Assessment" section
- All processing is **local** - no data is sent to cloud services

## Testing

### Run All Tests

```bash
# Test MCP integration
python tests/test_mcp_integration.py

# Test LLM connection
python tests/test_llm.py

# Verify MCP usage
python tests/verify_mcp_usage.py
```

### Manual Component Testing

**Test MCP Server:**
```bash
python mcp_server/server-v2.py
# Should start without errors and show available tools
```

**Test Processor:**
```bash
python automation/processor.py configs/aksess-sw01.txt
# Should generate output/aksess-sw01.md
```

**Test Watcher:**
```bash
python automation/watcher.py
# Then add a file to configs/ - should auto-process
```

## Advanced Usage

### Scheduled Documentation

**Windows (Task Scheduler):**
- Create a task that runs `python automation/watcher.py` on startup

**Linux/Mac (cron):**
```bash
# Add to crontab:
0 2 * * * cd /path/to/project && /usr/bin/python3 automation/watcher.py
```

### Integration with Other Systems

The processor can be extended to integrate with:
- NetBox (network documentation platform)
- Ansible (automation)
- Slack/Teams (notifications)
- Grafana (visualization)
- CMDB systems

Edit `automation/processor.py` to add custom integrations.

## Project Background

This system was developed as a research prototype to explore how AI can be leveraged to automate network documentation. It uses the Design Science Research Methodology (DSRM) framework.

**Research Question**: "How can AI be leveraged to automate network documentation?"

**Solution Approach**:
- Local LLM for privacy and control
- MCP integration for domain-specific knowledge
- Automated workflow for practical usability
- Version control for tracking changes

## Further Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System architecture deep-dive
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Comprehensive troubleshooting guide
- **[WORKFLOW.md](WORKFLOW.md)** - Visual workflow diagrams
- **[MCP_INTEGRATION_GUIDE.md](MCP_INTEGRATION_GUIDE.md)** - MCP integration details
- **[INDEX.md](INDEX.md)** - Complete documentation index

## Contributing

To extend this system:

1. **Add more MCP tools**: Edit `mcp_server/server-v2.py`
2. **Enhance documentation cache**: Update JSON files in `docs_cache/`
3. **Customize prompts**: Modify `automation/prompts/analysis_template.txt`
4. **Add processors**: Create new scripts in `automation/`
5. **Improve tests**: Add test cases in `tests/`

## License

This project is provided as-is for educational and professional use.

## Support

For issues or questions:
1. Check the [TROUBLESHOOTING.md](TROUBLESHOOTING.md) guide
2. Review your `config.json` settings
3. Verify your LLM is running and accessible
4. Check the console output for error messages
5. Review logs in `logs/mcp_server.log`

---

**Note**: This system is designed for analyzing Cisco switch configurations. It can be adapted for routers, firewalls, or other network devices by modifying the prompt templates and MCP server documentation cache.

**Technology Stack**: Python 3.8+, Local LLM (Ollama/LM Studio), MCP Protocol, Git
