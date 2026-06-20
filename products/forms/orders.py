from django import forms
from ..models.orders import Order, OrderItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'user',
            'status',
            'total_price',
        ]


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = [
            'order',
            'product',
            'quantity',
            'price',
        ]
