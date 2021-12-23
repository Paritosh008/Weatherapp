from django.shortcuts import render
import requests

def home(request):

    city = request.GET.get('city', "Lucknow")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=cbfd4ea659e4b5d9abea6452208a2c8e'
    data = requests.get(url).json()
    
    payload = {
        'city' : data['name'],
        'weather' : data['weather'][0]['main'],
        'icon' : data['weather'][0]['icon'],
        'kelvin_temperature' : data['main']['temp'],
        'celcius_temperature' :int(data['main']['temp'] - 273),
        'pressure' : data['main']['pressure'],
        'humidity' : data['main']['humidity'],
        'description' : data['weather'][0]['description']
    }

    context = {'data' : payload}
    print(context)
    return render(request,'home.html' , context)