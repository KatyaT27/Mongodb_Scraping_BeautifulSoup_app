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
authors = {}  # Use a dictionary to store unique author information

for quote in soup.find_all('div', class_='quote'):
    text = quote.find('span', class_='text').text
    author_name = quote.find('small', class_='author').text
    tags = [tag.text for tag in quote.find_all('a', class_='tag')]

    # Check if the author has been encountered before
    if author_name not in authors:
        # If the author is new, create an entry with default values
        authors[author_name] = {
            'fullname': author_name,
            'born_date': None,
            'born_location': None,
            'description': None
        }

        # Extract additional author information (if available)
        author_page_url = url + quote.find_next('a')['href']
        author_response = requests.get(author_page_url)
        author_soup = BeautifulSoup(author_response.text, 'html.parser')

        # Update author information with actual data if found
        born_info = author_soup.find('span', class_='author-born-date')
        if born_info:
            authors[author_name]['born_date'] = born_info.get_text()

        location_info = author_soup.find('span', class_='author-born-location')
        if location_info:
            authors[author_name]['born_location'] = location_info.get_text()

        description_info = author_soup.find('div', class_='author-description')
        if description_info:
            authors[author_name]['description'] = description_info.get_text()

    quotes.append({
        'tags': tags,
        'author': author_name,
        'quote': text
    })

# Convert the dictionary of authors to a list
authors_list = list(authors.values())

# Save the quotes to a JSON file
with open('quotes.json', 'w', encoding='utf-8') as json_file:
    json.dump(quotes, json_file, ensure_ascii=False, indent=4)

# Save the authors to a JSON file
with open('authors.json', 'w', encoding='utf-8') as json_file:
    json.dump(authors_list, json_file, ensure_ascii=False, indent=4)
