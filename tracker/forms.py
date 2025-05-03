from django.core.exceptions import ValidationError
from django import forms
from .models import FoodLog

class FoodLogForm(forms.ModelForm):
    class Meta:
        model = FoodLog
        fields = ['food_item', 'quantity']
        labels = {
            'food_item': 'Select Food Item',
            'quantity': 'Enter Quantity (in grams)',
        }
        widgets = {
            'food_item': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 100'}),
        }