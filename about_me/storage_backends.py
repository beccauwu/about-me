# from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import setting
from urllib.parse import urljoin

# class MediaStorage(S3Boto3Storage):
#     location = 'media'
#     file_overwrite = True

# class StaticStorage(S3Boto3Storage):
#     location = 'static'
#     default_acl = 'public-read'

# class MediaGCSStorage(GoogleCloudStorage):
#     """GoogleCloudStorage suitable for Django's Media files."""

#     def __init__(self, *args, **kwargs):
#         if not settings.MEDIA_URL:
#             raise Exception('MEDIA_URL has not been configured')
#         kwargs['location'] = setting('MEDIA_LOCATION')
        
#         super(MediaGCSStorage, self).__init__(*args, **kwargs)

#     def url(self, name):
#         """.url that doesn't call Google."""
#         return urljoin(settings.MEDIA_URL, name)


# class StaticGCSStorage(GoogleCloudStorage):
#     """GoogleCloudStorage suitable for Django's Static files"""

#     def __init__(self, *args, **kwargs):
#         if not settings.STATIC_URL:
#             raise Exception('STATIC_URL has not been configured')
#         kwargs['location'] = setting('STATIC_LOCATION')
#         super(StaticGCSStorage, self).__init__(*args, **kwargs)

#     def url(self, name):
#         """.url that doesn't call Google."""
#         return urljoin(settings.STATIC_URL, name)

StaticGCSStorage = lambda: GoogleCloudStorage(location='static')
MediaGCSStorage = lambda: GoogleCloudStorage(location='media')
                                        

# StaticRootS3Boto3Storage = lambda: S3Boto3Storage(location='static')
# MediaRootS3Boto3Storage = lambda: S3Boto3Storage(location='media')