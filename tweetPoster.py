import tweepy
import time
from datetime import datetime


# Authenticate account @EarsAndAPEyes to Twitter // Set variables
auth = tweepy.OAuthHandler("Y2eYWaFkRcHahkMMcX5IqaF1f", "jqFIdI7pOYYFQAgbbSuKlBMnjIERIDjz3r6EoVqbk7D5hQCwyb")
auth.set_access_token("1329343847902666752-FSvOVAVxwapGkgo0Y3vi3M6cgwBGKn",
                      "Ni8XoDhxFwKvYOtgI9X8Dv7buA9WDlQIKUyNOpUxAoDBR")
# wait_on_rate_limit_notify=True, This will print a notification when download limit is reached
api = tweepy.API(auth, wait_on_rate_limit_notify=True)

def tweetPost(tweetText):
    print("Tweeted -", tweetText,"-", (datetime.now()).strftime("%d/%m/%Y %H:%M:%S"))
    api.update_status((tweetText))
    print("Sleeping 6s")
    time.sleep(6)

#tweetPost("TestTweet2")


"""
tweets = api.user_timeline(screen_name=userID,
# 200 is the maximum allowed count
count=1,
# Necessary to keep full_text
# otherwise only the first 140 words are extracted
tweet_mode = 'extended'
)
for info in tweets:
    test = str(info.full_text)
    api.update_status(str(info.full_text))
    print(info.full_text)
    print("done")
"""