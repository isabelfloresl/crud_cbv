
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from authors.forms import AuthorForm
from authors.models import Author

# Create your views here.

class IndexView(TemplateView):
    template_name = 'authors/index.html'

class AuthorListView(ListView):
    model = Author
    template_name = 'authors/authors.html'
    context_object_name = 'authors'
    paginate_by = 10

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/create_author.html'
    success_url = reverse_lazy('authors:author_list') 

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/update_author.html'
    success_url = reverse_lazy('authors:author_list')

class AuthorDeleteView(DeleteView):
    model = Author 
    success_url = reverse_lazy('authors:author_list')
