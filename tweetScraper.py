import tweepy
import time
from tweetPoster import *
from datetime import datetime


# Authenticate account @---------- to Twitter // Set variables
auth = tweepy.OAuthHandler("--------------------------------------------------")
auth.set_access_token("--------------------------------------------------", "--------------------------------------------------")
# wait_on_rate_limit_notify=True, This will print a notification when download limit is reached
api = tweepy.API(auth, wait_on_rate_limit_notify=True)
userID = '----------'
update = True
empty = False
APIcount = 0
tweetCount = 0
#logfreq in minutes
logFrequency = 15
#logUpdater will help the log function
logUpdater = logFrequency
start_time = time.time()
print("Bot now running")


while empty == False:
    try:
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
        #Check at the end of loop if logFrequency minutes has passed
        if (time.time() - start_time) > (logFrequency * 60):
            print((datetime.now()).strftime("%d/%m/%Y %H:%M:%S"), "Bot has made:",APIcount,"API calls and made",tweetCount,"tweets in the last",logFrequency,"minutes")
            logFrequency += logUpdater

    ##################################################
    except Exception as ex:
        print((datetime.now()).strftime("%d/%m/%Y %H:%M:%S"), "- Error Occured rebooting in 30 seconds:",ex)
        time.sleep(30)
