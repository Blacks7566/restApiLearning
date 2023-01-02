from django.contrib import admin

# Register your models here.

from api.models import Sudent

@admin.register(Sudent)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll']