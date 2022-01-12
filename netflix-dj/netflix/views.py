from django.shortcuts import render

# Create your views here.
from .models import Sliders


def home(request):
    sliders = Sliders.objects.all()
    context = {
        'sliders' : sliders,
    }
    return render(request , 'netflix/home.html' , context)