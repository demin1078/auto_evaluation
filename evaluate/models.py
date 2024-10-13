from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


class Cars(models.Model):
    title = models.CharField(max_length=200)
    car_name = models.CharField(max_length=200)
    photo_url  = models.CharField(max_length=550)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    color = models.CharField(max_length=200)

    short_description = models.CharField(max_length=200)
    long_description = models.CharField(max_length=200)

    mileage = models.FloatField()
    price = models.FloatField()

