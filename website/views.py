from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile, Papers # '.' tells to go to the current directory and get the library
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'knowledgekeep/home.html', {})

def userlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)

        user = UserProfile.objects.get(email=email)
        print(user)

        if not user:
            print('User does not exist')

        # Authenticate user
        user = authenticate(email=email, password=password)

        print(user)

        # Log user in
        if not user:
            print('Error logging in!')

        
        login(request, user)

        # Redirecting to home
        return redirect('/')
    
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

def addpaper(request):

    # uploading file
    if request.method == 'POST':
        paper_title = request.POST['paper-title']
        paper_type = request.POST['paper-type']
        paper_description = request.POST['paper-description']
        published = request.POST['is-published']
        paper_file = request.FILES['file']

        # saving details to paper table
        paper = Papers(user=request.user, paper_name=paper_title, paper_description=paper_description, type=paper_type, is_published=published == 'yes', file=paper_file)
        paper.save()

    return render(request, 'knowledgekeep/addpaper.html', {})

def papers(request):
    papers = Papers.objects.all()
    print(papers)
    return render(request, 'knowledgekeep/papers.html', {'papers': papers})