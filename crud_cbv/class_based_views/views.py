from django.shortcuts import render

# Create your views here.

from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from class_based_views.forms import AuthorForm, BookForm
from class_based_views.models import Author, Book


class HomeView(TemplateView):
    template_name = 'index.html'


class AuthorListView(ListView):
    model = Author
    template_name = 'author.html'
    context_object_name = 'authors'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'create_author.html'
    success_url = reverse_lazy('author_list') 


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'update_author.html'
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(DeleteView):
    model = Author 
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author_list')


class BookListView(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'create_book.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'update_book.html'  
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book 
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

class SearchView(TemplateView):
    template_name = 'search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['query'] = query
        context['books'] = Book.objects.filter(title__icontains=query) if query else []
        context['authors'] = Author.objects.filter(name__icontains=query) if query else []
        return context


