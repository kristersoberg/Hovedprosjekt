# System Workflow Diagrams

Visual representations of how the Cisco Configuration Documentation System works.

---

## 🔄 Complete System Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         USER INTERACTION                                 │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                    User adds/modifies config file
                                  │
                                  ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                         CONFIGS DIRECTORY                                │
│                                                                          │
│   configs/                                                               │
│   ├── CORE-SW-01.txt    ← New or modified file                         │
│   ├── ACCESS-SW-02.txt                                                  │
│   └── DISTRIB-SW-03.txt                                                 │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                    File change detected (chokidar)
                                  │
                                  ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                          FILE WATCHER                                    │
│                       (automation/watcher.js)                            │
│                                                                          │
│  1. Detect file change                                                  │
│  2. Debounce (wait for stability)                                       │
│  3. Check processing lock                                               │
│  4. Spawn processor                                                     │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                      Spawn: node processor.js <file>
                                  │
                                  ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                        CONFIGURATION PROCESSOR                           │
│                       (automation/processor.js)                          │
│                                                                          │
│  Step 1: Read configuration file                                        │
│  Step 2: Extract IOS version                                           │
│  Step 3: Load prompt template                                           │
│  Step 4: Build complete prompt                                          │
│  Step 5: Send to LLM                                                    │
│  Step 6: Receive documentation                                          │
│  Step 7: Save to output/                                                │
│  Step 8: Git commit                                                     │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ↓                           ↓
┌──────────────────────────────┐   ┌──────────────────────────────┐
│       LOCAL LLM              │   │      MCP SERVER              │
│  (Ollama/LM Studio/etc)      │   │  (mcp-server/server.js)      │
│                              │   │                              │
│  • Receives prompt           │   │  • Cisco documentation       │
│  • Analyzes config           │◄──┤  • Command lookup            │
│  • Uses MCP tools            │───┤  • Feature docs              │
│  • Generates markdown        │   │  • Syntax validation         │
└──────────────────────────────┘   └──────────────────────────────┘
                    │
                    │
                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                         OUTPUT DIRECTORY                                 │
│                                                                          │
│   output/                                                                │
│   ├── CORE-SW-01.md       ← Generated documentation                    │
│   ├── ACCESS-SW-02.md                                                   │
│   └── DISTRIB-SW-03.md                                                  │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                     Git add + commit (if enabled)
                                  │
                                  ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                          GIT REPOSITORY                                  │
│                                                                          │
│  • Commits tracked                                                      │
│  • Version history maintained                                           │
│  • Optional push to remote                                              │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                                  │
                                  ↓
                           ✅ COMPLETE!
```

---

## 📋 Detailed Processing Steps

### Step-by-Step Breakdown

```
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: File Detection                                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  configs/CORE-SW-01.txt added/modified                          │
│              ↓                                                   │
│  Chokidar detects change                                        │
│              ↓                                                   │
│  Wait 2 seconds (stabilization)                                 │
│              ↓                                                   │
│  Trigger: processConfigFile()                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: Read Configuration                                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  fs.readFile('configs/CORE-SW-01.txt')                          │
│              ↓                                                   │
│  configContent = "version 15.2\nhostname CORE-SW-01..."         │
│              ↓                                                   │
│  File size: ~4KB                                                │
│  Lines: ~150                                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│ STEP 3: Extract IOS Version                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Regex patterns:                                                │
│  • /Cisco IOS Software.*Version ([0-9.()A-Z]+)/i               │
│  • /version ([0-9.]+)/i                                         │
│              ↓                                                   │
│  Match: "version 15.2"                                          │
│              ↓                                                   │
│  iosVersion = "15.2"                                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│ STEP 4: Build Prompt                                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Load: automation/prompts/analysis_template.txt                 │
│              ↓                                                   │
│  Replace placeholders:                                          │
│  • {{CONFIG_CONTENT}} → actual config text                     │
│  • {{IOS_VERSION}} → "15.2"                                    │
│  • {{FILENAME}} → "CORE-SW-01.txt"                             │
│              ↓                                                   │
│  Final prompt: ~6000 tokens                                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│ STEP 5: Call LLM                                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  POST http://localhost:11434/v1/chat/completions                │
│  {                                                               │
│    "model": "llama3.1:8b",                                      │
│    "messages": [                                                 │
│      {"role": "system", "content": "..."},                      │
│      {"role": "user", "content": "{{PROMPT}}"}                 │
│    ],                                                            │
│    "temperature": 0.7,                                          │
│    "max_tokens": 8000                                           │
│  }                                                               │
│              ↓                                                   │
│  Processing time: 30-120 seconds                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│ STEP 5a: LLM Uses MCP Tools (Optional)                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  LLM encounters: "switchport mode trunk"                        │
│              ↓                                                   │
│  Calls: search_command("switchport")                            │
│              ↓                                                   │
│  MCP Server reads: docs_cache/basic_commands.json               │
│              ↓                                                   │
│  Returns: {                                                      │
│    "description": "Sets interface as Layer 2...",              │
│    "syntax": "switchport mode <mode>",                          │
│    "modes": ["access", "trunk", ...]                           │
│  }                                                               │
│              ↓                                                   │
│  LLM uses info to enhance documentation                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│ STEP 6: Receive Documentation                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  LLM Response:                                                   │
│  {                                                               │
│    "choices": [{                                                 │
│      "message": {                                                │
│        "content": "# Switch Configuration Documentation..."    │
│      }                                                           │
│    }]                                                            │
│  }                                                               │
│              ↓                                                   │
│  Extract markdown content                                        │
│              ↓                                                   │
│  documentation = "# Switch Configuration..."                    │
│  Size: ~5000-10000 tokens                                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│ STEP 7: Save Documentation                                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Output filename: CORE-SW-01.md                                 │
│              ↓                                                   │
│  fs.writeFile('output/CORE-SW-01.md', documentation)            │
│              ↓                                                   │
│  File created: output/CORE-SW-01.md                             │
│  Size: ~15-30 KB                                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│ STEP 8: Git Commit                                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  git add output/CORE-SW-01.md                                   │
│              ↓                                                   │
│  git commit -m "Update documentation: CORE-SW-01.txt            │
│                                                                  │
│  Generated from: CORE-SW-01.txt                                 │
│  Timestamp: 2024-11-25T14:30:00.000Z                            │
│  Auto-generated by Cisco Config Documentation System"           │
│              ↓                                                   │
│  Commit created: a3f8b9c                                        │
│              ↓                                                   │
│  Optional: git push origin main                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                         ↓
                    ✅ SUCCESS!
```

---

## 🔌 MCP Server Interaction

```
┌──────────────────────────────────────────────────────────────────┐
│                         LLM PROCESSING                            │
│                                                                   │
│  LLM analyzing config and encounters unfamiliar command          │
└──────────────────────────────────────────────────────────────────┘
                              │
                              │ Need info about "spanning-tree"
                              │
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│                      MCP TOOL CALL REQUEST                        │
│                                                                   │
│  {                                                                │
│    "tool": "search_command",                                     │
│    "arguments": {                                                 │
│      "command": "spanning-tree",                                 │
│      "ios_version": "15.2"                                       │
│    }                                                              │
│  }                                                                │
└──────────────────────────────────────────────────────────────────┘
                              │
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│                       MCP SERVER PROCESSES                        │
│                                                                   │
│  1. Receive request via stdio                                    │
│  2. Parse command: "spanning-tree"                               │
│  3. Load: docs_cache/basic_commands.json                         │
│  4. Search for matching command                                  │
│  5. Format response                                              │
└──────────────────────────────────────────────────────────────────┘
                              │
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│                     DOCUMENTATION LOOKUP                          │
│                                                                   │
│  docs_cache/basic_commands.json:                                 │
│  {                                                                │
│    "spanning-tree": {                                            │
│      "description": "Configures Spanning Tree Protocol",         │
│      "syntax": "spanning-tree <options>",                        │
│      "examples": [                                                │
│        "spanning-tree mode rapid-pvst",                          │
│        "spanning-tree portfast"                                  │
│      ],                                                           │
│      "modes": ["pvst", "rapid-pvst", "mst"]                     │
│    }                                                              │
│  }                                                                │
└──────────────────────────────────────────────────────────────────┘
                              │
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│                      MCP TOOL RESPONSE                            │
│                                                                   │
│  {                                                                │
│    "content": [                                                   │
│      {                                                            │
│        "type": "text",                                           │
│        "text": "Command: spanning-tree\n\n{...}"                │
│      }                                                            │
│    ]                                                              │
│  }                                                                │
└──────────────────────────────────────────────────────────────────┘
                              │
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│                     LLM RECEIVES CONTEXT                          │
│                                                                   │
│  LLM now has:                                                    │
│  • Original config section                                       │
│  • Cisco documentation for spanning-tree                         │
│  • Syntax and examples                                           │
│  │                                                                │
│  Uses this to generate accurate documentation                    │
└──────────────────────────────────────────────────────────────────┘
                              │
                              ↓
                  Continue generating documentation...
```

---

## 🔁 Parallel Processing Flow

```
Multiple files added simultaneously:

configs/
├── SW-01.txt  ─┐
├── SW-02.txt  ─┤
└── SW-03.txt  ─┤
                │
                └──→ File Watcher detects all
                         │
                ┌────────┼────────┐
                │        │        │
                ↓        ↓        ↓
          ┌─────────┬─────────┬─────────┐
          │Process 1│Process 2│Process 3│
          │SW-01.txt│SW-02.txt│SW-03.txt│
          └─────────┴─────────┴─────────┘
                │        │        │
                └────────┼────────┘
                         │
            All use same LLM (sequential)
                         │
                ┌────────┼────────┐
                │        │        │
                ↓        ↓        ↓
          ┌─────────┬─────────┬─────────┐
          │ SW-01.md│ SW-02.md│ SW-03.md│
          └─────────┴─────────┴─────────┘
                │        │        │
                └────────┼────────┘
                         │
                    Git commits
                         │
                         ↓
                    All complete!
```

**Note**: Files are detected in parallel but processed sequentially to avoid overloading the LLM.

---

## 📊 Data Flow Diagram

```
INPUT                PROCESSING              EXTERNAL            OUTPUT
                                            SERVICES

┌──────────┐
│  .txt    │
│  Config  │─────┐
│  Files   │     │
└──────────┘     │
                 │
┌──────────┐     │    ┌──────────────┐
│ config.  │     ├───→│              │
│  json    │─────┤    │  Processor   │
└──────────┘     │    │              │
                 │    └──────┬───────┘
┌──────────┐     │           │
│ Prompt   │     │           │
│ Template │─────┘           │
└──────────┘                 │
                             │
                             ├──────→ ┌───────────┐
                             │        │    LLM    │
                             │        │  (Local)  │
                             │        └─────┬─────┘
                             │              │
                             │              ↓
                             │        ┌───────────┐
                             │        │    MCP    │
                             │        │  Server   │
                             │        └─────┬─────┘
                             │              │
                             │              ↓
                             │        ┌───────────┐     ┌──────────┐
                             │        │   Docs    │────→│ Markdown │
                             │        │   Cache   │     │   .md    │
                             │        └───────────┘     └──────────┘
                             │                                │
                             ├────────────────────────────────┘
                             │
                             ↓
                       ┌───────────┐
                       │    Git    │
                       │Repository │
                       └───────────┘
```

---

## ⏱️ Timeline View

```
TIME →

0s      User adds file to configs/
│
│       ┌─────────────────────────────┐
2s      │ File watcher debounce      │
│       └─────────────────────────────┘
│
│       Spawn processor
│
3s      ┌─────────────────────────────┐
│       │ Read file                   │
│       │ Extract version             │
│       │ Build prompt                │
5s      └─────────────────────────────┘
│
│       ┌─────────────────────────────┐
│       │                             │
│       │ Send to LLM                 │
10s     │                             │
│       │                             │
│       │ LLM processing...           │
30s     │                             │
│       │                             │
│       │ (Multiple MCP calls)        │
60s     │                             │
│       │                             │
│       │                             │
90s     │                             │
│       └─────────────────────────────┘
│
│       Receive response
│
│       ┌─────────────────────────────┐
92s     │ Save markdown               │
│       │ Git add                     │
│       │ Git commit                  │
95s     └─────────────────────────────┘
│
│       ✅ Complete!
│
100s    Ready for next file
```

---

## 🔄 State Machine

```
                    ┌──────────────┐
                    │    IDLE      │
                    └──────┬───────┘
                           │
                File Added │
                           │
                           ↓
                    ┌──────────────┐
                    │  DETECTED    │
                    └──────┬───────┘
                           │
              Debounce OK  │
                           │
                           ↓
                    ┌──────────────┐
               ┌────┤  PROCESSING  │────┐
               │    └──────────────┘    │
               │                         │
        Error  │                         │ Success
               │                         │
               ↓                         ↓
        ┌──────────────┐         ┌──────────────┐
        │    FAILED    │         │  COMPLETED   │
        └──────┬───────┘         └──────┬───────┘
               │                         │
               │                         │
               └────────┬────────────────┘
                        │
                        ↓
                 ┌──────────────┐
                 │    IDLE      │
                 └──────────────┘
```

---

## 🎭 Error Handling Flow

```
                    ┌──────────────┐
                    │ Start Process │
                    └──────┬────────┘
                           │
                           ↓
                    ┌──────────────┐
                    │  Read File   │
                    └──────┬────────┘
                           │
                ┌──────────┼──────────┐
                │ Success             │ Error
                ↓                     ↓
        ┌──────────────┐      ┌──────────────┐
        │ Extract Ver. │      │  Log Error   │
        └──────┬────────┘      │  Exit(1)     │
               │                └──────────────┘
               ↓
        ┌──────────────┐
        │ Build Prompt │
        └──────┬────────┘
               │
               ↓
        ┌──────────────┐
        │   Call LLM   │
        └──────┬────────┘
               │
    ┌──────────┼──────────┐
    │ Success             │ Error
    ↓                     ↓
┌──────────┐      ┌──────────────┐
│Save Docs │      │ Log LLM Err  │
└────┬─────┘      │  Exit(1)     │
     │            └──────────────┘
     ↓
┌──────────┐
│Git Commit│
└────┬─────┘
     │
     ├──────────┬──────────┐
     │ Success  │ Error    │
     ↓          ↓
┌─────────┐ ┌──────────┐
│Complete!│ │Log Warn  │
│Exit(0)  │ │Exit(0)   │ ← Still success!
└─────────┘ └──────────┘
```

---

## 📦 Package Dependencies

```
Root Project
│
├── mcp-server/
│   ├── @modelcontextprotocol/sdk
│   ├── cheerio (for future web scraping)
│   └── axios (for HTTP requests)
│
└── automation/
    ├── chokidar (file watching)
    ├── axios (LLM API calls)
    └── simple-git (version control)
```

---

*These workflows help visualize how the system operates end-to-end.*