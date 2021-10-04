from django.db import models
from sorl.thumbnail import ImageField


class Author(models.Model):
    name = models.CharField(max_length=280)

    @classmethod
    def create_author(cls, books):
        for book in books:
            for author in book['volumeInfo']['author']:
                Author.objects.create(
                    name=author
                )


class Category(models.Model):
    name = models.CharField(max_length=100)

    @classmethod
    def create_category(cls, books):
        for book in books:
            for category in book['volumeInfo']['categories']:
                Category.objects.create(
                    name=category
                )


class Book(models.Model):
    title = models.CharField(max_length=280)
    authors = models.ManyToManyField(Author)
    published_date = models.CharField(max_length=20, null=True)
    categories = models.ManyToManyField(Category)
    average_rating = models.PositiveIntegerField(null=True)
    ratings_counts = models.PositiveIntegerField(null=True)
    thumbnail = ImageField(upload_to='../static/images/')

    @classmethod
    def create_book(cls, books):
        for book in books:
            Book.objects.create(
                title=book['volumeInfo']['title'],
                authors=book['volumeInfo']['authors'],
                published_date=book['volumeInfo'].setdefault('publishedDate', ''),
                categories=book['volumeInfo'].setdefault('categories', ''),
                average_rating=book['volumeInfo'].setdefault('averageRating', None),
                ratings_counts=book['volumeInfo'].setdefault('ratingsCounts', None),
                thumbnail=book['volumeInfo']['imageLinks'].setdefault('thumbnail', None),
            )


def create_db(books):
    Author.create_author(books)
    Category.create_category(books)
    Book.create_book(books)


def clear_db():
    for author in Author.objects.all():
        author.delete()

    for category in Category.objects.all():
        category.delete()

    for book in Book.objects.all():
        book.delete()
