import os
from django.shortcuts import render
from django.conf import settings

# Create your views here.

def photo_gallery(request):
    kebfiles = os.listdir(os.path.join(settings.BASE_DIR, 'photography/static/photos/img/kebnekaise'))
    others = os.listdir(os.path.join(settings.BASE_DIR, 'photography/static/photos/img/others'))
    context = {
        'kebfiles': [os.path.join('photos/img/kebnekaise', kebfile) for kebfile in kebfiles],
        'others': [os.path.join('photos/img/others', other) for other in others]
        }
    return render(request, 'photos/photos.html', context)
