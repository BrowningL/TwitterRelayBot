import tweepy
import time
from tweetPoster import *
from datetime import datetime


# Authenticate account @SentryFeed to Twitter // Set variables
auth = tweepy.OAuthHandler("TaKRCVSWQwbuoro6urJ5yPszb", "EPneGfRaOLiKdRzhlNJ6t6NJ311q2DrINonkZ6HnTrm1e5fnxq")
auth.set_access_token("1329106117356609537-FoI7VGBMW4biy4pPGGyTf5y3LtDsdM", "D3V9tbPZSUuPb1p2QZvYcMmWdJmtCOp5lruyJA21BXLhY")
# wait_on_rate_limit_notify=True, This will print a notification when download limit is reached
api = tweepy.API(auth, wait_on_rate_limit_notify=True)
userID = 'OfficialDealer1'
update = True
empty = False
APIcount = 0
tweetCount = 0
#logfreq in minutes
logFrequency = 0.5
start_time = time.time()


while empty == False:

##################################################
#Get new 2 tweets
    tweets = api.user_timeline(screen_name = userID,
        count = 2,
        tweet_mode = "extended"
        )
    APIcount += 1
##################################################

    #account validation
    if len(tweets) == 0:
        print("Please make sure account has at least one tweet in it already")
        empty = True

##################################################
    # Setting the old tweet so that we can check for new tweets
    if update == True:
        oldTweet1 = tweets[0].full_text
        #print("Old tweet1 is now: ", oldTweet1)
        oldTweet2 = tweets[1].full_text
        #print("Old tweet2 is now: ", oldTweet2)
        update = False
        continue

##################################################
    #Set the new tweets
    newTweet1 = tweets[0].full_text
    newTweet2 = tweets[1].full_text

##################################################
    if oldTweet1 != newTweet2 and oldTweet2 != newTweet2:
        #print("both new")
        # tweet both newTweet1 and newTweet2
        tweetTwice(newTweet1,newTweet2)
        update = True
        tweetCount += 2
    elif oldTweet1 == newTweet2:
        #print("one new")
        #Tweet just newTweet1
        tweetOnce(newTweet1)
        update = True
        tweetCount += 1
    else:
        #print("No new tweet, sleeping 6 seconds -",(datetime.now()).strftime("%d/%m/%Y %H:%M:%S"))
        time.sleep(6)
##################################################
    #Check at the end of loop if 10 minutes has passed
    if (time.time() - start_time) > (logFrequency * 60):
        print((datetime.now()).strftime("%d/%m/%Y %H:%M:%S"), "Bot has made:",APIcount,"API calls and made",tweetCount,"tweets in the last",logFrequency,"minutes")
        logFrequency += logFrequency

##################################################
