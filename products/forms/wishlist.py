from django import forms
from models.wishlist import Wishlist


class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = [
            'user',
            'product',
        ]
