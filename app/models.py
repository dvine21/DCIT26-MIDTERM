from django.db import models
from django.urls import reverse


class Product(models.Model):
    ItemName = models.CharField(max_length=100)
    models.ForeignKey("auth.User", on_delete=models.CASCADE)
    Description = models.TextField()
    Price = models.CharField(max_length=100)
    Stock = models.PositiveIntegerField()

    def __str__(self):
        return self.ItemName

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk":self.pk})

class Order(models.Model):
    Status_choices = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    Status = models.CharField(max_length=20, choices=Status_choices, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f"{self.quantity} of {self.product.ItemName}"
    
class Shipping(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=100)
    carrier = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='in transit')
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Shipping for Order #{self.order.id}"