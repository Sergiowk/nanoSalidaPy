from django.urls import path, include
from .views import DriversListView, DriversCreateView, DriversDetailView


app_name="drivers"

urlpatterns = [
    path('', DriversListView.as_view(), name="home_drivers"),
    path('create/', DriversCreateView.as_view(), name="create_drivers"), 
    #<int:pk> is the driver id (primary key)
    path('details-<int:pk>/',DriversDetailView.as_view(), name="drivers_details")
]