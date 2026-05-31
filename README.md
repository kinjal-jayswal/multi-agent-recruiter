# 👔 Multi-Agent Recruiter — JK Data Lab

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Agentic AI](https://img.shields.io/badge/Agentic-AI-00FFD4?style=flat)](https://www.jkdatalab.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![Author](https://img.shields.io/badge/Author-JK_Data_Lab-blueviolet?style=flat)](https://www.jkdatalab.com)

> Four specialised AI agents collaborate to handle the full recruitment pipeline — from writing job descriptions to generating offer letters.

---

## What It Does

- **JD Writer Agent** — generates a professional job description based on role, skills, and experience level
- **Resume Screener Agent** — produces targeted screening questions to filter candidates before interviews
- **Interview Question Generator** — creates structured technical and behavioural interview questions (STAR method)
- **Offer Letter Writer Agent** — drafts a complete, personalised offer letter with salary and benefits
- **Demo Mode** — runs fully offline without any LLM backend; toggle via the sidebar checkbox

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Streamlit UI  (app.py)                 │
│  Role · Skills · Experience · Salary  ──▶  Run Button  │
└──────────────────────┬──────────────────────────────────┘
                       │  triggers all 4 agents
          ┌────────────┼────────────┬──────────────┐
          ▼            ▼            ▼              ▼
    📋 JD Writer  🔍 Screener  ❓ Interview   📄 Offer
                                Generator    Letter Writer
          │            │            │              │
          └────────────┴────────────┴──────────────┘
                       │  tabbed output + download
                  ┌────▼────┐
                  │  Tabs   │  (Job Description · Screening ·
                  └─────────┘   Interview · Offer Letter)
```

---

## Quick Start

### 1. Clone & install

```bash
git clone <repo-url>
cd 08_multi_agent_recruiter

# Create and activate virtual environment
python -m venv venv

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Run

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501` in your browser.

---

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| Demo Mode (sidebar) | `True` | Runs without any LLM — uses built-in templates |
| Job Role | — | Text input for the role being hired |
| Required Skills | `Python, ML, SQL, Data Analysis` | Comma-separated skills list |
| Years Experience | `3` | Slider 1–15 years |
| Salary Range | `$80,000 - $120,000` | Displayed in JD and offer letter |

### Optional: Ollama LAN Setup

```bash
ollama pull llama3
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

Disable **Demo Mode** in the sidebar to route agent calls through Ollama.

---

## Project Structure

```
08_multi_agent_recruiter/
├── app.py              # Main Streamlit app — all 4 agent flows
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── venv/               # Virtual environment (not committed)
```

---

## Requirements

| Package | Purpose |
|---------|---------|
| `streamlit>=1.35.0` | Web UI framework |
| `langchain>=0.2.0` | Agent orchestration |
| `langchain-community>=0.2.0` | Ollama & community LLM integrations |
| `requests>=2.31.0` | HTTP calls to external APIs |
| `pandas>=2.2.0` | Data handling |
| `numpy>=1.26.0` | Numerical operations |
| `plotly>=5.22.0` | Interactive charts |
| `openpyxl>=3.1.2` | Excel export |

---

## Module Series

This project is **Module 08** of the JK Data Lab Agentic AI series:

| # | Module |
|---|--------|
| … | … |
| 08 | **Multi-Agent Recruiter** ← you are here |

---

## License

MIT © [Kinjal Jayswal — JK Data Lab](https://www.jkdatalab.com)

---

<div align="center">
Built with ❤️ by <strong><a href="https://www.jkdatalab.com">JK Data Lab</a></strong><br>
📧 kinjal@jkdatalab.com &nbsp;|&nbsp; 🌐 www.jkdatalab.com
</div>
