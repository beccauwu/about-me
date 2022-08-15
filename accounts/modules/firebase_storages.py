import uuid
import pathlib
from .firebase_auths import CREDENTIALS, config
from .firebase_dbs import Profile
from firebase_admin import initialize_app, storage

storage_app = initialize_app(CREDENTIALS, {'storageBucket': config('FB_STORAGE_BUCKET')})
bucket = storage.bucket(storage_app)

class ImageUpload:
    def __init__(self, username, image_path, image_name, image_text=None, collection=None):
        self.username = username
        self.image_path = image_path
        self.image_name = image_name
        self.collection = collection
        self.random_name = str(uuid.uuid4().hex)
        self.text = image_text
        self.blob_path = f'{self.username}/{self.random_name}{pathlib.Path(self.image_path).suffix}'
    def upload(self):
        blob = bucket.blob(self.blob_path)
        blob.upload_from_filename(self.image_path)
        blob.make_public()
        Profile.add_image(username=self.username, image_path=self.blob_path, image_name=self.image_name, text=self.text)
        return blob.public_url
    def delete(self):
        blob = bucket.blob(self.username + self.collection + self.image_path)
        blob.delete()
