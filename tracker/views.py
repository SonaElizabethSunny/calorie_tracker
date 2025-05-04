from django.shortcuts import render, redirect
from .forms import FoodLogForm
from .models import FoodLog, FoodItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now


def home(request):
    food_items = FoodItem.objects.all()
    total_calories = 0
    selected_items = []

    if request.method == "POST":
        selected_ids = request.POST.getlist("food_items")
        selected_items = FoodItem.objects.filter(id__in=selected_ids)
        total_calories = sum(item.calories for item in selected_items)

    tips = ""
    if total_calories < 1500:
        tips = "Your intake is low. Consider adding more nutritious items."
    elif total_calories > 2500:
        tips = "High intake. Try balancing with some exercise."
    else:
        tips = "Great job! You're within a healthy range."

    context = {
        "food_items": food_items,
        "total_calories": total_calories,
        "selected_items": selected_items,
        "tips": tips,
    }
    return render(request, 'tracker/home.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def custom_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')


@login_required
def log_food(request):
    if request.method == 'POST':
        form = FoodLogForm(request.POST)
        if form.is_valid():
            food_log = form.save(commit=False)
            food_log.user = request.user
            food_log.save()
            return redirect('food_log_summary')
    else:
        form = FoodLogForm()

    # Pass food items to template to allow users to select foods
    food_items = FoodItem.objects.all()
    context = {
        'form': form,
        'food_items': food_items,
    }

    return render(request, 'tracker/log_food.html', context)


@login_required
def food_log_summary(request):
    today = now().date()
    food_logs = FoodLog.objects.filter(user=request.user, date=today)

    log_details = []
    total_calories = 0

    for log in food_logs:
        calories = log.quantity * log.food_item.calories_per_gram
        total_calories += calories
        log_details.append({
            'name': log.food_item.name,
            'quantity': log.quantity,
            'calories_per_gram': log.food_item.calories_per_gram,
            'calories': calories
        })

    return render(request, 'tracker/food_log_summary.html', {
        'log_details': log_details,
        'total_calories': total_calories
    })



