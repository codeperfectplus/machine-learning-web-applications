from django.shortcuts import render

def indexView(request):
    return render(request, "punctuation/index.html")

def predictView(request):
    if request.method=="POST":
        string = request.POST["string"]                        
        removePunc = request.POST.get("removePunc",False)

        if removePunc == "on":
            result = Punctuation(string) 
            context = {"result": result}
        else:        
            context = {"result": string}
        return render(request, "punctuation/predict.html", context)    

def Punctuation(string): 
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	for x in string.lower(): 
		if x in punctuations: 
			string = string.replace(x, "") 
	return string


#https://stackoverflow.com/questions/5895588/django-multivaluedictkeyerror-error-how-do-i-deal-with-it