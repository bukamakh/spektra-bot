import pyrebase
import os

config = {
  "apiKey": "AIzaSyC576DYcTg6rMKcyaClwYtAjzGDELneJ2o",
  "authDomain": "spektra-80eda.firebaseapp.com",
  "databaseURL": "https://spektra-80eda.firebaseio.com",
  "storageBucket": "spektra-80eda.appspot.com",
  "serviceAccount": os.path.dirname(os.path.realpath(__file__)) + "/admin.json"
}

firebase = pyrebase.initialize_app(config)