from django import forms
from ..models import Product, ProductImage


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'brand',
            'title',
            'slug',
            'description',
            'price',
            'discount_price',
            'stock',
            'is_featured',
        ]

        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 5
            }),
            'price': forms.NumberInput(attrs={
                'step': '0.01'
            }),
            'discount_price': forms.NumberInput(attrs={
                'step': '0.01'
            }),
        }


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
