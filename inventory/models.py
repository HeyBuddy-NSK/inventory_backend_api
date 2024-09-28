from django.db import models

# Create your models here.
class Item(models.Model):
    """
    Item model.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    item_id = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
