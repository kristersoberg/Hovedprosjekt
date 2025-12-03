# MCP Server Logging Guide

This guide explains how to view MCP server logs when running the system in different modes.

## Quick Summary

When `debug: true` is set in config.json, the MCP server automatically logs to:
- **File**: `logs/mcp_server.log` (when launched by processor)
- **stderr**: Terminal output (when run manually)

## Option 1: Automatic File Logging (Recommended)

When the processor launches the MCP server with debug mode enabled, logs are automatically written to a file.

### Setup
1. Enable debug in `config.json`:
   ```json
   {
     "mcp": {
       "debug": true
     }
   }
   ```

2. Run the processor normally:
   ```bash
   python automation\processor.py configs\your-config.txt
   ```

3. View logs in real-time:
   ```bash
   # PowerShell
   Get-Content logs\mcp_server.log -Wait -Tail 50

   # Or use a text editor that auto-refreshes
   code logs\mcp_server.log
   ```

### Log Location
- **Path**: `logs/mcp_server.log`
- **Format**: Appends to existing log (doesn't overwrite)
- **Auto-created**: The `logs/` directory is created automatically

### Benefits
- ✅ No need to manage separate terminal windows
- ✅ Logs persist after processor finishes
- ✅ Can review logs later for debugging
- ✅ Processor and server output are separated

## Option 2: Manual Server with Terminal Output

Run the server manually in a dedicated terminal window.

### Setup
1. Open a **separate terminal** for the MCP server

2. Navigate to project directory:
   ```bash
   cd c:\Git-lokalt\Hovedprosjekt
   ```

3. Enable debug and start server:
   ```powershell
   # PowerShell
   $env:MCP_DEBUG="true"
   python mcp_server\server-v2.py
   ```

   ```bash
   # Linux/Mac
   MCP_DEBUG=true python mcp_server/server-v2.py
   ```

4. In another terminal, run the processor:
   ```bash
   python automation\processor.py configs\your-config.txt
   ```

### Benefits
- ✅ See logs in real-time in dedicated window
- ✅ Easy to spot issues immediately
- ✅ Can restart server independently

### Drawbacks
- ❌ Need to manage two terminal windows
- ❌ Must manually set environment variable
- ❌ Logs disappear when terminal closes

## Option 3: Dual Output (File + stderr)

Modify server-v2.py to log to both file and terminal.

### Modify server-v2.py
Change the handlers section:

```python
# Log to both file and stderr
if log_file:
    handlers.append(logging.FileHandler(log_file, mode='a', encoding='utf-8'))
    handlers.append(logging.StreamHandler(sys.stderr))  # Also log to stderr
else:
    handlers.append(logging.StreamHandler(sys.stderr))
```

### Benefits
- ✅ See logs in real-time AND save to file
- ✅ Best of both worlds

### Drawbacks
- ❌ More verbose output in processor terminal
- ❌ Processor output mixed with server logs

## Option 4: Windows Terminal Split Panes

Use Windows Terminal to view logs and run processor side-by-side.

### Setup
1. Open Windows Terminal

2. Split pane (Alt+Shift+D or Alt+Shift+-)

3. **Left pane**: Watch logs
   ```powershell
   Get-Content logs\mcp_server.log -Wait -Tail 50
   ```

4. **Right pane**: Run processor
   ```powershell
   python automation\processor.py configs\your-config.txt
   ```

### Benefits
- ✅ See everything in one window
- ✅ Professional setup
- ✅ Easy to monitor

## Log Levels

### INFO Level (`debug: false`)
Shows high-level operations:
```
2025-12-03 20:35:19 - INFO - Client connected! Server is now active
2025-12-03 20:35:20 - INFO - Received call_tool request: search_command
2025-12-03 20:35:20 - INFO - Searching for command: 'vlan'
2025-12-03 20:35:20 - INFO - Successfully found documentation
2025-12-03 20:35:20 - INFO - Tool search_command completed in 0.023s
```

### DEBUG Level (`debug: true`)
Shows detailed internal operations:
```
2025-12-03 20:35:19 - DEBUG - Cache directory already exists
2025-12-03 20:35:19 - DEBUG - Registering list_tools handler...
2025-12-03 20:35:20 - DEBUG - Arguments: {
  "command": "vlan"
}
2025-12-03 20:35:20 - DEBUG - Reading from cache file: ...
2025-12-03 20:35:20 - DEBUG - Available commands: interface, ip address, ...
```

## Viewing Logs

### Real-time Viewing (PowerShell)
```powershell
# View last 50 lines and follow
Get-Content logs\mcp_server.log -Wait -Tail 50

# View all logs
Get-Content logs\mcp_server.log
```

### Real-time Viewing (Linux/Mac)
```bash
# View last 50 lines and follow
tail -f -n 50 logs/mcp_server.log

# View all logs
cat logs/mcp_server.log
```

### Search Logs
```powershell
# PowerShell - Find errors
Select-String -Path logs\mcp_server.log -Pattern "ERROR"

# PowerShell - Find specific command
Select-String -Path logs\mcp_server.log -Pattern "vlan"
```

```bash
# Linux/Mac - Find errors
grep "ERROR" logs/mcp_server.log

# Linux/Mac - Find specific command
grep "vlan" logs/mcp_server.log
```

### Clear Old Logs
```powershell
# PowerShell
Remove-Item logs\mcp_server.log

# Or truncate (keep file, clear content)
Clear-Content logs\mcp_server.log
```

## Troubleshooting

### No logs directory created
- The processor creates it automatically when debug is enabled
- Manually create: `mkdir logs`

### Log file is huge
- Logs append on each run
- Clear periodically: `Clear-Content logs\mcp_server.log`
- Or add log rotation (see below)

### Can't see recent logs
- Logs are buffered, may take a few seconds to appear
- Use `-Wait` flag in PowerShell to follow in real-time

### Server crashes, but no error in log
- Check processor output for connection errors
- Verify server path in config.json is correct
- Try running server manually to see startup errors

## Advanced: Log Rotation

To prevent log files from growing too large, add rotation:

```python
# In server-v2.py, replace FileHandler with RotatingFileHandler
from logging.handlers import RotatingFileHandler

handlers.append(RotatingFileHandler(
    log_file,
    mode='a',
    maxBytes=10*1024*1024,  # 10MB
    backupCount=5,
    encoding='utf-8'
))
```

This creates `mcp_server.log`, `mcp_server.log.1`, etc., keeping the 5 most recent logs.

## Recommended Workflow

For daily development:
1. Set `"debug": true` in config.json
2. Run processor normally
3. Keep a terminal open with: `Get-Content logs\mcp_server.log -Wait -Tail 50`
4. Review logs when issues occur

For production/automated runs:
1. Set `"debug": false` (less verbose)
2. Check logs only when investigating issues
3. Clear logs periodically to save space

## Summary Table

| Method | Pros | Cons | Best For |
|--------|------|------|----------|
| **File Logging** | Persistent, clean separation | Need separate viewer | Daily development |
| **Manual Server** | Real-time in terminal | Extra window management | Debugging sessions |
| **Dual Output** | See everything | Verbose processor output | Intensive debugging |
| **Split Panes** | Professional setup | Requires Windows Terminal | Long-running tasks |

Choose the method that fits your workflow!
