#!/usr/bin/env python3
"""
Unit tests for Cisco Configuration Parser

Tests the config_parser module to ensure correct extraction of configuration data.
"""

import sys
import unittest
from pathlib import Path

# Add automation directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "automation"))

from config_parser import CiscoConfigParser, parse_config_to_json


class TestCiscoConfigParser(unittest.TestCase):
    """Test cases for CiscoConfigParser class."""

    @classmethod
    def setUpClass(cls):
        """Set up test fixtures."""
        cls.test_config_path = Path(__file__).parent / "fixtures" / "sample_configs" / "test_switch.txt"

        if not cls.test_config_path.exists():
            raise FileNotFoundError(f"Test config not found: {cls.test_config_path}")

    def setUp(self):
        """Set up each test."""
        self.parser = CiscoConfigParser(str(self.test_config_path))
        self.parser.load_config()

    def test_load_config(self):
        """Test that config file loads successfully."""
        self.assertIsNotNone(self.parser.config_text)
        self.assertGreater(len(self.parser.config_text), 0)
        self.assertIsNotNone(self.parser.parse)

    def test_extract_device_info(self):
        """Test device information extraction."""
        device_info = self.parser._extract_device_info()

        self.assertEqual(device_info['hostname'], 'TEST-SW-01')
        self.assertEqual(device_info['ios_version'], '15.2')

    def test_extract_vlans(self):
        """Test VLAN extraction."""
        vlans = self.parser._extract_vlans()

        # Check VLAN IDs
        self.assertIn(10, vlans['vlan_ids'])
        self.assertIn(20, vlans['vlan_ids'])
        self.assertIn(30, vlans['vlan_ids'])

        # Check VLAN names
        self.assertEqual(vlans['vlan_names'].get(10), 'DATA')
        self.assertEqual(vlans['vlan_names'].get(20), 'VOICE')
        self.assertEqual(vlans['vlan_names'].get(30), 'GUEST')

    def test_extract_interfaces(self):
        """Test interface extraction."""
        interfaces = self.parser._extract_interfaces()

        self.assertGreater(len(interfaces), 0)

        # Find GigabitEthernet0/1
        g0_1 = next((i for i in interfaces if i['name'] == 'GigabitEthernet0/1'), None)
        self.assertIsNotNone(g0_1)
        self.assertEqual(g0_1['description'], 'Uplink to Core')
        self.assertEqual(g0_1['mode'], 'trunk')

        # Find GigabitEthernet0/2
        g0_2 = next((i for i in interfaces if i['name'] == 'GigabitEthernet0/2'), None)
        self.assertIsNotNone(g0_2)
        self.assertEqual(g0_2['description'], 'Access Port VLAN 10')
        self.assertEqual(g0_2['mode'], 'access')
        self.assertEqual(g0_2['access_vlan'], 10)

    def test_extract_routing(self):
        """Test routing extraction."""
        routing = self.parser._extract_routing()

        # Check static routes
        self.assertGreater(len(routing['static_routes']), 0)
        default_route = routing['static_routes'][0]
        self.assertEqual(default_route['network'], '0.0.0.0')
        self.assertEqual(default_route['mask'], '0.0.0.0')
        self.assertEqual(default_route['next_hop'], '192.168.1.1')

    def test_extract_management_config(self):
        """Test management configuration extraction."""
        mgmt = self.parser._extract_management_config()

        # Check management VLAN (svi = SVI interface number)
        self.assertEqual(mgmt['svi'], 1)
        self.assertEqual(mgmt['ip_address'], '192.168.1.10')
        self.assertEqual(mgmt['subnet_mask'], '255.255.255.0')

    def test_extract_hsrp_config(self):
        """Test HSRP extraction from SVIs."""
        vlans = self.parser._extract_vlans()

        # Find VLAN 1 SVI
        vlan1_svi = next((svi for svi in vlans['svi_interfaces'] if svi['vlan_id'] == 1), None)
        self.assertIsNotNone(vlan1_svi)

        # Check HSRP configuration
        self.assertGreater(len(vlan1_svi['hsrp']), 0)
        hsrp_group = vlan1_svi['hsrp'][0]
        self.assertEqual(hsrp_group['group'], 1)
        self.assertEqual(hsrp_group['virtual_ip'], '192.168.1.1')
        self.assertEqual(hsrp_group['priority'], 110)
        self.assertTrue(hsrp_group['preempt'])

    def test_extract_channel_group(self):
        """Test EtherChannel/channel-group extraction."""
        interfaces = self.parser._extract_interfaces()

        # Find interface with channel-group (range GigabitEthernet0/23-24)
        channel_intf = next((i for i in interfaces if i['channel_group']['number'] is not None), None)
        self.assertIsNotNone(channel_intf)
        self.assertEqual(channel_intf['channel_group']['number'], 1)
        self.assertEqual(channel_intf['channel_group']['mode'], 'active')

    def test_sanitize_secrets(self):
        """Test secrets sanitization."""
        test_config = """
        username admin privilege 15 secret 5 $1$abcd$efgh1234
        enable secret 5 $1$xyz$1234abcd
        snmp-server community public RO
        """

        sanitized = self.parser.sanitize_secrets(test_config)

        # Verify secrets are redacted
        self.assertIn('<REDACTED>', sanitized)
        self.assertNotIn('$1$abcd$efgh1234', sanitized)
        self.assertNotIn('$1$xyz$1234abcd', sanitized)
        self.assertNotIn('public', sanitized)

    def test_parse_config_to_json(self):
        """Test complete parsing to JSON."""
        result = parse_config_to_json(str(self.test_config_path))

        # Verify all major sections exist
        self.assertIn('device_info', result)
        self.assertIn('management', result)
        self.assertIn('vlans', result)
        self.assertIn('interfaces', result)
        self.assertIn('routing', result)

        # Verify some data
        self.assertEqual(result['device_info']['hostname'], 'TEST-SW-01')
        self.assertIn(10, result['vlans']['vlan_ids'])
        self.assertGreater(len(result['interfaces']), 0)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error handling."""

    def test_invalid_file_path(self):
        """Test handling of invalid file path."""
        with self.assertRaises(FileNotFoundError):
            parser = CiscoConfigParser("nonexistent.txt")
            parser.load_config()

    def test_empty_config(self):
        """Test handling of empty configuration."""
        # Create temporary empty file
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp:
            tmp_path = tmp.name

        try:
            parser = CiscoConfigParser(tmp_path)
            parser.load_config()
            device_info = parser._extract_device_info()

            # Should not crash, but return empty/default values
            self.assertIsInstance(device_info, dict)
        finally:
            Path(tmp_path).unlink()


if __name__ == '__main__':
    unittest.main(verbosity=2)
