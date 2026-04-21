# Quick Start


## Prerequisites

- Python 3.8+
- A running local LLM — [Ollama](https://ollama.ai) or [LM Studio](https://lmstudio.ai)

---

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

Recommended: use a virtual environment first.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## 2. Start your LLM

**Ollama:**
```bash
ollama pull llama3.1:8b
ollama serve
```

**LM Studio:** Open LM Studio → Local Server tab → select a model → Start Server.

See [LLM-SETUP.md](LLM-SETUP.md) for full configuration details and alternative LLMs.

---

## 3. Configure config.json

Open `config.json` and set `endpoint` and `model` to match your LLM:

**Ollama:**
```json
{
  "llm": {
    "endpoint": "http://localhost:11434/v1/chat/completions",
    "model": "llama3.1:8b"
  }
}
```

**LM Studio:**
```json
{
  "llm": {
    "endpoint": "http://localhost:1234/v1/chat/completions",
    "model": "llama-3.1-8b-instruct"
  }
}
```

Everything else in `config.json` can stay at defaults for now.

---

## 4. Add a Cisco config and run

Place a Cisco `show running-config` output (`.txt` file) in the `configs/` folder.
A sample config is already there if you want to test immediately.

**Watch mode** — processes any file dropped in `configs/` automatically:
```bash
python automation/watcher.py
```

**Single file** — process one file on demand:
```bash
python automation/processor.py configs/your-switch.txt
```

---

## 5. View results

Generated documentation is written to `output/your-switch.md`.

---

## Verify your setup

```bash
python tests/run_tests.py
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| LLM not connecting | Check your LLM server is running; verify `endpoint` in `config.json` |
| Module not found | Run `pip install -r requirements.txt`; check venv is activated |
| Git commit failed | Run `git config user.name` and `git config user.email`, or set `"git": {"enabled": false}` |
| Slow processing | Use a smaller model (7B), reduce `max_tokens` to 4000 |
| Output cuts off | Increase `max_tokens` in `config.json` |

Full details: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
