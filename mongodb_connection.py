from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

database = client["researchhub"]

collection = database["research_documents"]

documents = collection.find()

for document in documents:
    print(document)

client.close()