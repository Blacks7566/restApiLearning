from django.contrib import admin
from api.models import Employee
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','emp_name','emp_roll','emp_age','emp_salary']