import json
import requests
from urllib.parse import unquote
import nvdlib
import datetime

class NewsApi:
    def __init__(self, config):
        self.api_key = config.get("NEWS_API_KEY")
        self.url_hackernews = f"https://newsapi.org/v2/top-headlines?sources=hacker-news&apiKey={self.api_key}"
        self.url_techcrunch = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={self.api_key}"

    def get_news(self, url):
        response = requests.get(url)

        if not response.ok:
            print("HTTP Request failed")

        result = json.loads(response.text)
        if result['status'] != "ok":
            print("API request failed")
            print(f"{result['status']}")

        return result
    
    def get_hackernews(self):
        return self.get_news(self.url_hackernews)
    
    def get_techcrunch(self):
        return self.get_news(self.url_techcrunch)

    def get_cves(self):
        end = datetime.datetime.now()
        start = end - datetime.timedelta(days=1)
        results = nvdlib.searchCVE(pubStartDate=start, pubEndDate=end)
        severe_results = list(filter(lambda x: x.score and x.score[1], results))
        top_three = sorted(severe_results, key=lambda x: x.score[1], reverse=True)[:3]

        return top_three