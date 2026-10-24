# 🎓 K_M_S — Teachable Knowledge Management System

A streamlined, structured Knowledge Management System designed as the foundational repository for learning programming, capturing concepts, and developing sustainable documentation habits.

---

## 🎯 Educational Purpose & Objectives

Learning programming is not simply about consuming information; retaining, organizing, and applying knowledge is equally vital. The **K_M_S** provides an actionable, teachable architecture that empowers learners to:

1. **Capture Important Concepts:** Record mental models, theory, and core computer science foundations in tool-agnostic formats.
2. **Organize Notes Effectively:** Prevent information fragmentation using a structured Three-Layer taxonomy.
3. **Create Reusable References:** Build high-density cheat sheets and command references for fast retrieval.
4. **Track Discoveries and Lessons Learned:** Document real-world troubleshooting steps, error solutions, and daily reflections.
5. **Develop Personal Documentation Habits:** Cultivate professional engineering practices through documentation-as-code and version control.

The result is a personal knowledge base that grows in utility and value over time.

---

## 🏗️ Architecture: The Three-Layer Model

The system is organized into three distinct, interconnected layers:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                 K_M_S (TEACHABLE KNOWLEDGE MANAGEMENT SYSTEM)               │
├─────────────────────────────────────────────────────────────────────────────┤
│ 🧱 LAYER 1: SOFTWARE-CENTRIC (Where Tools & Configurations Live)            │
│    software/<tool_name>/ (00-overview to 06-troubleshooting)                │
│    Example: software/python/, software/git/                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ 🧭 LAYER 2: CROSS-CUTTING KNOWLEDGE (Durable Concepts & Shared Assets)      │
│    cheat_sheets/ | concepts/ | glossary/ | meta_learning/ | patterns/       │
│    templates/    | workflows/                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│ 🔗 LAYER 3: ACTIVE LEARNING (The Dynamic Practice & Creation Workspace)    │
│    courses/ | daily_notes/ | experiments/ | learning_queue/                 │
│    reference_library/ | research/                                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 🧱 Layer 1: Software-Centric Knowledge ([`software/`](software/README.md))
Tool-specific documentation organized by application name (e.g., `software/python/`, `software/git/`). Every tool directory follows a standard **7-file internal structure**:
- `00-overview.md` — High-level purpose and mental models.
- `01-installation.md` — Installation, setup, and verification.
- `02-core-concepts.md` — Essential principles specific to the tool.
- `03-workflows.md` — Repeatable step-by-step procedures.
- `04-commands.md` — Command references, CLI flags, and shortcuts.
- `05-projects/` — Lightweight learning artifacts and code spikes.
- `06-troubleshooting.md` — Error logs, root cause analysis, and fixes.

### 🧭 Layer 2: Cross-Cutting Knowledge
Durable, reusable knowledge that spans multiple programming languages, tools, and environments:
- **[`cheat_sheets/`](cheat_sheets/README.md)** — Quick-reference summaries and command cheat sheets.
- **[`concepts/`](concepts/README.md)** — Tool-agnostic computer science theory (e.g., computational thinking, abstraction, version control).
- **[`glossary/`](glossary/README.md)** — Terminology dictionary with atomic definitions (`glossary_items.json`).
- **[`meta_learning/`](meta_learning/README.md)** — Methods for learning how to learn, documentation habits, and architectural guidelines.
- **[`patterns/`](patterns/README.md)** — Reusable naming conventions, code layout standards, and minimal working examples.
- **[`templates/`](templates/README.md)** — Master scaffolding blueprints for creating new notes, tools, and courses.
- **[`workflows/`](workflows/README.md)** — Standard Operating Procedures for daily logging and note distillation.

### 🔗 Layer 3: Active Learning ([`active_learning/`](active_learning/README.md))
The high-velocity workspace where active learning occurs:
- **[`courses/`](active_learning/courses/README.md)** — Structured learning paths, syllabi, and exercise records.
- **[`daily_notes/`](active_learning/daily_notes/README.md)** — Daily journals capturing what you learned, built, and fixed.
- **[`experiments/`](active_learning/experiments/README.md)** — Sandboxes and temporary code spikes.
- **[`learning_queue/`](active_learning/learning_queue/README.md)** — Prioritized backlog of topics to explore.
- **[`reference_library/`](active_learning/reference_library/README.md)** — Curated books, official documentation links, and articles.
- **[`research/`](active_learning/research/README.md)** — Deep-dive exploratory notes and preliminary studies.

---

## 🚀 Quickstart: How to Use K_M_S as a Student

### Day 1: Daily Journaling
1. Open [`templates/daily_notes_template/01-daily-notes-template.md`](templates/daily_notes_template/01-daily-notes-template.md).
2. Copy it into `active_learning/daily_notes/` named with today's date (e.g., `YYYY-MM-DD-daily-notes.md`).
3. Log what you studied, problems you hit, and quick commands you learned.

### Day 7: Documenting Your First Tool
1. Copy [`templates/software_template/`](templates/software_template/) into `software/<your_tool>/`.
2. Fill in how you installed it, key commands you use, and common troubleshooting solutions.

### Day 30: Distilling Durable Concepts
1. Review your daily notes for recurring patterns.
2. Extract general principles into [`concepts/`](concepts/README.md) using [`templates/concept_template/01-concept-template.md`](templates/concept_template/01-concept-template.md).
3. Add quick syntax reminders to [`cheat_sheets/`](cheat_sheets/README.md).

---

## 🏷️ System Conventions

- **Directories:** Named in `snake_case` (e.g., `active_learning`, `daily_notes`).
- **Markdown Files:** Named in `numeric-prefix + kebab-case` (e.g., `01-setup-guide.md`).
- **Jupyter Notebooks:** Named in `snake_case` (e.g., `01_setup_guide.ipynb`).
- **1:1 Dual-Format Parity:** Every document exists as both a Markdown file (`.md`) and a Jupyter Notebook (`.ipynb`).
- **No Virtual Environments inside K_M_S:** Execution environments belong outside the knowledge repository.
