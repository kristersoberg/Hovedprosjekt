"""
Cisco IOS Configuration Parser
Extracts structured data from Cisco IOS configuration files using ciscoconfparse.
This provides deterministic, accurate extraction of configuration facts.
"""

import re
import json
from typing import Dict, List, Any, Optional
from ciscoconfparse import CiscoConfParse


class CiscoConfigParser:
    """Parse Cisco IOS configuration files into structured JSON format."""

    def __init__(self, config_file_path: str):
        """Initialize parser with configuration file path."""
        self.config_file_path = config_file_path
        self.parse = None
        self.config_text = ""

    def load_config(self) -> bool:
        """Load configuration file."""
        try:
            # Try UTF-8 first
            with open(self.config_file_path, 'r', encoding='utf-8') as f:
                self.config_text = f.read()
        except UnicodeDecodeError:
            # Fall back to latin-1
            with open(self.config_file_path, 'r', encoding='latin-1') as f:
                self.config_text = f.read()

        # Parse with ciscoconfparse
        self.parse = CiscoConfParse(self.config_file_path, syntax='ios')
        return True

    def sanitize_secrets(self, config_text: str) -> str:
        """
        Sanitize sensitive information from configuration text.

        Args:
            config_text: Raw configuration text

        Returns:
            Sanitized configuration text with secrets redacted
        """
        sanitized = config_text

        # Define patterns to redact with their replacements
        patterns = [
            # Username passwords (type 5, 7, or plaintext)
            (r'(username\s+\S+\s+(?:privilege\s+\d+\s+)?(?:secret|password)\s+(?:\d+\s+)?)\S+', r'\1<REDACTED>'),

            # Enable passwords
            (r'(enable\s+(?:secret|password)\s+(?:\d+\s+)?)\S+', r'\1<REDACTED>'),

            # SNMP community strings
            (r'(snmp-server\s+community\s+)\S+', r'\1<REDACTED>'),

            # TACACS/RADIUS keys
            (r'(tacacs-server\s+key\s+(?:\d+\s+)?)\S+', r'\1<REDACTED>'),
            (r'(radius-server\s+key\s+(?:\d+\s+)?)\S+', r'\1<REDACTED>'),

            # Crypto keys (ISAKMP, IPsec)
            (r'(key\s+\d+\s+)\S+', r'\1<REDACTED>'),
            (r'(pre-shared-key\s+(?:address\s+\S+\s+)?key\s+)\S+', r'\1<REDACTED>'),

            # Line passwords (VTY, console, aux)
            (r'(password\s+(?:\d+\s+)?)\S+', r'\1<REDACTED>'),

            # SNMP v3 auth/priv passwords
            (r'(snmp-server\s+user\s+\S+\s+\S+\s+(?:v3\s+)?auth\s+\w+\s+)\S+', r'\1<REDACTED>'),
            (r'(snmp-server\s+user\s+\S+\s+\S+\s+(?:v3\s+)?.*?priv\s+\w+\s+)\S+', r'\1<REDACTED>'),

            # Dot1x passwords
            (r'(dot1x\s+.*?password\s+(?:\d+\s+)?)\S+', r'\1<REDACTED>'),
        ]

        secrets_found = 0
        for pattern, replacement in patterns:
            matches = re.findall(pattern, sanitized, re.IGNORECASE | re.MULTILINE)
            if matches:
                secrets_found += len(matches)
            sanitized = re.sub(pattern, replacement, sanitized, flags=re.IGNORECASE | re.MULTILINE)

        if secrets_found > 0:
            print(f"   Sanitized {secrets_found} secret(s) from configuration")

        return sanitized

    def extract_all(self) -> Dict[str, Any]:
        """Extract all configuration data into structured JSON."""
        if not self.parse:
            self.load_config()

        return {
            "device_info": self._extract_with_fallback(self._extract_device_info, "device_info"),
            "management": self._extract_with_fallback(self._extract_management_config, "management"),
            "aaa": self._extract_with_fallback(self._extract_aaa_config, "aaa"),
            "vlans": self._extract_with_fallback(self._extract_vlans, "vlans"),
            "interfaces": self._extract_with_fallback(self._extract_interfaces, "interfaces"),
            "routing": self._extract_with_fallback(self._extract_routing, "routing"),
            "spanning_tree": self._extract_with_fallback(self._extract_spanning_tree, "spanning_tree"),
            "security": self._extract_with_fallback(self._extract_security_features, "security"),
            "services": self._extract_with_fallback(self._extract_network_services, "services"),
            "qos": self._extract_with_fallback(self._extract_qos_config, "qos"),
            "stacking": self._extract_with_fallback(self._extract_stacking_config, "stacking"),
            "raw_config": self.config_text
        }

    def _extract_with_fallback(self, extraction_func, section_name: str) -> Dict[str, Any]:
        """
        Wrapper to catch exceptions in individual extraction functions.
        Ensures parser doesn't crash on unexpected config variations.
        """
        try:
            return extraction_func()
        except Exception as e:
            print(f"   Warning: Failed to extract {section_name}: {e}")
            # Return empty structure instead of crashing
            return {}

    def _extract_device_info(self) -> Dict[str, Any]:
        """Extract basic device information."""
        info = {
            "hostname": None,
            "ios_version": None,
            "domain_name": None,
            "config_register": None
        }

        # Hostname - CRITICAL: Must be exact
        hostname_obj = self.parse.find_objects(r'^hostname\s+')
        if hostname_obj:
            match = re.search(r'^hostname\s+(\S+)', hostname_obj[0].text)
            if match:
                info["hostname"] = match.group(1)

        # IOS Version - parse from version line or banner
        version_obj = self.parse.find_objects(r'^version\s+')
        if version_obj:
            match = re.search(r'^version\s+(.+)', version_obj[0].text)
            if match:
                info["ios_version"] = match.group(1).strip()
        else:
            # Try to find in comments/banner
            for line in self.config_text.split('\n'):
                if 'IOS' in line and 'Version' in line:
                    match = re.search(r'Version\s+([0-9.()A-Z]+)', line)
                    if match:
                        info["ios_version"] = match.group(1)
                        break

        # Domain name
        domain_obj = self.parse.find_objects(r'^ip\s+domain[_-]name\s+')
        if domain_obj:
            match = re.search(r'^ip\s+domain[_-]name\s+(\S+)', domain_obj[0].text)
            if match:
                info["domain_name"] = match.group(1)

        # Config register
        config_reg_obj = self.parse.find_objects(r'^config-register\s+')
        if config_reg_obj:
            match = re.search(r'^config-register\s+(\S+)', config_reg_obj[0].text)
            if match:
                info["config_register"] = match.group(1)

        return info

    def _extract_management_config(self) -> Dict[str, Any]:
        """Extract management interface and access configuration."""
        mgmt = {
            "svi": None,
            "ip_address": None,
            "subnet_mask": None,
            "default_gateway": None,
            "ssh": {},
            "console": {},
            "vty": {},
            "banner": None
        }

        # Find management SVI (usually VLAN with IP address)
        vlan_intfs = self.parse.find_objects(r'^interface\s+Vlan')
        for vlan_intf in vlan_intfs:
            # Check if it has an IP address
            ip_addr = vlan_intf.re_search_children(r'^\s+ip\s+address\s+(\S+)\s+(\S+)')
            if ip_addr:
                match = re.search(r'^\s+ip\s+address\s+(\S+)\s+(\S+)', ip_addr[0].text)
                if match:
                    # Extract VLAN number
                    vlan_match = re.search(r'interface\s+Vlan(\d+)', vlan_intf.text)
                    mgmt["svi"] = int(vlan_match.group(1)) if vlan_match else None
                    mgmt["ip_address"] = match.group(1)
                    mgmt["subnet_mask"] = match.group(2)
                    break

        # Default gateway
        gateway_obj = self.parse.find_objects(r'^ip\s+default-gateway\s+')
        if gateway_obj:
            match = re.search(r'^ip\s+default-gateway\s+(\S+)', gateway_obj[0].text)
            if match:
                mgmt["default_gateway"] = match.group(1)

        # SSH configuration
        ssh_version = self.parse.find_objects(r'^ip\s+ssh\s+version\s+')
        if ssh_version:
            match = re.search(r'^ip\s+ssh\s+version\s+(\S+)', ssh_version[0].text)
            if match:
                mgmt["ssh"]["version"] = match.group(1)

        ssh_timeout = self.parse.find_objects(r'^ip\s+ssh\s+time-out\s+')
        if ssh_timeout:
            match = re.search(r'^ip\s+ssh\s+time-out\s+(\S+)', ssh_timeout[0].text)
            if match:
                mgmt["ssh"]["timeout"] = match.group(1)

        # Console line configuration
        console_line = self.parse.find_objects(r'^line\s+con\s+')
        if console_line:
            console_cfg = self._parse_line_config(console_line[0])
            mgmt["console"] = console_cfg

        # VTY line configuration
        vty_line = self.parse.find_objects(r'^line\s+vty\s+')
        if vty_line:
            vty_cfg = self._parse_line_config(vty_line[0])
            mgmt["vty"] = vty_cfg

        # Banner
        banner_obj = self.parse.find_objects(r'^banner\s+login\s+')
        if banner_obj:
            mgmt["banner"] = "Configured"

        return mgmt

    def _parse_line_config(self, line_obj) -> Dict[str, Any]:
        """Parse line (console/vty) configuration."""
        cfg = {
            "range": line_obj.text.strip(),
            "authentication": None,
            "transport_input": None,
            "access_class": None,
            "exec_timeout": None,
            "logging_synchronous": False
        }

        # Authentication
        auth = line_obj.re_search_children(r'^\s+login\s+authentication\s+')
        if auth:
            match = re.search(r'^\s+login\s+authentication\s+(\S+)', auth[0].text)
            if match:
                cfg["authentication"] = match.group(1)
        elif line_obj.re_search_children(r'^\s+login\s+local'):
            cfg["authentication"] = "local"
        elif line_obj.re_search_children(r'^\s+login'):
            cfg["authentication"] = "line"

        # Transport input
        transport = line_obj.re_search_children(r'^\s+transport\s+input\s+')
        if transport:
            match = re.search(r'^\s+transport\s+input\s+(.+)', transport[0].text)
            if match:
                cfg["transport_input"] = match.group(1).strip().split()

        # Access class (ACL)
        acl = line_obj.re_search_children(r'^\s+access-class\s+')
        if acl:
            match = re.search(r'^\s+access-class\s+(\S+)\s+(\S+)', acl[0].text)
            if match:
                cfg["access_class"] = {"acl": match.group(1), "direction": match.group(2)}

        # Logging synchronous
        if line_obj.re_search_children(r'^\s+logging\s+synchronous'):
            cfg["logging_synchronous"] = True

        return cfg

    def _extract_aaa_config(self) -> Dict[str, Any]:
        """Extract AAA configuration."""
        aaa = {
            "enabled": False,
            "authentication": [],
            "authorization": [],
            "accounting": [],
            "tacacs_servers": [],
            "radius_servers": [],
            "local_users": []
        }

        # Check if AAA is enabled
        if self.parse.find_objects(r'^aaa\s+new-model'):
            aaa["enabled"] = True

        # Authentication lists
        auth_objs = self.parse.find_objects(r'^aaa\s+authentication\s+')
        for obj in auth_objs:
            aaa["authentication"].append(obj.text.strip())

        # Authorization
        authz_objs = self.parse.find_objects(r'^aaa\s+authorization\s+')
        for obj in authz_objs:
            aaa["authorization"].append(obj.text.strip())

        # Accounting
        acct_objs = self.parse.find_objects(r'^aaa\s+accounting\s+')
        for obj in acct_objs:
            aaa["accounting"].append(obj.text.strip())

        # TACACS+ servers
        tacacs_objs = self.parse.find_objects(r'^tacacs-server\s+host\s+')
        for obj in tacacs_objs:
            match = re.search(r'^tacacs-server\s+host\s+(\S+)', obj.text)
            if match:
                aaa["tacacs_servers"].append(match.group(1))

        # RADIUS servers
        radius_objs = self.parse.find_objects(r'^radius-server\s+host\s+')
        for obj in radius_objs:
            match = re.search(r'^radius-server\s+host\s+(\S+)', obj.text)
            if match:
                aaa["radius_servers"].append(match.group(1))

        # Local users
        user_objs = self.parse.find_objects(r'^username\s+')
        for obj in user_objs:
            match = re.search(r'^username\s+(\S+)\s+privilege\s+(\d+)', obj.text)
            if match:
                aaa["local_users"].append({
                    "username": match.group(1),
                    "privilege": int(match.group(2))
                })
            else:
                match = re.search(r'^username\s+(\S+)', obj.text)
                if match:
                    aaa["local_users"].append({
                        "username": match.group(1),
                        "privilege": None
                    })

        return aaa

    def _extract_vlans(self) -> Dict[str, Any]:
        """Extract VLAN configuration."""
        vlans = {
            "vlan_ids": [],
            "vlan_names": {},  # {vlan_id: name}
            "svi_interfaces": [],
            "vtp": {
                "mode": None,
                "domain": None,
                "version": None
            }
        }

        # Find all VLAN IDs referenced in the config
        vlan_ids_set = set()

        # VLANs from interface configurations
        access_ports = self.parse.find_objects(r'^\s+switchport\s+access\s+vlan\s+')
        for port in access_ports:
            match = re.search(r'^\s+switchport\s+access\s+vlan\s+(\d+)', port.text)
            if match:
                vlan_ids_set.add(int(match.group(1)))

        # VLANs from trunk allowed lists
        trunk_allowed = self.parse.find_objects(r'^\s+switchport\s+trunk\s+allowed\s+vlan\s+')
        for trunk in trunk_allowed:
            match = re.search(r'^\s+switchport\s+trunk\s+allowed\s+vlan\s+(.+)', trunk.text)
            if match:
                vlan_list = match.group(1).strip()
                vlan_ids_set.update(self._parse_vlan_list(vlan_list))

        # VLANs from native VLAN
        native_vlan = self.parse.find_objects(r'^\s+switchport\s+trunk\s+native\s+vlan\s+')
        for native in native_vlan:
            match = re.search(r'^\s+switchport\s+trunk\s+native\s+vlan\s+(\d+)', native.text)
            if match:
                vlan_ids_set.add(int(match.group(1)))

        # VLANs from STP configuration
        stp_vlan = self.parse.find_objects(r'^spanning-tree\s+vlan\s+')
        for stp in stp_vlan:
            match = re.search(r'^spanning-tree\s+vlan\s+(.+?)\s+', stp.text)
            if match:
                vlan_list = match.group(1).strip()
                vlan_ids_set.update(self._parse_vlan_list(vlan_list))

        # VLANs from DHCP snooping
        dhcp_snoop = self.parse.find_objects(r'^ip\s+dhcp\s+snooping\s+vlan\s+')
        for dhcp in dhcp_snoop:
            match = re.search(r'^ip\s+dhcp\s+snooping\s+vlan\s+(.+)', dhcp.text)
            if match:
                vlan_list = match.group(1).strip()
                vlan_ids_set.update(self._parse_vlan_list(vlan_list))

        # VLANs from DAI
        dai_vlan = self.parse.find_objects(r'^ip\s+arp\s+inspection\s+vlan\s+')
        for dai in dai_vlan:
            match = re.search(r'^ip\s+arp\s+inspection\s+vlan\s+(.+)', dai.text)
            if match:
                vlan_list = match.group(1).strip()
                vlan_ids_set.update(self._parse_vlan_list(vlan_list))

        vlans["vlan_ids"] = sorted(list(vlan_ids_set))

        # Extract VLAN names from explicit VLAN declarations
        vlan_declarations = self.parse.find_objects(r'^vlan\s+\d+')
        for vlan_decl in vlan_declarations:
            # Get VLAN ID
            vlan_match = re.search(r'^vlan\s+(\d+)', vlan_decl.text)
            if not vlan_match:
                continue

            vlan_id = int(vlan_match.group(1))

            # Get VLAN name
            name_lines = vlan_decl.re_search_children(r'^\s+name\s+')
            if name_lines:
                name_match = re.search(r'^\s+name\s+(.+)', name_lines[0].text)
                if name_match:
                    vlans["vlan_names"][vlan_id] = name_match.group(1).strip()
                    # Also add to vlan_ids if not already there
                    if vlan_id not in vlan_ids_set:
                        vlan_ids_set.add(vlan_id)

        # Update vlan_ids list with any VLANs found in declarations
        vlans["vlan_ids"] = sorted(list(vlan_ids_set))

        # VLAN interfaces (SVIs)
        vlan_intfs = self.parse.find_objects(r'^interface\s+Vlan')
        for vlan_intf in vlan_intfs:
            vlan_match = re.search(r'interface\s+Vlan(\d+)', vlan_intf.text)
            if not vlan_match:
                continue

            vlan_id = int(vlan_match.group(1))

            svi_info = {
                "vlan_id": vlan_id,
                "description": None,
                "ip_address": None,
                "subnet_mask": None,
                "shutdown": False,
                "acl_in": None,
                "acl_out": None,
                "hsrp": [],  # List of HSRP groups
                "vrrp": []   # List of VRRP groups
            }

            # Description
            desc = vlan_intf.re_search_children(r'^\s+description\s+')
            if desc:
                match = re.search(r'^\s+description\s+(.+)', desc[0].text)
                if match:
                    svi_info["description"] = match.group(1).strip()

            # IP address
            ip_addr = vlan_intf.re_search_children(r'^\s+ip\s+address\s+')
            if ip_addr:
                match = re.search(r'^\s+ip\s+address\s+(\S+)\s+(\S+)', ip_addr[0].text)
                if match:
                    svi_info["ip_address"] = match.group(1)
                    svi_info["subnet_mask"] = match.group(2)

            # Shutdown status
            if vlan_intf.re_search_children(r'^\s+shutdown'):
                svi_info["shutdown"] = True

            # ACLs
            acl_in = vlan_intf.re_search_children(r'^\s+ip\s+access-group\s+\S+\s+in')
            if acl_in:
                match = re.search(r'^\s+ip\s+access-group\s+(\S+)\s+in', acl_in[0].text)
                if match:
                    svi_info["acl_in"] = match.group(1)

            acl_out = vlan_intf.re_search_children(r'^\s+ip\s+access-group\s+\S+\s+out')
            if acl_out:
                match = re.search(r'^\s+ip\s+access-group\s+(\S+)\s+out', acl_out[0].text)
                if match:
                    svi_info["acl_out"] = match.group(1)

            # HSRP - Extract detailed configuration
            hsrp_lines = vlan_intf.re_search_children(r'^\s+standby\s+')
            hsrp_groups = {}  # Track groups to aggregate config

            for hsrp_line in hsrp_lines:
                # Extract group number and parse different HSRP commands
                # Format: standby <group> <command>
                group_match = re.search(r'^\s+standby\s+(\d+)\s+(.+)', hsrp_line.text)
                if group_match:
                    group_num = int(group_match.group(1))
                    config = group_match.group(2).strip()

                    # Initialize group if not exists
                    if group_num not in hsrp_groups:
                        hsrp_groups[group_num] = {
                            "group": group_num,
                            "virtual_ip": None,
                            "priority": None,
                            "preempt": False,
                            "track": []
                        }

                    # Parse specific HSRP config
                    if config.startswith('ip '):
                        # Virtual IP: standby 1 ip 192.168.1.1
                        ip_match = re.search(r'ip\s+(\S+)', config)
                        if ip_match:
                            hsrp_groups[group_num]["virtual_ip"] = ip_match.group(1)

                    elif config.startswith('priority '):
                        # Priority: standby 1 priority 110
                        priority_match = re.search(r'priority\s+(\d+)', config)
                        if priority_match:
                            hsrp_groups[group_num]["priority"] = int(priority_match.group(1))

                    elif config.startswith('preempt'):
                        # Preempt: standby 1 preempt
                        hsrp_groups[group_num]["preempt"] = True

                    elif config.startswith('track'):
                        # Track: standby 1 track 1 decrement 20
                        track_match = re.search(r'track\s+(\d+)(?:\s+decrement\s+(\d+))?', config)
                        if track_match:
                            track_info = {
                                "object": int(track_match.group(1)),
                                "decrement": int(track_match.group(2)) if track_match.group(2) else None
                            }
                            hsrp_groups[group_num]["track"].append(track_info)

            # Convert groups dict to list
            svi_info["hsrp"] = list(hsrp_groups.values())

            # VRRP - Extract detailed configuration
            vrrp_lines = vlan_intf.re_search_children(r'^\s+vrrp\s+')
            vrrp_groups = {}  # Track groups to aggregate config

            for vrrp_line in vrrp_lines:
                # Extract group number and parse different VRRP commands
                # Format: vrrp <group> <command>
                group_match = re.search(r'^\s+vrrp\s+(\d+)\s+(.+)', vrrp_line.text)
                if group_match:
                    group_num = int(group_match.group(1))
                    config = group_match.group(2).strip()

                    # Initialize group if not exists
                    if group_num not in vrrp_groups:
                        vrrp_groups[group_num] = {
                            "group": group_num,
                            "virtual_ip": None,
                            "priority": None,
                            "preempt": False,
                            "track": []
                        }

                    # Parse specific VRRP config
                    if config.startswith('ip '):
                        # Virtual IP: vrrp 1 ip 192.168.1.1
                        ip_match = re.search(r'ip\s+(\S+)', config)
                        if ip_match:
                            vrrp_groups[group_num]["virtual_ip"] = ip_match.group(1)

                    elif config.startswith('priority '):
                        # Priority: vrrp 1 priority 110
                        priority_match = re.search(r'priority\s+(\d+)', config)
                        if priority_match:
                            vrrp_groups[group_num]["priority"] = int(priority_match.group(1))

                    elif config.startswith('preempt'):
                        # Preempt: vrrp 1 preempt
                        vrrp_groups[group_num]["preempt"] = True

                    elif config.startswith('track'):
                        # Track: vrrp 1 track 1 decrement 20
                        track_match = re.search(r'track\s+(\d+)(?:\s+decrement\s+(\d+))?', config)
                        if track_match:
                            track_info = {
                                "object": int(track_match.group(1)),
                                "decrement": int(track_match.group(2)) if track_match.group(2) else None
                            }
                            vrrp_groups[group_num]["track"].append(track_info)

            # Convert groups dict to list
            svi_info["vrrp"] = list(vrrp_groups.values())

            vlans["svi_interfaces"].append(svi_info)

        # VTP configuration
        vtp_mode = self.parse.find_objects(r'^vtp\s+mode\s+')
        if vtp_mode:
            match = re.search(r'^vtp\s+mode\s+(\S+)', vtp_mode[0].text)
            if match:
                vlans["vtp"]["mode"] = match.group(1)

        vtp_domain = self.parse.find_objects(r'^vtp\s+domain\s+')
        if vtp_domain:
            match = re.search(r'^vtp\s+domain\s+(\S+)', vtp_domain[0].text)
            if match:
                vlans["vtp"]["domain"] = match.group(1)

        vtp_version = self.parse.find_objects(r'^vtp\s+version\s+')
        if vtp_version:
            match = re.search(r'^vtp\s+version\s+(\S+)', vtp_version[0].text)
            if match:
                vlans["vtp"]["version"] = match.group(1)

        return vlans

    def _parse_vlan_list(self, vlan_string: str) -> set:
        """Parse VLAN list string (e.g., '1-10,20,30-35') into set of VLAN IDs."""
        vlan_set = set()
        parts = vlan_string.split(',')

        for part in parts:
            part = part.strip()
            if '-' in part:
                # Range
                start, end = part.split('-')
                try:
                    vlan_set.update(range(int(start), int(end) + 1))
                except ValueError:
                    pass
            else:
                # Single VLAN
                try:
                    vlan_set.add(int(part))
                except ValueError:
                    pass

        return vlan_set

    def _extract_interfaces(self) -> List[Dict[str, Any]]:
        """Extract all interface configurations."""
        interfaces = []

        # Get all interfaces
        intf_objs = self.parse.find_objects(r'^interface\s+')

        for intf_obj in intf_objs:
            # Skip VLAN interfaces (handled in VLANs section)
            if 'Vlan' in intf_obj.text:
                continue

            intf_info = {
                "name": None,
                "description": None,
                "mode": None,  # access, trunk, routed
                "access_vlan": None,
                "trunk_encapsulation": None,
                "trunk_native_vlan": None,
                "trunk_allowed_vlans": [],
                "shutdown": False,
                "speed": None,
                "duplex": None,
                "port_security": {
                    "enabled": False,
                    "max_macs": None,
                    "violation": None,
                    "sticky": False,
                    "aging_time": None,
                    "sticky_macs": []
                },
                "spanning_tree": {
                    "portfast": False,
                    "bpduguard": False,
                    "rootguard": False,
                    "loopguard": False
                },
                "storm_control": {
                    "broadcast": None,
                    "multicast": None,
                    "unicast": None
                },
                "dhcp_snooping_trust": False,
                "dhcp_snooping_limit": None,
                "arp_inspection_trust": False,
                "channel_group": {
                    "number": None,
                    "mode": None  # active, passive, desirable, auto, on
                },
                "ip_address": None,
                "subnet_mask": None
            }

            # Interface name
            match = re.search(r'^interface\s+(\S+)', intf_obj.text)
            if match:
                intf_info["name"] = match.group(1)

            # Description
            desc = intf_obj.re_search_children(r'^\s+description\s+')
            if desc:
                match = re.search(r'^\s+description\s+(.+)', desc[0].text)
                if match:
                    intf_info["description"] = match.group(1).strip()

            # Shutdown
            if intf_obj.re_search_children(r'^\s+shutdown'):
                intf_info["shutdown"] = True

            # Switchport mode
            mode_obj = intf_obj.re_search_children(r'^\s+switchport\s+mode\s+')
            if mode_obj:
                match = re.search(r'^\s+switchport\s+mode\s+(\S+)', mode_obj[0].text)
                if match:
                    intf_info["mode"] = match.group(1)

            # Access VLAN
            access_vlan = intf_obj.re_search_children(r'^\s+switchport\s+access\s+vlan\s+')
            if access_vlan:
                match = re.search(r'^\s+switchport\s+access\s+vlan\s+(\d+)', access_vlan[0].text)
                if match:
                    intf_info["access_vlan"] = int(match.group(1))

            # Trunk encapsulation
            trunk_enc = intf_obj.re_search_children(r'^\s+switchport\s+trunk\s+encapsulation\s+')
            if trunk_enc:
                match = re.search(r'^\s+switchport\s+trunk\s+encapsulation\s+(\S+)', trunk_enc[0].text)
                if match:
                    intf_info["trunk_encapsulation"] = match.group(1)

            # Native VLAN
            native_vlan = intf_obj.re_search_children(r'^\s+switchport\s+trunk\s+native\s+vlan\s+')
            if native_vlan:
                match = re.search(r'^\s+switchport\s+trunk\s+native\s+vlan\s+(\d+)', native_vlan[0].text)
                if match:
                    intf_info["trunk_native_vlan"] = int(match.group(1))

            # Allowed VLANs
            allowed_vlans = intf_obj.re_search_children(r'^\s+switchport\s+trunk\s+allowed\s+vlan\s+')
            if allowed_vlans:
                match = re.search(r'^\s+switchport\s+trunk\s+allowed\s+vlan\s+(.+)', allowed_vlans[0].text)
                if match:
                    vlan_list = match.group(1).strip()
                    intf_info["trunk_allowed_vlans"] = sorted(list(self._parse_vlan_list(vlan_list)))

            # Port security
            if intf_obj.re_search_children(r'^\s+switchport\s+port-security'):
                intf_info["port_security"]["enabled"] = True

                # Max MACs
                max_mac = intf_obj.re_search_children(r'^\s+switchport\s+port-security\s+maximum\s+')
                if max_mac:
                    match = re.search(r'^\s+switchport\s+port-security\s+maximum\s+(\d+)', max_mac[0].text)
                    if match:
                        intf_info["port_security"]["max_macs"] = int(match.group(1))

                # Violation mode
                violation = intf_obj.re_search_children(r'^\s+switchport\s+port-security\s+violation\s+')
                if violation:
                    match = re.search(r'^\s+switchport\s+port-security\s+violation\s+(\S+)', violation[0].text)
                    if match:
                        intf_info["port_security"]["violation"] = match.group(1)

                # Sticky MAC learning
                if intf_obj.re_search_children(r'^\s+switchport\s+port-security\s+mac-address\s+sticky'):
                    intf_info["port_security"]["sticky"] = True

                # Sticky MACs
                sticky_macs = intf_obj.re_search_children(r'^\s+switchport\s+port-security\s+mac-address\s+sticky\s+[0-9A-Fa-f]')
                for mac in sticky_macs:
                    match = re.search(r'^\s+switchport\s+port-security\s+mac-address\s+sticky\s+([0-9A-Fa-f.]+)', mac.text)
                    if match:
                        intf_info["port_security"]["sticky_macs"].append(match.group(1))

                # Aging time
                aging = intf_obj.re_search_children(r'^\s+switchport\s+port-security\s+aging\s+time\s+')
                if aging:
                    match = re.search(r'^\s+switchport\s+port-security\s+aging\s+time\s+(\d+)', aging[0].text)
                    if match:
                        intf_info["port_security"]["aging_time"] = int(match.group(1))

            # Spanning tree
            if intf_obj.re_search_children(r'^\s+spanning-tree\s+portfast'):
                intf_info["spanning_tree"]["portfast"] = True

            if intf_obj.re_search_children(r'^\s+spanning-tree\s+bpduguard\s+enable'):
                intf_info["spanning_tree"]["bpduguard"] = True

            if intf_obj.re_search_children(r'^\s+spanning-tree\s+guard\s+root'):
                intf_info["spanning_tree"]["rootguard"] = True

            if intf_obj.re_search_children(r'^\s+spanning-tree\s+guard\s+loop'):
                intf_info["spanning_tree"]["loopguard"] = True

            # Storm control
            bc_storm = intf_obj.re_search_children(r'^\s+storm-control\s+broadcast\s+level\s+')
            if bc_storm:
                match = re.search(r'^\s+storm-control\s+broadcast\s+level\s+(\S+)', bc_storm[0].text)
                if match:
                    intf_info["storm_control"]["broadcast"] = match.group(1)

            mc_storm = intf_obj.re_search_children(r'^\s+storm-control\s+multicast\s+level\s+')
            if mc_storm:
                match = re.search(r'^\s+storm-control\s+multicast\s+level\s+(\S+)', mc_storm[0].text)
                if match:
                    intf_info["storm_control"]["multicast"] = match.group(1)

            uc_storm = intf_obj.re_search_children(r'^\s+storm-control\s+unicast\s+level\s+')
            if uc_storm:
                match = re.search(r'^\s+storm-control\s+unicast\s+level\s+(\S+)', uc_storm[0].text)
                if match:
                    intf_info["storm_control"]["unicast"] = match.group(1)

            # DHCP snooping
            if intf_obj.re_search_children(r'^\s+ip\s+dhcp\s+snooping\s+trust'):
                intf_info["dhcp_snooping_trust"] = True

            dhcp_limit = intf_obj.re_search_children(r'^\s+ip\s+dhcp\s+snooping\s+limit\s+rate\s+')
            if dhcp_limit:
                match = re.search(r'^\s+ip\s+dhcp\s+snooping\s+limit\s+rate\s+(\d+)', dhcp_limit[0].text)
                if match:
                    intf_info["dhcp_snooping_limit"] = int(match.group(1))

            # ARP inspection trust
            if intf_obj.re_search_children(r'^\s+ip\s+arp\s+inspection\s+trust'):
                intf_info["arp_inspection_trust"] = True

            # Channel group
            channel = intf_obj.re_search_children(r'^\s+channel-group\s+')
            if channel:
                match = re.search(r'^\s+channel-group\s+(\d+)\s+mode\s+(\S+)', channel[0].text)
                if match:
                    intf_info["channel_group"]["number"] = int(match.group(1))
                    intf_info["channel_group"]["mode"] = match.group(2)

            # IP address (for routed interfaces)
            ip_addr = intf_obj.re_search_children(r'^\s+ip\s+address\s+')
            if ip_addr:
                match = re.search(r'^\s+ip\s+address\s+(\S+)\s+(\S+)', ip_addr[0].text)
                if match:
                    intf_info["ip_address"] = match.group(1)
                    intf_info["subnet_mask"] = match.group(2)

            # Speed/duplex
            speed = intf_obj.re_search_children(r'^\s+speed\s+')
            if speed:
                match = re.search(r'^\s+speed\s+(\S+)', speed[0].text)
                if match:
                    intf_info["speed"] = match.group(1)

            duplex = intf_obj.re_search_children(r'^\s+duplex\s+')
            if duplex:
                match = re.search(r'^\s+duplex\s+(\S+)', duplex[0].text)
                if match:
                    intf_info["duplex"] = match.group(1)

            interfaces.append(intf_info)

        return interfaces

    def _extract_routing(self) -> Dict[str, Any]:
        """Extract routing configuration."""
        routing = {
            "ip_routing_enabled": False,
            "default_gateway": None,
            "static_routes": [],
            "routing_protocols": []
        }

        # Check if IP routing is enabled
        if self.parse.find_objects(r'^ip\s+routing'):
            routing["ip_routing_enabled"] = True

        # Default gateway
        gateway = self.parse.find_objects(r'^ip\s+default-gateway\s+')
        if gateway:
            match = re.search(r'^ip\s+default-gateway\s+(\S+)', gateway[0].text)
            if match:
                routing["default_gateway"] = match.group(1)

        # Static routes
        static_routes = self.parse.find_objects(r'^ip\s+route\s+')
        for route in static_routes:
            match = re.search(r'^ip\s+route\s+(\S+)\s+(\S+)\s+(\S+)', route.text)
            if match:
                routing["static_routes"].append({
                    "network": match.group(1),
                    "mask": match.group(2),
                    "next_hop": match.group(3)
                })

        # Routing protocols
        if self.parse.find_objects(r'^router\s+ospf\s+'):
            routing["routing_protocols"].append("OSPF")

        if self.parse.find_objects(r'^router\s+eigrp\s+'):
            routing["routing_protocols"].append("EIGRP")

        if self.parse.find_objects(r'^router\s+rip'):
            routing["routing_protocols"].append("RIP")

        if self.parse.find_objects(r'^router\s+bgp\s+'):
            routing["routing_protocols"].append("BGP")

        return routing

    def _extract_spanning_tree(self) -> Dict[str, Any]:
        """Extract spanning tree configuration (PVST+, Rapid-PVST+, MST)."""
        stp = {
            "mode": None,
            "vlan_priorities": {},
            "global_features": [],
            "mst_configuration": None  # For MST mode
        }

        # STP mode
        mode_obj = self.parse.find_objects(r'^spanning-tree\s+mode\s+')
        if mode_obj:
            match = re.search(r'^spanning-tree\s+mode\s+(\S+)', mode_obj[0].text)
            if match:
                stp["mode"] = match.group(1)

        # Per-VLAN priorities (PVST/Rapid-PVST)
        priority_objs = self.parse.find_objects(r'^spanning-tree\s+vlan\s+.+\s+priority\s+')
        for obj in priority_objs:
            match = re.search(r'^spanning-tree\s+vlan\s+(.+?)\s+priority\s+(\d+)', obj.text)
            if match:
                vlan_list_str = match.group(1).strip()
                priority = int(match.group(2))
                vlan_ids = self._parse_vlan_list(vlan_list_str)
                for vlan_id in vlan_ids:
                    stp["vlan_priorities"][vlan_id] = priority

        # MST Configuration
        mst_config_obj = self.parse.find_objects(r'^spanning-tree\s+mst\s+configuration')
        if mst_config_obj:
            stp["mst_configuration"] = {
                "name": None,
                "revision": None,
                "instances": {}
            }

            # MST region name
            name_obj = mst_config_obj[0].re_search_children(r'^\s+name\s+')
            if name_obj:
                match = re.search(r'^\s+name\s+(.+)', name_obj[0].text)
                if match:
                    stp["mst_configuration"]["name"] = match.group(1).strip()

            # MST revision
            rev_obj = mst_config_obj[0].re_search_children(r'^\s+revision\s+')
            if rev_obj:
                match = re.search(r'^\s+revision\s+(\d+)', rev_obj[0].text)
                if match:
                    stp["mst_configuration"]["revision"] = int(match.group(1))

        # MST instance priorities
        mst_priority = self.parse.find_objects(r'^spanning-tree\s+mst\s+\d+\s+priority\s+')
        if mst_priority and stp["mst_configuration"]:
            for obj in mst_priority:
                match = re.search(r'^spanning-tree\s+mst\s+(\d+)\s+priority\s+(\d+)', obj.text)
                if match:
                    instance = int(match.group(1))
                    priority = int(match.group(2))
                    stp["mst_configuration"]["instances"][instance] = {"priority": priority}

        # Global STP features
        if self.parse.find_objects(r'^spanning-tree\s+portfast\s+default'):
            stp["global_features"].append("portfast-default")

        if self.parse.find_objects(r'^spanning-tree\s+extend\s+system-id'):
            stp["global_features"].append("extend-system-id")

        if self.parse.find_objects(r'^spanning-tree\s+uplinkfast'):
            stp["global_features"].append("uplinkfast")

        if self.parse.find_objects(r'^spanning-tree\s+backbonefast'):
            stp["global_features"].append("backbonefast")

        return stp

    def _extract_security_features(self) -> Dict[str, Any]:
        """Extract security feature configurations."""
        security = {
            "dhcp_snooping": {
                "enabled": False,
                "vlans": [],
                "information_option": True
            },
            "arp_inspection": {
                "enabled": False,
                "vlans": []
            },
            "ip_source_guard": False,
            "acls": [],
            "cdp_enabled": True,
            "lldp_enabled": False,
            "dot1x_enabled": False
        }

        # DHCP snooping
        if self.parse.find_objects(r'^ip\s+dhcp\s+snooping'):
            security["dhcp_snooping"]["enabled"] = True

        dhcp_vlans = self.parse.find_objects(r'^ip\s+dhcp\s+snooping\s+vlan\s+')
        for obj in dhcp_vlans:
            match = re.search(r'^ip\s+dhcp\s+snooping\s+vlan\s+(.+)', obj.text)
            if match:
                vlan_list = match.group(1).strip()
                security["dhcp_snooping"]["vlans"] = sorted(list(self._parse_vlan_list(vlan_list)))

        if self.parse.find_objects(r'^no\s+ip\s+dhcp\s+snooping\s+information\s+option'):
            security["dhcp_snooping"]["information_option"] = False

        # ARP inspection
        dai_vlans = self.parse.find_objects(r'^ip\s+arp\s+inspection\s+vlan\s+')
        if dai_vlans:
            security["arp_inspection"]["enabled"] = True
            for obj in dai_vlans:
                match = re.search(r'^ip\s+arp\s+inspection\s+vlan\s+(.+)', obj.text)
                if match:
                    vlan_list = match.group(1).strip()
                    security["arp_inspection"]["vlans"] = sorted(list(self._parse_vlan_list(vlan_list)))

        # IP Source Guard
        if self.parse.find_objects(r'^\s+ip\s+verify\s+source'):
            security["ip_source_guard"] = True

        # ACLs
        acl_objs = self.parse.find_objects(r'^ip\s+access-list\s+')
        for acl_obj in acl_objs:
            match = re.search(r'^ip\s+access-list\s+(standard|extended)\s+(\S+)', acl_obj.text)
            if match:
                acl_info = {
                    "type": match.group(1),
                    "name": match.group(2),
                    "entries": []
                }

                # Get ACL entries
                entries = acl_obj.re_search_children(r'^\s+(permit|deny)\s+')
                for entry in entries:
                    acl_info["entries"].append(entry.text.strip())

                security["acls"].append(acl_info)

        # Numbered ACLs
        numbered_acls = self.parse.find_objects(r'^access-list\s+\d+\s+')
        for acl_obj in numbered_acls:
            match = re.search(r'^access-list\s+(\d+)\s+(permit|deny)\s+(.+)', acl_obj.text)
            if match:
                acl_num = match.group(1)
                # Check if we already have this ACL
                existing = next((a for a in security["acls"] if a.get("number") == acl_num), None)
                if not existing:
                    acl_info = {
                        "type": "standard" if int(acl_num) < 100 else "extended",
                        "number": acl_num,
                        "entries": [acl_obj.text.strip()]
                    }
                    security["acls"].append(acl_info)
                else:
                    existing["entries"].append(acl_obj.text.strip())

        # CDP
        if self.parse.find_objects(r'^no\s+cdp\s+run'):
            security["cdp_enabled"] = False

        # LLDP
        if self.parse.find_objects(r'^lldp\s+run'):
            security["lldp_enabled"] = True

        # 802.1X
        if self.parse.find_objects(r'^aaa\s+.*\s+dot1x'):
            security["dot1x_enabled"] = True

        return security

    def _extract_network_services(self) -> Dict[str, Any]:
        """Extract network services configuration."""
        services = {
            "ntp": {
                "enabled": False,
                "servers": [],
                "authentication": False
            },
            "syslog": {
                "enabled": False,
                "servers": []
            },
            "snmp": {
                "enabled": False,
                "version": None
            },
            "dns": {
                "domain_name": None,
                "domain_lookup": True,
                "name_servers": []
            }
        }

        # NTP
        ntp_servers = self.parse.find_objects(r'^ntp\s+server\s+')
        if ntp_servers:
            services["ntp"]["enabled"] = True
            for obj in ntp_servers:
                match = re.search(r'^ntp\s+server\s+(\S+)', obj.text)
                if match:
                    services["ntp"]["servers"].append(match.group(1))

        if self.parse.find_objects(r'^ntp\s+authenticate'):
            services["ntp"]["authentication"] = True

        # Syslog
        logging_servers = self.parse.find_objects(r'^logging\s+\d+\.\d+\.\d+\.\d+')
        if logging_servers:
            services["syslog"]["enabled"] = True
            for obj in logging_servers:
                match = re.search(r'^logging\s+(\S+)', obj.text)
                if match:
                    services["syslog"]["servers"].append(match.group(1))

        # SNMP
        if self.parse.find_objects(r'^snmp-server\s+'):
            services["snmp"]["enabled"] = True

            if self.parse.find_objects(r'^snmp-server\s+.*\s+v3'):
                services["snmp"]["version"] = "v3"
            elif self.parse.find_objects(r'^snmp-server\s+community\s+'):
                services["snmp"]["version"] = "v2c"

        # DNS
        domain_name = self.parse.find_objects(r'^ip\s+domain[_-]name\s+')
        if domain_name:
            match = re.search(r'^ip\s+domain[_-]name\s+(\S+)', domain_name[0].text)
            if match:
                services["dns"]["domain_name"] = match.group(1)

        if self.parse.find_objects(r'^no\s+ip\s+domain[_-]lookup'):
            services["dns"]["domain_lookup"] = False

        name_servers = self.parse.find_objects(r'^ip\s+name-server\s+')
        for obj in name_servers:
            match = re.search(r'^ip\s+name-server\s+(\S+)', obj.text)
            if match:
                services["dns"]["name_servers"].append(match.group(1))

        return services

    def _extract_qos_config(self) -> Dict[str, Any]:
        """
        Extract QoS/CoS configuration (common on distribution/core switches).

        Returns:
            Dictionary containing QoS configuration
        """
        qos = {
            "enabled": False,
            "class_maps": [],
            "policy_maps": [],
            "service_policies": []
        }

        # MLS QoS (Modular QoS CLI) - common on Catalyst switches
        if self.parse.find_objects(r'^mls\s+qos'):
            qos["enabled"] = True

        # Class maps
        class_maps = self.parse.find_objects(r'^class-map\s+')
        for cm in class_maps:
            match = re.search(r'^class-map\s+(?:match-\w+\s+)?(\S+)', cm.text)
            if match:
                class_name = match.group(1)
                class_info = {
                    "name": class_name,
                    "match_criteria": []
                }

                # Extract match criteria
                matches = cm.re_search_children(r'^\s+match\s+')
                for m in matches:
                    class_info["match_criteria"].append(m.text.strip())

                qos["class_maps"].append(class_info)

        # Policy maps
        policy_maps = self.parse.find_objects(r'^policy-map\s+')
        for pm in policy_maps:
            match = re.search(r'^policy-map\s+(\S+)', pm.text)
            if match:
                policy_name = match.group(1)
                policy_info = {
                    "name": policy_name,
                    "classes": []
                }

                # Extract class associations
                classes = pm.re_search_children(r'^\s+class\s+')
                for cls in classes:
                    class_match = re.search(r'^\s+class\s+(\S+)', cls.text)
                    if class_match:
                        policy_info["classes"].append(class_match.group(1))

                qos["policy_maps"].append(policy_info)

        # Service policies (where applied)
        all_interfaces = self.parse.find_objects(r'^interface\s+')
        for intf in all_interfaces:
            service_policies = intf.re_search_children(r'^\s+service-policy\s+')
            for sp in service_policies:
                match = re.search(r'^\s+service-policy\s+(input|output)\s+(\S+)', sp.text)
                if match:
                    direction = match.group(1)
                    policy_name = match.group(2)
                    intf_match = re.search(r'^interface\s+(\S+)', intf.text)
                    if intf_match:
                        qos["service_policies"].append({
                            "interface": intf_match.group(1),
                            "direction": direction,
                            "policy_map": policy_name
                        })

        return qos

    def _extract_stacking_config(self) -> Dict[str, Any]:
        """
        Extract switch stack configuration (Catalyst 3750/3850/9300 series).

        Returns:
            Dictionary containing stacking configuration
        """
        stacking = {
            "enabled": False,
            "stack_members": [],
            "priority": {}
        }

        # Catalyst 3750/3850/9300 style stacking
        stack_objs = self.parse.find_objects(r'^switch\s+\d+\s+')
        if stack_objs:
            stacking["enabled"] = True

            for obj in stack_objs:
                # Extract switch number and priority
                match = re.search(r'^switch\s+(\d+)\s+priority\s+(\d+)', obj.text)
                if match:
                    member_id = int(match.group(1))
                    priority = int(match.group(2))

                    if member_id not in stacking["stack_members"]:
                        stacking["stack_members"].append(member_id)
                    stacking["priority"][member_id] = priority
                else:
                    # Just switch number without priority
                    match = re.search(r'^switch\s+(\d+)', obj.text)
                    if match:
                        member_id = int(match.group(1))
                        if member_id not in stacking["stack_members"]:
                            stacking["stack_members"].append(member_id)

        # Sort stack members
        stacking["stack_members"].sort()

        return stacking


def parse_config_to_json(config_file_path: str, output_json_path: Optional[str] = None, sanitize_secrets: bool = False) -> Dict[str, Any]:
    """
    Parse a Cisco IOS configuration file and return structured JSON.

    Args:
        config_file_path: Path to the configuration file
        output_json_path: Optional path to save JSON output
        sanitize_secrets: Whether to redact sensitive information (passwords, keys, etc.)

    Returns:
        Dictionary containing structured configuration data
    """
    parser = CiscoConfigParser(config_file_path)
    parser.load_config()

    # Sanitize secrets if requested
    if sanitize_secrets:
        parser.config_text = parser.sanitize_secrets(parser.config_text)
        # Re-parse with sanitized config
        from pathlib import Path
        import tempfile

        # Create temporary file with sanitized config
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as tmp:
            tmp.write(parser.config_text)
            tmp_path = tmp.name

        # Re-parse with sanitized config
        parser.parse = CiscoConfParse(tmp_path, syntax='ios')

        # Clean up temp file
        Path(tmp_path).unlink()

    structured_data = parser.extract_all()

    if output_json_path:
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(structured_data, f, indent=2, ensure_ascii=False)

    return structured_data


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python config_parser.py <config_file> [output_json]")
        sys.exit(1)

    config_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"Parsing configuration: {config_file}")
    data = parse_config_to_json(config_file, output_file)

    if output_file:
        print(f"Structured data saved to: {output_file}")
    else:
        print(json.dumps(data, indent=2))
