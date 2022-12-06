from rest_framework import serializers

from api.models import Student



class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    stu_class = serializers.CharField(max_length=100)
    age =  serializers.IntegerField()
    roll_no = serializers.IntegerField()


    def create(self,validate_data):

        return Student.objects.create(**validate_data)
