# Swarm AI Blog Writer 💎✨

A premium, multi-agent blog generation engine powered by **Structured Pydantic Intelligence** and **Groq (Llama 3.3 70B)**. This application orchestrates multiple specialized AI agents to create long-form, research-backed blog posts exported directly to professional PDF reports.

## ✨ Features

- **Multi-Agent Orchestration**: Specialized agents (Planner, Researcher, Writer) work in a synchronized Pydantic-validated pipeline.
- **70B-Powered Intelligence**: Standardized on **Llama 3.3 70B** for superior reasoning, long-form writing, and strict JSON schema adherence.
- **Comprehensive Content**: Mandated 5-section planning with deep-dive research for high-quality, 1000+ word articles.
- **SaaS Minimalist UI**: A stunning, high-contrast Vue.js 3 interface with GSAP animations and a boutique "Hard-Contrast" aesthetic.
- **Professional PDF**: Automatic conversion from Markdown to clean, formatted PDF reports with automated artifact cleanup.

## 🛠️ Tech Stack

- **Backend**: Flask (Python 3.10+)
- **Logic**: Pydantic (Structured Validation)
- **AI Inference**: Groq (Llama 3.3 70B)
- **Frontend**: Vue.js 3, Vite, Tailwind CSS, GSAP
- **PDF Engine**: FPDF2 (Custom formatting)

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.8+
- Node.js (for frontend development)
- Groq API Key

### 2. Installation
```bash
# Clone the repository
git clone <repository-url>
cd Agent

# Install backend dependencies
pip install -r requirements.txt

# Install frontend dependencies (optional for dev)
cd frontend && npm install && npm run build
```

### 3. Configuration
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_key_here
GEMINI_API_KEY=your_gemini_key_here
```

### 4. Running the App
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

## 📁 Project Structure

```text
Agent/
├── app.py                # Flask web server & job orchestration
├── core/                 # Core modular package
│   ├── agents.py         # Structured LLM & Agent definitions
│   ├── models.py         # Pydantic data models (BlogPlan, FinalBlog)
│   ├── swarm_logic.py    # Pipeline orchestration
│   └── pdf_generator.py  # Markdown-to-PDF formatting engine
├── frontend/             # Vue.js 3 + Vite source code
│   └── dist/             # Compiled production UI (Served by Flask)
├── generated_docs/       # Destination for generated PDF reports
└── requirements.txt      # Project dependencies
```

## 🧠 Multi-Agent Workflow

1.  **Planner Agent**: Generates a 5+ section comprehensive outline using 70B reasoning.
2.  **Researcher Agent**: Gathers deep-dive facts and sources for every section (70B-validated).
3.  **Writer Agent**: Crafts the final long-form Markdown content (target 1000+ words).
4.  **PDF Generator**: Sanitizes content and renders a professional PDF report.

## 🛡️ License
MIT License - Feel free to use and modify for your own projects!
