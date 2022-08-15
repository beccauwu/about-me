import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin.exceptions import UserNotFoundError, ExpiredIdTokenError
from decouple import config

CREDENTIALS = credentials.Certificate({
 "type": config('FB_TYPE'),
 "project_id": config('FB_PROJECT_ID'),
 "private_key_id": config('FB_PRIVATE_KEY_ID'),
 "private_key": config('FB_PRIVATE_KEY').replace("\\n", "\n"),
 "client_email": config('FB_CLIENT_EMAIL'),
 "client_id": config('FB_CLIENT_ID'),
 "auth_uri": config('FB_AUTH_URI'),
 "token_uri": config('FB_TOKEN_URI'),
 "auth_provider_x509_cert_url": config('FB_PROVIDER_X509_CERT_URL'),
 "client_x509_cert_url": config('FB_CLIENT_X509_CERT_URL')
})

AUTH_APP = firebase_admin.initialize_app(CREDENTIALS)

