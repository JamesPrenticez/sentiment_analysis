import praw
import config

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

for submission in reddit.subreddit("wallstreetbets").hot(limit=25):
    print(submission.title)
    