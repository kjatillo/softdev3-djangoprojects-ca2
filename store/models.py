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
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'genre', blank=True)  # ImageField from Pillow


    class Meta:
        ordering = ('name',) # sort results by name field ascending when quering database
        verbose_name = 'genre'
        verbose_name_plural = 'genres'
    
    def get_absolute_url(self):
        return reverse('shore:products_by_genre', args=[self.id])
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank = True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to = 'product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank = True, null= True)
    updated = models.DateTimeField(auto_now=True, blank = True, null= True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
    def get_absolute_url(self):
        return reverse('shore:product_detail', args=[self.genre.id, self.id])
    def __str__(self):
        return self.name