#!/usr/bin/env python3
"""
Setup script for Cisco Configuration Documentation System

Checks prerequisites, installs dependencies, and verifies the system is ready to run.
"""

import sys
import subprocess
import json
from pathlib import Path
import urllib.request
import urllib.error


class Colors:
    """ANSI color codes for terminal output."""
    RESET = '\033[0m'
    BRIGHT = '\033[1m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    CYAN = '\033[36m'


def log(message, color=Colors.RESET):
    """Print colored message."""
    print(f"{color}{message}{Colors.RESET}")


def log_header(message):
    """Print a section header."""
    print()
    log("═" * 55, Colors.CYAN)
    log(f"  {message}", Colors.BRIGHT + Colors.CYAN)
    log("═" * 55, Colors.CYAN)
    print()


def check_python_version():
    """Check Python version."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        log(f"❌ Python {version.major}.{version.minor} is too old. "
            f"Please install Python 3.8 or higher.", Colors.RED)
        sys.exit(1)

    log(f"✅ Python version: {version.major}.{version.minor}.{version.micro}", Colors.GREEN)


def check_config():
    """Check configuration file."""
    config_path = Path("config.json")

    try:
        with open(config_path, 'r') as f:
            config = json.load(f)

        log("✅ Configuration file found", Colors.GREEN)
        log(f"   LLM Endpoint: {config['llm']['endpoint']}", Colors.CYAN)
        log(f"   Model: {config['llm']['model']}", Colors.CYAN)
        log(f"   Git enabled: {config.get('git', {}).get('enabled', True)}", Colors.CYAN)

        return config
    except FileNotFoundError:
        log(f"❌ Error: config.json not found", Colors.RED)
        sys.exit(1)
    except json.JSONDecodeError as e:
        log(f"❌ Error: Invalid JSON in config.json: {e}", Colors.RED)
        sys.exit(1)


def install_dependencies():
    """Install Python dependencies."""
    log_header("Installing Dependencies")

    try:
        log("📦 Installing Python packages from requirements.txt...", Colors.YELLOW)
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        log("✅ Python packages installed", Colors.GREEN)

    except subprocess.CalledProcessError as e:
        log(f"❌ Failed to install dependencies: {e}", Colors.RED)
        log("   Try running manually:", Colors.YELLOW)
        log("   pip install -r requirements.txt", Colors.CYAN)
        sys.exit(1)


def test_llm_connection(config):
    """Test connection to LLM."""
    log_header("Testing LLM Connection")

    endpoint = config["llm"]["endpoint"]
    log(f"🔗 Testing connection to {endpoint}...", Colors.YELLOW)

    # Try to connect to the LLM
    try:
        # Try Ollama API endpoint
        test_url = endpoint.replace('/v1/chat/completions', '/api/tags')

        req = urllib.request.Request(test_url, method='GET')
        req.add_header('Content-Type', 'application/json')

        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                log("✅ LLM server is reachable", Colors.GREEN)
                return True
            else:
                log(f"⚠️  LLM server responded with status: {response.status}", Colors.YELLOW)
                log("   This might be okay if your LLM uses a different health check endpoint",
                    Colors.YELLOW)
                return False

    except urllib.error.URLError as e:
        log(f"⚠️  Could not connect to LLM server: {e.reason}", Colors.YELLOW)
        log(f"   Please ensure your LLM is running at: {endpoint}", Colors.YELLOW)
        log("   Common solutions:", Colors.CYAN)
        log("   - Start Ollama: 'ollama serve'", Colors.CYAN)
        log("   - Start LM Studio and enable local server", Colors.CYAN)
        log("   - Update config.json with correct endpoint", Colors.CYAN)
        return False
    except Exception as e:
        log(f"⚠️  Error testing LLM connection: {e}", Colors.YELLOW)
        return False


def initialize_git(config):
    """Initialize Git repository."""
    if not config.get("git", {}).get("enabled", True):
        log("ℹ️  Git integration is disabled in config.json", Colors.CYAN)
        return

    log_header("Initializing Git")

    try:
        # Check if already a git repo
        result = subprocess.run(
            ["git", "status"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            log("✅ Git repository already initialized", Colors.GREEN)
        else:
            raise subprocess.CalledProcessError(result.returncode, "git status")

    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            log("📦 Initializing Git repository...", Colors.YELLOW)
            subprocess.run(["git", "init"], check=True, capture_output=True)
            log("✅ Git repository initialized", Colors.GREEN)

            log("📝 Creating initial commit...", Colors.YELLOW)
            subprocess.run(["git", "add", "."], check=True, capture_output=True)
            subprocess.run(
                ["git", "commit", "-m", "Initial commit: Cisco Config Documentation System"],
                check=True,
                capture_output=True
            )
            log("✅ Initial commit created", Colors.GREEN)

        except subprocess.CalledProcessError as e:
            log(f"⚠️  Git initialization failed: {e}", Colors.YELLOW)
            log("   You can initialize Git manually later if needed", Colors.YELLOW)
        except FileNotFoundError:
            log("⚠️  Git not found. Install Git or disable in config.json", Colors.YELLOW)


def print_next_steps(config):
    """Print next steps for the user."""
    log_header("Setup Complete! 🎉")

    log("Next steps:", Colors.BRIGHT)
    print()

    log("1. Start the file watcher:", Colors.CYAN)
    log("   python automation/watcher.py", Colors.YELLOW)
    print()

    log("2. Add Cisco configuration files:", Colors.CYAN)
    log("   Place .txt files with 'show running-config' output in:", Colors.YELLOW)
    log("   ./configs/", Colors.YELLOW)
    print()

    log("3. View generated documentation:", Colors.CYAN)
    log("   Check the ./output/ folder for markdown files", Colors.YELLOW)
    print()

    if not config.get("git", {}).get("enabled", True):
        log("💡 Tip: Enable Git in config.json to track documentation changes", Colors.CYAN)
        print()

    log("📚 Documentation:", Colors.CYAN)
    log("   README.md - Full documentation", Colors.YELLOW)
    log("   QUICKSTART.md - Quick start guide", Colors.YELLOW)
    print()

    log("🧪 Test with sample configuration:", Colors.CYAN)
    log("   A sample config is in configs/SAMPLE-SWITCH.txt", Colors.YELLOW)
    log("   Start the watcher to process it automatically!", Colors.YELLOW)
    print()


def main():
    """Main setup function."""
    print("\033[2J\033[H")  # Clear screen

    log_header("Cisco Configuration Documentation System - Setup")

    log("This script will set up your system by:", Colors.CYAN)
    log("  ✓ Checking Python version", Colors.YELLOW)
    log("  ✓ Installing dependencies", Colors.YELLOW)
    log("  ✓ Verifying configuration", Colors.YELLOW)
    log("  ✓ Testing LLM connection", Colors.YELLOW)
    log("  ✓ Initializing Git (if enabled)", Colors.YELLOW)
    print()

    try:
        # Check Python version
        log_header("Checking Prerequisites")
        check_python_version()

        # Check configuration
        config = check_config()

        # Install dependencies
        install_dependencies()

        # Test LLM connection
        test_llm_connection(config)

        # Initialize Git
        initialize_git(config)

        # Print next steps
        print_next_steps(config)

        log("═" * 55, Colors.GREEN)
        log("  Setup completed successfully! ✅", Colors.BRIGHT + Colors.GREEN)
        log("═" * 55, Colors.GREEN)
        print()

    except KeyboardInterrupt:
        print()
        log("Setup cancelled by user", Colors.YELLOW)
        sys.exit(1)
    except Exception as e:
        print()
        log("═" * 55, Colors.RED)
        log("  Setup failed ❌", Colors.BRIGHT + Colors.RED)
        log("═" * 55, Colors.RED)
        print()
        log(f"Error: {str(e)}", Colors.RED)
        sys.exit(1)


if __name__ == "__main__":
    main()