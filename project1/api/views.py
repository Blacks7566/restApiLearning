from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from api.models import Student
from api.serializers import StudentSerilizer

from rest_framework.renderers import JSONRenderer

# Create your views here.





# def student_details(request):

#     st = Student.objects.get(id = 1)
#     print("-------------> ",st)
#     serializer = StudentSerilizer(st)
#     print("-------------> ",serializer.data)

#     json_data = JSONRenderer().render(serializer.data)
#     print("-------------> ",json_data)
     
#     return HttpResponse(json_data , content_type = 'application/json')




#-----------------------------------------    

def student_details(request,pid):

    st = Student.objects.get(id = pid)
    serializer = StudentSerilizer(st)
    # json_data = JSONRenderer().render(serializer.data)     
    # return HttpResponse(json_data , content_type = 'application/json')

    return JsonResponse(serializer.data)


def student_list(request):

    st = Student.objects.all()
    serializer = StudentSerilizer(st, many=True)
    json_data = JSONRenderer().render(serializer.data)
     
    return HttpResponse(json_data , content_type = 'application/json')








