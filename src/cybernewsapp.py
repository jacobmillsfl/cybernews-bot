import argparse
from dotenv import dotenv_values
from utils.discord_util import DiscordUtil
from utils.standalone_util import StandaloneUtil
from utils.news_api import NewsApi

if __name__ == "__main__":
    config = dotenv_values(".cybernews.env")
    NEWS_API_KEY = config.get("NEWS_API_KEY")
    DISCORD_AUTH_TOKEN = config.get("DISCORD_AUTH_TOKEN")
    DISCORD_GUILD = config.get("DISCORD_GUILD")
    DISCORD_CHANNEL_ID = config.get("DISCORD_CHANNEL_ID")

    command_parser = argparse.ArgumentParser(
        prog="Cybersecurity News App",
        usage="cybernewsapp.py [--discord]",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""\
    Cybersecurity News App.

    This app interfaces with news APIs to provide the latest information on
    cybersecurity and CVEs.""",
    )

    command_parser.add_argument(
        "--discord", action="store_true", help="Run the app in Discord mode"
    )

    args = command_parser.parse_args()
    news_api = NewsApi(config)

    if args.discord:
        print("Running in Discord mode")
        bot = DiscordUtil(config, news_api)
    else:
        bot = StandaloneUtil(news_api)

    # Once implemented within discord_util.py & standalone_util.py, enable bot.run()
    bot.run()

