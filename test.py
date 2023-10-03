import pymongo

# Set up the MongoDB client
client = pymongo.MongoClient("mongodb+srv://web13user:1234@cluster0.kgddv8w.mongodb.net/")
db = client["web13"]

# Access the "quotes" collection
collection = db["quotes"]

# Use findOne() to retrieve a single document
quote = collection.find_one()

# Print the retrieved document
print(quote)
