from django.shortcuts import render
from Blog.models import user
from django.contrib import messages, auth

def signup(request):
    return render(request,'SignUp.html')

def signin(request):
    return render(request,'login.html')
# Create your views here.

def creating_user(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password2']
        password = request.POST['password']
        
    print("entered here")
    return render(request,'index.html')