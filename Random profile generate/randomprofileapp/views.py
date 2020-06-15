from django.shortcuts import render
import numpy as np
from randomprofileapp.profilegenrator import Name

# Create your views here.
def indexView(request):
    if request.method== "POST":                
        name = Name()
        first, last, address, phone, email = name.full_profile()
        context = {"first":first, "last":last, "address":address, "phone":phone, "email":email}
        return render(request, "randomprofileapp/result.html", context)
    return render(request, "randomprofileapp/index.html")