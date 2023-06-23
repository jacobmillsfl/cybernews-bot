import argparse
from dotenv import dotenv_values
from utils.discord_util import DiscordUtil
from utils.standalone_util import StandaloneUtil
from utils.news_api import NewsApi

if __name__ == "__main__":
    config = dotenv_values(".cybernews.env")

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

    command_parser.add_argument(
        "--debug", action="store_true", help="Run the app in Debug mode"
    )

    args = command_parser.parse_args()

    config["discord"] = args.discord
    config["debug"] = args.debug

    if args.discord:
        print("Running in Discord mode")
        bot = DiscordUtil(config)
    else:
        bot = StandaloneUtil(config)

    # Once implemented within discord_util.py & standalone_util.py, enable bot.run()
    bot.run()

