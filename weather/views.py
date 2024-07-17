from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import City, SearchHistory
import requests
import ssl

import os
from dotenv import load_dotenv
load_dotenv()

@login_required
def search_weather(request):
    if request.method == "POST":
        city = request.POST.get("city")
        api_key = os.getenv("API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url, ssl_version=ssl.PROTOCOL_TLSv1_2)
        weather_data = response.json()
        SearchHistory.objects.create(user=request.user, city=city)
    else:
        weather_data = None

    search_history = SearchHistory.objects.filter(user=request.user)
    return render(request, "weather/weather.html", {"weather_data": weather_data, "search_history": search_history})


def autocomplete(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        cities = City.objects.filter(name__icontains=city).values_list('name', flat=True)[:10]
        return JsonResponse(list(cities), safe=False)
    return JsonResponse([], safe=False)
