from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class BasketItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  

    def subtotal(self):
        return self.product.price * self.quantity

class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(BasketItem)

    def total_price(self):
        return sum(item.subtotal() for item in self.items.all())