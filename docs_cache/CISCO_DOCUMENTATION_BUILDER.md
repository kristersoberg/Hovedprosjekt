# Cisco Documentation Builder Guide

## Overview
This guide explains how to build a local, air-gapped Cisco IOS documentation database for the MCP server.

## Approach: Structured JSON Documentation

Instead of scraping HTML pages, we build structured JSON files containing command and feature documentation extracted from publicly available Cisco documentation.

## Sources for Documentation

### Primary Sources (All Publicly Available)
1. **Cisco IOS Command Reference** - https://www.cisco.com/c/en/us/support/ios-nx-os-software/ios-15-4m-t/products-command-reference-list.html
2. **Cisco IOS Configuration Fundamentals** - Command reference books per IOS version
3. **Cisco Configuration Guides** - Feature-specific guides
4. **Cisco Security Configuration Guides** - Best practices
5. **Cisco Design Zone** - Architecture and design documentation

### Downloadable Documentation Packages
Cisco provides documentation in these formats:
- **HTML** - Full documentation websites (can be downloaded as ZIP)
- **PDF** - Individual command reference books
- **XML** - Structured data (some newer docs)

### How to Download (For Air-Gapped Systems)

#### Method 1: Download Full Command Reference
```bash
# Example for IOS 15.2
wget -r -np -k https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/

# This downloads entire command reference as HTML files
```

#### Method 2: Use Cisco's Documentation Portal
1. Go to: https://www.cisco.com/c/en/us/support/ios-nx-os-software/
2. Select your IOS version (e.g., IOS 15.2)
3. Click "Command References"
4. Download entire sections or specific books

#### Method 3: Download PDFs
- Navigate to specific command reference
- Use "Download" or "PDF" option
- Store locally in `docs_cache/cisco_ios/pdfs/`

## Documentation Structure

### Recommended Local Structure
```
docs_cache/
├── cisco_ios/
│   ├── 15.2/
│   │   ├── commands/
│   │   │   ├── core_commands.json         # Top 150 commands
│   │   │   ├── interface_commands.json    # Interface-specific
│   │   │   ├── security_commands.json     # Security features
│   │   │   ├── routing_commands.json      # Routing protocols
│   │   │   └── service_commands.json      # Services (NTP, SNMP, etc.)
│   │   ├── features/
│   │   │   ├── vlan.json
│   │   │   ├── spanning_tree.json
│   │   │   ├── security.json
│   │   │   └── services.json
│   │   ├── best_practices/
│   │   │   ├── security_hardening.json
│   │   │   ├── interface_config.json
│   │   │   └── general.json
│   │   └── html_cache/                    # Optional: Full HTML docs
│   ├── 12.2/
│   └── 16.x/
└── extraction_tools/
    ├── html_to_json.py                     # Convert downloaded HTML to JSON
    └── pdf_to_json.py                      # Extract from PDFs
```

## Building the Documentation Database

### Phase 1: Manual Creation (Quick Start - 1-2 days)
Create JSON files manually for the most common commands found in your configs.

**Priority Commands (from your actual configs):**
1. Interface commands (20 commands)
2. Security commands (15 commands)
3. AAA/Access commands (10 commands)
4. VLAN/STP commands (10 commands)
5. Service commands (15 commands)

**Estimated Effort:** 70 commands × 10 minutes each = ~12 hours

### Phase 2: Semi-Automated Extraction (1 week)
1. Download Cisco HTML documentation
2. Build parser to extract command info
3. Convert to structured JSON
4. Validate against known configs

### Phase 3: Comprehensive Database (2-3 weeks)
- 500+ commands documented
- Multiple IOS versions
- Cross-references and related commands
- Best practices integrated

## JSON Schema for Commands

See the detailed example in the previous response for the complete schema.

Key fields:
- `name`: Command name
- `syntax`: Full syntax with parameters
- `description`: What it does
- `modes`: Where it can be used
- `parameters`: Detailed parameter descriptions
- `examples`: Real-world usage examples
- `best_practices`: Recommendations
- `security_considerations`: Security implications
- `common_mistakes`: What to avoid
- `related_commands`: Connected commands

## Advantages of This Approach

### For Air-Gapped Systems
✅ Completely offline after initial download
✅ No external dependencies
✅ Fast lookups (no network latency)
✅ Version control friendly
✅ Easy to audit and validate

### For LLM Context
✅ Structured data perfect for RAG
✅ Precise information retrieval
✅ No HTML parsing overhead
✅ Can include examples and best practices
✅ Cross-referencing between commands

### For Research
✅ Repeatable and auditable
✅ Can track what documentation was used
✅ Easy to extend and improve
✅ Version-specific accuracy

## Storage Requirements

### Minimal Setup (Current)
- 13 commands: ~50 KB
- 5 features: ~100 KB
- **Total: ~150 KB**

### Recommended Setup (150 commands)
- 150 commands: ~2-3 MB
- 20 features: ~1 MB
- Best practices: ~500 KB
- **Total: ~5 MB**

### Comprehensive Setup (500+ commands)
- 500+ commands: ~10-15 MB
- 50+ features: ~3-4 MB
- Best practices: ~2 MB
- HTML cache (optional): ~500 MB - 2 GB
- **Total: 15-20 MB (JSON only) or 500 MB - 2 GB (with HTML)**

## Next Steps

1. **Review current command coverage gaps**
2. **Prioritize commands based on your actual configs**
3. **Choose documentation approach** (manual, semi-automated, or comprehensive)
4. **Download source documentation** (if using automation)
5. **Build or expand JSON database**
6. **Integrate with MCP server**
7. **Test and validate**

## Maintenance Strategy

### Regular Updates
- New IOS versions: Download and extract documentation
- New commands discovered: Add to database
- Best practices updates: Review and incorporate
- Validation: Test against real configs

### Version Control
- Track all changes to documentation
- Git commit each update with source reference
- Tag versions corresponding to IOS releases

## Legal Considerations

All Cisco public documentation is freely available and can be used for:
- Network administration
- Education and training
- Configuration automation
- Documentation generation

Ensure you:
- Only use publicly available documentation
- Maintain proper attribution
- Don't redistribute Cisco's copyrighted material
- Use internally for your network operations

## References

- Cisco IOS Command References: https://www.cisco.com/c/en/us/support/ios-nx-os-software/
- Cisco Configuration Guides: https://www.cisco.com/c/en/us/support/
- Cisco Design Zone: https://www.cisco.com/c/en/us/solutions/design-zone.html
