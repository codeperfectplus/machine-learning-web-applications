from django.shortcuts import render
import requests
from api.key import api_key
# Create your views here.
def indexView(request):
    if request.method == "POST":
        city_name = request.POST["city"].lower()                
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
        weather_data = requests.get(url).json()
        try:
            context = {                
                # City Information
                "city_name":weather_data["city"]["name"],
                "city_country":weather_data["city"]["country"],
                "city_population":weather_data["city"]["population"],
                # Temprature Information
                "temp": round(weather_data["list"][0]["main"]["temp"] -273.0),
                "temp_min":round(weather_data["list"][0]["main"]["temp_min"] -273.0),
                "temp_max": round(weather_data["list"][0]["main"]["temp_max"] -273.0),
                # Pressure, Humidity
                "pressure":weather_data["list"][0]["main"]["pressure"],
                "humidity":weather_data["list"][0]["main"]["humidity"],
                "sea_level":weather_data["list"][0]["main"]["sea_level"],                
                # Other Information
                "weather":weather_data["list"][1]["weather"][0]["main"],
                "description":weather_data["list"][1]["weather"][0]["description"],
                "icon":weather_data["list"][1]["weather"][0]["icon"],                
            }
        except:
            context = {            
            ####
            "city_name":"Search For Other City",
            "city_country":"Try Again With Other City",
            "city_population":"Try Again With Other City",
            ####
            "temp": "Try Again With Other City",
            "temp_min":"Try Again With Other City",
            "temp_max":"Try Again With Other City",
            ###
            "pressure":"Try Again With Other City",
            "humidity":"Try Again With Other City",
            "sea_level":"Try Again With Other City",
            
            ####
            "weather":"Try Again With Other City",
            "description":"Try Again With Other City",
            "icon":"Try Again With Other City",
            
        }

        return render(request, "gitapi/result.html", context)
    return render(request, "gitapi/index.html")
