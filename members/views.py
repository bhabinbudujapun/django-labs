from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def result(request):
    n1 = 0
    n2 = 0
    n1 = int(request.GET.get('num1'))
    n2 = int(request.GET.get('num2'))
    return render(request, 'result.html',{'result': n1+n2})

def members(request):
    return render(request, 'members.html',{"name": "Member"})

def home(request):
    return render(request, 'home.html',{"name": "Home"})    