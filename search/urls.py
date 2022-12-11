from django.urls import path
from .views import SearchResultsListView

app_name = 'search'

urlpatterns = [
    path('', SearchResultsListView.as_view(), name='search_result'),
]
