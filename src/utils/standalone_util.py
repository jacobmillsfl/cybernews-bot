from .news_api import NewsApi

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

Enter a command: """

    def run(self):
        """
        Presents user with a REPL where they can continually enter commands
        to be processed by the app
        """
        while True:
            command = input(self.menu)
            
            if command == "1":
                print(self.news_api.get_cves())
            elif command == "2":
                print(self.news_api.get_hackernews())
            elif command == "3":
                print(self.news_api.get_techcrunch())
            elif command == "quit":
                break
            else:
                print("Invalid command")
        print("Goodbye!")