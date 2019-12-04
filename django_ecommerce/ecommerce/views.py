from django.shortcuts import render


def home_page(request):
    return render(request, 'ecommerce/home.html')


def about(request):
    return render(request, 'ecommerce/about.html', {'title': 'About Us'})
