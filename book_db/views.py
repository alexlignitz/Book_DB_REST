import requests
from rest_framework import filters
from rest_framework import viewsets

from book_db.models import clear_db, Book
from book_db.serializers import BookSerializer


class BookListViewSet(viewsets.ModelViewSet):
    clear_db()
    api_url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
    response = requests.get(api_url)
    books_json = response.json()['items']
    Book.create_book(books_json)

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['published_date', 'authors']
    ordering_fields = ['published_date']
