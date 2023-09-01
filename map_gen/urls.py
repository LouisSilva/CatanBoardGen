from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_generator, name="map_generator"),
    path('map_generator', views.map_generator, name='map_generator'),
]
