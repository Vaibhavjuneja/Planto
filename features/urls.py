from django.urls import path
from .views import weather,all_diseases


urlpatterns = [
    path('weather/',weather,name="weather"),
    path('alldiseases/',all_diseases,name="all"),
]