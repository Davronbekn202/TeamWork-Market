from django import forms
from models.sizes import Size, ProductSize


class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = [
            'name',
        ]


class ProductSizeForm(forms.ModelForm):
    class Meta:
        model = ProductSize
        fields = [
            'product',
            'size',
        ]
