class Example:
    name = "Ada"


print("name:", getattr(Example(), "name"))
print("missing:", getattr(Example(), "missing", "default"))