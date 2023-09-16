import requests
import json


class RunThis:
    def __init__(self, stock_file_path, config_file_path):
        self.stock_file_path = stock_file_path
        self.config_file_path = config_file_path
        print("stock_data from class: ", stock_file_path)

    def StartApp(self):
        # Load the list of stock tickers from a JSON file
        with open(self.stock_file_path, "r") as tickers_file:
            data = json.load(tickers_file)
            # print("data from StartApp function: ", data)

            tickers = data["tickers"]
            periods = data["periods"]
            # print("tickers: ", tickers)
            # print("periods", periods)
            # Create an empty dictionary to store the stock data

        # Load your API key from a configuration file (config.json in this case)
        try:
            with open(self.config_file_path, "r") as config_file:
                config = json.load(config_file)
                api_key = config.get("api_key")
        except FileNotFoundError:
            print("Configuration file not found")
        except json.JSONDecodeError:
            print("Error decoding JSON in config file")

        # print("API key: ", api_key)
        all_stock_data = {}

        # Loop through each ticker and fetch data
        for ticker in tickers:
            # Construct the API request URL for each ticker
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={ticker}&apikey={api_key}&datatype=json"
            print("url: ", url)
            #  Send the request and parse the JSON response
            response = requests.get(url)
            stock_data = response.json()
            print("stock_data", stock_data)

            # Add the stock data to the dictionary with the ticker symbol as the key
            all_stock_data[ticker] = stock_data

        return all_stock_data


class StockDataAnalyzer:
    def __init__(self, stock_file_path):
        self.stock_file_path = stock_file_path

    def get_last_n_weeks_close_prices(self, symbol, n):
        weekly_data = self.json_path[symbol]["Weekly Time Series"]
        last_n_weeks = list(weekly_data.items())[:n]

        for week, data in last_n_weeks:
            close_price = data["4. close"]
            # print(f"Week: {week}, Close Price: {close_price}")


# Create an instance of the StockDataAnalyzer class
# analyzer = StockDataAnalyzer(stock_data)

# Get and print the last 2 weeks' close prices for TSLA
# analyzer.get_last_n_weeks_close_prices("TSLA", n=2)

app = RunThis(stock_file_path="tickers.json", config_file_path="config.json")
app.StartApp()
