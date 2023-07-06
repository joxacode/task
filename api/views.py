from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import serializer
from .models import Author, Book

# Create your views here.


class AuthorListAPIView(ListAPIView):
    serializer_class = serializer.AuthorSerializer
    queryset = Author.objects.all()


class BookListAPIView(ListAPIView):
    serializer_class = serializer.BookSerializer
    queryset = Book.objects.all()
