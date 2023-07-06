from rest_framework.serializers import ModelSerializer
from .models import Book, Author


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = ("id", "title", "description", "created_at")


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = ("id", "full_name", "website", "photo", "about", "created_at")

