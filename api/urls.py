from django.urls import path
from .views import BookListAPIView, AuthorListAPIView

urlpatterns = [
    path("book/", BookListAPIView.as_view()),
    path("author/", AuthorListAPIView.as_view()),
]
