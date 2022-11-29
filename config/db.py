from pymongo import MongoClient

# MongoDB attributes
mongodb_uri = f'mongodb+srv://d4:1234@learn.0fkccmi.mongodb.net/?retryWrites=true&w=majority'
port = 8000  


conn = MongoClient(mongodb_uri, port)
db = conn["usuariosTienda"]