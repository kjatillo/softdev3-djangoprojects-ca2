from django.contrib import admin
from .models import Genre, Product

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Genre, GenreAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'genre', 'available', 'created', 'updated']
    list_editable = ['price', 'available']
    list_per_page = 15
admin.site.register(Product, ProductAdmin)