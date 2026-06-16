from django import forms
from models.brands import Brand


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = [
            'name',
            'logo',
        ]
