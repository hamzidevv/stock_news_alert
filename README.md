# Stock Monitor & News Alert

This Python script tracks stock price fluctuations and sends you breaking news via email if the stock changes by more than 5% between the last two market days.

> **Note:** Currently set to monitor **Tesla Inc. (TSLA)**, but you can track **any company** by updating the `STOCK_NAME` and `COMPANY_NAME` constants in the script.

---

## Features

- Fetches the last two days' closing stock prices using the [Alpha Vantage API](https://www.alphavantage.co/).
- Calculates percentage change in stock value.
- If the change exceeds ±5%, it fetches the latest 3 news articles about the company from the [NewsAPI](https://newsapi.org/).
- Sends formatted news alerts directly to your email using SMTP.

---

## Requirements

- Python 3.x
- External APIs:
  - [Alpha Vantage API](https://www.alphavantage.co/)
  - [News API](https://newsapi.org/)
- Gmail account with SMTP access enabled

---

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/stock-monitor-alert.git
    cd stock-monitor-alert
    ```

2. **Install dependencies** (requests module):

    ```bash
    pip install requests
    ```

3. **Create a `config.py` file** in the root directory and add your credentials:

    ```python
    STOCK_API_KEY = "your_alpha_vantage_api_key"
    NEWS_API_KEY = "your_newsapi_api_key"
    EMAIL = "your_email@gmail.com"
    PASSWORD = "your_email_password_or_app_password"
    ```

---

## How It Works

1. Gets the daily stock data for the selected company.
2. Compares the last two closing prices.
3. If the absolute percentage change is greater than 5%:
   - Retrieves 3 latest news articles related to the company.
   - Sends each article to your email.

---

## Customize for Any Company

To monitor a different company, simply edit the following constants at the top of the script:

```python
STOCK_NAME = "AAPL"  # Change to the desired stock symbol
COMPANY_NAME = "Apple Inc"  # Corresponding company name for news
```

---

## Email Output Example

```
Subject: Stock News Alert 🚨

AAPL: 🔻6%
Headline: Apple shares drop after earnings miss.
Brief: Apple reported weaker-than-expected quarterly results...
```

---

## Important Notes

- Make sure **less secure app access** or **App Passwords** are enabled for your Gmail account.
- Do not share or commit your credentials.
- This script is a basic prototype and does not run on a schedule. To automate it, consider using cron (Linux/Mac) or Task Scheduler (Windows).

---

## 📄 License

This project is for educational purposes and not intended for production use or financial advice.
