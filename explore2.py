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


# Extract and print the close prices for each week
for week, data in stock_data["TSLA"]["Weekly Time Series"].items():
    close_price = data["4. close"]
    print(f"Week: {week}, Close Price: {close_price}")
