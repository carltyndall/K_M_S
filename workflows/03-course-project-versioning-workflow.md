# Course Project Versioning Workflow

Standard operating procedure for evolving a software project that is also a Udemy (or similar) training course. Source decision: use a **single GitHub repository** with **Git tags**, **GitHub Releases**, and **semantic course versioning** — not Gists.

---

## 🎯 Decision

| Approach | Use when |
| :--- | :--- |
| GitHub Gist | Tiny snippets, one-off demos, no releases |
| GitHub repository | Project evolves, students need downloads, docs, history |

**Chosen model:** one student-facing repository.

```text
Single Student Repository
    ↓
Git Tags
    ↓
GitHub Releases
    ↓
Semantic Course Versioning  v<Section>.<Lesson>
```

Do **not** publish secrets, tokens, passwords, or API keys. Prefer a private author repo and a public student repo if history is dirty.

---

## 🏷️ Version format

```text
v<Section>.<Lesson>
```

- **Major** = Udemy section
- **Minor** = lesson within that section

Examples: `v1.0` Course Overview, `v2.1` Python Programmer Development Environment, `v3.1` Install Python.

---

## 🧑‍🏫 Instructor workflow

At the **start** of a section or lesson, check out the previous checkpoint:

```bash
git checkout v2.0
```

Record the lesson. When the lesson is complete:

```bash
git add -A
git commit -m "feat: complete section 2 lesson 1 — Python PDE"
git tag -a v2.1 -m "Version 2.1 - Python Programmer Development Environment"
git push origin HEAD
git push origin v2.1
```

Create a GitHub Release from that tag:

- **Tag:** `v2.1`
- **Title:** `Version 2.1 - Python Programmer Development Environment`
- **Notes:** topics, assignment, next lesson (students can download ZIP/TAR without Git)

Sample release notes:

```markdown
# Lesson 5 - Functions

## Topics
- Function definitions
- Parameters
- Return values

## Assignment
Create a temperature conversion program.

## Next Lesson
Modules
```

---

## 🎓 Student workflow

Before watching a lesson:

```bash
git checkout v2.0
```

After the lesson, inspect the completed snapshot:

```bash
git checkout v2.1
git diff v2.0 v2.1
```

Or download the matching GitHub Release if Git is not yet in use.

---

## 📚 Course map (Pure Python / Udemy)

### Section 1: Course Overview

| Version | Topic |
| :--- | :--- |
| v1.0 | Course Overview |
| v1.1 | Goal 1 |
| v1.2 | Goal 2 |
| v1.3 | Goal 3 |
| v1.4 | Course Roadmap |
| v1.5 | Repository Tour |

### Section 2: Development Environment

| Version | Topic |
| :--- | :--- |
| v2.0 | What Is a Programmer's Development Environment? |
| v2.1 | Python Programmer Development Environment |
| v2.2 | Operating System Foundation |
| v2.3 | Development Environment Components |
| v2.4 | Hardware Considerations |
| v2.5 | Development Tools Overview |
| v2.6 | Preparing the Development Environment |

### Section 3: Python Installation

| Version | Topic |
| :--- | :--- |
| v3.0 | Installation Overview |
| v3.1 | Install Python |
| v3.2 | Verify Installation |
| v3.3 | Python.org Installation |
| v3.4 | Microsoft Store Installation |
| v3.5 | Managing Multiple Versions |
| v3.6 | Installing Packages |

### Section 4: Development Tools

| Version | Topic |
| :--- | :--- |
| v4.0 | Development Tools Overview |
| v4.1 | Visual Studio Code |
| v4.2 | VS Code Extensions |
| v4.3 | Integrated Terminal |
| v4.4 | Debugger |
| v4.5 | Source Control |
| v4.6 | Productivity Features |

### Section 5: Project Creation

| Version | Topic |
| :--- | :--- |
| v5.0 | Project Initialization |
| v5.1 | Repository Creation |
| v5.2 | GitHub Setup |
| v5.3 | Project Structure |
| v5.4 | README |
| v5.5 | .gitignore |
| v5.6 | First Release |

### Sections 6–15

```text
v6.x  Python Fundamentals
v7.x  Decisions and Loops
v8.x  Functions
v9.x  Modular Programming
v10.x File Processing
v11.x Object-Oriented Programming
v12.x Testing
v13.x Git and GitHub
v14.x Packaging and Distribution
v15.x Final Project
```

Lesson-level `vN.M` tags follow the same pattern as sections 1–5.

---

## 🔗 Related

- Git commands: [`software/git/04-commands.md`](../software/git/04-commands.md)
- Git workflows: [`software/git/03-workflows.md`](../software/git/03-workflows.md)
- Course workspace: [`active_learning/courses/`](../active_learning/courses/README.md)
