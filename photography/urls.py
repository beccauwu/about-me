from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.photo_gallery, name='start'),
    path('upload/', views.gallery_upload, name='galleryupload'),  # type: ignore
    path('posts/<int:pk>/', views.PhotoDetail.as_view(), name='photodetail'),
    path('posts/delete/<int:pk>/', views.photo_delete, name='deleteimage'),
    path('posts/comment/', views.post_comment, name='postcomment'),
]