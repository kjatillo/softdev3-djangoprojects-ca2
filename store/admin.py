from django.contrib import admin
from .models import Genre, Ebook

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Genre, GenreAdmin)

class EbookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'date_added', 'updated']
    list_editable = ['price', 'available']
    list_per_page = 15
admin.site.register(Ebook, EbookAdmin)
