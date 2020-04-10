from django.shortcuts import render
import json,requests
from .models import Disease

def weather(request):
    context={}
    if request.method == 'POST':
        api_key = "b624cf02602081e5d9a1582c00279b38"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = str(request.POST.get('email'))
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        context['x']=x
        return render(request,'features/weather.html',context)
    else:
        return render(request,'features/weather.html')


def all_diseases(request):
    rslt = Disease.objects.all()
    dis_dict = {'data':rslt}
    return render(request,template_name='features/all_diseases.html',context=dis_dict)
