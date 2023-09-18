import json


class MyClass:
    def __init__(self):
        self.periods = None  # Initialize attribute to store periods

    def my_method(self, stock_file_path):
        stonks = self.read_json(stock_file_path)
        if stonks is None:
            return None
        self.periods = stonks.get("periods")  # Store periods in the instance attribute

        print(f"periods from my_method: {self.periods}")

        print(f"Data received: {stock_file_path}")

    def read_json(self, file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"{file_path} not found")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON in {file_path}")
            return None


def my_function(periods):
    # # Instantiate class within function

    # stonks = read_json(stock_file_path)
    # if stonks is None:
    #     return None
    # periods = stonks.get("periods")

    print(f"periods from my_function: {periods}")


# Instantiate class
my_instance = MyClass()

# Pass data
my_instance.my_method(stock_file_path="tickers.json")

# Now periods is an attribute of my_instance, and we can pass it to my_function
my_function(my_instance.periods)
