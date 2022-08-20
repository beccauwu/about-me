from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.photo_gallery, name='photos'),
    path('upload/', views.gallery_upload, name='galleryupload'),
    path('photos/<int:pk>/', views.PhotoDetail.as_view(), name='photodetail'),
    path('photos/comment/', views.post_comment, name='postcomment'),
    path(
        'collection-create/',
        views.CollectionCreate.as_view(),
        name='collection-create',
    ),
]