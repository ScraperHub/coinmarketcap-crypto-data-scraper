import requests
from bs4 import BeautifulSoup
import csv
import json

# 🛡️ Crawlbase Smart Proxy setup
proxy_url = "http://_USER_TOKEN_:@smartproxy.crawlbase.com:8012"
proxies = {"http": proxy_url, "https": proxy_url}

# 🌐 CoinMarketCap URL
url = "https://coinmarketcap.com/"

# 📥 Send HTTP request using Crawlbase Smart Proxy
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers, proxies=proxies, verify=False)
soup = BeautifulSoup(response.text, "html.parser")

# 🧠 Extract cryptocurrency data (Top 10 coins)
crypto_data = []

# Select table rows containing the crypto data
rows = soup.select('table.cmc-table tbody tr')[:10]  # Get data for top 10 coins

# Loop through each row and extract the necessary data
for row in rows:
    try:
        name = row.select_one("p.coin-item-name").text.strip()
        symbol = row.select_one('p.coin-item-symbol').text.strip()
        price = row.select_one("div.sc-142c02c-0.lmjbLF").text.strip()

        crypto_data.append({
            "name": name,
            "symbol": symbol,
            "price_usd": price
        })
    except Exception as e:
        print("Skipping a row due to error:", e)

# ✅ Export data to CSV file
with open("crypto_prices.csv", "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["name", "symbol", "price_usd"])
    writer.writeheader()
    writer.writerows(crypto_data)

# ✅ Export data to JSON file
with open("crypto_prices.json", "w") as json_file:
    json.dump(crypto_data, json_file, indent=2)

print("✅ Crypto prices have been saved to 'crypto_prices.csv' and 'crypto_prices.json'")