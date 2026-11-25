import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "example.txt")
    with open(path, "w", encoding="utf-8") as file:
        file.write("Hello from a temporary file!\n")
    with open(path, encoding="utf-8") as file:
        print("file contents:", file.read().strip())