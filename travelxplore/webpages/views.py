from django.shortcuts import render
from . models import Destination

# Create your views here.


def home(request):
    dests = Destination.objects.all()
    return render(request, 'webpages/home.html', {'dests': dests})


def about(request):
    return render(request, 'webpages/about.html')


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    return render(request, 'webpages/contact.html')


def destinations(request):
    dests = Destination.objects.all().order_by('d_price')
    return render(request, 'webpages/destinations.html', {'dests': dests})


