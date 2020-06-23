from django.shortcuts import render
import praw
from reddit.secret import id, secret, user, pswd, agent

def indexView(request):
    if request.method == "POST":
        
        redditSearchWord = request.POST["redditSearchWord"]

        r1,r2,r3,r4,r5 = GetNews(redditSearchWord)            
        context = {"r1":r1, "r2":r2, "r3":r3, "r4":r4, "r5":r5}
        #print(context)

        return render(request, "reddit/result.html", context)
    return render(request, "reddit/index.html")    

def GetNews(searchWord):
    reddit = praw.Reddit(
                client_id=id, client_secret=secret, username=user, password=pswd, user_agent=agent,)

    subreddit = reddit.subreddit(searchWord)

    hot_python = subreddit.hot(limit=10)
        
    titleList = []        
    for submission in hot_python:   

        title = submission.title                
        titleList.append(title)                

    return  titleList[0], titleList[1], titleList[2], titleList[3], titleList[4],

