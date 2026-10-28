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

Example: `v1.0` Course Overview. Later tags (`v1.1`, `v2.0`, …) are filled in as lessons are recorded.

---

## 🧑‍🏫 Instructor workflow

At the **start** of a section or lesson, check out the previous checkpoint:

```bash
git checkout v1.0
```

Record the lesson. When the lesson is complete:

```bash
git add -A
git commit -m "feat: complete section N lesson M — <topic>"
git tag -a vN.M -m "Version N.M - <topic>"
git push origin HEAD
git push origin vN.M
```

Create a GitHub Release from that tag:

- **Tag:** `vN.M`
- **Title:** `Version N.M - <topic>`
- **Notes:** topics, assignment, next lesson (students can download ZIP/TAR without Git)

Sample release notes:

```markdown
# Lesson M - <topic>

## Topics
- TBD

## Assignment
TBD

## Next Lesson
TBD
```

---

## 🎓 Student workflow

Before watching a lesson:

```bash
git checkout vN.M   # previous checkpoint
```

After the lesson, inspect the completed snapshot:

```bash
git checkout vN.M   # this lesson
git diff vN.M-prev vN.M
```

Or download the matching GitHub Release if Git is not yet in use.

---

## 📚 Course map (Pure Python / Udemy)

Fill in topics as lessons are recorded. Only `v1.0` is current.

### Section 1: Course Introduction

| Version | Topic |
| :--- | :--- |
| v1.0 | Course Introduction |
| v1.1 | Why Another Python Course |
| v1.2 | TBD |
| v1.3 | TBD |

### Section 2: TBD

| Version | Topic |
| :--- | :--- |
| v2.0 | TBD |
| v2.1 | TBD |

### Section 3: TBD

| Version | Topic |
| :--- | :--- |
| v3.0 | TBD |
| v3.1 | TBD |

### Later sections

Add rows (`vN.M`) and section headings as the course grows.

---

## 🔗 Related

- Git commands: [`software/git/04-commands.md`](../software/git/04-commands.md)
- Git workflows: [`software/git/03-workflows.md`](../software/git/03-workflows.md)
- Course workspace: [`active_learning/courses/`](../active_learning/courses/README.md)
