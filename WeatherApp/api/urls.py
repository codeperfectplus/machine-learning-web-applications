from django.urls import path

from api.views import indexView, resultView

urlpatterns = [
    path("", indexView, name="home"),
    path("result", resultView, name="result"),
]
