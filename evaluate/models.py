from django.db import models
from django.urls import reverse

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


class Cars(models.Model):
    title = models.CharField(max_length=200)
    car_name = models.CharField(max_length=200)
    photo_url  = models.CharField(max_length=550)
    make = models.CharField(max_length=200, null=True)
    model = models.CharField(max_length=200, null=True)
    year = models.FloatField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)

    short_description = models.CharField(max_length=200, null=True)
    long_description = models.CharField(max_length=200, null=True)

    mileage = models.FloatField( null=True)
    price = models.FloatField( null=True)

    def get_absolute_url(self):
        return reverse('car_detail', args=[str(self.id)])

