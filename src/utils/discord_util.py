
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import discord
from discord.ext import commands
from .news_api import NewsApi

class DiscordUtil:
    """
    Discord API helper
    """
    def __init__(self, config: dict, news_api: NewsApi, debug=False):
        self.token = config.get("DISCORD_TOKEN")
        self.guild = config.get("DISCORD_GUILD")
        self.channel = config.get("DISCORD_CHANNEL")
        self.news_api = news_api
        self.debug = debug
        self.bot = commands.Bot(command_prefix='!')
        self.scheduler = AsyncIOScheduler()

    async def post_message(self):
        # TODO: change to post a Discord Embed with content deriving from the NewsApi
        channel = self.bot.get_channel(self.channel)
        await channel.send("Hello World.")

    def schedule_daily_post(self):
        if self.debug:
            self.post_message()
        else:
            self.scheduler.add_job(self.post_message, 'cron', hour=12)
            self.scheduler.start()

    def run(self):
        @self.bot.event
        async def on_ready():
            self.schedule_daily_post()
            print('Bot is ready')

        self.bot.run(self.token)
