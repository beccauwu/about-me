from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = True

class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'

StaticRootS3Boto3Storage = lambda: S3Boto3Storage(location='static')
MediaRootS3Boto3Storage = lambda: S3Boto3Storage(location='media')