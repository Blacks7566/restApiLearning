import io
from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def studentApi(request,pk=None):

    if request.method == 'GET':

        if pk is not None:

            data = Student.objects.get(id = pk)
            serializer = StudentSerializer(data)
            data = JSONRenderer().render(serializer.data)
            return HttpResponse(data, content_type='application/json')
        
        data = Student.objects.all()
        serializer = StudentSerializer(data,many=True)
        data = JSONRenderer().render(serializer.data)
        return HttpResponse(data, content_type='application/json')
    
    if request.method == 'POST':

        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        
        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Object created successfully ... '}
            return JsonResponse(response)
        return JsonResponse(serializer.errors)
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data = python_data, partial = True)

        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Object updated successfully ... '}
            return JsonResponse(response)
        return JsonResponse(serializer.errors)

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        response = {'msg':'Object deleted successfully ... '}
        return JsonResponse(response)
