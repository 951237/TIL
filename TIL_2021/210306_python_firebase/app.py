import pyrebase
import json

with opein("auth.json") as f:
    config = json.load(f)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

data = {"password" : 1234, "name" : "951237"}
db.child("user").child("temp123").update(data)