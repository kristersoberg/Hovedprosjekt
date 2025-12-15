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
import asyncio
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List
from git import Repo, InvalidGitRepositoryError

from mcp_client import CiscoMCPClient


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
            print(f" Error: config.json not found at {config_path}")
            print("   Make sure config.json exists in the project root")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f" Error: Invalid JSON in config.json: {e}")
            sys.exit(1)

        # Ensure output directory exists
        self.output_dir.mkdir(exist_ok=True)

        # MCP server path
        self.mcp_server_path = self.project_root / self.config.get("mcp", {}).get("server_path", "mcp_server/server.py")

    def process(self) -> Path:
        """Process the configuration file and generate documentation."""
        try:
            print(" Reading configuration file...")
            config_content = self._read_config_file()

            print(" Extracting IOS version...")
            ios_version = self._extract_ios_version(config_content)
            print(f"   Detected IOS version: {ios_version or 'Unknown'}")

            print(" Loading prompt template...")
            prompt = self._build_prompt(config_content, ios_version)

            # Enrich prompt with MCP documentation if enabled
            if self.config.get("mcp", {}).get("enabled", True):
                print(" Enriching with Cisco documentation from MCP server...")
                prompt = asyncio.run(self._enrich_prompt_with_mcp(config_content, ios_version, prompt))

            print(" Sending to LLM for analysis...")
            documentation = self._call_llm(prompt)

            print(" Saving documentation...")
            output_path = self._save_documentation(documentation)

            if self.config.get("git", {}).get("enabled", True):
                print(" Committing to Git...")
                self._commit_to_git(output_path)

            print(f" Documentation generated: {output_path}")
            return output_path

        except Exception as e:
            print(f" Processing failed: {str(e)}")
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
            print("  Prompt template not found, using default")
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

    def _extract_commands_from_config(self, config_content: str) -> List[str]:
        """
        Extract unique Cisco commands from configuration.

        Returns list of command keywords found in the config.
        """
        # Common Cisco commands to look for
        common_commands = [
            'interface', 'vlan', 'ip address', 'switchport', 'spanning-tree',
            'router', 'access-list', 'line', 'enable secret', 'hostname',
            'trunk', 'channel-group', 'vtp', 'port-channel'
        ]

        found_commands = set()
        config_lower = config_content.lower()

        for cmd in common_commands:
            if cmd in config_lower:
                found_commands.add(cmd)

        return list(found_commands)

    def _extract_features_from_config(self, config_content: str) -> List[str]:
        """
        Extract Cisco features being used in the configuration.

        Returns list of features found.
        """
        features = []
        config_lower = config_content.lower()

        # Check for various features
        if 'vlan' in config_lower:
            features.append('VLAN')
        if 'spanning-tree' in config_lower:
            features.append('STP')
        if 'router ospf' in config_lower:
            features.append('OSPF')
        if 'router eigrp' in config_lower:
            features.append('EIGRP')
        if 'vtp' in config_lower:
            features.append('VTP')
        if 'channel-group' in config_lower or 'port-channel' in config_lower:
            features.append('EtherChannel')

        return features

    async def _enrich_prompt_with_mcp(self, config_content: str, ios_version: Optional[str], prompt: str) -> str:
        """
        Enrich the prompt with relevant Cisco documentation from MCP server.

        Args:
            config_content: The configuration file content
            ios_version: Detected IOS version
            prompt: Original prompt

        Returns:
            Enriched prompt with documentation context
        """
        try:
            # Extract commands and features from config
            commands = self._extract_commands_from_config(config_content)
            features = self._extract_features_from_config(config_content)

            print(f"   Found {len(commands)} commands and {len(features)} features")

            # Get MCP configuration limits
            mcp_config = self.config.get("mcp", {})
            max_commands = mcp_config.get("max_commands", 3)
            max_features = mcp_config.get("max_features", 2)
            debug_mode = mcp_config.get("debug", False)

            # Connect to MCP server and fetch documentation
            client = CiscoMCPClient(self.mcp_server_path, debug=debug_mode)

            documentation_context = []

            async with client.connect():
                print("   Connected to MCP server")

                # Fetch command documentation (limit based on config)
                important_commands = commands[:max_commands]
                for cmd in important_commands:
                    print(f"   Fetching docs for command: {cmd}")
                    result = await client.search_command(cmd, ios_version)
                    if result["success"]:
                        # Trim the documentation to keep only essential info
                        doc_data = result['data']
                        # Limit each doc to ~500 characters
                        if len(doc_data) > 500:
                            doc_data = doc_data[:500] + "..."
                        documentation_context.append(f"### Command: {cmd}\n{doc_data}\n")

                # Fetch feature documentation (limit based on config)
                important_features = features[:max_features]
                for feature in important_features:
                    print(f"   Fetching docs for feature: {feature}")
                    result = await client.get_feature_docs(feature, ios_version)
                    if result["success"]:
                        # Trim feature docs too
                        doc_data = result['data']
                        if len(doc_data) > 800:
                            doc_data = doc_data[:800] + "..."
                        documentation_context.append(f"### Feature: {feature}\n{doc_data}\n")

            # Build enriched prompt
            if documentation_context:
                docs_section = "\n\n".join(documentation_context)

                # Create enriched prompt
                enriched_prompt = f"""{prompt}

## CISCO DOCUMENTATION REFERENCE

The following Cisco IOS documentation has been retrieved to help you understand the commands and features in this configuration:

{docs_section}

Use this documentation to provide accurate explanations and best practices in your analysis.
"""

                # Check if enriched prompt is too large (rough estimate)
                # Ollama models typically handle 4k-128k tokens depending on model
                # 1 token ≈ 4 characters, so we'll limit to ~100k characters for safety
                max_prompt_size = mcp_config.get("max_prompt_size", 100000)  # About 25k tokens, safe for most 8B models

                if len(enriched_prompt) > max_prompt_size:
                    print(f"   Warning: Enriched prompt too large ({len(enriched_prompt)} chars)")
                    print(f"   Reducing documentation to prevent GPU memory issues...")

                    # Use only the first 2-3 most important docs
                    reduced_docs = documentation_context[:min(3, len(documentation_context))]
                    docs_section = "\n\n".join(reduced_docs)

                    enriched_prompt = f"""{prompt}

## CISCO DOCUMENTATION REFERENCE (Summary)

Key Cisco documentation for this configuration:

{docs_section}

Use this documentation to provide accurate explanations.
"""
                    print(f"   Reduced to {len(reduced_docs)} documentation sections")

                    # If still too large, fall back to original prompt
                    if len(enriched_prompt) > max_prompt_size:
                        print(f"   Still too large, using original prompt without MCP docs")
                        return prompt

                print(f"   Added {len(documentation_context)} documentation sections to prompt")
                print(f"   Total prompt size: {len(enriched_prompt)} characters")
                return enriched_prompt
            else:
                print("   No documentation retrieved, using original prompt")
                return prompt

        except Exception as e:
            print(f"   Warning: Failed to enrich with MCP docs: {str(e)}")
            print("   Continuing with original prompt...")
            return prompt

    def _call_llm(self, prompt: str) -> str:
        """Call the LLM API."""
        llm_config = self.config["llm"]
        endpoint = llm_config["endpoint"]

        try:
            # Detect if using Ollama native API or OpenAI-compatible API
            if "/api/generate" in endpoint or "/api/chat" in endpoint:
                # Ollama native API format
                system_prompt = ("You are an expert Cisco network engineer. Analyze the configuration "
                               "and create comprehensive documentation in Markdown format.")

                full_prompt = f"{system_prompt}\n\n{prompt}"

                request_data = {
                    "model": llm_config["model"],
                    "prompt": full_prompt,
                    "stream": False,
                    "options": {
                        "temperature": llm_config.get("temperature", 0.7),
                        "num_predict": llm_config.get("max_tokens", 8000)
                    }
                }

                # Debug output
                print(f"   Sending request to Ollama:")
                print(f"   - Endpoint: {endpoint}")
                print(f"   - Model: {llm_config['model']}")
                print(f"   - Prompt size: {len(full_prompt)} characters")
                print(f"   - Max tokens to generate: {llm_config.get('max_tokens', 8000)}")

            else:
                # OpenAI-compatible API format
                request_data = {
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
                }

            response = requests.post(
                endpoint,
                json=request_data,
                headers={
                    "Content-Type": "application/json",
                    **({"Authorization": f"Bearer {llm_config['api_key']}"} if llm_config.get("api_key") else {})
                },
                timeout=llm_config.get("timeout", 300000) / 1000  # Convert ms to seconds
            )

            response.raise_for_status()
            data = response.json()

            # Extract content based on response format
            # Ollama native /api/generate format
            if "response" in data:
                content = data["response"]
            # OpenAI-compatible format
            elif "choices" in data and len(data["choices"]) > 0:
                content = data["choices"][0]["message"]["content"]
            # Ollama /api/chat format
            elif "message" in data and "content" in data["message"]:
                content = data["message"]["content"]
            else:
                raise ValueError("Unexpected LLM response format")

            # Debug: Show response length
            print(f"   LLM response length: {len(content)} characters")
            if len(content) == 0:
                print("   WARNING: LLM returned empty response!")

            return content

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
            print(f"    Committed: {relative_path}")

            # Push if configured
            if git_config.get("auto_push") and git_config.get("remote"):
                try:
                    remote = repo.remote(git_config["remote"])
                    branch = git_config.get("branch", "main")
                    print(f"   Pushing to {git_config['remote']}/{branch}...")
                    remote.push(branch)
                    print("    Pushed to remote")
                except Exception as e:
                    print(f"     Push failed: {str(e)}")

        except Exception as e:
            print(f"     Git commit failed: {str(e)}")
            # Don't fail the entire process if git fails


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print(" Usage: python processor.py <config-file-path>")
        sys.exit(1)

    config_file_path = Path(sys.argv[1])

    if not config_file_path.exists():
        print(f" Error: Configuration file not found: {config_file_path}")
        sys.exit(1)

    processor = ConfigProcessor(config_file_path)
    processor.process()


if __name__ == "__main__":
    main()