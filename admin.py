from django.contrib import admin
from .models import MenuItem, Order, OrderItem

    # Register your models here to make them accessible in the Django admin interface.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
        list_display = ('name', 'price', 'is_available', 'created_at', 'updated_at')
        list_filter = ('is_available',)
        search_fields = ('name', 'description')
        ordering = ('name',)

class OrderItemInline(admin.TabularInline):
        """
        Allows OrderItems to be edited directly within the Order admin page.
        """
        model = OrderItem
        extra = 0 # Don't show extra blank forms by default
        raw_id_fields = ('menu_item',) # Use a raw ID input for menu_item for better performance with many items

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
        list_display = ('id', 'customer_name', 'customer_phone', 'order_time', 'pickup_time', 'status', 'total_price')
        list_filter = ('status', 'order_time', 'pickup_time')
        search_fields = ('customer_name', 'customer_phone', 'notes')
        date_hierarchy = 'order_time' # Adds a date navigation bar
        inlines = [OrderItemInline] # Include OrderItems directly in the Order form
        readonly_fields = ('total_price', 'created_at', 'updated_at') # These fields are calculated or auto-set

        def save_model(self, request, obj, form, change):
            """
            Override save_model to calculate total_price when an order is saved
            through the admin interface.
            """
            super().save_model(request, obj, form, change)
            # Recalculate total price after saving order and its items
            obj.total_price = sum(item.quantity * item.price_at_order for item in obj.items.all())
            obj.save(update_fields=['total_price'])

    # No need to register OrderItem separately as it's an inline for Order
    # admin.site.register(OrderItem)