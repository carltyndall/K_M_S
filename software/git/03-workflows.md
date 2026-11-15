# Git: Standard Workflows

Step-by-step sequences for tracking daily knowledge updates.

## 🔄 Daily Commit Routine
1. Check changed files:
   ```powershell
   git status
   ```
2. Stage modified documentation:
   ```powershell
   git add active_learning/daily_notes/
   ```
3. Commit with a meaningful message:
   ```powershell
   git commit -m "docs: add daily learning log for today"
   ```

## 🏷️ Course Project Checkpoint (tags + releases)

Use semantic course versioning `v<Section>.<Lesson>` on the student repository. Full SOP: [`workflows/03-course-project-versioning-workflow.md`](../../workflows/03-course-project-versioning-workflow.md).

1. Finish the lesson on a clean commit.
2. Annotate the checkpoint:
   ```bash
   git tag -a v2.1 -m "Version 2.1 - Python Programmer Development Environment"
   git push origin v2.1
   ```
3. Publish a GitHub Release from that tag so students can download a ZIP without Git.
4. Students restore a lesson with `git checkout v2.1` or compare with `git diff v2.0 v2.1`.
