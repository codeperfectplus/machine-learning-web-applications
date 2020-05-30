from django.urls import path
from mnist.views import indexView, predictView

urlpatterns = [
    path("", indexView, name="mnist_home" ),
    path("predict", predictView, name="mnist_predict" ),
]

