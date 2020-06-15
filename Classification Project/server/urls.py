from django.urls import path
from server.views import IndexView

urlpatterns = [
    path("", IndexView, name="home"),
]
