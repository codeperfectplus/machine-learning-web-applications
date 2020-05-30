from django.shortcuts import render

def indexView(request):
    return render(request, "mnist/index.html")

def predictView(request):
    return render(request, "mnist/predict.html")