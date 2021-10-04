import requests
from rest_framework import viewsets

from book_db.models import clear_db, create_db, Book
from book_db.serializers import BookSerializer


class BookListViewSet(viewsets.ModelViewSet):
    clear_db()
    api_url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
    response = requests.get(api_url)
    books_json = response.json()['items']
    create_db(books_json)

    queryset = Book.objects.all()
    serializer_class = BookSerializer
