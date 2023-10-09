######################### Imports ##########################
import requests
from api_key import alpha_api, news_api, TW_SID, TW_AUTH
from twilio.rest import Client
from em

##################### Global Variables #####################
STOCK_NAME = "LMT"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

######################### Stock Data ##########################

stock_params = {
    "apikey": alpha_api,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()
# print(stock_data)

#Todat Close
time_series = stock_data["Time Series (Daily)"]
latest_date = max(time_series.keys())
close_price = float(time_series[latest_date]['4. close'])
# print(close_price)

#Yesterday Close
dates = list(time_series.keys())
dates.sort(reverse=True)
yesterday = dates[1]
yesterday_close = float(time_series[yesterday]['4. close'])
# print(yesterday_close)

#Compare Values
change_value = round(abs((close_price)-(yesterday_close)),2)
change_pecent = round((change_value / yesterday_close),4) * 100
# print(change_pecent)

if close_price > yesterday_close:
    change_direction = "+"
elif close_price < yesterday_close:
    change_direction = "-"
else:
    change_direction = ""

######################### News Data ##########################

news_params = {
    "apiKey": news_api,
    "q": STOCK_NAME
}

news_response = requests.get(NEWS_ENDPOINT,news_params)
news_response.raise_for_status()
news_data = news_response.json()
# print(news_data)
articles = news_data["articles"][:2]
# print (articles)


result_string = ""

for i, article in enumerate(articles, start=1):
    result_string += f"Headline : {article['title']}\n"
    result_string += f"Brief : {article['description']}\n"
    result_string += f"Content : {article['content']}\n"
    result_string += f"URL : {article['url']}\n\n"

# print(result_string)

######################### SMS Logic ##########################
account_sid = TW_SID
auth_token = TW_AUTH
client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='+18333241411',
#   body= f"Hello World",
#   to='+18178980345'
# )

# print(message.sid)

######################### Conditional SMS ##########################

# if change_pecent >= 5.0:
#     message = client.messages.create(
#     from_='+18333241411',
#     body= f"{STOCK_NAME}:{change_direction}{change_pecent}\n\n{result_string}",
#     to='+18178980345'
# )

# print(message.sid)

# #Test code:
body= f"{STOCK_NAME}:{change_direction}{change_pecent}\n\n{result_string}"
print(body)
