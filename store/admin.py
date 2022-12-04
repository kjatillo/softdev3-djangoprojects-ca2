from django.contrib import admin
from .models import Genre, Ebook
from django.db import models
from django.forms import TextInput, Textarea

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Genre, GenreAdmin)

class EbookAdmin(admin.ModelAdmin):
    # modify display fields to a certain size.
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':80})},
    }
    
    list_display = ['name', 'price', 'description', 'available', 'date_added', 'updated']
    list_editable = ['price', 'available']
    list_per_page = 15
admin.site.register(Ebook, EbookAdmin)