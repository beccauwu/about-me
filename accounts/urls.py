from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('logout/', views.logout_request, name='logout'),
    path('edit-image/<int:pk>/update', views.EditImageView.as_view(), name='editimage'),
    path('delete-image/<int:pk>/', views.DeleteImageView.as_view(), name='deleteimage'),
    path('', views.profile, name='profile'),
]
