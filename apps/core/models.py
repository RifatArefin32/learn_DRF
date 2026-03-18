from django.db import models

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')

    @property
    def is_in_stock(self):
        return self.stock > 0
    
    def __str__(self):
        return self.name