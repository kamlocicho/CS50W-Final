from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='products', blank=True)

    def __str__(self) -> str:
        return self.title


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class User(AbstractUser):
    watchlist = models.ManyToManyField(to=Product)
    cart = models.ManyToManyField(to=CartItem)
    total = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.username
