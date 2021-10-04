from rest_framework import serializers

from book_db.models import Book


class BookListViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
