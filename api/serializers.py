from rest_framework import serializers

from api.models import City, Weather

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['city', 'temperature', 'description']
