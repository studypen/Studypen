from .models import Classes
from rest_framework import serializers
from backend.user.serializers import UserSerializer


class ClassesSerializers(serializers.ModelSerializer):
    # I will optimize it in next life😅😅
    students = UserSerializer(many=True, read_only=True)
    teacher = UserSerializer(read_only=True)

    class Meta:
        model = Classes
        fields = ['id', 'name', 'code', 'teacher', 'students']
