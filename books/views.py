from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DeleteView

from books.models import Book


# Create your views here.


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "books/book_detail.html"


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author','description', 'price']
    template_name = "books/create_book.html"



class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author','description', 'price']
    template_name = "books/update_book.html"


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')  # Redirect URL after successful deletion
    template_name = 'books/delete_book.html'  # Template name for displaying the delete confirmation page
