import discord
from .news_api import NewsApi

class DiscordUtil:
    """
    Discord API helper
    """
    def __init__(self, config: dict, news_api: NewsApi):
        self.token = config.get("DISCORD_TOKEN")
        self.guild = config.get("DISCORD_GUILD")
        self.channel = config.get("DISCORD_CHANNEL")
        self.news_api = news_api

    def run(self):
        pass