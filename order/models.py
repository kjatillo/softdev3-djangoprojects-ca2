from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from vouchers.models import Voucher


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

    voucher = models.ForeignKey(
        Voucher, 
        related_name='orders', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL
    )
    discount = models.IntegerField(
        default=0, 
        validators=[
            MinValueValidator(0), 
            MaxValueValidator(100)
        ]
    )

    class Meta:
        db_table = 'Order'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    ebook = models.CharField(max_length=255)
    isbn = models.CharField(max_length=15)
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
