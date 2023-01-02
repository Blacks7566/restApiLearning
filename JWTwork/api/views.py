from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from api.models import Sudent
from api.serializers import StudentSeializer
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated
# Create your views here.



# Simple JWT

# simple jwt provides a json web Token authentication backend for the 
# Django Rest Framework It aims to cover the most common use 
# cases of jwt by offering a conservative set of default features it 
# also aims to be easily extensible in case a desired feature in not present


# we have to install jwt 


# pip install djangorestframework-simplejwt


# Get Token

# http POST http://127.0.0.1:8000/ username='name' password="password"

# its return token and refresh token

class StudentApi(ModelViewSet):
    queryset = Sudent.objects.all()
    serializer_class = StudentSeializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]









{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyNjU4MTA1LCJpYXQiOjE2NzI2NTc4MDUsImp0aSI6IjNjM2E0YTdkZDYxZjQ0YjY5ZGU3YzFjZjM5OWY3NTBhIiwidXNlcl9pZCI6Mn0.Jcbgbur628htBbaw1dh1yVgg90x3KR06xgMYQJX-5Hc",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3Mjc0NDIwNSwiaWF0IjoxNjcyNjU3ODA1LCJqdGkiOiI1ZTc2ZjI4YTEwYjc0ZDA1OTQwZmQ5OGU4NWEzYWMxNSIsInVzZXJfaWQiOjJ9.Md4L0ARhq-n5NF5zTvsZkZr8rUq0BzqLwlspDqMtyPQ"
}



# for create JWT Token 

# http POST http://127.0.0.1:8000/gettoken/ username="black" password="Nitin@7566"

{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyNjU5NDUwLCJpYXQiOjE2NzI2NTc4MDUsImp0aSI6ImRjMTkxZjI4YmQ1ZTQ5NGJhNGQ1NWI2NzM3YmI0MTA2IiwidXNlcl9pZCI6Mn0.b_zYNERYMu38oPUbk6bKkL2Sa50M-oEpU7wxfjusoAM"
}