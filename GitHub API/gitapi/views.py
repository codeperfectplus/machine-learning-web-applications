from django.shortcuts import render
import requests

# Create your views here.
def indexView(request):
    if request.method == "POST":
        username = request.POST["username"]
        url = f"https://api.github.com/users/{username}"
        user_data = requests.get(url).json()
        context = {
            "login":user_data["login"],
            "avatar_url":user_data["avatar_url"],
            "html_url":user_data["html_url"],
            "name":user_data["name"],
            "company":user_data["company"],
            "location":user_data["location"],
            "bio":user_data["bio"],
            "email":user_data["email"],
            "public_repos":user_data["public_repos"],
            "blog":user_data["blog"],
            "followers":user_data["followers"],
            "following":user_data["following"],
            "created_at":user_data["created_at"],
            "updated_at":user_data["updated_at"],
            "followers_url":user_data["followers_url"],
        }
        return render(request, "gitapi/result.html", context)
    return render(request, "gitapi/index.html")
