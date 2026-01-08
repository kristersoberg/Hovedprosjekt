#!/usr/bin/env python3
"""
Integration tests for the complete documentation system

Tests end-to-end workflow from config parsing to documentation generation.
"""

import sys
import unittest
import tempfile
from pathlib import Path

# Add automation directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "automation"))

from config_parser import parse_config_to_json
from structured_prompt_builder import StructuredPromptBuilder
from validator import DocumentationValidator


class TestEndToEndWorkflow(unittest.TestCase):
    """Test complete end-to-end workflow."""

    @classmethod
    def setUpClass(cls):
        """Set up test fixtures."""
        cls.test_config_path = Path(__file__).parent / "fixtures" / "sample_configs" / "test_switch.txt"

        if not cls.test_config_path.exists():
            raise FileNotFoundError(f"Test config not found: {cls.test_config_path}")

    def test_parse_to_structured_data(self):
        """Test parsing config to structured JSON."""
        structured_data = parse_config_to_json(str(self.test_config_path))

        # Verify structure
        self.assertIsInstance(structured_data, dict)
        self.assertIn('device_info', structured_data)
        self.assertIn('vlans', structured_data)
        self.assertIn('interfaces', structured_data)

    def test_build_prompt_from_structured_data(self):
        """Test building prompt from structured data."""
        structured_data = parse_config_to_json(str(self.test_config_path))
        prompt_builder = StructuredPromptBuilder(structured_data)

        prompt = prompt_builder.build_prompt()

        # Verify prompt contains expected data
        self.assertIsInstance(prompt, str)
        self.assertGreater(len(prompt), 100)
        self.assertIn('TEST-SW-01', prompt)
        self.assertIn('VLAN', prompt)

    def test_validation_workflow(self):
        """Test validation of generated documentation."""
        structured_data = parse_config_to_json(str(self.test_config_path))

        # Simulate LLM-generated documentation
        mock_documentation = """
        # Network Documentation for TEST-SW-01

        ## Device Information
        - **Hostname**: TEST-SW-01
        - **IOS Version**: 15.2

        ## VLANs
        - VLAN 10: DATA
        - VLAN 20: VOICE
        - VLAN 30: GUEST

        ## Interfaces
        ### GigabitEthernet0/1
        - Description: Uplink to Core
        - Mode: Trunk
        - Allowed VLANs: 10, 20, 30

        ### GigabitEthernet0/2
        - Description: Access Port VLAN 10
        - Mode: Access
        - Access VLAN: 10

        ## Management
        - Management VLAN: 1
        - IP Address: 192.168.1.10/24

        ## Routing
        - Default Route: 0.0.0.0/0 via 192.168.1.1
        """

        validator = DocumentationValidator(structured_data, mock_documentation)
        report = validator.validate_all()

        # Validation should pass with reasonable accuracy
        self.assertGreaterEqual(report.accuracy_percentage, 60)
        self.assertGreater(report.passed_checks, report.failed_checks)

    def test_secrets_sanitization_integration(self):
        """Test that secrets sanitization works in full workflow."""
        # Create temp config with secrets
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as tmp:
            tmp.write("""
hostname SECRET-TEST
!
username admin privilege 15 secret 5 $1$abcd$secret123
enable secret 5 $1$xyz$enablepass
snmp-server community publicCommunity RO
!
interface Vlan1
 ip address 10.0.0.1 255.255.255.0
!
end
            """)
            tmp_path = tmp.name

        try:
            # Parse with sanitization enabled
            structured_data = parse_config_to_json(tmp_path, sanitize_secrets=True)

            # Build prompt
            prompt_builder = StructuredPromptBuilder(structured_data)
            prompt = prompt_builder.build_prompt()

            # Verify secrets are redacted
            self.assertIn('<REDACTED>', prompt)
            self.assertNotIn('secret123', prompt)
            self.assertNotIn('enablepass', prompt)
            self.assertNotIn('publicCommunity', prompt)

        finally:
            Path(tmp_path).unlink()

    def test_complete_workflow_with_output(self):
        """Test complete workflow including output generation."""
        # Parse config
        structured_data = parse_config_to_json(str(self.test_config_path))

        # Build prompt
        prompt_builder = StructuredPromptBuilder(structured_data)
        prompt = prompt_builder.build_prompt()

        # Verify prompt was built
        self.assertGreater(len(prompt), 0)

        # Create mock documentation (simulating LLM output)
        mock_doc = f"""
        # Configuration Documentation

        **Hostname**: {structured_data['device_info']['hostname']}
        **IOS**: {structured_data['device_info']['ios_version']}

        ## VLANs
        """

        for vlan_id in structured_data['vlans']['vlan_ids']:
            mock_doc += f"\n- VLAN {vlan_id}"

        # Validate
        validator = DocumentationValidator(structured_data, mock_doc)
        report = validator.validate_all()

        # Should have some passing checks
        self.assertGreater(report.passed_checks, 0)


class TestErrorHandling(unittest.TestCase):
    """Test error handling in integration scenarios."""

    def test_invalid_config_file(self):
        """Test handling of invalid config file."""
        with self.assertRaises(FileNotFoundError):
            parse_config_to_json("nonexistent_file.txt")

    def test_malformed_config(self):
        """Test handling of malformed configuration."""
        # Create temp file with garbage data
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp:
            tmp.write("This is not a valid Cisco configuration!\n")
            tmp.write("Random garbage data!!!\n")
            tmp_path = tmp.name

        try:
            # Should not crash, but may have limited data
            structured_data = parse_config_to_json(tmp_path)
            self.assertIsInstance(structured_data, dict)

        finally:
            Path(tmp_path).unlink()


if __name__ == '__main__':
    unittest.main(verbosity=2)
