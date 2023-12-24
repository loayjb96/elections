import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class FirebaseDataReader:
    def __init__(self):
        # Check if the default app has already been initialized
        if not firebase_admin._apps:
            cred = credentials.Certificate(
                '/Users/loayjaber/elections/imported_files/elections-de049-firebase-adminsdk-6in3h-37fcce4207.json')
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://elections-de049-default-rtdb.firebaseio.com/'
            })

    def list_records(self):
        ref = db.reference('/')  # Adjust the path as needed
        return ref.get()

    def list_records_by_filter(self, filter_name: str, search_text: str):
        ref = db.reference('/')
        query = ref.order_by_child(filter_name).start_at(search_text).end_at(search_text + "\uf8ff")
        return query.get()

