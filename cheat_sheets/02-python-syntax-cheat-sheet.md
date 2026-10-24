# Python Syntax Cheat Sheet

Core language constructs and quick reminders.

## 🧱 Variables & Primitive Types
```python
age: int = 25
price: float = 19.99
name: str = "Alice"
is_active: bool = True
```

## 📦 Data Structures
```python
# List (ordered, mutable)
fruits = ["apple", "banana", "cherry"]

# Dictionary (key-value mapping)
user = {"id": 1, "name": "Alice"}

# Tuple (ordered, immutable)
coords = (10, 20)

# Set (unique elements)
unique_ids = {1, 2, 3}
```

## 🔁 Control Flow
```python
# Conditionals
if age >= 18:
    print("Adult")
else:
    print("Minor")

# For loop
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 3:
    print(count)
    count += 1
```

## ⚙️ Functions
```python
def calculate_total(price: float, tax_rate: float = 0.05) -> float:
    """Calculates total price including tax."""
    return price * (1 + tax_rate)
```
