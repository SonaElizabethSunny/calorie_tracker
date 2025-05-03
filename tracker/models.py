from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Food Item Model
from django.db import models

from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories_per_gram = models.FloatField()  # assuming calories per gram
    def __str__(self):
        return self.name


# Food Log Model
class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.FloatField()
    date = models.DateField(default=now)
    def __str__(self):
        return f"{self.user.username} ate {self.quantity}g of {self.food_item.name} on {self.date}"

# Daily Summary Model
class DailySummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total_calories = models.FloatField()

    def __str__(self):
        return f"Summary for {self.user.username} on {self.date}"
