from django.db import models


class Order(models.Model):
    token = models.CharField(max_length=255, blank=True)
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Total Order'
    )
    emailAddress = models.EmailField(
        max_length=255,
        blank=True,
        verbose_name='Email Address'
    )
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'Order'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    ebook = models.CharField(max_length=255)
    isbn = models.CharField(max_length=15, unique=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Price'
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'OrderItem'
    
    def __str__(self):
        return self.ebook
