from django.conf import settings
from django.shortcuts import HttpResponse

from rest_framework import generics
import joblib

from .models import IrisModel
from .serializers import IrisModelSerializer



class Loader:
    def __init__(self, filename, x_test):
        self.filename = filename
        self.X_test = x_test

    def load(self):
        loaded_model = joblib.load(self.filename,'rb')
        result = loaded_model.predict(X_test)
        return result

class IrisViewSet(generics.GenericAPIView):
    def post(self, request):
        if request.method == "POST":
            data = request.data
            
            flowerClass = Loader(settings.BASE_DIR + "/ML_MODEL/classifier.pkl", data).load()

            return HttpResponse(flowerClass)
        else:
            "No Model Found"
    