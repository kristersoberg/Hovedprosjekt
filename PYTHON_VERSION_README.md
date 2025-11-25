# Cisco Configuration Documentation System (Python Version)

An automated system that uses a local LLM to interpret Cisco switch configurations and generate comprehensive, human-readable documentation with version control.

> **Note**: This is the **Python version** of the system. All components have been rewritten in Python for easier deployment and better cross-platform compatibility.

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure your LLM (edit config.json)

# 3. Start the watcher
python automation/watcher.py

# 4. Add config files to configs/ folder
# Documentation automatically generated in output/
```

## ✨ Features

- ✅ **Automated Processing** - File watcher detects changes automatically
- ✅ **Local & Private** - All processing happens on your computer
- ✅ **MCP Integration** - LLM can look up Cisco documentation
- ✅ **Version Control** - Git tracks all documentation changes
- ✅ **Best Practices Analysis** - Evaluates configs against Cisco standards
- ✅ **Pure Python** - No Node.js required, easy virtual environment setup
- ✅ **Cross-Platform** - Works on Windows, Linux, and macOS

## 📦 Installation

### Prerequisites

- **Python 3.8+** ([download](https://www.python.org/downloads/))
- **Local LLM** (Ollama, LM Studio, etc.)
- **Git** (optional, for version control)

### Install

```bash
# Option 1: Using pip
pip install -r requirements.txt

# Option 2: Using virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Option 3: Using the setup script
python setup.py
```

## ⚙️ Configuration

Edit [config.json](config.json):

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
    "server_path": "./mcp_server/server.py",
    "enabled": true
  },
  "git": {
    "enabled": true,
    "auto_push": false,
    "remote": "origin",
    "branch": "main"
  }
}
```

## 🎯 Usage

### Automatic Mode (Recommended)

Start the file watcher to automatically process configs:

```bash
python automation/watcher.py
```

Add `.txt` files to the `configs/` directory and they'll be processed automatically.

### Manual Mode

Process a single configuration file:

```bash
python automation/processor.py configs/your-switch.txt
```

### Batch Processing

Process multiple files:

```bash
python automation/processor.py configs/*.txt
```

## 📁 Project Structure

```
.
├── automation/              # Processing automation
│   ├── watcher.py          # File watcher
│   ├── processor.py        # Configuration processor
│   └── prompts/            # LLM prompt templates
│       └── analysis_template.txt
├── mcp_server/             # MCP server for Cisco docs
│   └── server.py
├── configs/                # Input: Cisco configurations
│   └── SAMPLE-SWITCH.txt
├── output/                 # Output: Generated documentation
├── docs_cache/            # Cached Cisco documentation
├── requirements.txt        # Python dependencies
├── pyproject.toml         # Python project configuration
├── config.json            # System configuration
└── setup.py               # Automated setup script
```

## 🔧 Python Components

### File Watcher ([automation/watcher.py](automation/watcher.py))

Monitors the `configs/` directory using the `watchdog` library:

```python
# Run with:
python automation/watcher.py
```

### Processor ([automation/processor.py](automation/processor.py))

Processes configurations and generates documentation:

```python
# Run with:
python automation/processor.py <config-file>
```

### MCP Server ([mcp_server/server.py](mcp_server/server.py))

Provides Cisco documentation to the LLM:

```python
# Run with:
python mcp_server/server.py
```

## 📚 Dependencies

Core Python packages:

- **requests** (2.31.0+) - HTTP requests to LLM API
- **watchdog** (3.0.0+) - File system monitoring
- **GitPython** (3.1.40+) - Git integration
- **mcp** (0.9.0+) - Model Context Protocol support

Install all with:

```bash
pip install -r requirements.txt
```

## 🎓 Virtual Environment Setup

**Recommended for development:**

```bash
# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the system
python automation/watcher.py
```

## 🔄 How It Works

1. **File Detection**: Watchdog monitors `configs/` for `.txt` files
2. **Processing**: Processor extracts IOS version and builds prompt
3. **LLM Analysis**: Sends config to local LLM via HTTP API
4. **MCP Tools**: LLM queries MCP server for Cisco documentation
5. **Documentation**: Generates structured markdown
6. **Version Control**: Git commits the documentation
7. **Output**: Markdown saved to `output/`

## 🤖 MCP Server

The MCP server provides these tools to the LLM:

1. **search_command** - Look up Cisco IOS commands
2. **get_feature_docs** - Get feature documentation (VLAN, OSPF, STP, etc.)
3. **validate_syntax** - Validate command syntax
4. **explain_config_section** - Explain configuration blocks

Documentation is cached in `docs_cache/basic_commands.json`.

## 🛠️ Development

### Running Tests

```bash
# Install dev dependencies
pip install -r requirements.txt

# Run tests (when available)
pytest
```

### Code Formatting

```bash
# Format code with black
pip install black
black automation/ mcp_server/
```

### Type Checking

```bash
# Type check with mypy
pip install mypy
mypy automation/ mcp_server/
```

## 📊 Recommended LLM Models

| Model | RAM Required | Quality | Speed |
|-------|-------------|---------|-------|
| Llama 3.1 8B | 8GB | Good | Fast |
| Llama 3.1 70B | 48GB+ | Excellent | Slow |
| Mistral 7B | 8GB | Good | Fast |
| Mixtral 8x7B | 24GB | Very Good | Medium |

## 🔐 Security

- ✅ All processing is **local** (no cloud)
- ✅ No data sent to external APIs
- ✅ Configuration files may contain sensitive info - keep private
- ✅ Use `.gitignore` to exclude sensitive files
- ✅ Review documentation before sharing

## 🆘 Troubleshooting

### Import Error: Module not found

```bash
# Make sure dependencies are installed
pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.8+
```

### LLM Connection Failed

```bash
# Check if LLM is running
curl http://localhost:11434/api/version  # Ollama

# Verify endpoint in config.json
# Make sure firewall allows localhost connections
```

### Permission Denied (Linux/Mac)

```bash
# Make scripts executable
chmod +x automation/watcher.py
chmod +x automation/processor.py
chmod +x mcp_server/server.py
```

### Git Errors

```bash
# Initialize git
git init

# Configure user
git config user.name "Your Name"
git config user.email "your@email.com"

# Or disable in config.json
"git": {"enabled": false}
```

## 📖 Documentation

- **[README.md](README.md)** - Complete documentation
- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute setup guide
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Technical deep-dive
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Problem-solving guide
- **[WORKFLOW.md](WORKFLOW.md)** - Visual workflow diagrams

## 🎯 Use Cases

1. **Network Documentation** - Auto-generate docs for all switches
2. **Configuration Review** - Analyze configs for best practices
3. **Knowledge Transfer** - Create guides for new team members
4. **Compliance & Audit** - Track configuration changes
5. **Troubleshooting** - Understand current network state

## 🔄 Migrating from Node.js Version

If you used the previous Node.js version:

1. **Remove Node.js components** (already done if you're using this version)
2. **Install Python dependencies**: `pip install -r requirements.txt`
3. **Update scripts**:
   - `npm start` → `python automation/watcher.py`
   - `node processor.js` → `python automation/processor.py`
4. **Configuration**: `config.json` format is the same

## 📝 License

This project is provided as-is for educational and professional use.

## 🤝 Contributing

Contributions welcome! Areas for improvement:

- Additional Cisco command documentation
- Support for other network vendors
- Enhanced prompt templates
- Additional MCP tools
- Web UI for easier management

## ⭐ Highlights

### Why Python?

- ✅ **Easier Deployment** - Single language, no Node.js required
- ✅ **Virtual Environments** - Better dependency isolation
- ✅ **Native Libraries** - Better integration with system tools
- ✅ **Simpler** - Fewer moving parts
- ✅ **Cross-Platform** - Works everywhere Python works

### Key Improvements

- Simplified installation process
- Better error handling
- Cleaner code structure
- Native async support for MCP server
- Type hints for better IDE support

---

**Ready to start?** See [QUICKSTART.md](QUICKSTART.md) for a 5-minute setup guide!