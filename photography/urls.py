from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.photo_gallery, name='photos'),
    path('/upload', views.gallery_upload, name='galleryupload')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)