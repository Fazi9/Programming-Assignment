from django.db import models
from django.utils import timezone

class MenuItem(models.Model):
        """
        Represents a single item on the restaurant's menu.
        """
        name = models.CharField(max_length=200, unique=True, help_text="Name of the menu item (e.g., 'Cheeseburger')")
        description = models.TextField(blank=True, help_text="Short description of the item")
        price = models.DecimalField(max_digits=6, decimal_places=2, help_text="Price of the item (e.g., 12.99)")
        is_available = models.BooleanField(default=True, help_text="Is this item currently available for order?")
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
            ordering = ['name'] # Order menu items alphabetically by name

        def __str__(self):
            return self.name

class Order(models.Model):
        """
        Represents a customer's pickup order.
        """
        STATUS_CHOICES = [
            ('pending', 'Pending'),
            ('preparing', 'Preparing'),
            ('ready', 'Ready for Pickup'),
            ('picked_up', 'Picked Up'),
            ('cancelled', 'Cancelled'),
        ]

        customer_name = models.CharField(max_length=200, help_text="Name of the customer placing the order")
        customer_phone = models.CharField(max_length=20, blank=True, null=True, help_text="Customer's phone number for contact")
        order_time = models.DateTimeField(default=timezone.now, help_text="When the order was placed")
        pickup_time = models.DateTimeField(blank=True, null=True, help_text="Estimated or actual pickup time")
        status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', help_text="Current status of the order")
        total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, help_text="Total price of the order")
        notes = models.TextField(blank=True, help_text="Any special notes or requests for the order")
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
            ordering = ['-order_time'] # Order orders by most recent first

        def __str__(self):
            return f"Order #{self.id} for {self.customer_name} ({self.status})"

class OrderItem(models.Model):
        """
        Represents a single item within an order.
        Links to MenuItem and specifies quantity.
        """
        order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', help_text="The order this item belongs to")
        menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT, help_text="The menu item ordered")
        quantity = models.PositiveIntegerField(default=1, help_text="Quantity of the menu item")
        price_at_order = models.DecimalField(max_digits=6, decimal_places=2, help_text="Price of the item when the order was placed")

        def __str__(self):
            return f"{self.quantity} x {self.menu_item.name} in Order #{self.order.id}"

        class Meta:
            unique_together = ('order', 'menu_item') # A specific menu item can only appear once per order