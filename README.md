# Cisco Configuration Documentation System

Automatically generates structured, human-readable network documentation from Cisco `show running-config` output using a local LLM — no cloud services required.

## How it works

The system uses a hybrid pipeline:

1. **Parser** (`config_parser.py`) — deterministically extracts structured data from the raw config using `ciscoconfparse`. Facts like IP addresses, VLAN IDs, and hostnames are extracted with 100% accuracy before the LLM ever sees them.
2. **Prompt builder** (`structured_prompt_builder.py`) — assembles the structured data into a pre-filled prompt, so the LLM formats and explains rather than interprets raw CLI.
3. **LLM processor** (`processor.py`) — sends the prompt to your local Ollama or LM Studio instance and retrieves the generated Markdown documentation.
4. **Validator** (`validator.py`) — cross-references the LLM output against the parsed facts and reports an accuracy score.

This approach eliminates LLM fabrication of facts while keeping the output readable and contextual.

## Prerequisites

- Python 3.8+
- A local LLM — [Ollama](https://ollama.ai) or [LM Studio](https://lmstudio.ai)

## Quick start

```bash
# Install dependencies
pip install -r requirements.txt

# Configure your LLM endpoint in config.json
# (set llm.endpoint and llm.model to match your setup)

# Start the file watcher
python automation/watcher.py

# Drop a Cisco show running-config (.txt) into configs/
# Generated documentation appears in output/
```

See [docs/QUICKSTART.md](docs/QUICKSTART.md) for full setup instructions including virtual environment and LM Studio configuration.

## Features

- **Local and private** — all processing on your machine, no data leaves
- **98% parser coverage** — 11 configuration categories including VLANs, interfaces, routing, spanning tree, security, QoS, and stacking
- **Secrets sanitization** — passwords, SNMP communities, and TACACS keys are redacted before the LLM sees them
- **Automatic validation** — generated docs are cross-checked against parsed facts with a reported accuracy score
- **Watch mode** — file watcher processes configs automatically as they are added
- **Git integration** — auto-commits generated documentation on each run
- **Metrics tracking** — processing time, token usage, and validation accuracy stored in SQLite

## Documentation

| Document | Description |
|---|---|
| [docs/QUICKSTART.md](docs/QUICKSTART.md) | Installation and first run |
| [docs/LLM-SETUP.md](docs/LLM-SETUP.md) | Ollama and LM Studio configuration |
| [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | Common issues and fixes |
| [docs/PROSJEKTBESKRIVELSE.md](docs/PROSJEKTBESKRIVELSE.md) | Full architecture, design decisions, and results |

## Running tests

```bash
python tests/run_tests.py
```

## License

MIT
