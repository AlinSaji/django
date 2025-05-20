from django.shortcuts import render, redirect

from myapp.forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')


from django.contrib.auth.hashers import make_password  # To hash the password

def register_view(request):
    if request.method == "POST":
        # Capture the form data from POST request
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validation:
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            # Create the user with the given data
            user = User(username=username, email=email)
            user.password = make_password(password1)  # Make sure to hash the password
            user.save()

            # Success message and redirect to login or dashboard
            messages.success(request, "User created successfully!")
            return redirect('login')  # Redirect to the login page or another page after success

    # If it's a GET request, just render the form
    return render(request, "register.html")




def login_view(request):
    if request.method == "POST":
        
        
    
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            # Log in the user
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard after successful login
        else:
            messages.error(request, "Invalid username or password.")
       
    else:
        print("oomfi")

    return render(request, 'login.html')

def home_view(request):
    return render(request,'index.html')

