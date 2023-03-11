from django.urls import path
from .import views

app_name="weather"

urlpatterns = [
  path("", views.home, name='home'),
  path('delete_city/<str:city_name>', views.delete_city, name='delete')
]
