from rest_framework.permissions import IsAuthenticated
from .serializers import ClassesSerializers
from .models import Classes
from rest_framework import generics, status
from backend.classes.models import Invites, SheduleTime
from backend.classes.serializers import ClassesSheduleTimeSerializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from django.http import HttpRequest, HttpResponse
from django.db.models import Q
from itertools import chain


@api_view(['GET'])
@parser_classes([IsAuthenticated])
def join(request):
    # TODO response the reasone
    if 'v' not in request.query_params:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    code = request.query_params['v']
    try:
        class_item = Invites.objects.get(id=code).classes
    except Invites.DoesNotExist:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    if request.user == class_item.teacher:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    if request.user not in class_item.students.all():
        class_item.students.add(request.user)
        return Response({}, status=status.HTTP_202_ACCEPTED)
    return Response({}, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET'])
@parser_classes([IsAuthenticated])
def inviteLinks(request):
    # TODO response the reasone
    if 'c' not in request.query_params:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    clsId = request.query_params['c']
    try:
        invite = Invites.objects.get(classes__teacher=request.user,
                                     classes__id=clsId)
        return Response({"invite_id": invite.id})
    except Invites.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ClassesAPIView(generics.ListCreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # TODO: filter is teacher or student of class
        user = self.request.user
        queryset = Classes.objects.filter(Q(students=user) | Q(
            teacher=user)).order_by().distinct()
        return queryset

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
