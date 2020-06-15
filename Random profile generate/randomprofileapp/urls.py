from django.urls import path
from randomprofileapp.views import indexView

urlpatterns = [
    path("", indexView, name="profile_home"),    
]
