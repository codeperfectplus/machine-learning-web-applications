from django.urls import path
from sortingalgo.views import indexView, resultView

urlpatterns = [
    path("", indexView, name="sort_home"),
    path("result", resultView, name="sort_result")
]
