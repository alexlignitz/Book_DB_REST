import requests
from rest_framework import viewsets

from book_db.models import clear_db, create_db
from book_db.serializers import BookListViewSerializer


class BookListViewSet(viewsets.ModelViewSet):
    api_url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
    response = requests.get(api_url)
    books_json = response.json()['items']

    queryset = books_json
    clear_db()
    create_db(queryset)
    serializer_class = [BookListViewSerializer]





