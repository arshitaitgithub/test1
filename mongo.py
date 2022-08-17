import pymongo
client = pymongo.MongoClient("mongodb+srv://arshita:IHImEhcBIVOsLN2z@cluster0.geymmfm.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)