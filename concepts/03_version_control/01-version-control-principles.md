# Version Control Principles

Version control is a disciplined, outcome-oriented system for tracking, managing, and coordinating changes to artifacts over time, maximizing team collaboration efficiency, system reliability, and overall project utility.

---

## 🎯 Definition & Core Problem
- **What is this concept?**
  Version control is an infrastructure and workflow framework built upon key foundational principles:
  - **Snapshot State & Integrity:** Recording the exact state of a project at discrete milestones via immutable, cryptographically verifiable snapshots rather than fragile delta logs.
  - **Traceability & Attribution:** Maintaining an auditable lineage of changes answering what was modified, who performed it, when it occurred, and why, thereby ensuring complete accountability and operational transparency.
  - **Non-Destructive Branching & Concurrency:** Enabling parallel exploration, feature development, and experimentation in isolated branches without endangering mainline stability.
  - **Deterministic Reconciliation & Rollback:** Providing deterministic mechanisms to merge concurrent contributions, resolve conflicts systematically, and revert to known stable states when errors arise.

- **What problem does it address?**
  Without disciplined version control, collaborative development rapidly degenerates into chaotic overwrites, untraceable regressions, duplicated labor, and catastrophic data loss. Version control eliminates coordination bottlenecks and mitigates operational risk by preserving history, facilitating continuous integration, and ensuring that collective engineering effort yields maximal net utility.

## 🧠 Mental Model / Metaphor
### The Architectural Ledger and Blueprint Archive
Imagine an engineering firm constructing a complex municipal infrastructure project:
- **Snapshots:** Rather than scribbling unverified adjustments over existing plans, architects create complete, version-stamped blueprint sets for each approved milestone.
- **Traceability:** Every revision stamp identifies the responsible engineer, timestamp, and design rationale, making the engineering lineage transparent and audit-ready.
- **Branching:** Specialized engineering teams draft alternative structural proposals on isolated overlay drafts without disrupting the core master blueprint.
- **Deterministic Merge & Rollback:** Master inspectors systematically synthesize verified overlay changes into the primary construction plans, or instantly reinstate previous certified blueprints if an issue arises.

## 💻 Code Demonstration
```python
"""
Demonstrating Version Control Principles:
Goal: Implement a minimal, deterministic snapshot-based version control system to maximize change traceability and state integrity.
"""
import hashlib
import time
from typing import Dict, List, Optional


class Commit:
    """Represents an immutable snapshot of project state with cryptographic verification."""

    def __init__(
        self,
        tree: Dict[str, str],
        message: str,
        author: str,
        parent_hash: Optional[str] = None,
    ) -> None:
        self.tree = dict(tree)  # Immutable snapshot of file contents
        self.message = message
        self.author = author
        self.parent_hash = parent_hash
        self.timestamp = time.time()
        self.commit_hash = self._calculate_hash()

    def _calculate_hash(self) -> str:
        """Compute deterministic SHA-256 hash based on snapshot tree, metadata, and parent."""
        content_repr = f"{sorted(self.tree.items())}:{self.message}:{self.author}:{self.parent_hash}"
        return hashlib.sha256(content_repr.encode("utf-8")).hexdigest()[:8]


class Repository:
    """Manages snapshots, history log, and branch references to ensure reliable collaboration."""

    def __init__(self) -> None:
        self.commits: Dict[str, Commit] = {}
        self.branches: Dict[str, Optional[str]] = {"main": None}
        self.active_branch: str = "main"
        self.working_directory: Dict[str, str] = {}

    def write_file(self, filename: str, content: str) -> None:
        """Update or create a file in the working directory."""
        self.working_directory[filename] = content

    def commit(self, message: str, author: str) -> str:
        """Record an immutable snapshot of the current working directory."""
        parent_hash = self.branches.get(self.active_branch)
        new_commit = Commit(
            tree=self.working_directory,
            message=message,
            author=author,
            parent_hash=parent_hash,
        )
        self.commits[new_commit.commit_hash] = new_commit
        self.branches[self.active_branch] = new_commit.commit_hash
        return new_commit.commit_hash

    def log(self) -> List[str]:
        """Generate an audit trail of changes along the current branch lineage."""
        history: List[str] = []
        curr_hash = self.branches.get(self.active_branch)
        while curr_hash:
            c = self.commits[curr_hash]
            history.append(f"[{c.commit_hash}] {c.author}: {c.message}")
            curr_hash = c.parent_hash
        return history

    def checkout_snapshot(self, commit_hash: str) -> None:
        """Revert working state deterministically to a previous verified snapshot."""
        if commit_hash not in self.commits:
            raise KeyError(f"Snapshot {commit_hash} does not exist.")
        self.working_directory = dict(self.commits[commit_hash].tree)


# Example Execution
if __name__ == "__main__":
    repo = Repository()

    # 1. Initial State Commit
    repo.write_file("main.py", "print('Initial utility function')")
    hash1 = repo.commit("feat: initial utility function setup", author="Alice")

    # 2. Iterative Improvement
    repo.write_file("main.py", "print('Optimized utility function with error handling')")
    repo.write_file("config.json", '{"efficiency_target": 98.5}')
    hash2 = repo.commit("perf: enhance efficiency and add configuration", author="Bob")

    # 3. View Traceable History Log
    print("Commit History:")
    for entry in repo.log():
        print(f"  {entry}")

    # 4. Deterministic Rollback Demonstration
    print(f"Working Directory files: {list(repo.working_directory.keys())}")
    repo.checkout_snapshot(hash1)
    print(f"Files after rollback to {hash1}: {list(repo.working_directory.keys())}")
    print(f"Content of main.py: {repo.working_directory['main.py']}")
```

## 🔗 Related Concepts
- [Computational Thinking Foundations](../01_computational_thinking/01-computational-thinking-foundations.md)
- [Understanding Abstraction](../02_abstraction/01-understanding-abstraction.md)
- [Concepts Overview](../../concepts/README.md)
