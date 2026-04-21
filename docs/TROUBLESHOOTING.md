# Troubleshooting Guide

Common issues and their solutions for the Cisco Configuration Documentation System (Python version).

## Installation Issues

### ❌ "Python not found" or "python: command not found"

**Problem**: Python is not installed or not in PATH.

**Solution**:
1. Download and install Python from https://python.org/ (version 3.8 or higher)
2. During installation, check "Add Python to PATH"
3. Restart your terminal
4. Verify: `python --version` or `python3 --version`

---

### ❌ "pip: command not found"

**Problem**: pip is not installed or not in PATH.

**Solution**:
```bash
# Reinstall pip
python -m ensurepip --upgrade

# Or use python3
python3 -m ensurepip --upgrade

# Verify
pip --version
```

---

### ❌ "pip install fails with permission errors"

**Problem**: Permission denied during pip install.

**Solution (Linux/Mac)**:
```bash
# Option 1: Use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Option 2: Install with --user flag
pip install --user -r requirements.txt
```

**Solution (Windows)**:
- Run terminal as Administrator, or
- Use virtual environment (recommended):
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

---

### ❌ "ModuleNotFoundError: No module named 'xyz'"

**Problem**: Required Python package not installed.

**Solution**:
```bash
# Install all dependencies
pip install -r requirements.txt

# Or install specific package
pip install <package-name>

# Check installed packages
pip list
```

---

### ❌ "ImportError: cannot import name 'xyz'"

**Problem**: Package version incompatibility or missing dependencies.

**Solution**:
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Reinstall all dependencies
pip uninstall -r requirements.txt -y
pip install -r requirements.txt

# Clear pip cache
pip cache purge
```

---

## LLM Connection Issues

### ❌ "LLM API request failed" or Connection refused

**Problem**: Cannot connect to the LLM server.

**Diagnosis**:
```bash
# Check if LLM is running
curl http://localhost:11434/api/version  # For Ollama
```

**Solutions**:

**For Ollama**:
```bash
# Start Ollama
ollama serve

# Verify it's running
ollama list

# Test connection
curl http://localhost:11434/api/version
```

**For LM Studio**:
1. Open LM Studio
2. Go to "Local Server" tab
3. Click "Start Server"
4. Note the port number (usually 1234)
5. Update `config.json`:
   ```json
   {
     "llm": {
       "endpoint": "http://localhost:1234/v1/chat/completions"
     }
   }
   ```

**For other LLMs**:
- Ensure the server is running
- Check firewall settings
- Verify the port in `config.json` matches your LLM

---

### ❌ "Error: Unexpected LLM response format"

**Problem**: LLM returned data in an unexpected format.

**Diagnosis**:
Check what your LLM actually returns:
```bash
curl -X POST http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.1:8b",
    "messages": [{"role": "user", "content": "test"}]
  }'
```

**Solution**:
Modify `automation/processor.py` around line 120-140 to match your LLM's response format:

```python
# Add your format here
if "your_llm_format" in data:
    content = data["your_llm_format"]["text"]
```

---

### ❌ "Model 'llama3.1:8b' not found"

**Problem**: The specified model is not downloaded.

**Solution (Ollama)**:
```bash
# List available models
ollama list

# Pull the model
ollama pull llama3.1:8b

# Or use a different model that's already downloaded
# Update config.json with the model name from `ollama list`
```

**Solution (LM Studio)**:
1. Open LM Studio
2. Go to "Search" or "Discover"
3. Download a model (e.g., "llama-3.1-8b-instruct")
4. Update `config.json` with the exact model name shown in LM Studio

---

### ❌ "Request timeout"

**Problem**: LLM is taking too long to respond.

**Solutions**:
1. **Increase timeout** in `config.json`:
   ```json
   {
     "llm": {
       "timeout": 600000  // 10 minutes (in milliseconds)
     }
   }
   ```

2. **Use a smaller model**:
   ```bash
   ollama pull llama3.1:8b  # Instead of 70B
   ```

3. **Reduce max_tokens**:
   ```json
   {
     "llm": {
       "max_tokens": 4000  // Instead of 8000
     }
   }
   ```

4. **Enable GPU acceleration** (if available):
   - For Ollama: Automatically uses GPU if available
   - For LM Studio: Enable GPU in settings

---

## File Watcher Issues

### ❌ "Watcher not detecting new files"

**Problem**: Adding files to `configs/` doesn't trigger processing.

**Diagnosis**:
1. Is the watcher running?
   ```bash
   python automation/watcher.py
   # You should see: "✅ Watcher ready and monitoring for changes"
   ```

2. Are files in the correct location?
   ```bash
   # Files should be in:
   # <project-root>/configs/*.txt
   ls configs/
   ```

**Solutions**:
- Ensure watcher is running: `python automation/watcher.py`
- Verify file extension is `.txt` (not `.TXT` or `.config`)
- Check file permissions (must be readable)
- Try restarting the watcher (Ctrl+C, then restart)

---

### ❌ "File is processed multiple times"

**Problem**: Same config generates multiple documentation files.

**Cause**: File is being modified multiple times (e.g., by auto-save).

**Solution**:
The watcher has cooldown built-in (2 seconds). If this still happens:
1. Copy files instead of editing them in place
2. Increase cooldown time in `automation/watcher.py`:
   ```python
   if current_time - last_time > 5:  # 5 seconds instead of 2
   ```

---

### ❌ "watchdog module not found"

**Problem**: The watchdog package is not installed.

**Solution**:
```bash
pip install watchdog

# Or install all dependencies
pip install -r requirements.txt
```

---

## Processing Issues

### ❌ "Error loading config.json"

**Problem**: `config.json` not found or invalid.

**Solutions**:
1. **Check file exists**:
   ```bash
   ls config.json
   ```

2. **Validate JSON syntax**:
   - Use a JSON validator: https://jsonlint.com/
   - Check for missing commas, quotes, brackets

3. **Reset to default**:
   ```bash
   # Backup your config
   cp config.json config.json.backup

   # Recreate from template (see config.json in docs)
   ```

---

### ❌ "IOS version not detected"

**Problem**: Shows "IOS Version: Unknown" in output.

**Cause**: Version string format not recognized.

**Solution**:
Check your config file has a version line like:
```
version 15.2
```
or
```
Cisco IOS Software, Version 15.2(4)E7
```

If it's in a different format, modify `automation/processor.py`:
```python
def _extract_ios_version(self, config_content: str) -> Optional[str]:
    patterns = [
        r'Cisco IOS Software.*Version ([0-9.()A-Z]+)',
        r'IOS.*Version ([0-9.]+)',
        r'^version ([0-9.]+)',
        # Add your pattern here:
        r'your-custom-pattern',
    ]
    # ...
```

---

### ❌ "Documentation quality is poor"

**Problem**: Generated documentation is incomplete or inaccurate.

**Solutions**:

1. **Use a better model**:
   - Llama 3.1 70B instead of 8B
   - Mixtral 8x7B
   - Models specifically fine-tuned for technical text

2. **Adjust temperature** (in `config.json`):
   ```json
   {
     "llm": {
       "temperature": 0.3  // Lower = more consistent, less creative
     }
   }
   ```

3. **Improve the prompt** — edit `_build_task_instructions()` in `automation/structured_prompt_builder.py`:
   - Add more specific instructions
   - Adjust the required document sections
   - Change confidence level requirements

4. **Increase context**:
   ```json
   {
     "llm": {
       "max_tokens": 12000  // Allow longer responses
     }
   }
   ```

---

### ❌ "UnicodeDecodeError"

**Problem**: Cannot read configuration file due to encoding issues.

**Solution**:
The processor tries both UTF-8 and Latin-1 encoding. If still failing:
```python
# Modify automation/processor.py
def _read_config_file(self) -> str:
    try:
        with open(self.config_file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        # Try your specific encoding
        with open(self.config_file_path, 'r', encoding='cp1252') as f:
            return f.read()
```

---

## Git Issues

### ❌ "Git commit failed"

**Problem**: Errors when trying to commit documentation.

**Diagnosis**:
```bash
git status
git log
```

**Solutions**:

1. **Git not initialized**:
   ```bash
   git init
   ```

2. **Git user not configured**:
   ```bash
   git config user.name "Your Name"
   git config user.email "your@email.com"
   ```

3. **Nothing to commit** (not really an error):
   - Documentation hasn't changed
   - This is normal!

4. **Disable Git** if you don't need it:
   ```json
   {
     "git": {
       "enabled": false
     }
   }
   ```

---

### ❌ "Git push failed"

**Problem**: Auto-push to remote fails.

**Solutions**:

1. **Remote not configured**:
   ```bash
   git remote add origin https://github.com/yourusername/yourrepo.git
   ```

2. **Authentication failed**:
   - Set up SSH keys, or
   - Use personal access token, or
   - Disable auto-push:
     ```json
     {
       "git": {
         "auto_push": false
       }
     }
     ```

3. **Branch doesn't exist on remote**:
   ```bash
   git push -u origin main
   ```

---

### ❌ "GitPython module not found"

**Problem**: GitPython package not installed.

**Solution**:
```bash
pip install GitPython

# Or install all dependencies
pip install -r requirements.txt
```

---

## Performance Issues

### ❌ "Processing is very slow"

**Problem**: Takes 5+ minutes to process a single config.

**Solutions**:

1. **Use GPU acceleration**:
   - Ollama: Install CUDA/ROCm drivers
   - LM Studio: Enable GPU in settings

2. **Use smaller model**:
   ```bash
   ollama pull llama3.1:8b  # Not 70B
   ```

3. **Reduce output length**:
   ```json
   {
     "llm": {
       "max_tokens": 4000
     }
   }
   ```

4. **Use quantized models**:
   - Q4_K_M (faster, less accurate)
   - Q5_K_M (balanced)
   - Q8_0 (slower, more accurate)

5. **Simplify prompt**:
   - Edit `_build_task_instructions()` in `automation/structured_prompt_builder.py`
   - Remove less important sections from the document structure

---

### ❌ "System runs out of memory"

**Problem**: OOM error or system freezes.

**Solutions**:

1. **Use smaller model**:
   - 7B instead of 13B or 70B

2. **Close other applications**

3. **Increase swap space** (Linux):
   ```bash
   sudo fallocate -l 8G /swapfile
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   sudo swapon /swapfile
   ```

4. **Use cloud-based LLM** (requires code modification):
   - OpenAI API
   - Anthropic Claude API
   - Note: This sends configs to external servers!

---

## Output Issues

### ❌ "No output files generated"

**Problem**: `output/` folder is empty.

**Diagnosis**:
Check the processor logs for errors:
```bash
python automation/processor.py configs/test.txt
# Read the error messages
```

**Common causes**:
- LLM connection failed → Fix LLM connection
- Config file unreadable → Check permissions
- Disk full → Free up space
- Invalid config.json → Validate JSON

---

### ❌ "Output is incomplete"

**Problem**: Generated markdown cuts off mid-sentence.

**Cause**: Hit `max_tokens` limit.

**Solution**:
Increase in `config.json`:
```json
{
  "llm": {
    "max_tokens": 12000  // Or higher
  }
}
```

Check your LLM's maximum context window:
- Llama 3.1: 128K tokens (but 8-16K is practical)
- Mistral: 32K tokens
- Mixtral: 32K tokens

---

## Python Version Issues

### ❌ "SyntaxError: invalid syntax"

**Problem**: Python version too old.

**Solution**:
```bash
# Check version
python --version

# Must be 3.8 or higher
# Upgrade Python or use python3 command
python3 automation/watcher.py
```

---

### ❌ "asyncio errors" or "async/await issues"

**Problem**: Python version doesn't support async features.

**Solution**:
```bash
# Upgrade to Python 3.8+
# Or use python3 explicitly
python3 --version
python3 automation/watcher.py
```

---

## Windows-Specific Issues

### ❌ "Path errors on Windows"

**Problem**: Paths with spaces cause issues.

**Solution**:
Always use quotes:
```cmd
python automation\processor.py "C:\Program Files\configs\test.txt"
```

Or avoid spaces in paths entirely.

---

### ❌ "Permission denied on Windows"

**Problem**: Cannot create files or directories.

**Solutions**:
1. Run terminal as Administrator
2. Install project in user directory (not C:\Program Files)
3. Check antivirus isn't blocking Python

---

### ❌ "Scripts not executable on Windows"

**Problem**: Cannot run `.py` files directly.

**Solution**:
```cmd
# Use python explicitly
python automation\watcher.py

# Or associate .py files with Python
# Right-click .py file → Open with → Python
```

---

## Linux/Mac-Specific Issues

### ❌ "Permission denied (EACCES)"

**Problem**: Cannot execute scripts or access files.

**Solution**:
```bash
# Make scripts executable
chmod +x automation/watcher.py
chmod +x automation/processor.py

# Fix file permissions
chmod -R u+rw configs/ output/
```

---

### ❌ "python: command not found" (but python3 works)

**Problem**: Python is installed as `python3` not `python`.

**Solution**:
```bash
# Use python3 explicitly
python3 automation/watcher.py

# Or create alias
echo "alias python=python3" >> ~/.bashrc
source ~/.bashrc
```

---

## Virtual Environment Issues

### ❌ "Cannot activate virtual environment"

**Problem**: Virtual environment activation fails.

**Solution (Linux/Mac)**:
```bash
# Create venv
python -m venv venv

# Activate
source venv/bin/activate

# If permission denied
chmod +x venv/bin/activate
```

**Solution (Windows)**:
```cmd
# Create venv
python -m venv venv

# Activate
venv\Scripts\activate

# If execution policy error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### ❌ "Packages installed but still not found"

**Problem**: Installed packages in venv but Python can't find them.

**Solution**:
```bash
# Make sure venv is activated
# You should see (venv) in prompt

# Verify pip is from venv
which pip  # Linux/Mac
where pip  # Windows

# Should point to venv/bin/pip or venv\Scripts\pip

# If not, deactivate and reactivate
deactivate
source venv/bin/activate  # or venv\Scripts\activate
```

---

## Getting Help

If you're still stuck:

1. **Check logs**: Read error messages carefully
2. **Search issues**: Look for similar problems online
3. **Minimal test**: Try the simplest possible case
4. **Isolate component**: Test each part separately:
   - LLM connection
   - Processor script
   - Watcher

### Diagnostic Commands

```bash
# System info
python --version
pip --version
git --version

# Check LLM
curl http://localhost:11434/api/version  # Ollama

# Test processor
python automation/processor.py configs/SAMPLE-SWITCH.txt

# Check Git
git status
git log --oneline -5

# List installed packages
pip list
pip show requests watchdog GitPython
```

### Enable Debug Logging

Modify scripts to add verbose logging:

**In processor.py**:
```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Or add print statements
print(f"Debug: Config content length: {len(config_content)}")
```

---

## Common Gotchas

1. **Config file format**: Must be plain text `.txt` file
2. **LLM must be running**: Start before running watcher
3. **JSON syntax**: config.json must be valid JSON (no trailing commas!)
4. **Python version**: Must be 3.8+ (check with `python --version`)
5. **Case sensitivity**: Linux/Mac care about file name case
6. **Network ports**: Default ports must be available (11434, 1234, etc.)
7. **Firewalls**: May block localhost connections
8. **Working directory**: Run commands from correct directory
9. **Virtual environment**: Activate before running if using venv
10. **File encoding**: Config files should be UTF-8

---

## Still Having Issues?

1. Try the [QUICKSTART.md](QUICKSTART.md) guide from scratch
2. Check your `config.json` matches the format shown in QUICKSTART.md
3. Test with the provided `configs/SAMPLE-SWITCH.txt` first
5. Use a virtual environment to isolate dependencies
6. Check Python version: `python --version` (must be 3.8+)
7. Verify all packages installed: `pip list`