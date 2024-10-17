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
            'Price': car.price,
            # добавьте другие характеристики автомобиля здесь
        },
        'estimated_price': '---',  # это можно заменить реальной логикой оценки
    }
    return render(request, 'evaluate/car_detail.html', context)
