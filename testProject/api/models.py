from django.db import models

# Create your models here.

class Employee(models.Model):

    employee_name = models.CharField(max_length=100)
    employee_roll = models.CharField(max_length=100)
    employee_age = models.IntegerField()
    employee_salary = models.IntegerField()

    def __str__(self):
        return self.employee_name

