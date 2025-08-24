# restaurant_portal/core/forms.py

from django import forms
from .models import MenuItem, Order

class MenuItemForm(forms.ModelForm):
    """
    Form for adding and editing menu items.
    """
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'is_available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Item Name'}),
            'description': forms.Textarea(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'rows': 3, 'placeholder': 'Item Description'}),
            'price': forms.NumberInput(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Price'}),
        }

class OrderStatusUpdateForm(forms.ModelForm):
    """
    Form for updating an order's status.
    """
    class Meta:
        model = Order
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'}),
        }
        labels = {
            'status': 'Update Status',
        }

class OrderCreateForm(forms.ModelForm):
    """
    Form for creating a new Order.
    """
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_phone', 'notes']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Customer Name'}),
            'customer_phone': forms.TextInput(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Phone Number (optional)'}),
            'notes': forms.Textarea(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'rows': 3, 'placeholder': 'Any special requests or notes'}),
        }
        labels = {
            'customer_name': 'Customer Name',
            'customer_phone': 'Phone Number',
            'notes': 'Notes',
        }

class CheckoutForm(forms.ModelForm):
    """
    Form for customer checkout.
    """
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_phone']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Your Name'}),
            'customer_phone': forms.TextInput(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Your Phone Number'}),
        }
        labels = {
            'customer_name': 'Your Name',
            'customer_phone': 'Your Phone Number',
        }
from django import forms
from .models import MenuItem, Order

class MenuItemForm(forms.ModelForm):
    """
    Form for adding and editing menu items.
    """
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'is_available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Item Name'}),
            'description': forms.Textarea(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'rows': 3, 'placeholder': 'Item Description'}),
            'price': forms.NumberInput(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Price'}),
        }

class OrderStatusUpdateForm(forms.ModelForm):
    """
    Form for updating an order's status.
    """
    class Meta:
        model = Order
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'}),
        }
        labels = {
            'status': 'Update Status',
        }

class OrderCreateForm(forms.ModelForm):
    """
    Form for creating a new Order.
    """
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_phone', 'notes']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Customer Name'}),
            'customer_phone': forms.TextInput(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Phone Number (optional)'}),
            'notes': forms.Textarea(attrs={'class': 'shadow-sm appearance-none border rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'rows': 3, 'placeholder': 'Any special requests or notes'}),
        }
        labels = {
            'customer_name': 'Customer Name',
            'customer_phone': 'Phone Number',
            'notes': 'Notes',
        }

class CustomerDetailsForm(forms.Form):
    """
    A simple form to capture customer details for an order.
    """
    customer_name = forms.CharField(label='Your Name', max_length=100)
    phone_number = forms.CharField(label='Phone Number', max_length=20)