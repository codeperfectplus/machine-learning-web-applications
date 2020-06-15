from django.urls import path
from reddit.views import indexView

urlpatterns = [
    path("", indexView, name="reddit_home"),
]