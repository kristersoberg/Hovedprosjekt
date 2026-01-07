#!/usr/bin/env python3
"""
Unit tests for Documentation Validator

Tests the validator module to ensure correct validation of generated documentation.
"""

import sys
import unittest
from pathlib import Path

# Add automation directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "automation"))

from validator import DocumentationValidator, ValidationReport


class TestDocumentationValidator(unittest.TestCase):
    """Test cases for DocumentationValidator class."""

    def setUp(self):
        """Set up test data."""
        self.structured_data = {
            "device_info": {
                "hostname": "TEST-SW-01",
                "ios_version": "15.2",
                "domain_name": "example.com"
            },
            "management": {
                "vlan": 1,
                "ip_address": "192.168.1.10",
                "subnet_mask": "255.255.255.0"
            },
            "vlans": {
                "vlan_ids": [10, 20, 30],
                "vlan_names": {
                    10: "DATA",
                    20: "VOICE",
                    30: "GUEST"
                }
            },
            "interfaces": [
                {
                    "name": "GigabitEthernet0/1",
                    "description": "Uplink to Core",
                    "switchport_mode": "trunk"
                }
            ],
            "routing": {
                "static_routes": [
                    {
                        "destination": "0.0.0.0/0.0.0.0",
                        "next_hop": "192.168.1.1"
                    }
                ]
            }
        }

    def test_validate_hostname_success(self):
        """Test successful hostname validation."""
        markdown = "# Network Documentation for TEST-SW-01\n\nHostname: TEST-SW-01"

        validator = DocumentationValidator(self.structured_data, markdown)
        report = validator.validate_all()

        # Find hostname validation result
        hostname_results = [r for r in report.results if r.field_name == "Hostname"]
        self.assertGreater(len(hostname_results), 0)
        self.assertTrue(hostname_results[0].passed)

    def test_validate_hostname_failure(self):
        """Test failed hostname validation."""
        markdown = "# Network Documentation for WRONG-HOSTNAME\n\nHostname: WRONG"

        validator = DocumentationValidator(self.structured_data, markdown)
        report = validator.validate_all()

        # Accuracy should be less than 100%
        self.assertLess(report.accuracy_percentage, 100)
        self.assertGreater(report.failed_checks, 0)

    def test_validate_ios_version(self):
        """Test IOS version validation."""
        markdown = "IOS Version: 15.2"

        validator = DocumentationValidator(self.structured_data, markdown)
        report = validator.validate_all()

        # Find IOS version result
        ios_results = [r for r in report.results if r.field_name == "IOS Version"]
        self.assertGreater(len(ios_results), 0)
        self.assertTrue(ios_results[0].passed)

    def test_validate_vlan_presence(self):
        """Test VLAN presence validation."""
        markdown = """
        # VLANs
        - VLAN 10: DATA
        - VLAN 20: VOICE
        - VLAN 30: GUEST
        """

        validator = DocumentationValidator(self.structured_data, markdown)
        report = validator.validate_all()

        # Should find VLANs
        vlan_results = [r for r in report.results if "VLAN" in r.field_name]
        self.assertGreater(len(vlan_results), 0)

    def test_validate_ip_address(self):
        """Test IP address validation."""
        markdown = "Management IP: 192.168.1.10"

        validator = DocumentationValidator(self.structured_data, markdown)
        report = validator.validate_all()

        # Find IP address result
        ip_results = [r for r in report.results if "Management IP" in r.field_name]
        self.assertGreater(len(ip_results), 0)

    def test_validation_report_structure(self):
        """Test that validation report has correct structure."""
        markdown = "# TEST-SW-01\n\nHostname: TEST-SW-01\nIOS: 15.2"

        validator = DocumentationValidator(self.structured_data, markdown)
        report = validator.validate_all()

        # Check report structure
        self.assertIsInstance(report, ValidationReport)
        self.assertIsInstance(report.results, list)
        self.assertGreaterEqual(report.total_checks, 0)
        self.assertGreaterEqual(report.passed_checks, 0)
        self.assertGreaterEqual(report.failed_checks, 0)
        self.assertGreaterEqual(report.accuracy_percentage, 0)
        self.assertLessEqual(report.accuracy_percentage, 100)

    def test_empty_documentation(self):
        """Test validation with empty documentation."""
        markdown = ""

        validator = DocumentationValidator(self.structured_data, markdown)
        report = validator.validate_all()

        # Should fail many checks
        self.assertGreater(report.failed_checks, 0)
        self.assertLess(report.accuracy_percentage, 50)

    def test_accuracy_calculation(self):
        """Test accuracy percentage calculation."""
        # Perfect documentation
        markdown = """
        # TEST-SW-01
        Hostname: TEST-SW-01
        IOS Version: 15.2
        Domain: example.com
        Management IP: 192.168.1.10
        Subnet Mask: 255.255.255.0
        VLAN 10: DATA
        VLAN 20: VOICE
        VLAN 30: GUEST
        """

        validator = DocumentationValidator(self.structured_data, markdown)
        report = validator.validate_all()

        # Should have high accuracy
        self.assertGreater(report.accuracy_percentage, 70)
        self.assertGreater(report.passed_checks, report.failed_checks)


class TestValidationEdgeCases(unittest.TestCase):
    """Test edge cases in validation."""

    def test_missing_structured_data(self):
        """Test validation with missing structured data."""
        markdown = "# TEST\n\nSome documentation"
        structured_data = {}

        validator = DocumentationValidator(structured_data, markdown)
        report = validator.validate_all()

        # Should handle gracefully
        self.assertIsInstance(report, ValidationReport)

    def test_special_characters_in_markdown(self):
        """Test validation with special characters."""
        structured_data = {
            "device_info": {
                "hostname": "TEST-SW-01"
            }
        }
        markdown = "# Network Documentation\n\nHostname: TEST-SW-01\n\n**Bold** and *italic*"

        validator = DocumentationValidator(structured_data, markdown)
        report = validator.validate_all()

        # Should still find hostname
        hostname_results = [r for r in report.results if r.field_name == "Hostname"]
        self.assertGreater(len(hostname_results), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
