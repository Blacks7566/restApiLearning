import io
from django.shortcuts import render
from api.serializers import EmployeeSerializer
from api.models import Employee
from django.http import JsonResponse,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
def stu_data(request):

    data = Employee.objects.all()
    serializer = EmployeeSerializer(data,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')

def stu_data_id(request,pk):
    data = Employee.objects.get(id = pk)
    serializer = EmployeeSerializer(data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')

@csrf_exempt
def stu_data_create(request):

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg':'employee created successfully ..!'}
            return JsonResponse(response)

        return JsonResponse(serializer.errors)    















    