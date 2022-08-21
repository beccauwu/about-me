from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('logout/', views.logout_request, name='logout'),
    path('edit-image/<int:pk>/update', views.EditImageView.as_view(), name='editimage'),
    path('profile/<int:pk>/', views.UserView.as_view(), name='profiledetails'),
    path('follow/<int:pk>/', views.follow_user, name='followuser'),
    path('unfollow/<int:pk>/', views.unfollow_user, name='unfollowuser'),
    path('', views.profile, name='profile'),
]
