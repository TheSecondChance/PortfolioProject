from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Product, Category


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


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
    
def userLogout(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('home')

def design(request):
    if request.user.is_authenticated:
        
        category = request.GET.get('category')
        if category == None:
            product = Product.objects.all()
        else:
            product = Product.objects.filter(category__name=category)

        categories = Category.objects.all()
        context = {
            'products':product,
            'categories': categories
        }
        return render(request, 'category.html', context)

    else:
        pro = Product.objects.all().order_by()[:3]
        return render(request, 'design.html', {'pro': pro})
    
def contact(request):
    return render(request, 'contact.html')