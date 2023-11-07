from pymongo.mongo_client import MongoClient
import json

uri ="mongodb+srv://vishnumurali835:8888888888888@vishnumurali.gan12f1.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
"""try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)"""
    
database=client['Database']

#type(database)

collection=database['Company_review']

#type(collection)

with open('JSON_details.json', 'r') as json_file:
    data = json.load(json_file)
    #print(data)
    
result = collection.insert_one(data)

data=[]
for i in collection.find({'Company_Name':"TCS"}):
    data.append(i)
    print(data)

