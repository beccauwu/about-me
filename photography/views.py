import os
from django.shortcuts import render
from django.conf import settings

# Create your views here.

def photo_gallery(request):
    kebnekaise = os.listdir(os.path.join(settings.BASE_DIR, 'photography/static/photos/img/kebnekaise'))
    riksgransen = os.listdir(os.path.join(settings.BASE_DIR, 'photography/static/photos/img/riksgransen'))
    others = os.listdir(os.path.join(settings.BASE_DIR, 'photography/static/photos/img/others'))
    context = {
        'kebnekaise': [os.path.join('photos/img/kebnekaise', file) for file in kebnekaise],
        'riksgransen': [os.path.join('photos/img/riksgransen', file) for file in riksgransen],
        'others': [os.path.join('photos/img/others', file) for file in others]
        }
    return render(request, 'photos/photos.html', context)
