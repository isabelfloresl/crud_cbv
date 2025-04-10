from django.views.generic import TemplateView
from django.db.models import Q
from authors.models import Author
from books.models import Book


class HomeView(TemplateView):
    template_name = 'index.html'
    
class SearchView(TemplateView):
    template_name = 'search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['query'] = query
        context['books'] = Book.objects.filter(title__icontains=query) if query else []
        context['authors'] = Author.objects.filter(name__icontains=query) if query else []
        return context