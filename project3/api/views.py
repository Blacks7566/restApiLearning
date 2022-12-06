import io
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from api.serializers import StudentSerializer
from api.models import Student
# Create your views here.

@csrf_exempt  # bypass the csrf token 
def stuApi(request,pk=None):

    if request.method == 'POST':

        json_data = request.body # store request body into a variable
        stream = io.BytesIO(json_data) # convert into in stream data
        python_data = JSONParser().parse(stream) # parse stream into python native data
        serializer = StudentSerializer(data = python_data) # pass data into serizlizer

        if serializer.is_valid(): # check data is valid or not

            serializer.save()
            response = {'msg':'object created successfully ...!'}
            return JsonResponse(response)

        return JsonResponse(serializer.errors)

    if request.method == 'GET':
        if pk is not None:
            data = Student.objects.get(id = pk)
            serializer = StudentSerializer(data) 
            json_data = JSONRenderer().render(serializer.data)

            return HttpResponse(json_data)
        
        data = Student.objects.all()
        serializer = StudentSerializer(data,many=True) 
        json_data = JSONRenderer().render(serializer.data)

        return HttpResponse(json_data)

    if request.method == 'PUT':

        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data  = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id =id)
        serializer = StudentSerializer(stu,data = python_data, partial = True)

        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Object updated successfully ..'}
            return JsonResponse(response)
        
        return JsonResponse(serializer.errors)

    if request.method == 'DELETE':

        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id')

        stu = Student.objects.get(id = id)
        stu.delete()

        response = {'msg':'Object is deleted successfully..!'}

        return JsonResponse(response)
    return JsonResponse(serializer.errors)










    
    
    



