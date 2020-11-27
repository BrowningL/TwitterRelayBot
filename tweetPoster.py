import tweepy
import time
from datetime import datetime


# Authenticate account @EarsAndAPEyes to Twitter // Set variables
auth = tweepy.OAuthHandler("Y2eYWaFkRcHahkMMcX5IqaF1f", "jqFIdI7pOYYFQAgbbSuKlBMnjIERIDjz3r6EoVqbk7D5hQCwyb")
auth.set_access_token("1329343847902666752-FSvOVAVxwapGkgo0Y3vi3M6cgwBGKn",
                      "Ni8XoDhxFwKvYOtgI9X8Dv7buA9WDlQIKUyNOpUxAoDBR")
# wait_on_rate_limit_notify=True, This will print a notification when download limit is reached
api = tweepy.API(auth, wait_on_rate_limit_notify=True)

def tweetOnce(tweetText1):
    #print("Tweeted -", tweetText1,"-", (datetime.now()).strftime("%d/%m/%Y %H:%M:%S"))
    print((datetime.now()).strftime("%d/%m/%Y %H:%M:%S")," : Time of Tweet")
    api.update_status((tweetText1))
    #print("Sleeping 6s")
    time.sleep(6)

def tweetTwice(tweetText1, tweetText2):
    api.update_status((tweetText1))
    #print((datetime.now()).strftime("%d/%m/%Y %H:%M:%S"), "Tweeted -", tweetText1,"-", )
    print((datetime.now()).strftime("%d/%m/%Y %H:%M:%S")," : Time of Tweet")
    api.update_status((tweetText2))
    print((datetime.now()).strftime("%d/%m/%Y %H:%M:%S")," : Time of Tweet")
    #print((datetime.now()).strftime("%d/%m/%Y %H:%M:%S"), "Tweeted -", tweetText2,"-", )
    #print("Sleeping 6s")
    time.sleep(6)
