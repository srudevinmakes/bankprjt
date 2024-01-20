from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login as auth_login  # Rename the login function

def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth_login(request, user)  # Rename the login function to auth_login
                    return redirect('application')
                else:
                    messages.error(request, 'Account is not active. Please contact support.')
            else:
                user_exists = User.objects.filter(username=username).exists()
                if user_exists:
                    messages.error(request, 'Incorrect password')
                else:
                    messages.error(request, 'Incorrect Username')

        except SomeSpecificException as e:
            messages.error(request, f'Error: {e}')

    return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            confirmpassword = request.POST['password1']

            if password == confirmpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username Taken")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email Taken")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                    last_name=last_name, email=email)

                    user.save()
                    return redirect('login')

            else:
                messages.info(request, "Password not matching")
                return redirect('register')
        except MultiValueDictKeyError:
            messages.error(request, "Missing required field(s)")
            return redirect('register')

    return render(request, 'register.html')


def logout(request):
    # Your logout logic (optional)
    return redirect('index')

def form(request):
    if request.method == 'POST':
        messages.success(request, 'Your application has been registered successfully!')
        return redirect('application_submitted')

    district = ['ernakulam', 'kozhikode']
    branch = {
        'ernakulam': ['Aluva', 'Edapally', 'Angamaly', 'Other Branches'],
        'kozhikode': ['Kondotty', 'Ramanattukara', 'Mukkam', 'Thamarassery', 'Other Branches'],
        # Add other districts and branches as needed
    }

    return render(request, 'form.html', {'districts': district, 'branches': branch})

def index(request):
    # Your view logic here
    return render(request, 'base.html')

def about(request):
    # Your view logic here
    return render(request, 'about.html')

def application(request):
    if request.method =='POST':
        return redirect('form')
    return render(request,'application.html')

def application_submitted(request):
    if request.method == 'POST':
        return redirect('home')  # Use the correct name
    return render(request, 'application_submitted.html')

def home(request):
    # Your view logic here
    return render(request, 'home.html')
