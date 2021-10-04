import requests

from book_db.models import clear_db, create_db

api_url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
response = requests.get(api_url)
books_json = response.json()['items']


