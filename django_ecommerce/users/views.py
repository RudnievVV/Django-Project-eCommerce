import os
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django_ecommerce.settings import MEDIA_ROOT
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserUpdateAddressForm
from .models import Profile, UserAddress


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_profile = Profile()
            user_profile.user = user
            user_profile.save()
            messages.success(request, 'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    general_current_user_img = User.objects.get(username=request.user.profile.user)
    general_current_user_img = general_current_user_img.profile.image.url
    if request.method == "POST" and request.POST.get('update_user') is not None:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            if general_current_user_img != '/media/images/user/default.jpg' and general_current_user_img != request.user.profile.image.url:
                os.unlink(os.path.join(MEDIA_ROOT, 'images', 'user', 'profile_pics', general_current_user_img.split('/')[-1]))
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('my-account')
    elif request.method == "POST" and request.POST.get('add_address') is not None:
        u_address_form = UserUpdateAddressForm(request.POST, instance=request.user)
        if u_address_form.is_valid():
            u_address_form = UserAddress()
            u_address_form.user = request.user
            u_address_form.company = request.POST.get('company')
            u_address_form.phone_number = request.POST.get('phone_number')
            u_address_form.address_1 = request.POST.get('address_1')
            u_address_form.address_2 = request.POST.get('address_2')
            u_address_form.city = request.POST.get('city')
            u_address_form.country = request.POST.get('country')
            u_address_form.postal_code = request.POST.get('postal_code')
            u_address_form.fax = request.POST.get('fax')
            u_address_form.save()
            messages.success(request, f'You added the new address!')
            return redirect('my-account')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_address_form = UserUpdateAddressForm()

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'u_address_form': u_address_form,
        'title': 'My Account',
    }

    return render(request, 'users/profile.html', context)


@login_required
def delete_address(request, id=id):
    if len(User.objects.get(id=request.user.id).user_addresses.filter(id=id)):
        User.objects.get(id=request.user.id).user_addresses.get(id=id).delete()
        messages.success(request, f'You deleted the address!')
    else:
        messages.warning(request, f'Something went wrong!')
    return redirect('my-account')


@login_required
def update_address(request, id=id):
    if request.method == "POST":
        if len(User.objects.get(id=request.user.id).user_addresses.filter(id=id)):
            address = get_object_or_404(User.objects.get(id=request.user.id).user_addresses, pk=id)
            form = UserUpdateAddressForm(request.POST, instance=address)
            if form.is_valid():
                form.save()
                messages.success(request, f'You updated the address!')
                return redirect('my-account')
        else:
            return HttpResponse(400, "Something went wrong!")
    else:
        address = get_object_or_404(User.objects.get(id=request.user.id).user_addresses, pk=id)
        form = UserUpdateAddressForm(instance=address)

        context = {
            'form': form,
            'title': 'Adress Update',
        }
        return render(request, 'users/address_update.html', context)
