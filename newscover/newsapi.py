import json
import requests
from datetime import datetime, timedelta

API_KEY = 'f15624e4ec014be8946eaf297c9bd6ec'
SHOW_ARTICLES_URL_TEMPLATE = "https://newsapi.org/v2/everything?language=en&q={}&from={}&apiKey={}"

def get_lookback_date(lookback_days):

    '''returns a string representing a date <lookback_days> days ago'''

    today = datetime.now()    
    n_days_ago = today - timedelta(days=lookback_days)
    return (n_days_ago.strftime("%Y-%m-%d"))
    
    

def fetch_latest_news(api_key, news_keywords, lookback_days=10):

    '''queries the NewsAPI and returns a python list of english news articles (represented as dictionaries) containing those news keywords and published within the last <lookback_days>'''

    if news_keywords is None:
        raise TypeError("news_keywords cannot be None")

    date_10_days_ago = get_lookback_date(lookback_days)
    query_string = SHOW_ARTICLES_URL_TEMPLATE.format(news_keywords, date_10_days_ago, api_key)
    
    response = requests.get(query_string)

    data = response.json()

    return data["articles"]

def main():
    print(fetch_latest_news(API_KEY, "tesla"))

if __name__ == "__main__":
    main()