from django.shortcuts import render

# Create your views here.
from api.serializers import StudentSerializer
from api.models import Student
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,AllowAny,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly




# # basic authentication api


# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer 
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]



# session Authentication api

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer 
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]


# token authentications api

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# in Httpei 

# # get 

# http htpp://127.0.0.1:8000 / studentapi/ 'Autherization:Token asljfsladfjla;sfjsjfl'