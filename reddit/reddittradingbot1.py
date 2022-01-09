import praw
import config
from textblob import TextBlob

reddit = praw.Reddit(
    client_id=config.REDDIT_ID,
    client_secret=config.REDDIT_SECRET,
    password=config.REDDIT_PASS,
    user_agent="USERAGENT",
    username=config.REDDIT_USER,
)

# print(reddit) 

# for comment in reddit.subreddit("redditdev").comments(limit=25):
#     print(comment.author)
#     print(comment.body)

# for submission in reddit.subreddit("walsentimentListreetbets").hot(limit=25):
#     print(submission.title)

# walsentimentListreetbets
# bitcoin
# bitcoinmarkets
# nio (is a compeditor for tesla, potentially if the sentiment is poor for neo we could infer that thats a good sign to buy tsla)

sentimentList = []
neededSentiment = []

def Average(sentimentList):
    if len(sentimentList) == 0
        return len(sentimentList)
    else:
        return sum(sentimentList[-neededSentiment:] / neededSentiment)

for comment in reddit.subreddit("bitcoinmarkets").stream.comments():
    print(comment.body)
    
    redditComment = comment.body
    blob = TextBlob(redditComment)
    sent = blob.sentiment

    print("********** Sentiment is: " + str(sent.polarity) + "***********")
    
    if sent.polarity != 0.0:
        sentimentList.append(sent)

        if round(Average(sentimentList) > 0.5 and len(sentimentList > 300)):
            print("BUY")
        elif round(Average(sentimentList) < 0.5) and len(sentimentList) > neededSentiments
            print("SELL")
