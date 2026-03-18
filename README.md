# Swarm Agent Blog Writer 🚀

A premium, multi-agent blog generation engine powered by **Swarm Intelligence** and **Groq (Llama 3.3 70B)**. This application orchestrates multiple specialized AI agents to create long-form, research-backed blog posts (800-1200 words) exported directly to professional PDF reports.

## ✨ Features

- **Multi-Agent Orchestration**: Specialized agents (Admin, Planner, Researcher, Writer, and Editor) work in a synchronized workflow.
- **70B-Powered Intelligence**: Standardized on **Llama 3.3 70B** for superior reasoning, long-form writing, and stable tool use.
- **Comprehensive Content**: Mandated 5-section planning with deep-dive research for high-quality, 1000+ word articles.
- **Bulletproof Communication**: Custom API compatibility layer that handles Groq/Gemini metadata and ensures stable agent handoffs.
- **Modern UI**: A sleek, dark-mode interface built with GSAP animations and Glassmorphism design.
- **Professional PDF**: Automatic conversion from Markdown to clean, formatted PDF reports.

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **AI Framework**: OpenAI Swarm (Modular Architecture)
- **Inference**: Groq (Llama 3.3 70B & 3.1 8B)
- **Frontend**: HTML5, Vanilla CSS, JavaScript (GSAP)
- **PDF Engine**: FPDF2 with Unicode support

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.8+
- Groq API Key
- Gemini API Key (Optional fallback)

### 2. Installation
```bash
# Clone the repository
git clone <repository-url>
cd Agent

# Install dependencies
pip install -r requirements.txt
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
│   ├── swarm_logic.py    # Multi-agent definitions & "Bulletproof" API layer
│   └── pdf_generator.py  # Markdown-to-PDF formatting engine
├── static/               # Sleek frontend assets (CSS/JS)
├── templates/            # Glassmorphism HTML templates
├── generated_docs/       # Destination for generated PDF reports
└── requirements.txt      # Project dependencies
```

## 🧠 Multi-Agent Workflow

1.  **Admin Agent**: Receives initial topic and initiates the planning phase.
2.  **Planner Agent**: Generates a 5+ section comprehensive outline.
3.  **Researcher Agent**: Gathers deep-dive facts and use-cases for every section.
4.  **Writer Agent**: Crafts the long-form content (target 800-1200 words).
5.  **Editor Agent**: Refines, formats, and finalizes the professional blog post.

## 🛡️ License
MIT License - Feel free to use and modify for your own projects!
