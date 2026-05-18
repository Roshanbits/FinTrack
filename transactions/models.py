from django.db import models

# Create your models here.
class Transaction(models.Model):
    customer_name = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.customer_name
    
