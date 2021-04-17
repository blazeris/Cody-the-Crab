import pyrebase


class FirebaseConnection():
    def __init__(self):
        config = {
            "apiKey": "AIzaSyBIk_Z5t5PdO1D_vXbEEoZ_qL7K7flVoAE",
            "authDomain": "study-buddy-231d1.firebaseapp.com",
            "databaseURL": "https://study-buddy-231d1-default-rtdb.firebaseio.com/",
            "storageBucket": "study-buddy-231d1.appspot.com"
        }
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()
        self.s = firebase.storage()

    def DB_set(self, data, location):
        locations = location.split('/')
        child = self.db
        for l in locations:
            child = child.child(l)
        child.set(data)

    def DB_get(self, location):
        locations = location.split('/')
        child = self.db
        for l in locations:
            child = child.child(l)
        return child.get()
