from django.shortcuts import render
import numpy as np

from sortingalgo.mergesort import mergeSort
from sortingalgo.bubblesort import BubbleSort

def indexView(request):
    if request.method== "POST":
        values = request.POST["values"]
        choosedAlgoritm = request.POST.get("sort", "bubble")

        #print(choosedAlgoritm)
        values = map(int, values.strip().split())
        values = list(values)

        #print(values)
        if choosedAlgoritm == "bubble":
            result = mergeSort(values)
            print(result)
            context = {"result" : result, "algo": choosedAlgoritm, "time": "UnderConstruction"}

        else:
            sort = BubbleSort()
            result = sort(values)
            print(result)
            context = {"result" : result, "algo": choosedAlgoritm, "time": "UnderConstruction"}
            
        return render(request, "sortingalgo/result.html", context)
    return render(request, "sortingalgo/index.html")
    