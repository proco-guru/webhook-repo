#TODO 1:importing required file and classes
import pymongo
from bson.json_util import dumps

#TODO 2: Establish the connect between Mongodb and python using pymongo
client =pymongo.MongoClient('mongodb://127.0.0.1:27017/')

#TODO 3: Create the Database having name githubDb
create_database=client['githubDb']

#TODO 4: Create Db Collection having name events
dbCollection=create_database['events']

#TODO 5: Create function to push generated Event in DB collection
def insert(data):
      dbCollection.insert_one(data)

#TODO 6: Create function to get all Events from DB
def find(query):
    docs = dbCollection.find()
    res=dumps(docs)
    return res

