from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import BikeSerializer
from api.models import Bike
# Create your views here.


class BikeApi(APIView):

    def get(self,request,format=None):
        id = request.data.get('id')
        if id is not None:
            bt = Bike.objects.get(id=id)
            serializer = BikeSerializer(bt)
            return Response(serializer.data)
        bt = Bike.objects.all()
        serializer = BikeSerializer(bt,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = BikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete object update successfully..!'})
        return Response(serializer.errors)    

    def put(self,request,format=None):
        id = request.data.get('id')
        bt = Bike.objects.get(id=id)
        serializer = BikeSerializer(bt,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial Object update successfully..!'})
        return Response(serializer.errors)

    def patch(self,request,format=None):
        id = request.data.get('id')
        bt = Bike.objects.get(id=id)
        serializer = BikeSerializer(bt,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Object created successfully..!'})
        return Response(serializer.errors)

    def delete(self,request,format=None):
        id = request.data.get('id')
        bt = Bike.objects.get(id=id)
        bt.delete()
        return Response({'msg':'Object deleted successfully..!'})
