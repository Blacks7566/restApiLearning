
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuApi/', views.stu_data),
    path('stuApi/<int:pk>', views.stu_data_id),
    path('stucreate/', views.stu_data_create),
]
