from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def design(request):
    return render(request, 'design.html')

def userLogin(request):
    return render(request, 'login.html')

def userRegister(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def userLogin(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have been LogedIn"))
            return redirect('home')
        else:
            messages.success(request, ("Something Error"))
            return redirect('login')
    else:
        context = {'form':form}
        return render(request, 'login.html', context)