import os
import requests
from twilio.rest import Client
from datetime import datetime, timedelta, timezone

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "81KF5C9RKMBSDL9E"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "7ddb4eb993124701bf32845f6cd9b861"

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

#print(f"{TWILIO_ACCOUNT_SID} : {TWILIO_AUTH_TOKEN}")

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
parameters_news = {
            "function":"TIME_SERIES_DAILY",
            "symbol": STOCK_NAME,
            "apikey": STOCK_API_KEY
        }

response = requests.get(STOCK_ENDPOINT, params=parameters_news)
response.raise_for_status()
data_news = response.json()
#print(data)

#dict to list
# data_dict = data_news["Time Series (Daily)"]
# data_list = [value for (key, value) in data_dict.items()]
# yesterday_data = data_list[0]

today = datetime.today().date()
yesterday_str = (today - timedelta(days=1)).strftime('%Y-%m-%d')
yesterday_closing_price = float(data_news["Time Series (Daily)"][yesterday_str]["4. close"])
print(f"yesterday: $ {yesterday_closing_price}")

#TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_str = (today - timedelta(days=2)).strftime('%Y-%m-%d')
before_yesterday_closing_price = float(data_news["Time Series (Daily)"][before_yesterday_str]["4. close"])
print(f"before yesterday: $ {before_yesterday_closing_price}")

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
dif_price = abs(yesterday_closing_price - before_yesterday_closing_price)
print(f"abs dif= {dif_price}")

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percent = (dif_price / before_yesterday_closing_price ) * 100
diff_percent = round(diff_percent, 2)
print(f"{diff_percent}%" )

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 0.1: 
    print("Get News...")


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    parameters_news = {
                "q": COMPANY_NAME,
                "apikey": NEWS_API_KEY
            }

    response_news = requests.get(NEWS_ENDPOINT, params=parameters_news)
    response_news.raise_for_status()
    data_news = response_news.json()

    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. 
    # Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = data_news["articles"][:3]


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"Headline: {article['title']}.\nBrief {article['description']}" for article in three_articles]
    
    if yesterday_closing_price - before_yesterday_closing_price < 0:
        up_down = "🔻"
    else:
        up_down = "🔺"

    #TODO 9. - Send each article as a separate message via Twilio.
    for article in formatted_articles:
        print("sending SMS...")
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
         
        msg = (f"{STOCK_NAME}: {up_down} {diff_percent}%\n"
               f"{formatted_articles}")

        print(msg)

        message = client.messages \
                        .create(
                            body=msg,
                            from_='+17473024549',
                            to='+56977964322'
                        )

        print(message.status)


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

