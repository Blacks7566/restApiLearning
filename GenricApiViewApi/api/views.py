from api.serilaizers import EmployeeSerializer
from api.models import Employee
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin


class EmployeeApiLC(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
        
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)



class EmployeeApiRUD(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)

        
    