class Example:
    def __init__(self):
        self.name = "unknown"


item = Example()
setattr(item, "name", "Ada")
print("name:", item.name)