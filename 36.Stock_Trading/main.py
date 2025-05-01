import requests
from dotenv import load_dotenv
import os
import pandas as pd
import io
load_dotenv("../.env")  # Carrega as variáveis do arquivo .env
NEWSAPI = os.getenv("NEWSAPI")
ALPHAVANTAGE = os.getenv("ALPHAVANTAGE")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
def load_data():
    response = requests.get('https://www.alphavantage.co/query',
                 params={
                     'function': 'TIME_SERIES_DAILY',
                     'symbol': STOCK,
                     'apikey': ALPHAVANTAGE,
                     'datatype': 'csv'
                        }
                 )
    response.raise_for_status()
    data = pd.read_csv(io.StringIO(response.text))
    data.index=pd.to_datetime(data['timestamp'])
    return data['close']

def  get_news():
    response = requests.get("https://newsapi.org/v2/everything",
                            params = {
                                'q': "Tesla Inc",
                                'apiKey' : NEWSAPI,
                                'language': 'en'
                            }
                       )
    return response.json()['articles'][:3]



data = load_data()
yesterday = 1
day_before_yesterday = 1.06
STOCK_price_delta = (yesterday-day_before_yesterday)/yesterday
if abs(STOCK_price_delta)>0.05:
    news = get_news()

for i in news:
    if (yesterday-day_before_yesterday)>0:
        msg = (f"{STOCK}: 🔺{round(STOCK_price_delta*100,2)}"
               f"\nHeadline: {i['title']}"
               f"\nBrief: {i["description"]}")
    else:
        msg = (f"{STOCK}: 🔻{round(STOCK_price_delta*100,2)}"
               f"\nHeadline: {i['title']}"
               f"\nBrief: {i["description"]}")
    print(msg)

