import os
import requests
from django.http import JsonResponse
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def get_weather(request):
    city = request.GET.get('city', 'Delhi')
    api_key = os.getenv('OPENWEATHER_API_KEY')  # read key from .env
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city + ',IN',
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code != 200:
        print("API error:", data)
        return JsonResponse({'error': 'City not found or API error'}, status=400)

    rainfall = data.get('rain', {}).get('1h', 0)
    monsoon = 'rain' in data['weather'][0]['description'].lower()

    result = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'weather': data['weather'][0]['description'],
        'wind_speed': data['wind']['speed'],
        'pressure': data['main']['pressure'],
        'rainfall_mm_last_hour': rainfall,
        'monsoon': monsoon
    }

    return JsonResponse(result)
# Django settings for weather_project project.