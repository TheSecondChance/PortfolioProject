from django.db import models


class Category(models.Model):
    
    name = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='furniture', null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    describtion = models.TextField()
    
    def __str__(self):
        return self.name