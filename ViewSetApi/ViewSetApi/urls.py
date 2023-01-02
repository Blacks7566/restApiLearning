"""ViewSetApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken.views import obtain_auth_token
# for coustom authenticate token

from api.auth import CustomAuthToken


router = DefaultRouter()

router.register('studentApi',views.StudentViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')), # adding for session authention login
    # path('gettoken/', obtain_auth_token), # for generate token
    path('gettoken/', CustomAuthToken.as_view()), # for generate token coustom
]


# and we have to install httpie 
# run server and 
# on  auother terminal  run this commad
# http POST http://127.0.0.1:8000/gettoken/ username='admin' password='admin'