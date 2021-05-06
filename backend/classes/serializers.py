from .models import Classes
from rest_framework import serializers
from backend.user.serializers import UserSerializer
from backend.classes.models import SheduleTime


class ClassesSerializers(serializers.ModelSerializer):
    # I will optimize it in next life😅😅
    # students = UserSerializer(many=True, read_only=True)
    students = serializers.SerializerMethodField()
    teacher = UserSerializer(read_only=True)

    class Meta:
        model = Classes
        fields = ['id', 'name', 'code', 'teacher', 'students']

    def get_students(self, obj):
        return obj.students.count()


class ClassesSheduleTimeSerializers(serializers.ModelSerializer):
    # I will optimize it in next life😅😅
# students = UserSerializer(many=True, read_only=True)

    class Meta:
        model = SheduleTime
        fields = ['id', 'day_of_week', 'start_time', 'end_time']
