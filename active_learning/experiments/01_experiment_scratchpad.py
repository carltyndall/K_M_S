"""Experiment Scratchpad.

Use this file for quick code spikes and exploratory tests.
"""

def test_computation() -> int:
    numbers = [x * 2 for x in range(1, 6)]
    return sum(numbers)

if __name__ == "__main__":
    result = test_computation()
    print(f"Computed experiment result: {result}")
