<a href="https://crawlbase.com/signup?utm_source=github&utm_medium=readme&utm_campaign=crawling_api_banner" target="_blank">
  <img src="https://github.com/user-attachments/assets/afa4f6e7-25fb-442c-af2f-b4ddcfd62ab2" 
       alt="crawling-api-cta" 
       style="max-width: 100%; border: 0;">
</a>


# coinmarketcap-crypto-data-scraper

## 📝 Description

This repository contains a Python scraper to extract real-time cryptocurrency prices from [CoinMarketCap](https://coinmarketcap.com/). The script uses the [Crawlbase Smart Proxy](https://crawlbase.com/smart-proxy) to avoid IP blocks and bypass bot protections, ensuring reliable access to dynamic content.

It extracts data for the top 10 cryptocurrencies, including their name, symbol, and current price in USD, and saves the results to both CSV and JSON files.

➡ Read the full blog [here](https://crawlbase.com/blog/how-to-scrape-crypto-prices-from-coinmarketcap/) to learn more.

## 📦 Features

- Scrapes top 10 crypto coins from CoinMarketCap
- Extracts:

  - Coin Name
  - Symbol
  - Price in USD

- Stores data in:
  - `crypto_prices.csv`
  - `crypto_prices.json`
- Uses [Crawlbase Smart Proxy](https://crawlbase.com/smart-proxy) to bypass anti-scraping measures

## 💻 Environment Setup

1. **Install Python 3.7 or higher**
   Check version:

```bash
python --version
```

2. **Install Required Libraries**

```bash
pip install requests beautifulsoup4
```

## 🚀 How to Run

1. **Get Your Crawlbase Smart Proxy Token**
   Sign up at [Crawlbase](https://crawlbase.com/signup) and get your Smart Proxy token.
2. **Update the Script**
   Replace `_USER_TOKEN_` in the proxy URL with your actual Crawlbase token.

```python
proxy_url = "http://_USER_TOKEN_:@smartproxy.crawlbase.com:8012"
```

### 3. Run the Scraper

```bash
python coinmarketcap_crypto_data_scraper.py
```

This will output two files in your directory:

- `crypto_prices.csv`
- `crypto_prices.json`

## 🧪 Sample Output

**crypto_prices.json**

```json
[
  {
    "name": "Bitcoin",
    "symbol": "BTC",
    "price_usd": "$27,384.91"
  },
  ...
]
```

**crypto_prices.csv**

```typescript
name, symbol, price_usd;
Bitcoin, BTC, $27, 384.91;
Ethereum, ETH, $1, 823.77;
```

## 🛡 Why Use Crawlbase Smart Proxy?

CoinMarketCap uses bot protection techniques that can block basic scrapers. Crawlbase Smart Proxy:

- Rotates IPs automatically
- Handles CAPTCHAs
- Provides fully rendered HTML for JavaScript-heavy pages

Learn more: [Crawlbase Smart Proxy](https://crawlbase.com/smart-proxy)
