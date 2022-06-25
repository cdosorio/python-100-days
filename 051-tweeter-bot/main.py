from speed_bot import SpeedTestBot
from twitter_bot import TweeterBot

PROMISED_DOWN = 999
PROMISED_UP = 20
PROVIDER = "Telkom"
CHROME_DRIVER_PATH = "C:\Dev\chromedriver"

speed_bot = SpeedTestBot(CHROME_DRIVER_PATH)
speed_bot.get_internet_speed()

if speed_bot.down < PROMISED_DOWN or speed_bot.up < PROMISED_UP:
    complaint = (f"Hey {PROVIDER} why is my internet speed {speed_bot.down} down/{speed_bot.up} up"
                f"when I should have {PROMISED_DOWN} down/{PROMISED_UP} up? #speedtest\n\n")
     
    print(complaint)
    # twitter_bot = TweeterBot()
    # twitter_bot.tweet_at_provider(complaint)
else:
    print(f"Good speeds today! {speed_bot.down} down/{speed_bot.up} up")