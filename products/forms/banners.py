from django import forms
from ..models.banners import Banner


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = [
            'title',
            'subtitle',
            'image',
            'active',
        ]
