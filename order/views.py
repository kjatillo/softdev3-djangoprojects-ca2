from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from .models import Order, OrderItem


class OrderHistory(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            email = str(request.user.email)
            order_details = Order.objects.filter(emailAddress=email)

        return render(
            request,
            'order/order_history.html',
            {'order_details': order_details}
        )


class OrderDetail(LoginRequiredMixin, View):
    def get(self, request, order_id):
        if request.user.is_authenticated:
            email = str(request.user.email)
            order = Order.objects.get(id=order_id, emailAddress=email)
            order_items = OrderItem.objects.filter(order=order)
        
        return render(
            request,
            'order/order_detail.html',
            {
                'order': order,
                'order_items': order_items
            }
        )


def thank_you(request, order_id):
    if order_id:
        customer_order = get_object_or_404(
            Order, 
            id=order_id,
        )
    
    
    return render(
        request,
        'thank_you.html',
        {
            'customer_order': customer_order
        }
    )
