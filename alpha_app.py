import requests
import json


class RunThis:
    def __init__(self, stock_data):
        self.json_data = stock_data
        print("stock_data: ", stock_data)

    def StartApp(self, RunThis):
        # Load the list of stock tickers from a JSON file
        with open(self.json_data, "r") as tickers_file:
            data = json.load(tickers_file)
            print("data: ", data)

            tickers = data["tickers"]
            periods = data["periods"]
            print("tickers: ", tickers)
            print("periods", periods)
            # Create an empty dictionary to store the stock data

        # Load your API key from a configuration file (config.json in this case)
        with open("config.json", "r") as config_file:
            config = json.load(config_file)

        api_key = config.get("api_key")
        # print("API key: ", api_key)
        all_stock_data = {}

        # Loop through each ticker and fetch data
        for ticker in tickers:
            # Construct the API request URL for each ticker
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={ticker}&apikey={api_key}&datatype=json"

            #  Send the request and parse the JSON response
            response = requests.get(url)
            stock_data = response.json()
            print("stock_data", stock_data)

            # Add the stock data to the dictionary with the ticker symbol as the key
            all_stock_data[ticker] = stock_data


class StockDataAnalyzer:
    def __init__(self, stock_data):
        self.json_data = stock_data

    def get_last_n_weeks_close_prices(self, symbol, n):
        weekly_data = self.json_data[symbol]["Weekly Time Series"]
        last_n_weeks = list(weekly_data.items())[:n]

        for week, data in last_n_weeks:
            close_price = data["4. close"]
            # print(f"Week: {week}, Close Price: {close_price}")


# Create an instance of the StockDataAnalyzer class
# analyzer = StockDataAnalyzer(stock_data)

# Get and print the last 2 weeks' close prices for TSLA
# analyzer.get_last_n_weeks_close_prices("TSLA", n=2)

app = RunThis("tickers.json")
app.StartApp("tickers.json")
