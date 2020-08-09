from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=100, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    smoking = models.BooleanField(null=True)
    childeren = models.BooleanField(null=True)
    color = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=True)
    seats = models.IntegerField(null=True)
    image = models.ImageField(upload_to='images/product/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits= 10, decimal_places=0)

    class Meta:
        ordering = ('create_time',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product', args=[self.id])

class Order(models.Model):
    costumer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    product_price = models.DecimalField(max_digits=10, decimal_places=0)
    product_count = models.PositiveIntegerField()
    order_cost = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return str(self.id)

class Invoice(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    invoice_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



