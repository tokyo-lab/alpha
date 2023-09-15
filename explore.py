import requests
import json
import pandas as pd

# Load your API key from a configuration file (config.json in this case)
with open("config.json", "r") as config_file:
    config = json.load(config_file)

api_key = config.get("api_key")
# print("API key: ", api_key)

# Load the list of stock tickers from a JSON file
# Load the list of stock tickers from a JSON file
with open("tickers.json", "r") as tickers_file:
    data = json.load(tickers_file)
    print("data: ", data)

    tickers = data["tickers"]
    print("tickers: ", tickers)
# Initialize an empty DataFrame to store the stock data
all_data = pd.DataFrame()

# Loop through each ticker and fetch data
for ticker in tickers:
    # Construct the API request URL for each ticker
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={ticker}&apikey={api_key}&datatype=json"

    # Send the request and decode the response
    r = requests.get(url)
    # data = pd.read_csv(io.StringIO(r.decode("utf-8")))
    data = r.json()

    print(data)
