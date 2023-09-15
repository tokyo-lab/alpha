import json

# Load the JSON data from the file
with open("stock_data.json", "r") as json_file:
    stock_data = json.load(json_file)

# Initialize a dictionary to store close prices for each week
close_prices = {}

# Iterate through each ticker and its data
for ticker, data in stock_data.items():
    weekly_data = data.get("Weekly Time Series", {})

    # Iterate through each week's data
    for week, week_data in weekly_data.items():
        close_price = float(week_data.get("4. close", 0))  # Extract the close price

        # Add the close price to the close_prices dictionary
        if week not in close_prices:
            close_prices[week] = {}
        close_prices[week][ticker] = close_price

# Now, close_prices contains the close prices for each week, organized by week and ticker symbol
# You can access the close prices like close_prices[week][ticker]


# Get the last three weeks' data
last_three_weeks = list(stock_data["TSLA"]["Weekly Time Series"].items())[:3]

# Extract and print the close prices for the last three weeks
for week, data in last_three_weeks:
    close_price = data["4. close"]
    # print(f"Week: {week}, Close Price: {close_price}")


class StockDataAnalyzer:
    def __init__(self, json_data):
        self.json_data = json_data

    def get_last_n_weeks_close_prices(self, symbol, n):
        weekly_data = self.json_data[symbol]["Weekly Time Series"]
        last_n_weeks = list(weekly_data.items())[:n]

        for week, data in last_n_weeks:
            close_price = data["4. close"]
            # print(f"Week: {week}, Close Price: {close_price}")


# Create an instance of the StockDataAnalyzer class
analyzer = StockDataAnalyzer(stock_data)

# Get and print the last 2 weeks' close prices for TSLA
analyzer.get_last_n_weeks_close_prices("TSLA", n=2)
