from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('signup/', views.signup, name='signup'),
]


