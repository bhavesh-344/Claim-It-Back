from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import RegistrationForm 
from .forms import LoginForm 


def user_login(request):
    if request.method == "POST":
        print("Status : Post")
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  
            print(user)
            if user is not None:
                print("Login")
                login(request, user)
                return redirect('home')  
            else:
                form.add_error(None, "Invalid email or password")
    else:
        print("Not Login")
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)  
        if form.is_valid(): 
            form.save()
            return redirect("user_login") 
    else:
        form = RegistrationForm()  

    return render(request, "accounts/sign_up.html", {"form": form})  


def forgotPass():
    pass

def mailVerification():
    pass