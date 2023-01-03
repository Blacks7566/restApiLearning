from rest_framework import serializers

from api.models import Sudent

class StudentSeializer(serializers.ModelSerializer):
    class Meta:
        model = Sudent
        fields = '__all__'