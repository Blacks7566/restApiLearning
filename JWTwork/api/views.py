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
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyNjYxNzg3LCJpYXQiOjE2NzI2NjE0ODcsImp0aSI6IjljZWFiY2Q5NzNhZDQ2ZDc4MGIzZTJjYmEzMGQyMDkwIiwidXNlcl9pZCI6Mn0.xvYF17jiFzw93dVk8GfwjwvBeSMrKIJvJkRkI9nhNng",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3Mjc0Nzg4NywiaWF0IjoxNjcyNjYxNDg3LCJqdGkiOiJiNTRjMWJjNmEwMjQ0MzA3OGYyOWYwODNkNTY4YzFmMCIsInVzZXJfaWQiOjJ9.5fZboIhcZYaPEG8SPT0k9bPpfjEjbChCI66TxVZAbG8"
}

# for create JWT Token 

# http POST http://127.0.0.1:8000/gettoken/ username="black" password="Nitin@7566"

{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyNjYxMzU4LCJpYXQiOjE2NzI2NTc4MDUsImp0aSI6IjhiYjU2MjkxYWE1ODQyNzNhZTIzYjc0MDM2NjNiMDQyIiwidXNlcl9pZCI6Mn0.sOYkMYAQBiohoZYtCvM1xXezV9KZRdExzOwPwFjV3HE"
}