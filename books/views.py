from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from books.forms import BookForm
from books.models import Book

class IndexView(TemplateView):
    template_name = 'books/index.html'

class BookListView(ListView):
    model = Book
    template_name = 'books/books.html'
    context_object_name = 'books'
    paginate_by = 10

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create_book.html'
    success_url = reverse_lazy('books:book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/update_book.html'  
    success_url = reverse_lazy('books:book_list')

class BookDeleteView(DeleteView):
    model = Book 
    success_url = reverse_lazy('books:book_list')

