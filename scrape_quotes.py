import requests
from bs4 import BeautifulSoup
import json

# Send a GET request to the website
url = 'http://quotes.toscrape.com'
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find quotes and authors on the page
quotes = []
authors = set()  # Use a set to store unique author names

for quote in soup.find_all('div', class_='quote'):
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    tags = [tag.text for tag in quote.find_all('a', class_='tag')]

    quotes.append({'text': text, 'author': author, 'tags': tags})
    authors.add(author)

# Convert the set of authors to a list
authors_list = [{'fullname': author} for author in authors]

# Save the quotes to a JSON file
with open('quotes.json', 'w', encoding='utf-8') as json_file:
    json.dump(quotes, json_file, ensure_ascii=False, indent=4)

# Save the authors to a JSON file
with open('authors.json', 'w', encoding='utf-8') as json_file:
    json.dump(authors_list, json_file, ensure_ascii=False, indent=4)
