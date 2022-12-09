from django.urls import path
from . import views

# -------------------------------
app_name = 'cart'
# -------------------------------

urlpatterns = [
    path('add/<uuid:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<uuid:book_id>/', views.cart_remove, name='cart_remove'),
    path('clear_cart/<uuid:book_id>/', views.clear_cart, name='clear_cart'),
]
