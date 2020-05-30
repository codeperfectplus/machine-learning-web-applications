import praw
from reddit.secret import id, secret, user, pswd, agent

def GetNews(searchWord):
    reddit = praw.Reddit(
                client_id=id, client_secret=secret, username=user, password=pswd, user_agent=agent,)

    subreddit = reddit.subreddit(searchWord)

    hot_python = subreddit.hot(limit=10)
    
    for submission in hot_python:
        if not submission.stickied:
            news = submission.title            
            return news

print(GetNews("python"))