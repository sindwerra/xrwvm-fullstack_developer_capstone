# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return "Car name is {}".format(self.name)


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


class CarModel(models.Model):
    CAR_TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('wagon', 'Wagon'),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    tp = models.CharField(
        max_length=10, choices=CAR_TYPE_CHOICES, default="SUV"
    )
    year = models.IntegerField(
        default=2024,
        validators=[
            MaxValueValidator(2024),
            MinValueValidator(2015),
        ]
    )

    def __str__(self):
        return "Car make is {}, car model is {}".format(
            self.car_make.name,
            self.name,
        )
