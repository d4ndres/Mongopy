from pymongo import MongoClient

# MongoDB attributes
mongodb_uri = 'mongodb+srv://d4:1016@guiac4.3wtun5e.mongodb.net/?retryWrites=true&w=majority'
port = 8000  


conn = MongoClient(mongodb_uri, port)
db = conn["tiendaOnline"]