from django.shortcuts import render


def index(request):
    return render(request, 'gymstore/index.html')


def packages(request):
    return render(request, 'gymstore/packages.html')


def about(request):
    return render(request, 'gymstore/about.html')
