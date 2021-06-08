from backend.messages.serializers import ClassMessegeSerializers
from rest_framework.permissions import IsAuthenticated
from .models import ClassMessage, Classes
from rest_framework import generics
from django.db.models import Q


# Create your views here.


class ClassMessageAPIView(generics.ListCreateAPIView):
    serializer_class = ClassMessegeSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if 'c' not in self.request.query_params:
            raise "class id is requrie"
        clsId = self.request.query_params['c']
        cls = Classes.objects.filter(Q(students=user) or Q(
            teacher=user)).get(id=clsId)

        queryset = ClassMessage.objects.filter(
            classes=cls).order_by().distinct()
        return queryset

    def perform_create(self, serializer):
        serializer.save(msg__sender=self.request.user)
