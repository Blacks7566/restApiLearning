from rest_framework import serializers
from api.models import Employee


class EmployeeSerializer(serializers.Serializer):
    employee_name = serializers.CharField(max_length=100)
    employee_roll = serializers.CharField(max_length=100)
    employee_age = serializers.IntegerField()
    employee_salary = serializers.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)