# 🎓 Courses

Structured learning paths, curricula outlines, and module notes.

---

## 🎯 Purpose

The `courses/` directory in Layer 3 provides dedicated workspaces for structured learning programs, online courses, tutorials, and certifications. It organizes course materials into predictable modules so you can track progression from syllabus to completed exercises.

---

## 🏗️ Standard Course Structure

Every course directory follows the standard 4-file scaffold from [`templates/course_template/`](../../templates/course_template/README.md):

- **`00-overview.md`** — High-level description, prerequisites, and learning outcomes.
- **`01-syllabus.md`** — Module-by-module breakdown, lesson schedule, and progress tracking.
- **`02-notes.md`** — Lecture notes, synthesized key takeaways, and conceptual summaries.
- **`03-exercises.md`** — Hands-on practice tasks, coding exercises, and solution notes.

---

## 🔄 Course Workflow

1. **Scaffold:** Copy [`templates/course_template/`](../../templates/course_template/README.md) into `active_learning/courses/<course_name>/` (named in `snake_case`).
2. **Plan:** Outline modules and objectives in `00-overview.md` and `01-syllabus.md`.
3. **Execute:** Record insights in `02-notes.md` and solve problem sets in `03-exercises.md`.
4. **Distill:** Promote reusable mental models to [`concepts/`](../../concepts/README.md) and tool workflows to [`software/`](../../software/README.md) using the [Distillation Workflow](../../workflows/02-knowledge-distillation-and-promotion-workflow.md).

---

## 📂 Available Courses
- **[`kms_foundations/`](./kms_foundations/README.md)** — Foundational course on building and maintaining your Knowledge Management System.
