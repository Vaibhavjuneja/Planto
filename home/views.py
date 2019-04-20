from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,template_name="home.html")

def Planto(request):
    return render(request,template_name="Planto.html")
