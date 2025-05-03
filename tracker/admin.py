from django.contrib import admin
from .models import FoodItem, FoodLog, DailySummary

admin.site.register(FoodItem)
admin.site.register(FoodLog)
admin.site.register(DailySummary)

