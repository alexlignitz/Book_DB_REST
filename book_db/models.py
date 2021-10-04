from django.db import models
from sorl.thumbnail import ImageField
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile


# class Author(models.Model):
#     name = models.CharField(max_length=280)
#
#     @classmethod
#     def create_author(cls, books):
#         for book in books:
#             if book['volumeInfo']['authors']:
#                 for author in book['volumeInfo']['authors']:
#                     Author.objects.create(
#                         name=author
#                     )
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#
#     @classmethod
#     def create_category(cls, books):
#         for book in books:
#             if book['volumeInfo']['categories']:
#                 for category in book['volumeInfo']['categories']:
#                     Category.objects.create(
#                         name=category
#                     )
from Book_DB_REST import settings


class Book(models.Model):
    title = models.CharField(max_length=280)
    authors = models.CharField(max_length=280, default='')
    published_date = models.CharField(max_length=20, null=True)
    categories = models.CharField(max_length=280, default='')
    average_rating = models.PositiveIntegerField(null=True)
    ratings_counts = models.PositiveIntegerField(null=True)
    thumbnail = ImageField(upload_to=settings.MEDIA_ROOT, null=True)

    @classmethod
    def create_book(cls, books):
        for book in books:
            title = book['volumeInfo']['title']
            authors = book['volumeInfo'].setdefault('authors', '')
            published_date = book['volumeInfo'].setdefault('publishedDate', '')
            categories = book['volumeInfo'].setdefault('categories', '')
            average_rating = book['volumeInfo'].setdefault('averageRating', None)
            ratings_counts = book['volumeInfo'].setdefault('ratingsCounts', None)

            b = Book(
                title=title,
                authors=authors,
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
# Author.create_author(books)
# Category.create_category(books)
    Book.create_book(books)


def clear_db():
    # for author in Author.objects.all():
    #     author.delete()
    #
    # for category in Category.objects.all():
    #     category.delete()

    for book in Book.objects.all():
        book.delete()

