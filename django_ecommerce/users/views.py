from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    """rendering register page with register functionality"""
    # returning content based on request method; if POST, register user, if not, return register html
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', {
                                                    'form': form,
                                                    })


@login_required
def profile(request):
    """rendering my account page for a specific user"""

    return render(request, 'users/profile.html', {
                                                    'title': 'My Account'
                                                    })