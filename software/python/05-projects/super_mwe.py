class Animal:
    def speak(self):
        return "sound"


class Dog(Animal):
    def speak(self):
        return super().speak() + ": woof"


print(Dog().speak())