# Cyber News Discord Bot


## Installation

This application is designed to run in a Python runtime environment. Ensure you have Python3 installed before continuing.


First, create a Python virtual environment:
```
python3 -m venv cybernews-env
```
Then, activate the virtual environment:
```
source cybernews-env/bin/activate
```
Next, upgrade `pip` and install dependencies:
```
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```
Finally, create a dotenv file for secrets:
```
cat > .cybernews.env << EOF
NEWS_API_KEY=""
DISCORD_TOKEN=""
DISCORD_GUILD=""
DISCORD_CHANNEL=""
EOF
```
That's it! You can now run the application.

## Running
Before attempting to run the app, ensure you have completed the initialization step.

Ensure you are in the virtual environment:
```
source cybernews-env/bin/activate
```
Then, run the app:
```
python3 src/cybernewsapp.py
```

## Access Tokens

- To use the news api, you will need to [register an account on newsapi.org](https://newsapi.org/register).

- To create a discord bot and receive a discord token, you will need to [create a new Discord application](https://discord.com/developers/applications).