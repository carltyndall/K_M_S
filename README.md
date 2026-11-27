# 🎓 K_M_S — Teachable Knowledge Management System

A streamlined, structured Knowledge Management System designed as the foundational repository for learning programming, capturing concepts, and developing sustainable documentation habits.

## 🎯 Educational Purpose & Objectives

Learning programming is not simply about consuming information; retaining, organizing, and applying knowledge is equally vital. The **K_M_S** provides an actionable, teachable architecture that empowers learners to:

1. **Capture Important Concepts:** Record mental models, theory, and core computer science foundations in tool-agnostic formats.
2. **Organize Notes Effectively:** Prevent information fragmentation using a structured Three-Layer taxonomy.
3. **Create Reusable References:** Build high-density cheat sheets and command references for fast retrieval.
4. **Track Discoveries and Lessons Learned:** Document real-world troubleshooting steps, error solutions, and daily reflections.
5. **Develop Personal Documentation Habits:** Cultivate professional engineering practices through documentation-as-code and version control.

The result is a personal knowledge base that grows in utility and value over time.

## 🏗️ Architecture: The Three-Layer Model

```text
K_M_S (TEACHABLE KNOWLEDGE MANAGEMENT SYSTEM)
├── 🧱 LAYER 1: SOFTWARE-CENTRIC (Tools & Configurations)
│   software/<tool_name>/ (00-overview to 06-troubleshooting)
│   Examples: software/python/, software/git/, software/uv/
├── 🧭 LAYER 2: CROSS-CUTTING KNOWLEDGE (Concepts & Shared Assets)
│   cheat_sheets/ | concepts/ | glossary/ | meta_learning/ | patterns/
│   templates/ | workflows/
└── 🔗 LAYER 3: ACTIVE LEARNING (Practice & Creation)
    courses/ | daily_notes/ | experiments/ | learning_queue/
    reference_library/ | research/  (under active_learning/)
```

The directories are a starting scaffold: their indexes describe intended content, not a prefilled reference library. Create notes as needed; the suggested software structure below is a plan, not a prerequisite for starting.

### 🧱 Layer 1: Software-Centric Knowledge ([`software/`](software/README.md))

Tool-specific documentation organized by application name (e.g., [`software/python/`](software/python/README.md), [`software/git/`](software/git/README.md), [`software/uv/`](software/uv/README.md)). A tool directory can grow into this standard **7-part internal structure**:

- `00-overview.md` — High-level purpose and mental models.
- `01-installation.md` — Installation, setup, and verification.
- `02-core-concepts.md` — Essential principles specific to the tool.
- `03-workflows.md` — Repeatable step-by-step procedures.
- `04-commands.md` — Command references, CLI flags, and shortcuts.
- `05-projects/` — Lightweight learning artifacts and code spikes.
- `06-troubleshooting.md` — Error logs, root cause analysis, and fixes.

The [Python directory](software/python/README.md) provides indexes for future notes on built-in constants, functions and types, exceptions, keywords, expressions, statements, methods, the data model, the standard library, and a Python glossary. It is not yet a complete Python reference.

### 🧭 Layer 2: Cross-Cutting Knowledge

Durable, reusable knowledge that spans multiple programming languages, tools, and environments:

- **[`cheat_sheets/`](cheat_sheets/README.md)** — Quick-reference summaries and command cheat sheets.
- **[`concepts/`](concepts/README.md)** — Tool-agnostic computer science theory (e.g., computational thinking, abstraction, version control).
- **[`glossary/`](glossary/README.md)** — Terminology dictionary with atomic definitions (optionally in `glossary_items.json`).
- **[`meta_learning/`](meta_learning/README.md)** — Methods for learning how to learn, documentation habits, and architectural guidelines.
- **[`patterns/`](patterns/README.md)** — Reusable naming conventions, code layout standards, and minimal working examples.
- **[`templates/`](templates/README.md)** — Master scaffolding blueprints for creating notes, tools, and courses.
- **[`workflows/`](workflows/README.md)** — Procedures for daily logging and note distillation.

### 🔗 Layer 3: Active Learning ([`active_learning/`](active_learning/README.md))

The workspace where active learning occurs:

- **[`courses/`](active_learning/courses/README.md)** — Structured learning paths, syllabi, and exercise records.
- **[`daily_notes/`](active_learning/daily_notes/README.md)** — Daily journals capturing what you learned, built, and fixed.
- **[`experiments/`](active_learning/experiments/README.md)** — Sandboxes and temporary code spikes.
- **[`learning_queue/`](active_learning/learning_queue/README.md)** — Prioritized backlog of topics to explore.
- **[`reference_library/`](active_learning/reference_library/README.md)** — Curated books, official documentation links, and articles.
- **[`research/`](active_learning/research/README.md)** — Deep-dive exploratory notes and preliminary studies.

## Start a learning session

1. On Windows 11, copy this starter folder to a location you can edit. Open it and its `.md` files in any text editor. Paths such as `active_learning\daily_notes\` below are relative to that folder.
2. Copy the [daily note template](templates/daily-note.md) into `active_learning\daily_notes\` and name it with today's date, for example `2026-11-25-daily-notes.md`. Record your topic, source and date, and explain what you learned in your own words.
3. Predict and try a small example. For a Python loop, use the code in [loop practice](active_learning/experiments/loop-practice.md): predict the total, run it in your existing Python environment, then try an empty list. Record the results in your daily note.
4. Write a recall question, answer it without looking, and check your answer. Review again tomorrow and next week; adjust the schedule to your needs.
5. Copy the [knowledge note template](templates/knowledge-note.md) into `concepts\` for a general insight or `software\` for tool-specific details. Name it for the topic, link your daily note and source, and include an example and a recall question.
6. When solving a new problem, retrieve the note, apply the idea, and update it with what you learned. Check current documentation for version-sensitive details.

See the illustrative [daily note](active_learning/daily_notes/2026-11-24-daily-notes.md), its promoted [loop concept](concepts/loops.md), and [Python-specific note](software/python-loops.md). The complete process is in the [learning loop](workflows/learning-loop.md).

AI can help you explore, but verify suggestions against reliable documentation or a small test before relying on them; do not share private information. Git can preserve your history if you use it, but is not required.