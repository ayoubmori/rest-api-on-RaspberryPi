from pymongo import MongoClient



client = MongoClient('mongodb://192.168.1.6:27017/')
db = client['test']
