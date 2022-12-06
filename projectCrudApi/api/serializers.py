from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    student_class = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    roll_no = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

        instance.name = validated_data.get('name',instance.name)
        instance.student_class = validated_data.get('student_class',instance.student_class)
        instance.age = validated_data.get('age',instance.age)
        instance.roll_no = validated_data.get('roll_no',instance.roll_no)
        instance.save()
        return instance