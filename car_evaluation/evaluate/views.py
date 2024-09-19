from django.shortcuts import render
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
