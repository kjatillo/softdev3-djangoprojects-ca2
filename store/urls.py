from django.urls import path
from . import views

# ---------------------------------
app_name = 'store'
# ---------------------------------

urlpatterns = [
    path('', views.product_view, name='all_products'),
    path('<uuid:genre_id>/', views.product_view, name = 'products_by_genre'),
    path('<uuid:genre_id>/<uuid:product_id>', views.product_detail, name = 'product_detail'),
]
