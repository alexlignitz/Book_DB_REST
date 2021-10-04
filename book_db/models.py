from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=280)
    authors = models.CharField(max_length=100, null=True)
    published_date = models.CharField(max_length=20, null=True)
    categories = models.CharField(max_length=280, null=True)
    average_rating = models.PositiveIntegerField(null=True)
    ratings_counts = models.PositiveIntegerField(null=True)
    thumbnail = models.URLField(null=True)

    @classmethod
    def create_book(cls, books):
        for book in books:
            title = book['volumeInfo']['title']
            authors = book['volumeInfo'].setdefault('authors', ['Unknown'])
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
                b.thumbnail = image_info['thumbnail']
                b.save()
            except:
                pass
            b.save()


def clear_db():
    for book in Book.objects.all():
        book.delete()
