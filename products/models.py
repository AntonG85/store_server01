from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='Products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    slug = models.CharField(max_length=256)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'