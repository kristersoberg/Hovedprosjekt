# Logging System Documentation

The Cisco Configuration Documentation system includes a comprehensive logging framework with configurable verbosity levels.

## Configuration

Logging is configured in `config.json`:

```json
{
  "logging": {
    "enabled": true,
    "log_dir": "./logs",
    "verbose": false,
    "debug": false
  }
}
```

### Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `enabled` | boolean | `true` | Enable/disable logging system |
| `log_dir` | string | `"./logs"` | Directory to store log files |
| `verbose` | boolean | `false` | Show INFO level messages on console |
| `debug` | boolean | `false` | Show DEBUG level messages on console and in logs |

## Verbosity Levels

### Normal Mode (default)
**Console output:** Only step markers and warnings/errors
**Log file:** Full debug information

```json
"logging": {
  "verbose": false,
  "debug": false
}
```

**Console example:**
```
▶ Parsing configuration into structured data
▶ Building structured prompt
▶ Sending to LLM for analysis
▶ Saving documentation
▶ Validating documentation
WARNING  | WARNING: 6 checks failed
▶ Committing to Git
✓ Documentation generated: output/aksess-sw01.md
```

### Verbose Mode
**Console output:** Steps + progress details
**Log file:** Full debug information

```json
"logging": {
  "verbose": true,
  "debug": false
}
```

**Console example:**
```
============================================================
 Processing: aksess-sw01.txt
============================================================
▶ Parsing configuration into structured data
INFO     |   Detected device: aksess-sw01
INFO     |   IOS version: 12.2(37)SE1
INFO     |   VLANs found: 4
INFO     |   Interfaces found: 26
▶ Building structured prompt
INFO     |   Prompt size: 12543 characters
▶ Sending to LLM for analysis
INFO     |   LLM response length: 5421 characters
▶ Validating documentation
INFO     |   Accuracy: 76.0%
INFO     |   Passed: 19/25 checks
WARNING  | WARNING: 6 checks failed
```

### Debug Mode
**Console output:** Everything including debug traces
**Log file:** Full debug information with timestamps

```json
"logging": {
  "verbose": true,
  "debug": true
}
```

**Console example:**
```
============================================================
 Processing: aksess-sw01.txt
============================================================
▶ Parsing configuration into structured data
INFO     |   Detected device: aksess-sw01
INFO     |   IOS version: 12.2(37)SE1
DEBUG    |   Device info: {
DEBUG    |     "hostname": "aksess-sw01",
DEBUG    |     "ios_version": "12.2(37)SE1",
DEBUG    |     "domain_name": "krister.local"
DEBUG    |   }
▶ Building structured prompt
INFO     |   Prompt size: 12543 characters
DEBUG    |   First 500 chars of prompt: You are an expert Cisco network engineer...
▶ Validating documentation
DEBUG    |     Failed: Domain Name - Value 'krister.local' not found in documentation
DEBUG    |     Failed: VLAN 666 - Value '666' not found in documentation
```

## Log Files

### Location
Log files are stored in the directory specified by `log_dir` (default: `./logs/`)

### File Format
Each run creates a new log file with timestamp:
```
logs/documentation_20260105_143022.log
```

### Log File Contents
Log files always contain full DEBUG level information with timestamps:

```
2026-01-05 14:30:22 | INFO     | cisco_doc_generator |
============================================================
2026-01-05 14:30:22 | INFO     | cisco_doc_generator |  Processing: aksess-sw01.txt
2026-01-05 14:30:22 | INFO     | cisco_doc_generator | ============================================================
2026-01-05 14:30:22 | WARNING  | cisco_doc_generator | ▶ Parsing configuration into structured data
2026-01-05 14:30:23 | INFO     | cisco_doc_generator |   Detected device: aksess-sw01
2026-01-05 14:30:23 | INFO     | cisco_doc_generator |   IOS version: 12.2(37)SE1
2026-01-05 14:30:23 | DEBUG    | cisco_doc_generator |   Device info: {"hostname": "aksess-sw01", ...}
2026-01-05 14:30:23 | WARNING  | cisco_doc_generator | ▶ Building structured prompt
2026-01-05 14:30:23 | INFO     | cisco_doc_generator |   Prompt size: 12543 characters
2026-01-05 14:30:23 | DEBUG    | cisco_doc_generator |   First 500 chars of prompt: You are an expert...
```

## Usage Examples

### Run with default (quiet) output
```bash
python automation/processor.py configs/aksess-sw01.txt
```

### Run with verbose output
Edit `config.json`:
```json
"logging": {
  "verbose": true
}
```

### Run with full debug output
Edit `config.json`:
```json
"logging": {
  "verbose": true,
  "debug": true
}
```

### Disable logging entirely
Edit `config.json`:
```json
"logging": {
  "enabled": false
}
```

## What Gets Logged

### Always Logged (Normal Mode)
- Processing steps (parsing, prompt building, LLM call, validation, git commit)
- Final accuracy percentage
- Warnings (validation failures)
- Errors and exceptions

### Verbose Mode (INFO) Adds
- Device detection details (hostname, IOS version, VLAN count, interface count)
- Prompt size
- LLM response length
- Detailed validation results
- File paths

### Debug Mode (DEBUG) Adds
- Full device information JSON
- Prompt preview (first 500 characters)
- LLM response preview (first 500 characters)
- Individual validation failures with details
- Exception stack traces
- Internal processing details

## Benefits

1. **Quick Runs**: Normal mode shows only essential progress
2. **Troubleshooting**: Verbose mode helps understand what's happening
3. **Deep Debugging**: Debug mode reveals all internal details
4. **Historical Record**: Log files preserve full execution history
5. **Performance Analysis**: Timestamps show where time is spent

## Log Retention

Log files are never automatically deleted. To manage log file storage:

```bash
# Delete logs older than 7 days (Linux/macOS)
find logs/ -name "documentation_*.log" -mtime +7 -delete

# Delete all logs (Windows PowerShell)
Remove-Item logs\documentation_*.log

# Keep only last 10 log files (Linux/macOS)
ls -t logs/documentation_*.log | tail -n +11 | xargs rm
```
