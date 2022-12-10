from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from store.models import Ebook
from .models import Cart, CartItem
from django.conf import settings
from order.models import Order, OrderItem
import stripe
# Voucher
from vouchers.models import Voucher
from vouchers.forms import VoucherApplyForm
from decimal import Decimal


# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_to_cart(request, book_id):
    book = Ebook.objects.get(id=book_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(book=book, cart=cart)
        cart_item.qty += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(book=book, cart=cart, qty=1)
        cart_item.save()
    return redirect('cart:cart_detail')
# query the cart for all the cart items & calculate the total amount for each cart item


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(
            request))  # get the session key
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.book.price * cart_item.qty)
            counter += cart_item.qty
    except ObjectDoesNotExist:
        pass
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total*100)
    description = ' Ebook Store - New Order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY

    if request.method == 'POST':
        print(request.POST)
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            # billingName = request.POST['stripeBillingName']

            customer = stripe.Customer.create(email=email, source=token)
            stripe.Charge.create(amount=stripe_total, currency="eur",
                                 description=description, customer=customer.id)

            # Creating the order
            try:
                order_details = Order.objects.create(
                    token=token,
                    total=total,
                    emailAddress=email,
                    # billingName=billingName
                )
                order_details.save()

                for order_item in cart_items:
                    ord_it = OrderItem.objects.create(
                        ebook=order_item.book.name,
                        # qty=order_item.book.qty,
                        price=order_item.book.price,
                        order=order_details
                    )
                    ord_it.save()
                    # remove item from cart after order is placed
                    cart_remove(request, order_item.book_id)
                    print('The order has been created')

                # redirect to thank you page
                return redirect('order:thank_you', order_details.id)

            except ObjectDoesNotExist:
                pass

        except stripe.error.CardError as stripeError:
            return stripeError
    # return context variables
    return render(request,
                  'cart.html',
                  {
                      'cart_items': cart_items,
                      'total': total,
                      'counter': counter,
                      'data_key': data_key,
                      'stripe_total': stripe_total,
                      'description': description
                  }
                  )
    # voucher
    discount = 0
    voucher_id = 0
    new_total = 0
    voucher = None



def cart_remove(request, book_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    book = get_object_or_404(Ebook, id=book_id)
    cart_item = CartItem.objects.get(book=book, cart=cart)
    if cart_item.qty > 1:
        cart_item.qty -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')


def clear_cart(request, book_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    book = get_object_or_404(Ebook, id=book_id)
    cart_item = CartItem.objects.get(book=book, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')
