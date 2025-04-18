from django.db import models

# Create your models here.
class Shop(models.Model):
    product_name = models.CharField(max_length=100)
    product_explain = models.TextField()
    product_price = models.DecimalField(max_digits=10,decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    
    def summary(self):
        return self.product_name[:100]