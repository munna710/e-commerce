from django.db import models

# Create your models here.
from orders.models import Order

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Completed'),
        (2, 'Failed'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    amount = models.FloatField()
    status = models.IntegerField(choices=PAYMENT_STATUS_CHOICES, default=0)
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_method = models.CharField(max_length=50)
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.transaction_id} for Order {self.order.id}"