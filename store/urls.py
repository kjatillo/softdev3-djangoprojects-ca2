from django.urls import path
from . import views

# ---------------------------------
app_name = 'store'
# ---------------------------------

urlpatterns = [
    path('', views.book_view, name='all_books'),
    path('<uuid:genre_id>/', views.book_view, name = 'books_by_genre'),
    path('<uuid:genre_id>/<uuid:book_id>', views.book_detail, name = 'book_detail'),
    path('new/', views.BookCreateView.as_view(), name='book_create'),
]
