import json


class MyClass:
    def my_method(self, stock_file_path):
        stonks = read_json(stock_file_path)
        if stonks is None:
            return None
        periods = stonks.get("periods")

        print(f"periods from my_method: {periods}")

        print(f"Data received: {stock_file_path}")


def read_json(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{file_path} not found")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {file_path}")
        return None


def my_function(stock_file_path):
    # Instantiate class within function

    stonks = read_json(stock_file_path)
    if stonks is None:
        return None
    periods = stonks.get("periods")

    print(f"periods from my_function: {periods}")


# Instantiate class
my_instance = MyClass()

# Pass data
my_instance.my_method(stock_file_path="tickers.json")
my_function(stock_file_path="tickers.json")
