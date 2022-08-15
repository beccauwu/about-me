from .firebase_auths import CREDENTIALS, config
from firebase_admin import firestore, initialize_app

db_app = initialize_app(CREDENTIALS, {'projectId': config('FB_PROJECT_ID')})

db = firestore.client(db_app)

class CustomUser:
    def __init__(self, email, username, uid, bio=None, pfp=None):
        self.email = email
        self.username = username
        self.uid = uid
        self.bio = bio
        self.pfp = pfp
    def create(self):
        doc_ref = db.collection(u'users').document(self.uid)
        doc_ref.set({
            u'email': self.email,
            u'username': self.username,
            u'uid': self.uid,
            u'bio': self.bio,
            u'pfp': self.pfp
        })
    def update(self):
        doc_ref = db.collection(u'users').document(self.uid)
        doc_ref.update({
            u'email': self.email,
            u'username': self.username,
            u'uid': self.uid,
            u'bio': self.bio,
            u'pfp': self.pfp
        })
    def delete(self):
        doc_ref = db.collection(u'users').document(self.uid)
        doc_ref.delete()
