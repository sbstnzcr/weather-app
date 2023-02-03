import datetime
import requests

from django.db.models import Avg
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import City, Weather
from api.serializers import CitySerializer, WeatherSerializer

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=557a4da9a85c172a0fbcf33a63cb0cdd'


class WeatherListView(CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get(self, request):
        cities = City.objects.all()
        weather_data = []

        for city in cities:
            r = requests.get(url.format(city.name)).json()
            weather = {
            'city':r['name'],
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['main'],
            }
            weather_data.append(weather)
        
        return Response(weather_data)

class WeatherDetailView(APIView):
    now = datetime.datetime.now()
    # queryset = Weather.objects.filter(created_at__lte=now, created_at__gt=now-datetime.timedelta(days=7)).values()
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get(self, request):
        print(request.data)

