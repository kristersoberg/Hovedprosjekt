#!/usr/bin/env python3
"""
Configuration Processor

Processes Cisco configuration files and generates human-readable documentation
using a local LLM.
"""

import sys
import json
import re
import time
import requests
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List
from git import Repo, InvalidGitRepositoryError

from config_parser import parse_config_to_json
from structured_prompt_builder import StructuredPromptBuilder
from validator import DocumentationValidator
from logger import init_logger, get_logger
from metrics_tracker import init_metrics, get_metrics


class ConfigProcessor:
    """Process Cisco configuration files."""

    def __init__(self, config_file_path: Path, dry_run: bool = False):
        self.config_file_path = Path(config_file_path)
        self.config_filename = self.config_file_path.name
        self.dry_run = dry_run

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

        # Initialize logging
        log_config = self.config.get("logging", {})
        if log_config.get("enabled", True):
            log_dir = self.project_root / log_config.get("log_dir", "logs")
            verbose = log_config.get("verbose", False)
            debug = log_config.get("debug", False)
            self.logger = init_logger(log_dir, verbose=verbose, debug=debug)
        else:
            self.logger = None

        # Ensure output directory exists
        self.output_dir.mkdir(exist_ok=True)

        # Initialize token usage tracking
        self.last_token_usage = None

        # Initialize metrics tracker (if available)
        self.metrics_tracker = get_metrics()

    def _validate_config_file(self, config_text: str) -> bool:
        """
        Validate that file looks like a Cisco configuration.

        Args:
            config_text: Raw configuration file content

        Returns:
            True if file appears to be a valid Cisco config, False otherwise
        """
        # Check for common Cisco config markers
        cisco_markers = [
            'version ',      # IOS version line
            'hostname ',     # Hostname declaration
            'interface ',    # Interface configurations
            '!',            # Cisco comment marker
        ]

        markers_found = sum(1 for marker in cisco_markers if marker in config_text)

        if markers_found < 2:
            if self.logger:
                self.logger.error(f"File does not appear to be a Cisco configuration (found {markers_found}/4 markers)")
                self.logger.error("Expected markers: version, hostname, interface, !")
            else:
                print(f"  Error: File does not appear to be a Cisco configuration")
                print(f"  Found {markers_found}/4 expected markers")
            return False

        if self.logger:
            self.logger.progress(f"Config validation passed ({markers_found}/4 markers found)")

        return True

    def process(self) -> Path:
        """Process the configuration file and generate documentation."""
        try:
            # Start timing
            import time
            start_time = time.time()

            if self.logger:
                self.logger.section(f"Processing: {self.config_filename}")
                self.logger.progress(f"Started at: {datetime.now().strftime('%H:%M:%S')}")

            # Step 0: Validate input file
            if self.logger:
                self.logger.step("Validating input file")
            else:
                print(" Validating input file...")

            config_text = self._read_config_file()
            if not self._validate_config_file(config_text):
                raise ValueError(f"{self.config_filename} does not appear to be a valid Cisco configuration file")

            # Step 1: Parse configuration
            if self.logger:
                self.logger.step("Parsing configuration into structured data")
            else:
                print(" Parsing configuration into structured data...")

            # Check if secrets sanitization is enabled
            security_config = self.config.get("security", {})
            sanitize_secrets = security_config.get("sanitize_secrets", False)

            if sanitize_secrets:
                if self.logger:
                    self.logger.progress("Secrets sanitization is enabled")
                else:
                    print("   Secrets sanitization enabled")

            structured_data = parse_config_to_json(str(self.config_file_path), sanitize_secrets=sanitize_secrets)

            parse_elapsed = time.time() - start_time
            if self.logger:
                self.logger.progress(f"Parsing completed in {parse_elapsed:.2f} seconds")

            device_info = structured_data.get("device_info", {})
            hostname = device_info.get("hostname") or "Unknown"
            ios_version = device_info.get("ios_version") or "Unknown"
            vlan_count = len(structured_data.get('vlans', {}).get('vlan_ids', []))
            interface_count = len(structured_data.get('interfaces', []))

            if self.logger:
                self.logger.progress(f"Detected device: {hostname}")
                self.logger.progress(f"IOS version: {ios_version}")
                self.logger.progress(f"VLANs found: {vlan_count}")
                self.logger.progress(f"Interfaces found: {interface_count}")
                self.logger.debug(f"Device info: {json.dumps(device_info, indent=2)}")
            else:
                print(f"   Detected device: {hostname}")
                print(f"   IOS version: {ios_version}")
                print(f"   VLANs found: {vlan_count}")
                print(f"   Interfaces found: {interface_count}")

            # Step 2: Build structured prompt
            if self.logger:
                self.logger.step("Building structured prompt")
            else:
                print(" Building structured prompt...")

            prompt_builder = StructuredPromptBuilder(structured_data)
            prompt = prompt_builder.build_prompt()

            if self.logger:
                self.logger.progress(f"Prompt size: {len(prompt)} characters")
                self.logger.debug(f"First 500 chars of prompt: {prompt[:500]}")
            else:
                print(f"   Prompt size: {len(prompt)} characters")

            # Step 3: Send to LLM (or skip in dry-run mode)
            if self.dry_run:
                if self.logger:
                    self.logger.step("Dry-run mode: Saving prompt to file (skipping LLM)")
                else:
                    print(" Dry-run mode: Saving prompt to file (skipping LLM)...")

                # Save prompt to file for inspection
                prompt_file = self.output_dir / f"{self.config_filename.replace('.txt', '')}-prompt.txt"
                with open(prompt_file, 'w', encoding='utf-8') as f:
                    f.write(prompt)

                if self.logger:
                    self.logger.success(f"Prompt saved to: {prompt_file}")
                    self.logger.info("Dry-run complete. Run without --dry-run to generate documentation.")
                else:
                    print(f" Prompt saved to: {prompt_file}")
                    print(" Dry-run complete. Run without --dry-run to generate documentation.")

                return prompt_file

            else:
                if self.logger:
                    self.logger.step("Sending to LLM for analysis")
                else:
                    print(" Sending to LLM for analysis...")

                llm_start = time.time()
                documentation = self._call_llm(prompt)
                llm_elapsed = time.time() - llm_start

                if self.logger:
                    self.logger.progress(f"LLM analysis completed in {llm_elapsed:.2f} seconds")
                    self.logger.progress(f"LLM response length: {len(documentation)} characters")
                    self.logger.debug(f"First 500 chars of response: {documentation[:500]}")
                else:
                    print(f"   LLM processing took {llm_elapsed:.2f} seconds")

            # Step 4: Save documentation
            if self.logger:
                self.logger.step("Saving documentation")
            else:
                print(" Saving documentation...")

            output_path = self._save_documentation(documentation)

            if self.logger:
                self.logger.progress(f"Saved to: {output_path}")

            # Step 5: Validate documentation
            if self.config.get("validation", {}).get("enabled", True):
                if self.logger:
                    self.logger.step("Validating documentation")
                else:
                    print(" Validating documentation...")

                validation_report = self._validate_documentation(structured_data, documentation, output_path)

                # Save validation report
                validation_report_path = output_path.parent / f"{output_path.stem}-validation.json"
                with open(validation_report_path, 'w', encoding='utf-8') as f:
                    json.dump(validation_report.to_dict(), f, indent=2, ensure_ascii=False)

                if self.logger:
                    self.logger.progress(f"Accuracy: {validation_report.accuracy_percentage:.1f}%")
                    self.logger.progress(f"Passed: {validation_report.passed_checks}/{validation_report.total_checks} checks")
                    if validation_report.failed_checks > 0:
                        self.logger.warning(f"WARNING: {validation_report.failed_checks} checks failed")
                        self.logger.debug(f"Validation report: {validation_report_path}")
                        for result in validation_report.results:
                            if not result.passed:
                                self.logger.debug(f"  Failed: {result.field_name} - {result.error_message}")
                else:
                    print(f"   Accuracy: {validation_report.accuracy_percentage:.1f}%")
                    print(f"   Passed: {validation_report.passed_checks}/{validation_report.total_checks} checks")
                    if validation_report.failed_checks > 0:
                        print(f"   WARNING: {validation_report.failed_checks} checks failed")
                        print(f"   Validation report: {validation_report_path}")

            # Step 6: Commit to Git
            if self.config.get("git", {}).get("enabled", True):
                if self.logger:
                    self.logger.step("Committing to Git")
                else:
                    print(" Committing to Git...")
                self._commit_to_git(output_path)

            # Calculate total time
            total_elapsed = time.time() - start_time

            # Record metrics
            if self.metrics_tracker:
                config_size = self.config_file_path.stat().st_size if self.config_file_path.exists() else 0
                doc_size = output_path.stat().st_size if output_path.exists() else 0

                metrics = {
                    'config_file': self.config_filename,
                    'timestamp': datetime.now(),
                    'parse_time_seconds': parse_elapsed,
                    'llm_call_time_seconds': llm_elapsed,
                    'total_time_seconds': total_elapsed,
                    'config_size_bytes': config_size,
                    'generated_doc_size_bytes': doc_size,
                    'llm_model': self.config['llm']['model'],
                    'llm_temperature': self.config['llm'].get('temperature', 0.7),
                    'validation_enabled': self.config.get("validation", {}).get("enabled", True),
                    'error_occurred': False,
                }

                # Add validation metrics if available
                if self.config.get("validation", {}).get("enabled", True) and 'validation_report' in locals():
                    metrics['validation_accuracy_percent'] = validation_report.accuracy_percentage
                    metrics['total_validation_checks'] = validation_report.total_checks
                    metrics['failed_validation_checks'] = validation_report.failed_checks

                # Add token usage if available
                if self.last_token_usage:
                    metrics['prompt_tokens'] = self.last_token_usage.get('prompt_tokens')
                    metrics['completion_tokens'] = self.last_token_usage.get('completion_tokens')
                    metrics['total_tokens'] = self.last_token_usage.get('total_tokens')

                # Add secrets sanitization info
                security_config = self.config.get("security", {})
                metrics['secrets_sanitized'] = 1 if security_config.get("sanitize_secrets", False) else 0

                try:
                    self.metrics_tracker.record_processing(metrics)
                    if self.logger:
                        self.logger.debug("Metrics recorded successfully")
                except Exception as metrics_error:
                    if self.logger:
                        self.logger.warning(f"Failed to record metrics: {metrics_error}")

            if self.logger:
                self.logger.success(f"Documentation generated: {output_path}")
                self.logger.progress(f"Total processing time: {total_elapsed:.2f} seconds")
                self.logger.progress(f"  - Parsing: {parse_elapsed:.2f}s")
                self.logger.progress(f"  - LLM analysis: {llm_elapsed:.2f}s")
                self.logger.info(f"\nLog file saved to: {self.logger.get_log_path()}")
            else:
                print(f" Documentation generated: {output_path}")
                print(f" Total time: {total_elapsed:.2f} seconds")

            return output_path

        except Exception as e:
            # Record error in metrics
            if self.metrics_tracker:
                try:
                    error_metrics = {
                        'config_file': self.config_filename,
                        'timestamp': datetime.now(),
                        'llm_model': self.config['llm']['model'],
                        'error_occurred': True,
                        'error_message': str(e),
                    }
                    self.metrics_tracker.record_processing(error_metrics)
                except:
                    pass  # Don't fail on metrics recording failure

            if self.logger:
                self.logger.error(f"Processing failed: {str(e)}")
                self.logger.debug(f"Exception details:", exc_info=True)
            else:
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

    def _validate_documentation(self, structured_data: Dict[str, Any], documentation: str, output_path: Path):
        """
        Validate generated documentation against structured data.

        Args:
            structured_data: Parsed configuration data
            documentation: Generated markdown documentation
            output_path: Path where documentation was saved

        Returns:
            ValidationReport
        """
        validator = DocumentationValidator(structured_data, documentation)
        report = validator.validate_all()
        return report

    def _call_llm(self, prompt: str, max_retries: int = 3) -> str:
        """
        Call the LLM API with retry logic.

        Args:
            prompt: The prompt to send to the LLM
            max_retries: Maximum number of retry attempts (default 3)

        Returns:
            LLM response content

        Raises:
            Exception: If all retry attempts fail
        """
        llm_config = self.config["llm"]
        endpoint = llm_config["endpoint"]

        for attempt in range(max_retries):
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
                        "max_tokens": llm_config.get("max_tokens", 8000),
                        "options": {
                            "num_ctx": llm_config.get("num_ctx", 4096)
                        }
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

                # Track token usage
                if "usage" in data:
                    usage = data["usage"]
                    prompt_tokens = usage.get("prompt_tokens", "unknown")
                    completion_tokens = usage.get("completion_tokens", "unknown")
                    total_tokens = usage.get("total_tokens", "unknown")

                    if self.logger:
                        self.logger.progress(f"Token usage - Prompt: {prompt_tokens}, Completion: {completion_tokens}, Total: {total_tokens}")
                    else:
                        print(f"   Token usage: {total_tokens} total ({prompt_tokens} prompt + {completion_tokens} completion)")

                    # Store for potential metrics tracking
                    self.last_token_usage = {
                        "prompt_tokens": prompt_tokens,
                        "completion_tokens": completion_tokens,
                        "total_tokens": total_tokens
                    }
                else:
                    if self.logger:
                        self.logger.debug("Token usage information not available in LLM response")

                return content

            except requests.exceptions.Timeout:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                    if self.logger:
                        self.logger.warning(f"LLM request timed out, retrying in {wait_time}s... (attempt {attempt + 1}/{max_retries})")
                    else:
                        print(f"   ⚠ LLM timeout, retrying in {wait_time}s... (attempt {attempt + 1}/{max_retries})")

                    time.sleep(wait_time)
                else:
                    error_msg = f"LLM request timed out after {max_retries} attempts"
                    if self.logger:
                        self.logger.error(error_msg)
                    raise Exception(error_msg)

            except requests.exceptions.ConnectionError:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                    if self.logger:
                        self.logger.warning(f"Could not connect to LLM server, retrying in {wait_time}s... (attempt {attempt + 1}/{max_retries})")
                    else:
                        print(f"   ⚠ Connection failed, retrying in {wait_time}s... (attempt {attempt + 1}/{max_retries})")

                    time.sleep(wait_time)
                else:
                    error_msg = f"Could not connect to LLM server at {endpoint} after {max_retries} attempts. Check if the server is running."
                    if self.logger:
                        self.logger.error(error_msg)
                    raise Exception(error_msg)

            except requests.exceptions.RequestException as e:
                # For other errors (like 4xx/5xx status codes), don't retry
                if hasattr(e, 'response') and e.response is not None:
                    error_msg = f"LLM API error: {e.response.status_code}"
                    try:
                        error_data = e.response.json()
                        if "error" in error_data:
                            error_msg += f" - {error_data['error'].get('message', str(error_data['error']))}"
                    except:
                        error_msg += f" - {e.response.text}"

                    if self.logger:
                        self.logger.error(error_msg)
                    raise Exception(error_msg)
                else:
                    error_msg = f"LLM API request failed: {str(e)}"
                    if self.logger:
                        self.logger.error(error_msg)
                    raise Exception(error_msg)

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
        print(" Usage: python processor.py <config-file-path> [--dry-run]")
        print("   --dry-run: Generate and save prompt without calling LLM")
        sys.exit(1)

    config_file_path = Path(sys.argv[1])

    if not config_file_path.exists():
        print(f" Error: Configuration file not found: {config_file_path}")
        sys.exit(1)

    # Initialize metrics tracker
    project_root = config_file_path.parent.parent
    metrics_dir = project_root / "metrics"
    metrics_dir.mkdir(exist_ok=True, parents=True)
    metrics_db = metrics_dir / "processing_metrics.db"
    init_metrics(metrics_db)

    # Check for dry-run flag
    dry_run = "--dry-run" in sys.argv

    processor = ConfigProcessor(config_file_path, dry_run=dry_run)
    processor.process()


if __name__ == "__main__":
    main()