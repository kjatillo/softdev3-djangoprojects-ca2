from django.contrib import admin
from .models import Genre

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Genre, GenreAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display['name', 'price', 'description', 'category', 'stock', 
    'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 15
admin.site.register(Product, ProductAdmins)