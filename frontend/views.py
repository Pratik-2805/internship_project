from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def register_view(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def profile_view(request):
    return render(request, 'profile.html')

def tasks_view(request):
    return render(request, 'tasks.html')
