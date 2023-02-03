from django.urls import path
from api.views import WeatherListView, WeatherDetailView

urlpatterns = [
    path('weather/', WeatherListView.as_view()),
    path('weather/<int:id>', WeatherDetailView.as_view()),
]
