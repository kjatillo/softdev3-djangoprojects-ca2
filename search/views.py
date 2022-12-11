from django.db.models import Q
from django.views.generic import ListView
from store.models import Ebook, Genre
from django.shortcuts import render


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


def filterView(request):
    qs = Ebook.objects.all()
    title_contains_query = request.GET.get('title_contains')
    isbn_exact_query = request.GET.get('isbn_exact')
    title_or_author_query = request.GET.get('title_or_author')
    genre = request.GET.get('genre')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    if title_contains_query != '' and title_contains_query is not None:
        qs = qs.filter(name__icontains=title_contains_query)
    elif isbn_exact_query != '' and isbn_exact_query is not None:
        qs = qs.filter(isbn=isbn_exact_query)
    elif title_or_author_query != '' and title_or_author_query is not None:
        qs = qs.filter(
            Q(name__icontains=title_or_author_query) | Q(author__icontains=title_or_author_query)
        ).distinct()
    elif genre != '' and genre is not None:
        qs = qs.filter(genre__name=genre.title())

    if date_min != '' and date_min is not None:
        qs = qs.filter(date_added__gte=date_min)
    
    if date_max != '' and date_max is not None:
        qs = qs.filter(date_added__lt=date_max)

    context = {
        'queryset': qs,
        }

    return render(
        request,
        'advance_search.html',
        context,
    )
