from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Book', {'fields': ['book'],}),
        ('ISBN', {'fields': ['isbn'],}),
        ('Price', {'fields': ['price'],}),
    ]
    readonly_fields = [
        'book',
        'isbn',
        'price'
    ]
    can_delete = False
    max_num = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'billingName',
        'emailAddress',
        'created'
    ]
    list_display_links = ('id', 'billingName')
    search_fields = [
        'id',
        'billingName',
        'emailAddress'
    ]
    readonly_fields = [
        'id',
        'token',
        'total',
        'emailAddress',
        'created',
        'billingName',
    ]
    fieldsets = [
        (
            'ORDER INFORMATION', {
                'fields': [
                    'id',
                    'token',
                    'total',
                    'created'
                ]
            }
        ),
        ('BILLING INFORMATION', {'fields': ['billingName']})
    ]

    inlines = [OrderItemAdmin]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Order, OrderAdmin)
