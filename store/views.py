from django.shortcuts import render, get_object_or_404
from .models import Genre, Ebook
# Create your views here.

def book_view(request, genre_id=None):
    genre = None
    books = Ebook.objects.filter(available=True)
    if genre_id:
        genre = get_object_or_404(Genre, id=genre_id)
        books = Ebook.objects.filter(genre=genre, available=True)
        
    # paginator = Paginator(products, 6)
    # try:
    #     page = int(request.GET.get('page', '1'))
    # except:
    #     page = 1
    # try:
    #     products = paginator.page(page)
    # except (EmptyPage, InvalidPage):
    #     products = paginator.page(paginator.num_pages)
        
    return render(request, 'store/genre.html', {
        'genre': genre,
        'ebooks': books
    })

def book_detail(request, genre_id, book_id):
    book = get_object_or_404(Ebook, genre_id=genre_id, id=book_id)
    return render(request, 'store/book.html', {'book':book})