class Person:
    def __init__(self, name, age):
        self._name = name  # Private attribute with a single underscore
        self._age = age  # Private attribute with a single underscore

    def get_name(self):
        return self._name

    # def set_name(self, name):
    #     self._name = name

    def get_age(self):
        return self._age

    # def set_age(self, age):
    #     if age >= 0:
    #         self._age = age

    def speak(self):
        print(f"{self._name} says hello!")


# Creating an instance of the Person class
person = Person("Cooper", 6)

# Accessing attributes and calling methods
print(person.get_name())  # Output: "Alice"
print(person.get_age())  # Output: 30
person.speak()  # Output: "Alice says hello!"
