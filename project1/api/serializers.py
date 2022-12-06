from rest_framework import serializers




class StudentSerilizer(serializers.Serializer):

    name = serializers.CharField(max_length=20)
    stu_class = serializers.CharField(max_length=20)
    age = serializers.CharField(max_length=20)
    roll_number = serializers.IntegerField()

