from django.shortcuts import render

# Create your views here.
def home(request):
    content = 'Welcome, to Django world'
    return render(request, 'index.html', content)