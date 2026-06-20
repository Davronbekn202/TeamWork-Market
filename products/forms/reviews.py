from django import forms
from ..models.reviews import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'product',
            'user',
            'rating',
            'comment',
        ]
