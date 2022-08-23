from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings
from urllib.parse import urljoin

StaticRootS3Boto3Storage = lambda: S3Boto3Storage(location='static')
MediaRootS3Boto3Storage = lambda: S3Boto3Storage(location='media')

def staturl(name):
    """Return the full URL to a static file."""
    return urljoin(settings.STATIC_URL, name)
