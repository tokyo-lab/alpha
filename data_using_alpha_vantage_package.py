from alpha_vantage.timeseries import TimeSeries
from bs4 import BeautifulSoup
import pandas as pd
import io
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

api_key = config.get("api_key")
print("apik key: ", api_key)

ts1 = TimeSeries(key=api_key)

# Retrieve the monthly time series data for AAPL
# data, meta_data = ts1.get_monthly("AAPL")
data = ts1.get_weekly("AAPL")


# Print the data
print("Monthly Time Series Data for AAPL:")
print(data)

# Optionally, you can print the metadata as well
print("Meta Data:")
# print(meta_data)
