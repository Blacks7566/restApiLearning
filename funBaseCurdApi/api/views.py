from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import EmployeeSerializer
from api.models import Employee
from rest_framework import status

# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def empApi(request):

    if request.method == 'GET':

        id = request.data.get('id')
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data
        serializer = EmployeeSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg':'Object created successfuly..!'},status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors)
        
    if request.method == 'PUT':
        id = request.data.get('id')
        emp = Employee.objects.get(id = id)
        serializer = EmployeeSerializer(emp,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Object Complete Update successfuly..!'})
        
        return Response(serializer.errors)

    if request.method == 'PATCH':
        id = request.data.get('id')
        emp = Employee.objects.get(id = id)
        serializer = EmployeeSerializer(emp,data=request.data,partial =True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Object Partial Update successfuly..!'})
        
        return Response(serializer.errors)

    if request.method == 'DELETE':
        data = request.data.get('id')
        emp = Employee.objects.get(id=data)
        emp.delete()
        return Response({'msg':'Object deleted successfuly..!'})


