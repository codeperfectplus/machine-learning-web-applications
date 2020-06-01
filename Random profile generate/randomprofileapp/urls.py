from django.urls import path
from randomprofileapp.views import indexView, resultView

urlpatterns = [
    path("", indexView, name="profile_home"),
    path("profile_result", resultView, name="profile_result")
]
