import os
from dotenv import load_dotenv
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

load_dotenv()  # take environment variables from .env.

PROMISED_DOWN = os.getenv("PROMISED_DOWN")
PROMISED_UP = os.getenv("PROMISED_UP")


bot = InternetSpeedTwitterBot(PROMISED_UP, PROMISED_DOWN)
down_speed, up_speed = bot.get_internet_speed()
bot.tweet_at_provider(down_speed, up_speed)

bot.close_window()
