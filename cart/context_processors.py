from .models import Cart, CartItem
from .views import _cart_id

def cart_count(request):
    book_count = 0
    if 'admin' in request.path: # if admin is logged in
        return {}               # return emplty dictionary
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                book_count += cart_item.qty
        except Cart.DoesNotExist:
            book_count = 0
    return {
        'book_count': book_count
    }