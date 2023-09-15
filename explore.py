import requests
import json

# Load your API key from a configuration file (config.json in this case)
with open("config.json", "r") as config_file:
    config = json.load(config_file)

api_key = config.get("api_key")
# print("API key: ", api_key)

# Load the list of stock tickers from a JSON file
with open("tickers.json", "r") as tickers_file:
    data = json.load(tickers_file)
    print("data: ", data)

    tickers = data["tickers"]
    print("tickers: ", tickers)
# Create an empty dictionary to store the stock data
all_stock_data = {}

# Loop through each ticker and fetch data
for ticker in tickers:
    # Construct the API request URL for each ticker
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={ticker}&apikey={api_key}&datatype=json"

    #  Send the request and parse the JSON response
    response = requests.get(url)
    stock_data = response.json()

    # Add the stock data to the dictionary with the ticker symbol as the key
    all_stock_data[ticker] = stock_data

# Save all_stock_data as a JSON file
with open("stock_data.json", "w") as json_file:
    json.dump(all_stock_data, json_file, indent=4)
