from django.db import models

# Create your models here.
class Bike(models.Model):

    bike_name = models.CharField(max_length=100)
    bike_model = models.CharField(max_length=100)
    bike_cc = models.IntegerField()
    bike_average = models.IntegerField()
    def __str__(self):
        return self.bike_name