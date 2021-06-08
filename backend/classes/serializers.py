from .models import Classes
from rest_framework import serializers
from backend.user.serializers import UserSerializer
from backend.classes.models import Invites, SheduleTime


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

    def create(self, validated_data):
        c = super().create(validated_data)
        invite = Invites.objects.create(classes=c)
        invite.save()
        # TODO: return the invite link as response
        return c


class ClassesSheduleTimeSerializers(serializers.ModelSerializer):
    # I will optimize it in next life😅😅
    # students = UserSerializer(many=True, read_only=True)

    class Meta:
        model = SheduleTime
        fields = ['id', 'classes', 'day_of_week', 'start_time', 'end_time']
