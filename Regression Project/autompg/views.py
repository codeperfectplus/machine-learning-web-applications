from django.shortcuts import render
import numpy as np
import joblib

with open("autompg/model/autompg.pkl", "rb") as file:
    model = joblib.load(file)

def indexView(request):
    if request.method == "POST":
        cylinders = request.POST["cylinders"]
        displacement = request.POST["displacement"]
        horsepower = request.POST["horsepower"]
        weight = request.POST["weight"]
        acceleration = request.POST["acceleration"]
        modelyear = request.POST["modelyear"]
        origin = request.POST["origin"]

        data = [cylinders,displacement,horsepower,weight,acceleration,modelyear,origin]
        print(data)
        data = np.array(data).reshape(-1, 7)
        result = model.predict(data)[0]
        result = round(result, 2)
        print(result)
        context = {"result": result}
        
        return render(request, 'autompg/predict.html',context)
    return render(request, "autompg/index.html")
    