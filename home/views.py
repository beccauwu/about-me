from django.shortcuts import render

# Create your views here.

# from .models import Question


def index(request):
    context = {}
    context['scripts'] = ["{% static 'home/js/home.js' %}"]
    return render(request, 'home.html', context)
