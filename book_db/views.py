import requests
from rest_framework import viewsets

from book_db.models import clear_db, create_db, Book
from book_db.serializers import BookListViewSerializer


class BookListViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        clear_db()
        api_url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
        response = requests.get(api_url)
        books_json = response.json()['items']
        create_db(books_json)
        q = Book.objects.all()
        return q

    queryset = create_db
    serializer_class = BookListViewSerializer
