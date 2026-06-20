from django import forms
from ..models.cart import Cart, CartItem


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user']


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = [
            'cart',
            'product',
            'quantity',
        ]
