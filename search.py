from db import connect_to_db  # Import the connect_to_db function from db.py
from models import Author, Quote

def search_by_author(author_name, collection):
    try:
        # Connect to the database using the function from db.py
        connect_to_db()

        # Search for quotes by author name in the "quotes" collection
        query = {"author.fullname": {"$regex": f".*{author_name}.*", "$options": "i"}}
        print(f"Searching for quotes by author: {author_name}")
        quotes = Quote.objects(__raw__=query)

        # Print the number of quotes found
        print(f"Number of quotes found: {len(quotes)}")

        # Iterate through the quotes and replace the author ObjectId with the author's name
        author_quotes = []
        for quote in quotes:
            author_id = quote.author.id
            author_details = Author.objects(id=author_id).first()
            if author_details:
                quote.author = author_details.fullname
            author_quotes.append(quote)

        return author_quotes
    except Exception as e:
        print(f"An error occurred: {e}")
        return []



def search_by_tag(tag, collection):
    try:
        db = connect_to_db()
        if db:
            # Search for quotes by tag in the "quotes" collection
            query = {"tags": tag}
            quotes = db[collection].find(query)
            return list(quotes)
        else:
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def search_by_tags(tags, collection):
    try:
        db = connect_to_db()
        if db:
            # Split the input tags by commas
            tag_list = tags.split(",")

            # Search for quotes with any of the specified tags in the "quotes" collection
            query = {"tags": {"$in": tag_list}}
            quotes = db[collection].find(query)
            return list(quotes)
        else:
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def print_quotes(quotes):
    for quote in quotes:
        print(quote["quote"])
