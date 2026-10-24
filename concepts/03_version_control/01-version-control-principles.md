# Version Control Principles

Version control is the practice of tracking and managing changes to software code and documents over time.

---

## 🏛️ Core Principles
1. **Snapshot State:** Rather than saving incremental diffs, modern version control records the entire tree state at every commit milestone.
2. **Immutability:** Once a commit is recorded in history, its contents and cryptographic hash cannot change.
3. **Traceability:** Every modification answers:
   - *What was changed?* (`git diff`)
   - *Who changed it?* (`git log`)
   - *Why was it changed?* (Commit message)
