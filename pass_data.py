# Method 1: Directly pass the variable as an argument to the function


class MyClass:
    def __init__(self, value):
        self.value = value


def my_function(some_value):
    print(f"Value from class: {some_value}")


# Create an object of MyClass
obj = MyClass(42)

# Pass the value to my_function
my_function(obj.value)

# Method 2: Return the value from a method and then pass it to the function


class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


def my_function(some_value):
    print(f"Value from class: {some_value}")


# Create an object of MyClass
obj = MyClass(42)

# Pass the value to my_function
my_function(obj.get_value())
