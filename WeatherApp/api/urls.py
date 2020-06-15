from django.urls import path

from api.views import indexView

urlpatterns = [
    path("", indexView, name="home"),    
]
