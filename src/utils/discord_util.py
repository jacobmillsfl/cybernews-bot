from apscheduler.schedulers.asyncio import AsyncIOScheduler
import discord
from discord.ext import commands
from datetime import date, datetime
from typing import List

from .news_api import NewsApi
from models.cve_data import Description, CVSSMetric, Weakness, Reference, CWE, Vulnerability
from models.news_data import Source, Article, NewsData

class DiscordUtil:
    """
    Discord API helper
    """
    def __init__(self, config: dict):
        self.token = config.get("DISCORD_TOKEN")
        self.guild = config.get("DISCORD_GUILD")
        self.DISCORD_CHANNEL_CVES = int(config.get("DISCORD_CHANNEL_CVES"))
        self.DISCORD_CHANNEL_TECHCRUNCH = int(config.get("DISCORD_CHANNEL_TECHCRUNCH"))
        self.DISCORD_CHANNEL_HACKERNEWS = int(config.get("DISCORD_CHANNEL_HACKERNEWS"))
        self.debug = config.get("debug")

        self.bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())
        self.scheduler = AsyncIOScheduler()
        self.news_api = NewsApi(config)

    async def post_hackernews(self):
        """

        """
        data = self.news_api.get_hackernews()
        news = NewsData(data)
        todays_news = []
        for article in news.articles:
            # Convert UTC datetime to a naive datetime object
            utc_datetime = datetime.strptime(article.published_at, '%Y-%m-%dT%H:%M:%SZ')

            # Get the current date in UTC
            current_date = date.today()

            # Extract the date component from the UTC datetime
            datetime_date = utc_datetime.date()

            # Only include articles from today
            if current_date == datetime_date:
                todays_news.append(article)
        
        # for news in todays_news:
        #     pass

    async def post_cves(self):
        """
        Collect latest CVEs and post to Discord as an embed
        """

        # Get CVE data
        #count = 3
        data = self.news_api.get_cves()
        vulns : List[Vulnerability] = []
        for vuln in data:
            vulns.append(Vulnerability(vuln.__dict__))

        # Create embeds        
        for vuln in vulns:
            color = discord.Color.red()
            descriptions = list(filter(lambda x: x.lang == "en", vuln.descriptions))
            description_en = "\n".join([desc.value for desc in descriptions])

            embed = discord.Embed(
                title       = vuln.id,
                description = description_en,
                color       = color,
                url         = vuln.url
            )
            embed.set_author(
                name = vuln.source_identifier,
                #icon_url=
            )
            embed.set_footer(
                text = vuln.published
            )

            embed.add_field(
                name   = "Vector",
                value  = vuln.v31_vector,
                inline = False
            )
            embed.add_field(
                name   = "Score",
                value  = vuln.v31_score,
                inline = True
            )
            embed.add_field(
                name   = "Severity",
                value  = vuln.v31_severity,
                inline = True
            )
            embed.add_field(
                name   = "Status",
                value  = vuln.vuln_status,
                inline = True
            )
            channel = self.bot.get_channel(self.DISCORD_CHANNEL_CVES)
            await channel.send(embed=embed)

    async def post_message(self):
        await self.post_cves()

    async def schedule_daily_post(self):
        if self.debug:
            await self.post_message()
        else:
            self.scheduler.add_job(self.post_message, 'cron', hour=12)
            self.scheduler.start()

    def run(self):
        @self.bot.event
        async def on_ready():
            print('Bot is ready')
            await self.schedule_daily_post()

        self.bot.run(self.token)
