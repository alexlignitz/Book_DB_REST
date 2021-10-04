from django.db import models
from sorl.thumbnail import ImageField
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile

from Book_DB_REST import settings


class Book(models.Model):
    title = models.CharField(max_length=280)
    authors = models.CharField(max_length=100, null=True)
    published_date = models.CharField(max_length=20, null=True)
    categories = models.CharField(max_length=280, null=True)
    average_rating = models.PositiveIntegerField(null=True)
    ratings_counts = models.PositiveIntegerField(null=True)
    thumbnail = ImageField(upload_to=settings.MEDIA_ROOT, null=True)

    @classmethod
    def create_book(cls, books):
        for book in books:
            title = book['volumeInfo']['title']
            authors = book['volumeInfo'].setdefault('authors', 'Unknown')
            author_lst = []
            for author in authors:
                author_lst.append(author)
            published_date = book['volumeInfo'].setdefault('publishedDate', '')
            categories = book['volumeInfo'].setdefault('categories', 'No categories assigned')
            average_rating = book['volumeInfo'].setdefault('averageRating', 0)
            ratings_counts = book['volumeInfo'].setdefault('ratingsCounts', 0)

            b = Book(
                title=title,
                authors=author_lst,
                published_date=published_date,
                categories=categories,
                average_rating=average_rating,
                ratings_counts=ratings_counts,
            )
            b.save()

            try:
                image_info = book['volumeInfo']['imageLinks']
                thumbnail_url = image_info['thumbnail']
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(urlopen(thumbnail_url).read())
                img_temp.flush()
                b.thumbnail.save(f"image_{b.id}", File(img_temp))
            except:
                pass
            b.save()


def create_db(books):
    Book.create_book(books)


def clear_db():
    for book in Book.objects.all():
        book.delete()

