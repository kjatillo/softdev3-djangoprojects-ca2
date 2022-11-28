from django.shortcuts import render, get_object_or_404
from .models import Genre, Product
# Create your views here.

def product_view(request, genre_id=None):
    genre = None
    products = Product.objects.filter(available=True)
    if genre_id:
        genre = get_object_or_404(Genre, id=genre_id)
        products = Product.objects.filter(genre=genre, available=True)
    return render(request, 'store/genre.html', {
        'genre': genre,
        'prods': products
    })

def product_detail(request, genre_id, product_id):
    product = get_object_or_404(Product, genre_id=genre_id, id=product_id)
    return render(request, 'shop/product.html', {'product':product})