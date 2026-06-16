from django.db import models
from .orders import Order


class Payment(models.Model):
    METHOD = (
        ('card', 'Card'),
        ('cash', 'Cash'),
        ('paypal', 'Paypal')
    )
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    method = models.CharField(max_length=20, choices=METHOD)
    paid = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.order, self.method, self.paid
