from django.shortcuts import render
import json,requests
from .models import Disease



# Create your views here.
def weather(request):

    if request.method == 'POST':
        api_key = "b624cf02602081e5d9a1582c00279b38"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        city_name = str(request.POST.get('email'))

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        response = requests.get(complete_url)

        x = response.json()

        if x["cod"] != "404":

            # store the value of "main"
            # key in variable y
            y = x["main"]

            # store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]

            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]

            # store the value corresponding
            # to the "humidity" key of y
            current_humidiy = y["humidity"]

            # store the value of "weather"
            # key in variable z
            z = x["weather"]

            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]

            # print following values
            data = {"dt":" Temperature (in kelvin unit) = " +
                  str(current_temperature) +
                  "\n atmospheric pressure (in hPa unit) = " +
                  str(current_pressure) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy)  +
                  "\n description = " +
                  str(weather_description)}

        else:
            print(" City Not Found ")

        return render(request,template_name='features/weather.html',context=data)
    else:
        return render(request,template_name='features/weather.html')


def all_diseases(request):

    rslt = Disease.objects.all()
    dis_dict = {'data':rslt}
    return render(request,template_name='features/all_diseases.html',context=dis_dict)
