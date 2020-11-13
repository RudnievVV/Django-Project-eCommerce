from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def user_register(request):
    """rendering user register page with user register functionality"""
    # returning content based on request method; if POST, register user, if not, return register html
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            new_user.username = username.lower() # needed to make username lowercase and then on login page login user with lower case username
            new_user.save()
            messages.success(request, f'{username}, your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', {
                                                    'form': form,
                                                    })


def user_login(request):
    """rendering login page with user login functionality"""
    # returning content based on request method; if POST, login user, if not, return login html
    if request.method == "POST":
        username = request.POST['username'].lower() # needed to lower because in DB username is in lower case
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            messages.error(request, "Your username and password didn't match. Please try again.")
            return redirect('login')
    else:
        return render(request, 'users/login.html')


@login_required
def profile(request):
    """rendering my account page for a specific user"""

    return render(request, 'users/profile.html', {
                                                    'title': 'My Account'
                                                    })