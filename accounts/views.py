from django.contrib.auth import login, get_user_model, logout
from django.shortcuts import render
from .forms import UserCreationForm, UserLoginForm
from django.http import HttpResponseRedirect, Http404


User=get_user_model()


# def home(request):
#     context={}
#     if request.user.is_authenticated:
#         city=request.user.profile
#         context={'user_profile':city}
#         context['data']='You are logged in'
#     return render(request, 'home.html', context)

def register(request, *args, **kwargs):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/login')
    return render(request, 'accounts/register.html', {'form':form})
        



def user_login(request, *args, **kwargs):
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj=form.cleaned_data.get('user_obj')             
        # user_obj=User.objects.get(username__iexact=query)
        login(request, user_obj)
        return HttpResponseRedirect('/')
    return render(request, 'accounts/login.html', {'form':form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/') 
