######################### Imports ##########################
import requests
from api_key import alpha_api, news_api, TW_SID, TW_AUTH
from twilio.rest import Client

##################### Global Variables #####################
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

######################### Stock Data ##########################

# stock_params = {
#     "apikey": alpha_api,
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK_NAME
# }

# stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
# stock_response.raise_for_status()
# stock_data = stock_response.json()
# # print(stock_data)

######################### News Data ##########################

news_params = {
    "apiKey": news_api,
    "q": STOCK_NAME
}

news_response = requests.get(NEWS_ENDPOINT,news_params)
news_response.raise_for_status()
news_data = news_response.json()
print(news_data)



######################### SMS Logic ##########################
account_sid = TW_SID
auth_token = TW_AUTH
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18333241411',
  body= f"Hello World",
  to='+18178980345'
)

print(message.sid)

