from django.urls import path
from punctuation.views import indexView


urlpatterns = [
    path("", indexView, name="punc_home"),    
]
