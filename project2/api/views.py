from django.shortcuts import render

from django.http import HttpResponse , JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.serializers import StudentSerializer
from api.models import Student
import io

from django.views.decorators.csrf import csrf_exempt
# Create your views here

@csrf_exempt
def student_create(request):

    if request.method == "POST":

        json_data = request.body

        stream = io.BytesIO(json_data)
        python_navtive_data = JSONParser().parse(stream)

        serializer = StudentSerializer(data = python_navtive_data)
        if serializer.is_valid():
            
            serializer.save()

            resp = {'msg':'data created'}
            # j_data = JSONRenderer().render(resp)


            return JsonResponse(resp)

        return JSONRenderer().render(serializer.errors) 





        

