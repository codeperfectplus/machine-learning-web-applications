from django.urls import path
from sortingalgo.views import indexView

urlpatterns = [
    path("", indexView, name="sort_home"),
]
