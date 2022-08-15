from .firebase_auths import CREDENTIALS, config
from firebase_admin import firestore, initialize_app

db_app = initialize_app(CREDENTIALS, {'projectId': config('FB_PROJECT_ID')})

db = firestore.client(db_app)

class Profile:
    def __init__(self, username, bio=None, pfp=None):
        self.username = username
        self.bio = bio
        self.pfp = pfp
    def create(self):
        doc_ref = db.collection(u'users').document(self.username)
        doc_ref.set({
            u'bio': self.bio,
            u'pfp': self.pfp
        })
    def update(self):
        doc_ref = db.collection(u'users').document(self.username)
        doc_ref.update({
            u'bio': self.bio,
            u'pfp': self.pfp
        })
    def delete(self):
        doc_ref = db.collection(u'users').document(self.username)
        doc_ref.delete()
    def add_image(self, image_path, image_name, text='empty'):
        doc_ref = db.collection(u'users').document(self.username)
        doc_ref.update({
            u'images': {
                image_name : {
                    u'path': image_path,
                    u'text': text
                },
            },
        })
