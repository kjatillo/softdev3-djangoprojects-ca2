from django.db import models
import uuid
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name=models.CharField(unique=True, max_length=250)
    image = models.ImageField(upload_to = 'genre', blank=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ('name',)
        
    def get_absolute_url(self):
        return reverse("store:products_by_genre", args=[self.id])
    
    def __str__(self):
        return self.name
    
    
    class Product(models.Model):
        id = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False) # ebook id
        name = models.CharField(unique=True, max_length=250) # ebook name
        description = models.TextField(blank=True)
        genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
        price = models.DecimalField(max_digits=8, decimal_places=2)
        image = models.imageField(upload_to = 'product', blank = True)
        stock = model.IntegerField()
        created = models.DateField(auto_now_add=True, blank = True, null= True)
        updated = models.DateField(auto_now=True, blank = True, null= True)
        
        class Meta:
            verbose_name = 'Book'
            verbose_name_plural = 'Books'
            ordering = ('name',)
            
        def get_absolute_url(self):
            return reverse('shore:product_detail', args=[self.genre.id, self.id])
        
        def __str__(self):
            return self.name