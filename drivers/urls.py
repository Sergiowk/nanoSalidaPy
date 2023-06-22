from django.urls import path, include
from .views import DriversList


app_name="drivers"

urlpatterns = [
    path('', DriversList.as_view(), name="home_drivers")
]