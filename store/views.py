from django.shortcuts import render, get_object_or_404
from .models import Genre, Ebook
# Create your views here.

def book_view(request, genre_id=None):
    genre = None
    books = Ebook.objects.filter(available=True)
    if genre_id:
        genre = get_object_or_404(Genre, id=genre_id)
        books = Ebook.objects.filter(genre=genre, available=True)
    return render(request, 'store/genre.html', {
        'genre': genre,
        'ebooks': books
    })

def book_detail(request, genre_id, book_id):
    book = get_object_or_404(Ebook, genre_id=genre_id, id=book_id)
    return render(request, 'store/book.html', {'book':book})