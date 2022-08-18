from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('logout/', views.logout_request, name='logout'),
    path('', views.profile, name='profile'),
]
