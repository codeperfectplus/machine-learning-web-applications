from django.urls import path
from autompg.views import indexView, predictView

urlpatterns = [
    path("", indexView, name="autompg_home"),
    path("mpg_predict", predictView, name="mpg_predict"),
]
