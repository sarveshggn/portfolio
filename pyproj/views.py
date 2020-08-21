from django.shortcuts import render
from .models import Pyproject

# Create your views here.

def pypro(request):
    pyprojects = Pyproject.objects
    return render(request, 'pyproj/pyprojhome.html', {'pyprojects': pyprojects})