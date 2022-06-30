from django.contrib import admin

from ecommerce.models import Category, Product, User

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(User)