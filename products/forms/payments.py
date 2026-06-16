from django import forms
from models.payments import Payment


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'order',
            'paid',
            'transaction_id',
        ]