from django import forms
from models.colors import Color, ProductColor


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = [
            'name',
            'code',
        ]


class ProductColorForm(forms.ModelForm):
    class Meta:
        model = ProductColor
        fields = [
            'product',
            'color',
        ]
