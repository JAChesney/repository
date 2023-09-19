from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile # '.' tells to go to the current directory and get the library
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'knowledgekeep/home.html', {})

def userlogin(request):
    return render(request, 'knowledgekeep/login.html', {})

def userlogout(request):
    logout(request)
    return redirect('/')

def signup(request):
    print(request.method)
    # Once using POST add the name to the header and check.
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # print(username, email, password)

        # Check whether user already exist

        # Adding user to database
        user = UserProfile(full_name=username, email=email)
        user.set_password(password)
        user.save()

        user = UserProfile.objects.get(email=email)

        # Authenticate user
        user = authenticate(email=email, password=password)

        print(user)

        # Log user in
        if not user:
            print('Error logging in!')

        
        login(request, user)

        # Redirecting to home
        return redirect('/')

    return render(request, 'knowledgekeep/signup.html', {})
