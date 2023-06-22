from .news_api import NewsApi
from models.cve_data import Description, CVSSMetric, Weakness, Reference, CWE, Vulnerability
from models.news_data import Source, Article, NewsData
import json

class StandaloneUtil:
    """
    Discord API helper
    """
    def __init__(self, news_api: NewsApi):
        self.news_api = news_api
        self.menu = """
1) Latest CVEs
2) Hackernews stories
3) Techcrunch stories
4) quit

Enter a command: """

    def run(self):
        """
        Presents user with a REPL where they can continually enter commands
        to be processed by the app
        """
        while True:
            command = input(self.menu)
            
            if command == "1":
                data = self.news_api.get_cves()
                vulns = []
                for vuln in data:
                    vulns.append(Vulnerability(vuln.__dict__))
                for vuln in vulns:
                    print(vuln)
                    print()
            elif command == "2":
                data = self.news_api.get_hackernews()
                news = NewsData(data)
                for article in news.articles:
                    print(article)
            elif command == "3":
                data = self.news_api.get_techcrunch()
                news = NewsData(data)
                for article in news.articles:
                    print(article)
            elif command in ["4","quit"]:
                break
            else:
                print("Invalid command")
        print("Goodbye!")