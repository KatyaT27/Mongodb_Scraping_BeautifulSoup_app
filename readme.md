
# Your Quote Collection Program

This program allows you to perform web scraping of quotes and authors and store them in a MongoDB database.

## Requirements

Make sure you have installed all the required packages using the `requirements.txt` file. You can install them by running the following command:

```bash
pip install -r requirements.txt
```

## Running the Program

1. Start web scraping by running the command:

```bash
/opt/homebrew/bin/python3 scrape_quotes.py
```

This command will create `quotes.json` and `authors.json` files containing the collected data about quotes and authors.

2. Connect to the MongoDB database by modifying the database URI in the `db.py` file if necessary.

3. Load data into the MongoDB database using the command:

```bash
/opt/homebrew/bin/python3 load_data.py
```

This command will load data from the `quotes.json` and `authors.json` files into your MongoDB database.

4. Run the main program to interact with the data:

```bash
/opt/homebrew/bin/python3 main.py
```

You will be able to search for quotes by author name, tags, and more.

## Exiting

To exit the program, enter the `exit` command.

That's it! You can now use your program to collect and work with quotes and authors.
