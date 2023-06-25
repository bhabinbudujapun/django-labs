from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def members(request):
    return render(request, 'members.html',{"name": "Member"})

def home(request):
    return render(request, 'home.html',{"name": "Home"})