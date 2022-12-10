from django.shortcuts import render
from store.models import Ebook
# Create your views here.

def filterView(request):
    # book_contains = request.GET.get('book_contains')
    # print(book_contains)
    
    qset = Ebook.objects.all()
    book_contains_query = request.GET.get('book_contains')
    if book_contains_query != '' and book_contains_query is not None:
        qset = qset.filter(book__icontains=book_contains_query)
    
    context = {
        'queryset': qset
    }
    
    return render(request, 'search.html', context)