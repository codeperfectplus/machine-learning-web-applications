from django.urls import path, include
from rest_framework import routers

from server import views

from server.views import IrisViewSet

""" router = routers.DefaultRouter()

router.register(r'Iris', IrisViewSet) """

urlpatterns = [
    
    path('api/', views.IrisViewSet.as_view(), name='get_salary'),
]
