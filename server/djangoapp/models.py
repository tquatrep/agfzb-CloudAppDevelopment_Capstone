from django.db import models
from django.utils.timezone import now


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class CarModel(models.Model):
    COLOR_CHOICES = (
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'WAGON'),
    )
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dealer_id = models.IntegerField()
    car_type = models.CharField(max_length=50, choices=COLOR_CHOICES)
    year = models.DateField()

    def __str__(self):
        return "Name: "+self.name+"\n"+"Type: "+self.car_type+"\n"+"Year: "+str(self.year)+"\n"

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data