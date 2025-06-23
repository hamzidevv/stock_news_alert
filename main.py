import requests
import smtplib
import config

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = config.STOCK_API_KEY
NEWS_API_KEY = config.NEWS_API_KEY
MY_EMAIL = config.EMAIL
MY_PASSWORD = config.PASSWORD

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()][0:2]

closing_price_list = [float(data["4. close"]) for data in data_list]
yesterday_closing_price = closing_price_list[0]
day_before_yesterday_closing_price = closing_price_list[1]

difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / yesterday_closing_price) * 100)

if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }

    response = requests.get(NEWS_ENDPOINT, params=news_params)
    three_articles = response.json()["articles"][:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    for article in formatted_articles:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: Stock News Alert 🚨\n"
                        f"Content-Type: text/plain; charset=utf-8\n\n"
                        f"{article}".encode("utf-8")
            )
