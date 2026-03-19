# Swarm AI Blog Writer

A production-grade, multi-agent blog generation engine powered by **Pydantic AI structured validation** and **Groq (Llama 3.3 70B)**. Multiple specialized AI agents orchestrate in a synchronized pipeline to create long-form, research-backed blog posts exported as professional PDF reports.

---

## Features

- **Multi-Agent Orchestration**: Planner, Researcher, Writer, and Editor agents work in a Pydantic-validated pipeline.
- **70B-Powered Intelligence**: Standardized on Llama 3.3 70B via Groq for superior reasoning and strict schema adherence.
- **Comprehensive Content**: 5-section planning with deep-dive research producing 1000+ word articles.
- **Premium SaaS UI**: Vue.js 3 + GSAP + Tailwind CSS with a high-contrast minimalist aesthetic and bento-grid layout.
- **Professional PDF Export**: Automatic Markdown-to-PDF rendering with automated artifact cleanup.
- **Vercel Deployment**: Serverless-ready architecture with flat API structure and Vite-built frontend.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Vue.js 3, Vite 5, Tailwind CSS 3, GSAP 3, TypeScript |
| Icons | Lucide Vue Next |
| Backend | Flask (Python 3.10+), Serverless via Vercel |
| AI Inference | Groq API — Llama 3.3 70B |
| Validation | Pydantic v2 |
| PDF Engine | FPDF2 |
| Environment | python-dotenv |

---

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- Groq API Key

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd Swarm-Agent-Orchestrator

# Install frontend dependencies
npm install

# Install backend dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_key_here
```

### Running (Development)

```bash
# Start the Vite frontend dev server
npm run dev

# In a separate terminal, start the Flask API
python api/index.py
```

Visit `http://localhost:5173` in your browser.

### Building for Production

```bash
npm run build
```

---

## Project Structure

```text
Swarm-Agent-Orchestrator/
├── api/
│   ├── index.py              # Flask serverless entry point
│   └── core/                 # Core modular package
│       ├── agents.py         # LLM & Agent definitions
│       ├── models.py         # Pydantic data models (BlogPlan, FinalBlog)
│       ├── swarm_logic.py    # Pipeline orchestration
│       └── pdf_generator.py  # Markdown-to-PDF engine
├── src/
│   ├── components/
│   │   ├── Navbar.vue        # Floating pill navigation
│   │   ├── Hero.vue          # Hero section with CTA
│   │   ├── Features.vue      # Bento-grid feature cards
│   │   ├── AgentSwarm.vue    # Four-agent showcase cards
│   │   ├── Workspace.vue     # Topic input & swarm launcher
│   │   └── Footer.vue        # Site footer
│   ├── App.vue               # Root application with live generation panel
│   ├── main.ts               # App entry point
│   └── style.css             # Global Tailwind + custom styles
├── generated_docs/           # Generated PDF reports (local)
├── dist/                     # Built frontend (Vite output)
├── tailwind.config.js        # Custom tokens (shadows, colors)
├── vercel.json               # Vercel routing configuration
├── requirements.txt          # Python dependencies
└── package.json              # Node dependencies (v1.2.0)
```

---

## Multi-Agent Workflow

```
User Prompt
    │
    ▼
Planner Agent  ──► Generates 5-section structured outline (Llama 3.3 70B)
    │
    ▼
Researcher Agent ──► Deep-dive research for each section (Llama 3.3 70B)
    │
    ▼
Writer Agent  ──► Crafts final 1000+ word Markdown content (Llama 3.3 70B)
    │
    ▼
PDF Generator ──► Sanitizes content and exports professional PDF report
```

---

## Deployment

This project is configured for **Vercel** deployment with a flat, serverless-compatible architecture.

```bash
vercel deploy
```

The `vercel.json` routes all `/api/*` requests to the Flask serverless handler in `api/index.py`, while the Vite-built frontend is served from `dist/`.

---

## License

MIT License — Feel free to use and modify for your own projects.
