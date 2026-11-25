class Person:
    def __init__(self, name):
        self.name = name


print("instance attributes:", vars(Person("Ada")))