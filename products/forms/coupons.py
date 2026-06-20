from django import forms
from ..models.coupons import Coupon


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = [
            'code',
            'discount',
            'active',
        ]
