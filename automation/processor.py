#!/usr/bin/env python3
"""
Configuration Processor

Processes Cisco configuration files and generates human-readable documentation
using a local LLM.
"""

import sys
import json
import re
import requests
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any
from git import Repo, InvalidGitRepositoryError


class ConfigProcessor:
    """Process Cisco configuration files."""

    def __init__(self, config_file_path: Path):
        self.config_file_path = Path(config_file_path)
        self.config_filename = self.config_file_path.name

        # Determine project paths
        self.project_root = self.config_file_path.parent.parent
        self.output_dir = self.project_root / "output"
        self.prompts_dir = Path(__file__).parent / "prompts"

        # Load system configuration
        config_path = self.project_root / "config.json"
        try:
            with open(config_path, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print(f"❌ Error: config.json not found at {config_path}")
            print("   Make sure config.json exists in the project root")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"❌ Error: Invalid JSON in config.json: {e}")
            sys.exit(1)

        # Ensure output directory exists
        self.output_dir.mkdir(exist_ok=True)

    def process(self) -> Path:
        """Process the configuration file and generate documentation."""
        try:
            print("📖 Reading configuration file...")
            config_content = self._read_config_file()

            print("🔍 Extracting IOS version...")
            ios_version = self._extract_ios_version(config_content)
            print(f"   Detected IOS version: {ios_version or 'Unknown'}")

            print("📋 Loading prompt template...")
            prompt = self._build_prompt(config_content, ios_version)

            print("🤖 Sending to LLM for analysis...")
            documentation = self._call_llm(prompt)

            print("💾 Saving documentation...")
            output_path = self._save_documentation(documentation)

            if self.config.get("git", {}).get("enabled", True):
                print("📦 Committing to Git...")
                self._commit_to_git(output_path)

            print(f"✅ Documentation generated: {output_path}")
            return output_path

        except Exception as e:
            print(f"❌ Processing failed: {str(e)}")
            raise

    def _read_config_file(self) -> str:
        """Read the configuration file."""
        try:
            with open(self.config_file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            # Try with different encoding
            with open(self.config_file_path, 'r', encoding='latin-1') as f:
                return f.read()

    def _extract_ios_version(self, config_content: str) -> Optional[str]:
        """Extract IOS version from configuration."""
        patterns = [
            r'Cisco IOS Software.*Version ([0-9.()A-Z]+)',
            r'IOS.*Version ([0-9.]+)',
            r'^version ([0-9.]+)',
        ]

        for pattern in patterns:
            match = re.search(pattern, config_content, re.IGNORECASE | re.MULTILINE)
            if match:
                return match.group(1)

        return None

    def _build_prompt(self, config_content: str, ios_version: Optional[str]) -> str:
        """Build the LLM prompt from template."""
        template_path = self.prompts_dir / "analysis_template.txt"

        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                template = f.read()
        except FileNotFoundError:
            print("⚠️  Prompt template not found, using default")
            template = self._get_default_template()

        # Replace placeholders
        prompt = template.replace('{{CONFIG_CONTENT}}', config_content)
        prompt = prompt.replace('{{IOS_VERSION}}', ios_version or 'Unknown')
        prompt = prompt.replace('{{FILENAME}}', self.config_filename)
        prompt = prompt.replace('{{TIMESTAMP}}', datetime.now().isoformat())

        return prompt

    def _get_default_template(self) -> str:
        """Get default prompt template."""
        return """You are a Cisco network engineer analyzing a switch configuration file. Your task is to create comprehensive, human-readable documentation.

Configuration File: {{FILENAME}}
IOS Version: {{IOS_VERSION}}

CONFIGURATION:
```
{{CONFIG_CONTENT}}
```

Please analyze this configuration and create detailed documentation in Markdown format following this structure:

# Switch Configuration Documentation: {{FILENAME}}

## Overview
- **Hostname**: [Extract hostname]
- **IOS Version**: {{IOS_VERSION}}
- **Configuration Purpose**: [Brief description of switch role]

## VLANs
List all configured VLANs with their names and purposes.

## Interfaces
Document all interface configurations, including:
- Physical interfaces
- Port-channels
- VLANs (SVIs)

## Routing
Document routing configuration (OSPF, EIGRP, static routes, etc.)

## Spanning Tree
Document STP configuration and settings.

## Security Features
Document security configurations (port security, ACLs, etc.)

## Services
Document configured services (DHCP, NTP, SNMP, etc.)

## Best Practices Analysis
Evaluate against Cisco best practices and provide recommendations.

---
*Documentation generated automatically on {{TIMESTAMP}}*
"""

    def _call_llm(self, prompt: str) -> str:
        """Call the LLM API."""
        llm_config = self.config["llm"]

        try:
            response = requests.post(
                llm_config["endpoint"],
                json={
                    "model": llm_config["model"],
                    "messages": [
                        {
                            "role": "system",
                            "content": "You are an expert Cisco network engineer. You have access to Cisco "
                                     "documentation via MCP tools. Use them to verify command syntax and features "
                                     "when analyzing configurations."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "temperature": llm_config.get("temperature", 0.7),
                    "max_tokens": llm_config.get("max_tokens", 8000)
                },
                headers={
                    "Content-Type": "application/json",
                    **({"Authorization": f"Bearer {llm_config['api_key']}"} if llm_config.get("api_key") else {})
                },
                timeout=llm_config.get("timeout", 300000) / 1000  # Convert ms to seconds
            )

            response.raise_for_status()
            data = response.json()

            # Extract content based on response format
            # OpenAI-compatible format
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
            # Ollama format
            elif "message" in data and "content" in data["message"]:
                return data["message"]["content"]
            # Generic fallback
            elif "response" in data:
                return data["response"]
            else:
                raise ValueError("Unexpected LLM response format")

        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                error_msg = f"LLM API error: {e.response.status_code}"
                try:
                    error_data = e.response.json()
                    if "error" in error_data:
                        error_msg += f" - {error_data['error'].get('message', str(error_data['error']))}"
                except:
                    error_msg += f" - {e.response.text}"
                raise Exception(error_msg)
            else:
                raise Exception(f"LLM API request failed: {str(e)}. "
                              f"Check if the LLM server is running at {llm_config['endpoint']}")

    def _save_documentation(self, documentation: str) -> Path:
        """Save the generated documentation."""
        # Generate output filename
        output_filename = self.config_filename.replace('.txt', '.md')
        output_path = self.output_dir / output_filename

        # Write documentation
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(documentation)

        return output_path

    def _commit_to_git(self, output_path: Path):
        """Commit the documentation to Git."""
        git_config = self.config.get("git", {})

        if not git_config.get("enabled", True):
            print("   Git integration disabled in config")
            return

        try:
            # Open or initialize repository
            try:
                repo = Repo(self.project_root)
            except InvalidGitRepositoryError:
                print("   Initializing Git repository...")
                repo = Repo.init(self.project_root)

                # Create .gitignore if it doesn't exist
                gitignore_path = self.project_root / ".gitignore"
                if not gitignore_path.exists():
                    with open(gitignore_path, 'w') as f:
                        f.write("__pycache__/\n*.pyc\n*.log\n.DS_Store\n"
                               "docs_cache/*.html\n.env\n.venv/\nvenv/\n")
                    repo.index.add([str(gitignore_path)])

            # Add the output file
            relative_path = output_path.relative_to(self.project_root)
            repo.index.add([str(relative_path)])

            # Create commit message
            timestamp = datetime.now().isoformat()
            commit_message = f"""Update documentation: {self.config_filename}

Generated from: {self.config_filename}
Timestamp: {timestamp}
Auto-generated by Cisco Config Documentation System"""

            # Commit
            repo.index.commit(commit_message)
            print(f"   ✅ Committed: {relative_path}")

            # Push if configured
            if git_config.get("auto_push") and git_config.get("remote"):
                try:
                    remote = repo.remote(git_config["remote"])
                    branch = git_config.get("branch", "main")
                    print(f"   Pushing to {git_config['remote']}/{branch}...")
                    remote.push(branch)
                    print("   ✅ Pushed to remote")
                except Exception as e:
                    print(f"   ⚠️  Push failed: {str(e)}")

        except Exception as e:
            print(f"   ⚠️  Git commit failed: {str(e)}")
            # Don't fail the entire process if git fails


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("❌ Usage: python processor.py <config-file-path>")
        sys.exit(1)

    config_file_path = Path(sys.argv[1])

    if not config_file_path.exists():
        print(f"❌ Error: Configuration file not found: {config_file_path}")
        sys.exit(1)

    processor = ConfigProcessor(config_file_path)
    processor.process()


if __name__ == "__main__":
    main()