from django.urls import path
from . import views

urlpatterns = [
    path('', views.filterView, name='filter_search'),
]
