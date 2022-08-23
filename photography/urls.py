from django.urls import path
from . import views


urlpatterns = [
    path('', views.PhotosView.as_view(), name='start'),
    path('upload/', views.gallery_upload, name='galleryupload'),
    path('posts/<int:pk>/', views.PhotoDetail.as_view(), name='photodetail'),
    path('posts/<int:pk>/delete/', views.photo_delete, name='deleteimage'),
    path('posts/<int:pk>/like/', views.post_like, name='like'),
    path('posts/<int:pk>/unlike/', views.post_unlike, name='unlike'),
    path('following/', views.FollowingView.as_view(), name='following'),
    path('search/', views.PhotoSearch.as_view(), name='search'),
    path('collection/<int:pk>/', views.CollectionView.as_view(), name='collection'),
    path('posts/<int:pk>/comment/', views.post_comment, name='postcomment'),
    path('posts/comment/<int:pk>/delete/', views.comment_delete, name='deletecomment'),
]