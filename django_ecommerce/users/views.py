import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django_ecommerce.settings import MEDIA_ROOT
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileUpdateAddressForm
from .models import Profile


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    general_current_user_img = User.objects.get(username=request.user.profile.user)
    general_current_user_img = general_current_user_img.profile.image.url
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        p_address_form = ProfileUpdateAddressForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            if general_current_user_img != '/media/images/user/default.jpg' and general_current_user_img != request.user.profile.image.url:
                os.unlink(os.path.join(MEDIA_ROOT, 'images', 'user', 'profile_pics', general_current_user_img.split('/')[-1]))
            p_form.save()
            p_address_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('my-account')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        p_address_form = ProfileUpdateAddressForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'p_address_form': p_address_form,
        'title': 'My Account',
    }

    return render(request, 'users/profile.html', context)
