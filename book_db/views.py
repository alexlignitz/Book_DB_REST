import requests

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from book_db.models import clear_db, Book
from book_db.serializers import BookSerializer

clear_db()


class BookListViewSet(viewsets.ModelViewSet):
    """
    List of books fetched from the external API with query parameter "Hobbit".
    """

    api_url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
    response = requests.get(api_url)
    books_json = response.json()['items']
    Book.create_book(books_json)

    serializer_class = BookSerializer

    def get_queryset(self):
        """
        If any filtering or sorting parameters are being added in url query_params,
        the view will show filtered or sorted list.
        Otherwise it will show the full list of books sorted by object id.
        """

        queryset = Book.objects.all()
        year = self.request.query_params.get('published_date')
        author = self.request.query_params.get('author')
        sort = self.request.query_params.get('sort')
        if year is not None:
            queryset = queryset.filter(published_date__icontains=year)
        elif author is not None:
            queryset = queryset.filter(authors__icontains=author)
        elif sort is not None:
            if sort == 'published_date':
                queryset = Book.objects.all().order_by('published_date')
            elif sort == '-published_date':
                queryset = Book.objects.all().order_by('-published_date')
        return queryset


class LibraryView(APIView):
    """
    This view has no GET method, the POST method allows to fetch the data from external API
    with the dict {"q": $"lookup_word"} and save it to the existing database with books.
    """

    def post(self, request, *args, **kwargs):
        data = request.data
        if data['q']:
            keyword = data['q']
            api_url = f"https://www.googleapis.com/books/v1/volumes?q={keyword}"
            response = requests.get(api_url)
            books_json = response.json()['items']
            Book.create_book(books_json)
            message = 'Database updated'
            return Response({'success': message})
        else:
            message = 'Invalid query'
            return Response({'error': message})
