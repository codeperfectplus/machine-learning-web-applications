from django.urls import path
from server.views import IndexView, PredictView

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("predict", PredictView.as_view(), name="predict")
]
