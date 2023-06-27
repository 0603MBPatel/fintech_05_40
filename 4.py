# person.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")

# Example usage
person1 = Person("John", 25)
person1.introduce()
