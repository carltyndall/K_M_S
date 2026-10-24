# Python: Core Concepts

Fundamental mental models for understanding how Python programs execute.

## 🧠 Mental Model: The Interpreter & Execution
Python code is executed line-by-line by the CPython interpreter:
1. Source code (`.py`) is parsed into an Abstract Syntax Tree (AST).
2. The AST is compiled into bytecode (`.pyc`).
3. The Python Virtual Machine (PVM) evaluates the bytecode instructions.

## 🧱 Key Building Blocks
- **Variables & Data Types:** Integers (`int`), Floats (`float`), Strings (`str`), Booleans (`bool`).
- **Data Collections:** Lists (`list`), Dictionaries (`dict`), Tuples (`tuple`), Sets (`set`).
- **Control Flow:** Conditional branching (`if/elif/else`), Loops (`for`, `while`).
- **Functions:** Named blocks of reusable code defined with `def`.
