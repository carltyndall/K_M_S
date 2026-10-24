# Git: Core Concepts

Essential mental models for mastering version control.

## 🧠 Mental Model: The Three Trees
1. **Working Directory:** The local files you see and edit on disk.
2. **Staging Area (Index):** The draft snapshot of changes prepared for the next commit (`git add`).
3. **Commit History (Repository):** Permanent, immutable record of snapshots (`git commit`).

```text
[ Working Directory ] ── git add ──> [ Staging Area ] ── git commit ──> [ Repository ]
```
