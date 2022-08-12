from . import views
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('update/', views.update_profile, name='profile_update'),
]
