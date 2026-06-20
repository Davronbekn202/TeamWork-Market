from django import forms
from ..models.addresses import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'user',
            'full_name',
            'phone',
            'country',
            'city',
            'address',
            'zip_code',
        ]

