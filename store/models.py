from django.db import models
import uuid
from django.urls import reverse

# Create your models here.
    
class Genre(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/genre', blank=True)  # ImageField from Pillow


    class Meta:
        ordering = ('name',) # sort results by name field ascending when quering database
    
    def get_absolute_url(self):
        return reverse('store:books_by_genre', args=[self.id])
    
    def __str__(self):
        return self.name

class Ebook(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=100, default=None)
    description = models.TextField(blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=15) # international standard isbn max_digit=15
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/book', blank=True)
    available = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        ordering = ('name',)   
         
    def get_absolute_url(self):
        return reverse('store:book_detail', args=[self.genre.id, self.id])
    
    def __str__(self):
        return self.name
