from django.urls import path

from gitapi.views import indexView, resultView

urlpatterns = [
    path("", indexView, name="gitapi_home"),
    path("gitapi_result", resultView, name="gitapi_result"),
]
