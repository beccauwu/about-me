from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.PhotosView.as_view(), name='start'),
    path('upload/', views.gallery_upload, name='galleryupload'),  # type: ignore
    path('posts/<int:pk>/', views.PhotoDetail.as_view(), name='photodetail'),
    path('posts/<int:pk>/delete/', views.photo_delete, name='deleteimage'),
    path('posts/<int:pk>/like/', views.post_like, name='postlike'),
    path('following/', views.FollowingView.as_view(), name='following'),
    path('search/', views.PhotoSearch.as_view(), name='search'),
    path('collection/<int:pk>/', views.CollectionView.as_view(), name='collection'),
    path('posts/comment/', views.post_comment, name='postcomment'),
]