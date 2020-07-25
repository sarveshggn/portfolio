from django.shortcuts import render
from .models import Dsproject

# Create your views here.

def dspro(request):
    dsprojects = Dsproject.objects
    return render(request, 'dsproj/dsprojhome.html', {'dsprojects': dsprojects})