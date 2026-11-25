class Example:
    def __init__(self):
        self.label = "temporary"


item = Example()
delattr(item, "label")
print("label remains:", hasattr(item, "label"))