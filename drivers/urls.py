from django.urls import path
from .views import DriversList

app_name="drivers"

urlpatterns = [
    path('', DriversList.as_view(), name="home")
]