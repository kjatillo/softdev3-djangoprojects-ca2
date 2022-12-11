from django.db.models import Q
from django.views.generic import ListView
from store.models import Ebook


class SearchResultsListView(ListView):
    model = Ebook
    context_object_name = 'ebook_list'
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        
        return Ebook.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) | 
            Q(author__icontains=query) |
            Q(genre__name__icontains=query)
        )

    def get_context_data(self, **kwargs):
        context = super(SearchResultsListView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        
        return context
