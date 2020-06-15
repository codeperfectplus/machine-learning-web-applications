from django.shortcuts import render
import re
from punctuation.removePunctuations import Punctuation

def indexView(request):
    if request.method=="POST":
        string = request.POST["string"]                        
        removePunc = request.POST.get("removePunc",False)
        removeDigit = request.POST.get("removeDigit", False)
        
        try:
            if removeDigit == "on":            
                result = re.sub(r"\d", "", string)                
            else:
                result = string
                               
            if removePunc == "on":
                result = Punctuation(result) 
                context = {"result": result}
            else:        
                context = {"result": result}
        except:
            context = {"result": string}
            
        return render(request, "punctuation/predict.html", context)    
    return render(request, "punctuation/index.html")

#https://stackoverflow.com/questions/5895588/django-multivaluedictkeyerror-error-how-do-i-deal-with-it