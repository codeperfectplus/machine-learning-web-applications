from django.shortcuts import render
import numpy as np
import joblib

with open("server/model/classifier.pkl", 'rb') as file:    # test case in tests.py REVIEW
    model = joblib.load(file)

def IndexView(request):
    if request.method == "POST":
        slength = request.POST["slength"]
        swidth = request.POST["swidth"]
        plength = request.POST["plength"]
        pwidth = request.POST["pwidth"]

        data = [slength, swidth, plength, pwidth]
        data = np.array(data).reshape(-1, 4)
        result = model.predict(data)

        predict_flower = ['Setosa', 'versicolor', 'virginica']
        result = predict_flower[result[0]]

        context = {"result": result}
        return render(request, "predict.html", context)
    return render(request, 'index.html')