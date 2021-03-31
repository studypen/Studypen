from .models import Classes
from rest_framework import serializers


class ClassesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'  # ['name', 'code', 'teacher', 'students']
