from django.urls import path
from reddit.views import indexView, resultView

urlpatterns = [
    path("", indexView, name="reddit_home"),
    path("result", resultView, name="reddit_result"),
]