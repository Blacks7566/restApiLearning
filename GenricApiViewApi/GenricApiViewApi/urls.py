
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', views.EmployeeApiLC.as_view()),
    path('apis/<int:pk>/', views.EmployeeApiRUD.as_view()),
]
