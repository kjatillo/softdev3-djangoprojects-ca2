from django.urls import path
from .views import SearchResultsListView, filterView

app_name = 'search'

urlpatterns = [
    path('', SearchResultsListView.as_view(), name='search_result'),
    path('advance/', filterView, name='advance_search_result'),
]
