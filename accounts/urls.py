from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/<int:pk>/', views.UserView.as_view(), name='profiledetails'),
    path('follow/<int:pk>/', views.follow_user, name='followuser'),
    path('unfollow/<int:pk>/', views.unfollow_user, name='unfollowuser'),
    path('update/', views.profile_update, name='profileupdate'),
    path('tos/', TemplateView.as_view(template_name='tos.html'), name='tos'),
    path('pp/', TemplateView.as_view(template_name='pp.html'), name='pp'),
    path('', views.ProfileView.as_view(), name='profile'),
]
