import tweepy
import time
from tweetPoster import *

# Authenticate account @SentryFeed to Twitter // Set variables
auth = tweepy.OAuthHandler("TaKRCVSWQwbuoro6urJ5yPszb", "EPneGfRaOLiKdRzhlNJ6t6NJ311q2DrINonkZ6HnTrm1e5fnxq")
auth.set_access_token("1329106117356609537-FoI7VGBMW4biy4pPGGyTf5y3LtDsdM", "D3V9tbPZSUuPb1p2QZvYcMmWdJmtCOp5lruyJA21BXLhY")
# wait_on_rate_limit_notify=True, This will print a notification when download limit is reached
api = tweepy.API(auth, wait_on_rate_limit_notify=True)
userID = 'crypDat_io'
update = True
empty = False
APIcount = 0
tweetCount = 0
#logfreq in minutes
logFrequency = 20
start_time = time.time()

while empty == False:
    tweets = api.user_timeline(screen_name = userID,
        count = 1,
        tweet_mode = "extended"
        )
    APIcount += 1

    #account validation
    if len(tweets) == 0:
        print("Please make sure account has at least one tweet in it already")
        empty = True

    for info in tweets:
        #Setting the old tweet so that we can check for new tweets
        if update:
            oldTweet = str(info.full_text)
            print("Old tweet is now: ", oldTweet)
            update = False

        #If new tweet does not equal old tweet, proceed
        elif (str(info.full_text)) != oldTweet:
            #Set update to be True so that the old tweet can be set to new one
            update = True
            #Sending tweet to account B for repost
            tweetPost(str(info.full_text))
            tweetCount += 1

        else:
            #print("No new tweet, sleeping 6 seconds -",(datetime.now()).strftime("%d/%m/%Y %H:%M:%S"))
            time.sleep(6)
    #Check at the end of loop if 10 minutes has passed
    if (time.time() - start_time) > (logFrequency * 60):
        print("Bot has made:",APIcount,"API calls and made",tweetCount,"tweets in the last",logFrequency,"minutes")
        logFrequency += logFrequency

