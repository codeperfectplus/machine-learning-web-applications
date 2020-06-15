from django.urls import path
from autompg.views import indexView

urlpatterns = [
    path("", indexView, name="autompg_home"),
]
