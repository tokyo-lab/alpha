import requests
import json
import os


class RunThis:
    def __init__(self, stock_file_path, config_file_path):
        self.stock_file_path = stock_file_path
        self.config_file_path = config_file_path
        print("stock_data from class: ", stock_file_path)

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

    def StartApp(self):
        data = self.read_json(self.stock_file_path)
        if data is None:
            return None
        tickers = data["tickers"]
        periods = data["periods"]

        config = self.read_json(self.config_file_path)
        if config is None:
            return None
        api_key = config.get("api_key")

        all_stock_data = {}
        for ticker in tickers:
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={ticker}&apikey={api_key}&datatype=json"
            print("url: ", url)
            print("ticker: ", ticker)
            response = requests.get(url)
            all_stock_data[ticker] = response.json()
            weekly_data = data.get("Weekly Time Series", {})

        # Initialize a dictionary to store close prices for each week
        close_prices = {}

        # Iterate through each ticker and its data
        for ticker, data in all_stock_data.items():
            weekly_data = data.get("Weekly Time Series", {})
            last_n_weeks = list(weekly_data.items())[:periods]
            print("last_n_weeks:", last_n_weeks)

            # Iterate through each week's data

            for week, week_data in last_n_weeks:
                close_price = float(
                    week_data.get("4. close", 0)
                )  # Extract the close price

                # Add the close price to the close_prices dictionary
                if week not in close_prices:
                    close_prices[week] = {}
                    close_prices[week][ticker] = close_price

                print("close price: ", close_price)

        return all_stock_data


# Example of usage
app = RunThis(stock_file_path="tickers.json", config_file_path="config.json")
all_stock_data = app.StartApp()
