from django.urls import path, include
from .views import DriversListView, DriversCreateView


app_name="drivers"

urlpatterns = [
    path('', DriversListView.as_view(), name="home_drivers"),
    path('create/', DriversCreateView.as_view(), name="create_drivers")
]