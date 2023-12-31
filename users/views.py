from django.shortcuts import render, redirect
# third party imports
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required  

from django.contrib import messages

# import within
from .forms import CreateUserForm 



# Create your views here.


# REGISTER
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm ()

        if request.method == 'POST':
            form = CreateUserForm (request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                success_message = messages.success(request, 'Account successfully created for '+ user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'users/register.html', context)

# LOGIN
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect!')

        return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='login')
def index(request):
    return render(request, 'users/index.html')