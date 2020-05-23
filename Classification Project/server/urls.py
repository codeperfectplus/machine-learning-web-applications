from django.urls import path
from server.views import IndexView, PredictView

urlpatterns = [
    path("", IndexView, name="home"),
    path("predict", PredictView, name="predict")
]
