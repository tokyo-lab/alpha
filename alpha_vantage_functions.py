import requests
import json
import io
import pandas as pd
from bs4 import BeautifulSoup

with open("config.json", "r") as config_file:
    config = json.load(config_file)

api_key = config.get("api_key")
print("apik key: ", api_key)

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = (
    "https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=AAPL&apikey="
    + str(api_key)
    + "&datatype=csv"
)
r = requests.get(url).content
# data = r.json()
data = pd.read_csv(io.StringIO(r.decode("utf-8")))

print(data)
