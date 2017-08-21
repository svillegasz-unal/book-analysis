from urllib.parse import urlparse as url
import requests
import json

from authors import authors
from data import clean_data
import env


query = '?' + '&'.join([str(param) + "=" + str(value) for param, value in env.PARAMS.items()])

books_data = []
for author in authors:
    books = author.get('books')
    for book in books:
        r = requests.get(env.ENDPOINT + query.format(book_title = book, key = env.API_KEY))
        cleaned_data = clean_data(r.json(), author.get('name'), book)
        if cleaned_data: books_data.append(json.dumps(cleaned_data))

with open('data.txt', 'w') as outfile:
    outfile.write('[' + ','.join(books_data) + ']')


