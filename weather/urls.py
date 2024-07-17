from django.urls import path

from .views import search_weather, autocomplete

urlpatterns = [
    path('weather/', search_weather, name='weather'),
    path('autocomplete/', autocomplete, name='autocomplete'),
]
