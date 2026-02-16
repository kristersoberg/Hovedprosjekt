"""
Documentation Validator

Validates generated documentation against source configuration data.
Provides accuracy metrics for research evaluation.
"""

import re
import json
from typing import Dict, Any, List, Tuple
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class ValidationResult:
    """Result of validation check."""
    field_name: str
    expected_value: Any
    found_value: Any = None
    passed: bool = False
    location: str = None  # Where in markdown this was found
    error_message: str = None


@dataclass
class ValidationReport:
    """Complete validation report."""
    total_checks: int = 0
    passed_checks: int = 0
    failed_checks: int = 0
    warnings: List[str] = field(default_factory=list)
    results: List[ValidationResult] = field(default_factory=list)

    @property
    def accuracy_percentage(self) -> float:
        """Calculate accuracy percentage."""
        if self.total_checks == 0:
            return 0.0
        return (self.passed_checks / self.total_checks) * 100

    @property
    def hallucination_count(self) -> int:
        """Count of hallucinated (incorrect) facts."""
        return self.failed_checks

    def add_result(self, result: ValidationResult):
        """Add a validation result."""
        self.results.append(result)
        self.total_checks += 1
        if result.passed:
            self.passed_checks += 1
        else:
            self.failed_checks += 1

    def add_warning(self, message: str):
        """Add a warning."""
        self.warnings.append(message)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "total_checks": self.total_checks,
            "passed_checks": self.passed_checks,
            "failed_checks": self.failed_checks,
            "accuracy_percentage": round(self.accuracy_percentage, 2),
            "hallucination_count": self.hallucination_count,
            "warnings": self.warnings,
            "results": [
                {
                    "field": r.field_name,
                    "expected": str(r.expected_value),
                    "found": str(r.found_value) if r.found_value else "Not found",
                    "passed": r.passed,
                    "location": r.location,
                    "error": r.error_message
                }
                for r in self.results
            ]
        }


class DocumentationValidator:
    """Validate generated documentation against source data."""

    def __init__(self, structured_data: Dict[str, Any], markdown_content: str):
        """
        Initialize validator.

        Args:
            structured_data: Parsed configuration data
            markdown_content: Generated markdown documentation
        """
        self.data = structured_data
        self.markdown = markdown_content
        self.report = ValidationReport()

    # Values that are too short/generic to validate via presence check
    SKIP_VALUES = {
        "True", "False", "true", "false", "None", "none", "enabled", "disabled",
        "yes", "no", "up", "down", "active", "inactive", "default"
    }

    # Structured data keys to skip during generic validation (internal/meta fields)
    SKIP_KEYS = {
        "enabled", "shutdown", "count", "total", "raw_config"
    }

    # Phrases in LLM output that indicate "not configured" claims
    NEGATIVE_PHRASES = [
        r"[Nn]ot\s+configured",
        r"[Nn]ot\s+enabled",
        r"[Nn]o\s+\w+\s+configured",
        r"[Nn]one\s+configured",
        r"[Nn]ot\s+present",
        r"[Nn]ot\s+set",
        r"[Nn]o\s+\w+\s+servers?"
    ]

    # Map from negative-claim context keywords to structured data paths
    NEGATIVE_CLAIM_MAP = {
        "ntp": ["services.ntp.servers"],
        "snmp": ["services.snmp.enabled"],
        "syslog": ["services.syslog.servers"],
        "logging": ["services.syslog.servers"],
        "dns": ["services.dns.name_servers"],
        "routing": ["routing.protocols"],
        "ospf": ["routing.protocols"],
        "eigrp": ["routing.protocols"],
        "bgp": ["routing.protocols"],
        "dhcp snooping": ["security.dhcp_snooping.enabled"],
        "arp inspection": ["security.arp_inspection.enabled"],
        "dai": ["security.arp_inspection.enabled"],
        "port security": ["security.port_security"],
        "dot1x": ["security.dot1x_enabled"],
        "802.1x": ["security.dot1x_enabled"],
        "cdp": ["security.cdp_enabled"],
        "lldp": ["security.lldp_enabled"],
        "spanning tree": ["spanning_tree.mode"],
        "stp": ["spanning_tree.mode"],
        "hsrp": ["vlans.hsrp_groups"],
        "vrrp": ["vlans.vrrp_groups"],
        "qos": ["qos.enabled"],
        "acl": ["security.acls"],
    }

    def validate_all(self) -> ValidationReport:
        """
        Run all validation checks.

        Returns:
            ValidationReport with all results
        """
        print("  Running validation checks...")

        # Specific field validators
        self._validate_device_info()
        self._validate_management()
        self._validate_vlans()
        self._validate_interfaces()
        self._validate_security()
        self._validate_services()

        # Generic validators (catch-all)
        self._validate_parsed_values_present()
        self._validate_negative_claims()

        print(f"    Completed {self.report.total_checks} checks")
        print(f"    Passed: {self.report.passed_checks}")
        print(f"    Failed: {self.report.failed_checks}")
        print(f"    Accuracy: {self.report.accuracy_percentage:.1f}%")

        return self.report

    def _validate_device_info(self):
        """Validate device information."""
        device_info = self.data.get("device_info", {})

        # Hostname - CRITICAL
        hostname = device_info.get("hostname")
        if hostname:
            result = self._check_field_in_markdown(
                "Hostname",
                hostname,
                [
                    rf"hostname[:\s]+[`\"]?{re.escape(hostname)}[`\"]?",
                    rf"#\s+.*{re.escape(hostname)}",  # In title
                    rf"Device[:\s]+{re.escape(hostname)}",
                    rf"\*\*Device\s+Name\*\*[:\s]+.*{re.escape(hostname)}",  # Router format
                    rf"Device\s+Name[:\s]+.*{re.escape(hostname)}"  # Router format without bold
                ]
            )
            self.report.add_result(result)

        # IOS Version
        ios_version = device_info.get("ios_version")
        if ios_version:
            result = self._check_field_in_markdown(
                "IOS Version",
                ios_version,
                [
                    rf"IOS[:\s]+.*{re.escape(ios_version)}",
                    rf"IOS\s+Version[:\s]+.*{re.escape(ios_version)}",
                    rf"\*\*IOS\s+Version\*\*[:\s]+.*{re.escape(ios_version)}",
                    rf"Version[:\s]+.*{re.escape(ios_version)}"  # Generic version match
                ]
            )
            self.report.add_result(result)

        # Domain Name
        domain_name = device_info.get("domain_name")
        if domain_name:
            result = self._check_field_in_markdown(
                "Domain Name",
                domain_name,
                [rf"domain[:\s]+.*{re.escape(domain_name)}"]
            )
            self.report.add_result(result)

    def _validate_management(self):
        """Validate management configuration."""
        mgmt = self.data.get("management", {})

        # Management IP
        mgmt_ip = mgmt.get("ip_address")
        if mgmt_ip:
            result = self._check_field_in_markdown(
                "Management IP Address",
                mgmt_ip,
                [rf"(?:IP|address)[:\s]+.*{re.escape(mgmt_ip)}"]
            )
            self.report.add_result(result)

        # Default Gateway
        gateway = mgmt.get("default_gateway")
        if gateway:
            result = self._check_field_in_markdown(
                "Default Gateway",
                gateway,
                [
                    rf"(?:gateway|Gateway)[:\s*]+.*{re.escape(gateway)}",
                    rf"\*\*.*(?:gateway|Gateway)\*\*[:\s]+{re.escape(gateway)}"
                ]
            )
            self.report.add_result(result)

        # SSH Version
        ssh_version = mgmt.get("ssh", {}).get("version")
        if ssh_version:
            result = self._check_field_in_markdown(
                "SSH Version",
                ssh_version,
                [
                    rf"SSH[:\s]+.*(?:version|v)[\s]*{re.escape(ssh_version)}",
                    rf"SSH\s+Version\*?\*?[:\s]+{re.escape(ssh_version)}",
                    rf"\*\*SSH\s+Version\*\*[:\s]+{re.escape(ssh_version)}"
                ]
            )
            self.report.add_result(result)

        # VTY Transport
        vty_transport = mgmt.get("vty", {}).get("transport_input")
        if vty_transport:
            transport_str = ', '.join(vty_transport) if isinstance(vty_transport, list) else str(vty_transport)
            result = self._check_field_in_markdown(
                "VTY Transport Input",
                transport_str,
                [
                    rf"(?:transport|Transport)[:\s]+.*{re.escape(transport_str)}",
                    rf"\*\*Transport\s+Input\*\*[:\s]+.*{re.escape(transport_str)}",
                    rf"{re.escape(transport_str)}\s+transport\s+input",  # "ssh transport input only"
                    rf"transport\s+input\s+only"  # Matches "SSH transport input only"
                ]
            )
            self.report.add_result(result)

    def _validate_vlans(self):
        """Validate VLAN configuration."""
        vlans = self.data.get("vlans", {})

        # Total VLAN count
        vlan_ids = vlans.get("vlan_ids", [])
        if vlan_ids:
            vlan_count = len(vlan_ids)
            result = self._check_numeric_value_in_markdown(
                "VLAN Count",
                vlan_count,
                [
                    rf"(?:Total|total)\s+VLANs?[:\s]+(\d+)",
                    rf"(\d+)\s+VLANs?",
                    rf"\*\*Total\s+VLANs?\s+\w+\*\*[:\s]+(\d+)",
                    rf"Total\s+VLANs?\s+\w+[:\s]+(\d+)"
                ]
            )
            self.report.add_result(result)

            # Check individual VLANs are mentioned
            for vlan_id in vlan_ids[:5]:  # Check first 5 VLANs
                result = self._check_field_in_markdown(
                    f"VLAN {vlan_id}",
                    str(vlan_id),
                    [
                        rf"VLAN\s+{vlan_id}\b",
                        rf"vlan\s+{vlan_id}\b",
                        rf"VLAN[:\s]+{vlan_id}\b",
                        rf"\b{vlan_id}[,\s]",  # In comma-separated lists
                        rf"[,\s]{vlan_id}\b"   # In comma-separated lists
                    ]
                )
                self.report.add_result(result)

        # SVI interfaces
        svi_interfaces = vlans.get("svi_interfaces", [])
        for svi in svi_interfaces:
            if svi.get("ip_address"):
                result = self._check_field_in_markdown(
                    f"VLAN {svi['vlan_id']} IP",
                    svi["ip_address"],
                    [rf"{re.escape(svi['ip_address'])}"]
                )
                self.report.add_result(result)

    def _validate_interfaces(self):
        """Validate interface configuration."""
        interfaces = self.data.get("interfaces", [])

        if not interfaces:
            return

        # Total interface count
        total = len(interfaces)
        result = self._check_numeric_value_in_markdown(
            "Total Interfaces",
            total,
            [
                rf"\*\*Total\s+Interfaces\*\*[:\s]+(\d+)",  # More specific pattern first
                rf"(?:Total|total)\s+(?:interfaces|Interfaces)[:\s]+(\d+)",
                rf"Total\s+Interfaces[:\s]+(\d+)"
            ]
        )
        self.report.add_result(result)

        # Active interfaces count
        active = sum(1 for i in interfaces if not i.get("shutdown"))
        result = self._check_numeric_value_in_markdown(
            "Active Interfaces",
            active,
            [
                rf"(?:Active|active)[:\s]+(\d+)",
                rf"(\d+)\s+active",
                rf"\*\*Active[^:]*\*\*[:\s]+(\d+)",  # Matches "**Active (no shutdown)**: 4"
                rf"Active\s+\([^)]+\)[:\s]+(\d+)"    # Matches "Active (no shutdown): 4"
            ]
        )
        self.report.add_result(result)

        # Shutdown interfaces count
        shutdown = total - active
        result = self._check_numeric_value_in_markdown(
            "Shutdown Interfaces",
            shutdown,
            [
                rf"(?:Shutdown|shutdown)[:\s]+(\d+)",
                rf"(\d+)\s+shutdown",
                rf"\*\*Shutdown\*\*[:\s]+(\d+)",     # Matches "**Shutdown**: 22"
                rf"Shutdown[:\s]+(\d+)"              # Matches "Shutdown: 22"
            ]
        )
        self.report.add_result(result)

        # Check first few interfaces are mentioned
        for intf in interfaces[:3]:
            intf_name = intf.get("name")
            if intf_name:
                result = self._check_field_in_markdown(
                    f"Interface {intf_name}",
                    intf_name,
                    [rf"{re.escape(intf_name)}"]
                )
                # Fallback: accept if the interface is covered by a range
                if not result.passed and self._is_interface_in_range(intf_name):
                    result.passed = True
                    result.found_value = f"{intf_name} (within documented range)"
                    result.error_message = None
                self.report.add_result(result)

    def _validate_security(self):
        """Validate security features."""
        security = self.data.get("security", {})

        # DHCP Snooping
        dhcp_snoop = security.get("dhcp_snooping", {})
        if dhcp_snoop.get("enabled"):
            result = self._check_field_in_markdown(
                "DHCP Snooping Status",
                "enabled",
                [
                    rf"DHCP\s+Snooping[:\s]+.*(?:Enabled|enabled|✓)",
                    rf"dhcp\s+snooping"
                ]
            )
            self.report.add_result(result)

            # DHCP Snooping VLANs
            dhcp_vlans = dhcp_snoop.get("vlans", [])
            if dhcp_vlans:
                vlan_str = ','.join(map(str, dhcp_vlans))
                # Also check for dash-separated format (e.g., "11-12")
                vlan_dash_str = f"{dhcp_vlans[0]}-{dhcp_vlans[-1]}" if len(dhcp_vlans) > 1 else str(dhcp_vlans[0])
                result = self._check_field_in_markdown(
                    "DHCP Snooping VLANs",
                    vlan_str,
                    [
                        rf"snooping.*(?:VLAN|vlan)s?[:\s]+.*{re.escape(vlan_str)}",
                        rf"snooping.*(?:VLAN|vlan)s?[:\s]+.*{re.escape(vlan_dash_str)}",
                        rf"Enabled\s+on\s+VLANs\*?\*?[:\s]+{re.escape(vlan_dash_str)}",
                        rf"Enabled\s+on\s+VLANs\*?\*?[:\s]+{re.escape(vlan_str)}"
                    ]
                )
                self.report.add_result(result)

        # ARP Inspection
        dai = security.get("arp_inspection", {})
        if dai.get("enabled"):
            result = self._check_field_in_markdown(
                "Dynamic ARP Inspection",
                "enabled",
                [
                    rf"(?:DAI|ARP\s+Inspection)[:\s]+.*(?:Enabled|enabled|✓)",
                    rf"arp\s+inspection"
                ]
            )
            self.report.add_result(result)

        # CDP Status
        cdp_enabled = security.get("cdp_enabled", True)
        cdp_status = "disabled" if not cdp_enabled else "enabled"
        result = self._check_field_in_markdown(
            "CDP Status",
            cdp_status,
            [
                rf"CDP[:\s]+.*{cdp_status}",
                rf"\*\*CDP\*\*[:\s]+.*{cdp_status}",
                rf"CDP.*(?:Status|status)[:\s]+{cdp_status}",
                rf"no\s+cdp"  # Matches "no cdp run" in raw config references
            ]
        )
        self.report.add_result(result)

    def _validate_services(self):
        """Validate network services."""
        services = self.data.get("services", {})

        # NTP
        ntp = services.get("ntp", {})
        if ntp.get("enabled"):
            ntp_servers = ntp.get("servers", [])
            if ntp_servers:
                for server in ntp_servers[:2]:  # Check first 2 servers
                    result = self._check_field_in_markdown(
                        f"NTP Server {server}",
                        server,
                        [rf"NTP.*{re.escape(server)}"]
                    )
                    self.report.add_result(result)

        # Syslog
        syslog = services.get("syslog", {})
        if syslog.get("enabled"):
            syslog_servers = syslog.get("servers", [])
            if syslog_servers:
                for server in syslog_servers[:2]:
                    result = self._check_field_in_markdown(
                        f"Syslog Server {server}",
                        server,
                        [
                            rf"(?:Syslog|syslog|[Ll]ogging).*{re.escape(server)}",
                            rf"\*\*Logging\s+Server\*\*.*{re.escape(server)}",  # Multi-line format
                            rf"IP\s+Address[:\s]+`?{re.escape(server)}`?"  # "IP Address: `10.91.0.10`"
                        ]
                    )
                    self.report.add_result(result)

    # ── Generic validators ───────────────────────────────────────────

    # Regex to detect interface names like FastEthernet0/3, GigabitEthernet0/1
    _INTF_NAME_RE = re.compile(
        r'^(FastEthernet|GigabitEthernet|Ethernet|TenGigabitEthernet|'
        r'FortyGigabitEthernet|HundredGigabitEthernet|Fa|Gi|Te|Fo|Hu)'
        r'(\d+(?:/\d+)*)$',
        re.IGNORECASE
    )

    def _is_interface_in_range(self, intf_name: str) -> bool:
        """Check if an interface name falls within a range documented in the markdown.

        For example, if the markdown contains 'FastEthernet0/1-4' or
        'FastEthernet0/1–24', this returns True for 'FastEthernet0/3'.
        """
        m = self._INTF_NAME_RE.match(intf_name)
        if not m:
            return False

        intf_type = m.group(1)
        slot_port = m.group(2)  # e.g. "0/3"

        # Split into slot prefix and final port number: "0/3" -> ("0/", 3)
        if '/' in slot_port:
            parts = slot_port.rsplit('/', 1)
            slot_prefix = parts[0] + '/'
            port_num = int(parts[1])
        else:
            slot_prefix = ''
            port_num = int(slot_port)

        # Build regex to find range patterns in the markdown
        # Matches e.g. FastEthernet0/1-4, FastEthernet0/1–24 (en-dash or hyphen)
        intf_type_escaped = re.escape(intf_type)
        slot_escaped = re.escape(slot_prefix)
        range_pattern = re.compile(
            rf'{intf_type_escaped}{slot_escaped}(\d+)\s*[–\-]\s*(\d+)',
            re.IGNORECASE
        )

        for match in range_pattern.finditer(self.markdown):
            range_start = int(match.group(1))
            range_end = int(match.group(2))
            if range_start <= port_num <= range_end:
                return True

        return False

    def _validate_parsed_values_present(self):
        """Generic validation: walk all parsed structured data and verify
        that every meaningful leaf value appears somewhere in the documentation."""
        values = self._extract_leaf_values(self.data, prefix="")

        for path, value in values:
            str_val = str(value)

            # Skip values that are too short/generic to validate
            if len(str_val) < 3 or str_val in self.SKIP_VALUES:
                continue
            # Skip booleans — they are covered by specific validators
            if isinstance(value, bool):
                continue
            # Skip small integers (likely counts, not meaningful identifiers)
            if isinstance(value, int) and value < 10:
                continue

            found = str_val.lower() in self.markdown.lower()

            # Fallback: check if this is an interface name covered by a range
            if not found and self._is_interface_in_range(str_val):
                found = True

            result = ValidationResult(
                field_name=f"Parsed value: {path}",
                expected_value=str_val,
                passed=found,
                found_value=str_val if found else None,
                error_message=(
                    f"Parsed value '{str_val}' from {path} not found in documentation"
                    if not found else None
                )
            )
            self.report.add_result(result)

    def _extract_leaf_values(self, data, prefix: str) -> List[Tuple[str, Any]]:
        """Recursively extract leaf values from structured data.

        Returns a list of (dotted_path, value) tuples.
        """
        results = []

        if isinstance(data, dict):
            for key, val in data.items():
                if key in self.SKIP_KEYS:
                    continue
                new_prefix = f"{prefix}.{key}" if prefix else key
                results.extend(self._extract_leaf_values(val, new_prefix))
        elif isinstance(data, list):
            for i, item in enumerate(data):
                new_prefix = f"{prefix}[{i}]"
                results.extend(self._extract_leaf_values(item, new_prefix))
        else:
            # Leaf value
            if data is not None and str(data).strip():
                results.append((prefix, data))

        return results

    def _validate_negative_claims(self):
        """Detect 'Not configured' / 'Not enabled' claims in documentation
        and cross-reference against parser data to catch false negatives."""
        for phrase_pattern in self.NEGATIVE_PHRASES:
            for match in re.finditer(phrase_pattern, self.markdown):
                # Get surrounding context (the line containing the match)
                start = self.markdown.rfind("\n", 0, match.start()) + 1
                end = self.markdown.find("\n", match.end())
                if end == -1:
                    end = len(self.markdown)
                line = self.markdown[start:end].strip()

                # Check each keyword → data-path mapping
                for keyword, data_paths in self.NEGATIVE_CLAIM_MAP.items():
                    if keyword.lower() in line.lower():
                        for data_path in data_paths:
                            value = self._resolve_data_path(data_path)
                            if self._is_meaningful_value(value):
                                result = ValidationResult(
                                    field_name=f"Negative claim: {keyword}",
                                    expected_value=f"Data exists at {data_path}",
                                    passed=False,
                                    found_value=line[:80],
                                    error_message=(
                                        f"Documentation says '{match.group()}' for {keyword}, "
                                        f"but parser found data at {data_path}: {str(value)[:60]}"
                                    )
                                )
                                self.report.add_result(result)

    def _resolve_data_path(self, path: str) -> Any:
        """Resolve a dotted path like 'services.ntp.servers' against self.data."""
        current = self.data
        for part in path.split("."):
            if isinstance(current, dict):
                current = current.get(part)
            else:
                return None
            if current is None:
                return None
        return current

    @staticmethod
    def _is_meaningful_value(value) -> bool:
        """Check if a value indicates something is actually configured
        (non-empty, non-False, non-None)."""
        if value is None:
            return False
        if isinstance(value, bool):
            return value
        if isinstance(value, (list, dict)):
            return len(value) > 0
        if isinstance(value, str):
            return len(value.strip()) > 0
        return True

    def _check_field_in_markdown(
        self,
        field_name: str,
        expected_value: Any,
        patterns: List[str]
    ) -> ValidationResult:
        """
        Check if a field value appears in markdown.

        Args:
            field_name: Name of field being checked
            expected_value: Expected value
            patterns: List of regex patterns to try

        Returns:
            ValidationResult
        """
        result = ValidationResult(
            field_name=field_name,
            expected_value=expected_value
        )

        # Try each pattern
        for pattern in patterns:
            try:
                match = re.search(pattern, self.markdown, re.IGNORECASE | re.MULTILINE | re.DOTALL)
                if match:
                    result.passed = True
                    result.found_value = match.group(0)
                    result.location = f"Line with: {match.group(0)[:50]}..."
                    return result
            except re.error as e:
                result.error_message = f"Regex error: {e}"
                continue

        # Not found
        result.passed = False
        result.found_value = None
        result.error_message = f"Value '{expected_value}' not found in documentation"

        return result

    def _check_numeric_value_in_markdown(
        self,
        field_name: str,
        expected_value: int,
        patterns: List[str]
    ) -> ValidationResult:
        """
        Check if a numeric value appears in markdown.

        Args:
            field_name: Name of field being checked
            expected_value: Expected numeric value
            patterns: List of regex patterns with capture group for number

        Returns:
            ValidationResult
        """
        result = ValidationResult(
            field_name=field_name,
            expected_value=expected_value
        )

        # Try each pattern
        for pattern in patterns:
            try:
                match = re.search(pattern, self.markdown, re.IGNORECASE | re.MULTILINE | re.DOTALL)
                if match:
                    # Extract the number from capture group
                    found_number = int(match.group(1))
                    result.found_value = found_number
                    result.location = f"Line with: {match.group(0)[:50]}..."

                    if found_number == expected_value:
                        result.passed = True
                        return result
                    else:
                        result.passed = False
                        result.error_message = f"Expected {expected_value}, found {found_number}"
                        return result
            except (re.error, ValueError, IndexError) as e:
                continue

        # Not found
        result.passed = False
        result.found_value = None
        result.error_message = f"Numeric value {expected_value} not found in documentation"

        return result


def validate_documentation(
    structured_data_path: str,
    markdown_path: str,
    output_report_path: str = None
) -> ValidationReport:
    """
    Validate generated documentation against structured data.

    Args:
        structured_data_path: Path to structured JSON data
        markdown_path: Path to generated markdown
        output_report_path: Optional path to save validation report

    Returns:
        ValidationReport
    """
    # Load structured data
    with open(structured_data_path, 'r', encoding='utf-8') as f:
        structured_data = json.load(f)

    # Load markdown
    with open(markdown_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Run validation
    validator = DocumentationValidator(structured_data, markdown_content)
    report = validator.validate_all()

    # Save report if requested
    if output_report_path:
        with open(output_report_path, 'w', encoding='utf-8') as f:
            json.dump(report.to_dict(), f, indent=2, ensure_ascii=False)
        print(f"  Validation report saved: {output_report_path}")

    return report


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python validator.py <structured_json> <markdown_file> [output_report.json]")
        sys.exit(1)

    structured_json = sys.argv[1]
    markdown_file = sys.argv[2]
    output_report = sys.argv[3] if len(sys.argv) > 3 else None

    print(f"Validating: {markdown_file}")
    print(f"Against: {structured_json}")

    report = validate_documentation(structured_json, markdown_file, output_report)

    print("\n" + "="*60)
    print("VALIDATION REPORT")
    print("="*60)
    print(f"Total Checks: {report.total_checks}")
    print(f"Passed: {report.passed_checks}")
    print(f"Failed: {report.failed_checks}")
    print(f"Accuracy: {report.accuracy_percentage:.1f}%")
    print(f"Hallucinations: {report.hallucination_count}")

    if report.warnings:
        print(f"\nWarnings: {len(report.warnings)}")
        for warning in report.warnings:
            print(f"  - {warning}")

    if report.failed_checks > 0:
        print(f"\nFailed Checks:")
        for result in report.results:
            if not result.passed:
                print(f"  X {result.field_name}: {result.error_message}")

    print("="*60)
