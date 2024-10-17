from django.shortcuts import render, get_object_or_404
from .models import TodoItem, Cars
import random

def evaluate_car(request):
    car_characteristics = {
        'Make': 'Toyota',
        'Model': 'Camry',
        'Year': '2020',
        'Mileage': '15,000 miles',
        'Color': 'White'
    }
    estimated_price = ''
    if request.method == 'POST':
        estimated_price = f"${random.randint(5000, 30000)}"
    return render(request, 'evaluate/evaluate_car.html', {
        'car_characteristics': car_characteristics,
        'estimated_price': estimated_price
    })

def database(request):
    cars = Cars.objects.all()
    return render(request, 'evaluate/database.html',  {'cars': cars})

def about(request):
    return render(request, 'evaluate/about.html')

def car_detail(request, pk):
    car = get_object_or_404(Cars, pk=pk)
    context = {
        'car': car,
        'car_characteristics': {
            'Title': car.title,
            'Car Name': car.car_name,
            'Color': car.color,
            'mileage': car.mileage,
            'описание':car.short_description,
            'Price': car.price,
            # добавьте другие характеристики автомобиля здесь
        },
        'estimated_price': '---',  # это можно заменить реальной логикой оценки
    }
    return render(request, 'evaluate/car_detail.html', context)

def market_changes(request):
    # Пример значимых изменений. Вы можете заменить это реальными данными.
    changes = [
        "Market saw a 5% increase in used car sales.",
        "Electric vehicle adoption rates have doubled.",
        "New car prices have risen by 3% due to supply chain issues.",
        "The introduction of new safety regulations.",
        "Significant investment in autonomous driving technology."
    ]

    context = {
        'changes': changes,
    }

    return render(request, 'evaluate/market_changes.html', context)
