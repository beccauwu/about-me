from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='resume/resume.html'), name='resume'),
]
