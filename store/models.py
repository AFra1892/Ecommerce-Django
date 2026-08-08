from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    brand = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    base_price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.CharField(max_length=100,blank=True)
    main_image = models.ImageField(upload_to='products/',blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# a Product has Many Variant
# AirForce 1 has variant Size and variant colors

class Variant(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='variants')
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    sku = models.CharField(max_length=50,unique=True)
    stock_count = models.PositiveIntegerField(default=0)
    price_override = models.DecimalField(max_digits=10, decimal_places=2 , blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product' , 'size' , 'color')  # prevents duplicate size/color rows for the same product


    def __str__(self):
        return f"{self.product.name} - {self.size} - {self.color} ({self.sku})"
        
