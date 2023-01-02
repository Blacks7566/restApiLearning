from rest_framework import serializers

from api.models import Sudent

class StudentSeializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'