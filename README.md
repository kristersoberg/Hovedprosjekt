# Cisco Configuration Documentation System

An automated system that uses a local LLM to interpret Cisco switch configurations and generate comprehensive, human-readable documentation with version control.

## Features

- 🤖 **Automated Processing**: File watcher automatically detects new/changed configuration files
- 📚 **MCP Server**: Provides LLM access to Cisco IOS documentation for accurate interpretation
- 🔍 **IOS Version Detection**: Automatically extracts IOS version from configurations
- 📝 **Structured Documentation**: Generates detailed markdown documentation following best practices
- 🔄 **Version Control**: Automatic Git commits for documentation changes
- 🎯 **Best Practices Analysis**: Evaluates configurations against Cisco recommendations

## Project Structure

```
.
├── configs/              # Input: Place Cisco running-config .txt files here
├── output/               # Output: Generated markdown documentation
├── docs_cache/           # Cached Cisco IOS documentation
├── mcp-server/           # MCP server for Cisco documentation access
│   ├── server.js
│   └── package.json
├── automation/           # Main automation scripts
│   ├── watcher.js        # File monitoring service
│   ├── processor.js      # Configuration processor
│   ├── prompts/          # LLM prompt templates
│   │   └── analysis_template.txt
│   └── package.json
├── config.json           # System configuration
├── .gitignore
└── README.md
```

## Prerequisites

- **Node.js** 18.0.0 or higher
- **Local LLM** (e.g., Ollama, LM Studio, etc.)
- **Git** (optional, for version control features)

## Installation

### 1. Install Dependencies

Install dependencies for both the MCP server and automation system:

```bash
cd mcp-server
npm install
cd ../automation
npm install
cd ..
```

### 2. Configure Your LLM

Edit `config.json` to match your local LLM setup:

```json
{
  "llm": {
    "endpoint": "http://localhost:11434/v1/chat/completions",
    "model": "llama3.1:8b",
    "api_key": "",
    "temperature": 0.7,
    "max_tokens": 8000,
    "timeout": 300000
  }
}
```

**Common LLM Endpoints:**
- **Ollama**: `http://localhost:11434/v1/chat/completions`
- **LM Studio**: `http://localhost:1234/v1/chat/completions`
- **Text Generation WebUI**: `http://localhost:5000/v1/chat/completions`

### 3. Configure the MCP Server for Your LLM

Your local LLM needs to be configured to connect to the MCP server. The exact method depends on your LLM platform:

#### For Ollama with MCP Support:
Create or edit your MCP configuration file (location varies by LLM):

```json
{
  "mcpServers": {
    "cisco-docs": {
      "command": "node",
      "args": ["G:\\Fagskolen Hovedfagsprosjekt Lokal\\mcp-server\\server.js"],
      "env": {}
    }
  }
}
```

#### For LM Studio:
Check LM Studio's MCP integration documentation for configuration steps.

**Note**: Not all local LLMs support MCP yet. If your LLM doesn't support MCP, the system will still work, but the LLM won't have access to the Cisco documentation tools. Consider using a model that supports tool/function calling for best results.

## Usage

### Starting the System

1. **Start the file watcher**:
   ```bash
   cd automation
   npm start
   ```

2. **Add or modify configuration files**:
   - Place `.txt` files containing Cisco `show running-config` output in the `configs/` folder
   - The system will automatically detect and process them

### Manual Processing

To process a single configuration file manually:

```bash
cd automation
node processor.js "../configs/your-config.txt"
```

### Output

Generated documentation will be saved in the `output/` folder as markdown files with the same name as the input configuration file.

Example:
- Input: `configs/CORE-SW-01.txt`
- Output: `output/CORE-SW-01.md`

## Configuration Options

### config.json

```json
{
  "llm": {
    "endpoint": "http://localhost:11434/v1/chat/completions",
    "model": "llama3.1:8b",
    "api_key": "",
    "temperature": 0.7,
    "max_tokens": 8000,
    "timeout": 300000
  },
  "mcp": {
    "server_path": "./mcp-server/server.js",
    "enabled": true
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

**Options Explained:**

- **llm.endpoint**: Your local LLM API endpoint
- **llm.model**: The model name to use
- **llm.api_key**: API key if required (leave empty for Ollama)
- **llm.temperature**: LLM creativity (0.0-1.0, lower = more deterministic)
- **llm.max_tokens**: Maximum response length
- **llm.timeout**: Request timeout in milliseconds

- **mcp.enabled**: Enable/disable MCP server integration
- **mcp.server_path**: Path to MCP server script

- **git.enabled**: Enable/disable Git integration
- **git.auto_push**: Automatically push commits to remote
- **git.remote**: Git remote name
- **git.branch**: Git branch to commit to

## MCP Server

The MCP server provides the following tools to the LLM:

### Available Tools

1. **search_command**: Look up Cisco IOS command documentation
   ```javascript
   search_command({ command: "interface", ios_version: "15.2" })
   ```

2. **get_feature_docs**: Get documentation for Cisco features
   ```javascript
   get_feature_docs({ feature: "VLAN", ios_version: "15.2" })
   ```

3. **validate_syntax**: Validate command syntax
   ```javascript
   validate_syntax({ command: "ip address 192.168.1.1 255.255.255.0", context: "interface" })
   ```

4. **explain_config_section**: Get explanations for configuration blocks
   ```javascript
   explain_config_section({ config_block: "router ospf 1\n network 10.0.0.0 0.255.255.255 area 0" })
   ```

### Extending Documentation

To add more command documentation, edit:
```
docs_cache/basic_commands.json
```

The MCP server can be extended to fetch documentation from Cisco's website or other sources.

## Workflow

1. **File Detection**: Watcher detects new/changed `.txt` file in `configs/`
2. **IOS Version Extraction**: System extracts IOS version from configuration
3. **Prompt Generation**: Creates detailed analysis prompt with configuration content
4. **LLM Analysis**: LLM analyzes configuration using MCP tools for documentation lookup
5. **Documentation Generation**: LLM generates structured markdown documentation
6. **Save Output**: Documentation saved to `output/` folder
7. **Git Commit**: Changes automatically committed (if Git enabled)

## Customizing Documentation Format

Edit the prompt template to customize the output:
```
automation/prompts/analysis_template.txt
```

The template uses placeholders:
- `{{CONFIG_CONTENT}}`: The configuration file content
- `{{IOS_VERSION}}`: Detected IOS version
- `{{FILENAME}}`: Configuration filename

## Troubleshooting

### LLM Connection Issues

**Problem**: "LLM API request failed: ECONNREFUSED"

**Solution**:
- Ensure your LLM server is running
- Verify the endpoint URL in `config.json`
- Check if the port is correct (Ollama default: 11434)

### MCP Server Not Working

**Problem**: LLM doesn't use Cisco documentation

**Solution**:
- Verify your LLM supports MCP (Model Context Protocol)
- Check MCP server configuration in your LLM's settings
- Test MCP server manually: `node mcp-server/server.js`

### File Watcher Not Detecting Changes

**Problem**: New files in `configs/` are not processed

**Solution**:
- Ensure the watcher is running: `cd automation && npm start`
- Check file extension is `.txt`
- Verify file permissions

### Git Errors

**Problem**: Git commits failing

**Solution**:
- Initialize Git repository: `git init`
- Configure Git user: `git config user.name "Your Name"` and `git config user.email "your@email.com"`
- Or disable Git in `config.json`: `"git.enabled": false`

## Recommended LLM Models

For best results, use models with:
- Good instruction following
- Support for long context (8K+ tokens)
- Tool/function calling capabilities
- Technical knowledge

**Recommended models:**
- Llama 3.1 (8B or 70B)
- Mistral (7B or larger)
- Mixtral 8x7B
- CodeLlama
- Qwen 2.5

## Performance Tips

1. **Use appropriate model size**: Larger models provide better analysis but are slower
2. **Adjust max_tokens**: Reduce for faster processing, increase for detailed docs
3. **Configure temperature**: Lower (0.3-0.5) for more consistent output
4. **Batch processing**: Process multiple configs during off-hours

## Version Control

The system automatically creates Git commits for each documentation update:

```
commit 3a8f4b2
Author: System
Date:   Mon Nov 25 14:30:00 2024

    Update documentation: CORE-SW-01.txt

    Generated from: CORE-SW-01.txt
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
- The system will note security concerns in the "Best Practices Analysis" section

## Contributing

To extend this system:

1. **Add more MCP tools**: Edit `mcp-server/server.js`
2. **Enhance documentation**: Update `docs_cache/basic_commands.json`
3. **Customize prompts**: Modify `automation/prompts/analysis_template.txt`
4. **Add processors**: Create new scripts in `automation/`

## License

This project is provided as-is for educational and professional use.

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review your `config.json` settings
3. Verify your LLM is running and accessible
4. Check the console output for error messages

---

**Note**: This system is designed for analyzing Cisco switch configurations. It can be adapted for routers, firewalls, or other network devices by modifying the prompt templates and MCP server documentation.