from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from books.models import Book


# Create your views here.


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'