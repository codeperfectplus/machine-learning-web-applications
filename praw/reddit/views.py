from django.shortcuts import render
import praw
from reddit.secret import id, secret, user, pswd, agent

def indexView(request):
    return render(request, "reddit/index.html")

def resultView(request):
    if request.method == "POST":
        
        redditSearchWord = request.POST["redditSearchWord"]

        result = GetNews(redditSearchWord)            
        context = {"result": result}
        print(context)

        return render(request, "reddit/result.html", context)

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
