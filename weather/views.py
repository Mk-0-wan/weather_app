from django.shortcuts import render, redirect
import requests
from .forms import CityForm
from .models import City


def home(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=648c4f2b635ecac77f7a20c982f61bfe'

    error = ""
    message = ""
    message_class = ''

    forms = CityForm()

    if request.method == 'POST':
        forms = CityForm(request.POST)
        if forms.is_valid():
          new_city = forms.cleaned_data['name']
          check_if_exist = City.objects.filter(name=new_city).count()
          if check_if_exist == 0:
            code = requests.get(url.format(new_city)).json()
            #print(code)
            if code['cod'] == 200:
              forms.save()
            else:
              error = "City doesn't exist in the world!"
              print(error)
          else:
            error = "Can't make a copy"
    if error:
      message = error
      message_class = 'bg-red-600'
    else:
      message = "City added succefully"
      message_class = 'bg-gray-500'
        

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
                'city': city.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
                }
        weather_data.append(city_weather)
        
    context = {
      'weather_data': weather_data,
      'forms': forms,
      'message': message,
      'message_class': message_class
      }

    return render(request, "weather/home.html", context)

def delete_city(request, city_name):
  City.objects.get(name=city_name).delete()
  return redirect("/")
