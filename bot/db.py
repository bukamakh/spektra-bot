import pyrebase

config = {
  "apiKey": "AIzaSyC576DYcTg6rMKcyaClwYtAjzGDELneJ2o",
  "authDomain": "spektra-80eda.firebaseapp.com",
  "databaseURL": "https://spektra-80eda.firebaseio.com",
  "storageBucket": "spektra-80eda.appspot.com",
  "serviceAccount": "/admin.json"
}

firebase = pyrebase.initialize_app(config)