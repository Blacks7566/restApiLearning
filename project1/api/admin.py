from django.contrib import admin

# Register your models here.

from api.models import Student




@admin.register
class StudentAdmin(admin.ModelAdmin):

    list_display=['id','name','stu_class','age','roll_number']

