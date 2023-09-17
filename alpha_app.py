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

        config = self.read_json(self.config_file_path)
        if config is None:
            return None
        api_key = config.get("api_key")

        all_stock_data = {}
        for ticker in tickers:
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={ticker}&apikey={api_key}&datatype=json"
            print("url: ", url)
            response = requests.get(url)
            all_stock_data[ticker] = response.json()

        return all_stock_data


class StockDataAnalyzer(RunThis):
    def __init__(self, all_stock_data, stock_file_path, config_file_path):
        super().__init__(stock_file_path, config_file_path)
        self.all_stock_data = all_stock_data
        print("all_stock_data: ", all_stock_data)

    def get_last_n_weeks_close_prices(self, symbol, n):
        try:
            with open(self.stock_file_path, "r") as tickers_file:
                data = json.load(tickers_file)
        except FileNotFoundError:
            print("Stock file not found")
            return
        except json.JSONDecodeError:
            print("Error decoding JSON in stock file")
            return

        weekly_data = self.all_stock_data[symbol]["Weekly Time Series"]
        last_n_weeks = list(weekly_data.items())[:n]

        for week, data in last_n_weeks:
            close_price = data["4. close"]
            print(f"Week: {week}, Close Price: {close_price}")


# Example of usage
app = RunThis(stock_file_path="tickers.json", config_file_path="config.json")
all_stock_data = app.StartApp()
if all_stock_data:
    analyzer = StockDataAnalyzer(all_stock_data, "tickers.json", "config.json")
    analyzer.get_last_n_weeks_close_prices("MSFT", 2)
