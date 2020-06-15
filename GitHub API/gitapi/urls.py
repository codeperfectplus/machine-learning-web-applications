from django.urls import path
from gitapi.views import indexView

urlpatterns = [
    path("", indexView, name="gitapi_home"),    
]
