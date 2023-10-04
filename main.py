from search import search_by_author, search_by_tag, search_by_tags, print_quotes
from db import connect_to_db
from load_data import load_data_from_json

# Connect to the MongoDB database
connect_to_db()

# Assuming you have data loading functions, you can use them to load data
# into your MongoDB database here

while True:
    command = input("Enter a command (name, tag, tags, all, exit): ").strip()

    if command == "exit":
        print("Exiting the script.")
        break
    elif command.startswith("name:"):
        author_name = command.split(":", 1)[1].strip()
        quotes = search_by_author(author_name, "quotes")
    elif command.startswith("tag:"):
        tag = command.split(":", 1)[1].strip()
        quotes = search_by_tag(tag, "quotes")
    elif command.startswith("tags:"):
        tags = command.split(":", 1)[1].strip()
        quotes = search_by_tags(tags, "quotes")
    elif command == "all":
        # Fetch all quotes from the "quotes" collection
        quotes = search_by_author("", "quotes")
    else:
        print("Invalid command. Please use 'name:', 'tag:', 'tags:', 'all', or 'exit'.")
        continue

    if quotes:
        print_quotes(quotes)
    else:
        print("No quotes found.")
