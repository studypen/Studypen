from rest_framework.permissions import IsAuthenticated
from .serializers import ClassesSerializers
from .models import Classes
from rest_framework import generics, status
from backend.classes.models import SheduleTime
from backend.classes.serializers import ClassesSheduleTimeSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpRequest, HttpResponse


class ClassesAPIView(generics.ListCreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class SheduleTimeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: HttpRequest) -> HttpResponse:
        if 'class' not in request.query_params:
            return Response({"detail": "class id not provided"},
                            status=status.HTTP_400_BAD_REQUEST)

        class_id = request.query_params['class']
        # TODO: check if the student or teacher acsses the classShedule
        try:
            classes = Classes.objects.get(id=class_id)
        except Classes.DoesNotExist:
            return Response({"detail": "Class does not exist"},
                            status=status.HTTP_404_NOT_FOUND)
        sheduleTime = SheduleTime.objects.filter(classes=classes)
        serializer = ClassesSheduleTimeSerializers(sheduleTime, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassesSheduleTimeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
