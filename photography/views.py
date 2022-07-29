import os
from django.shortcuts import render
from django.conf import settings

# Create your views here.

def photo_gallery(request):
    files = os.listdir(os.path.join(settings.BASE_DIR, 'photography/static/photos/img/kebnekaise'))
    context = {'files': [os.path.join('photos/img/kebnekaise', file) for file in files]}
    return render(request, 'photos/photos.html', context)

