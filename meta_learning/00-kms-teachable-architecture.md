# K_M_S Teachable Architecture Specification

The Knowledge Management System (KMS) separates *where* knowledge is applied, *what* universal principles it represents, and the *active process* of learning it.

---

## 🏛️ Strategic Rationale

1. **Clean Separation of Concerns:**
   - Tools change (Layer 1: `software/`).
   - Concepts endure (Layer 2: `concepts/`, `cheat_sheets/`).
   - Daily learning moves fast (Layer 3: `active_learning/`).
2. **Dual-Format Parity:** Markdown (`.md`) and Jupyter Notebooks (`.ipynb`) exist as 1:1 pairs, supporting static reading and interactive execution.
3. **Lightweight & Portable:** No runtime virtual environments or IDE caches inside the KMS directory root.
