from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ClassesSerializers
from .models import Classes
from django.db.models import Q
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_class(request):
    # it might work
    request.data['teacher'] = request.user
    serializer = ClassesSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_class(request):
    to_update = Classes.objects.get(
        pk=request.data.pk, teacher=request.user)
    serializer = ClassesSerializers(instance=to_update, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def class_list(request):
    print(request)
    classes = Classes.objects.filter(Q(students=request.user) | Q(
        teacher=request.user)).order_by().distinct()

    serializer = ClassesSerializers(instance=classes, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_class(request):
    try:
        delete_class = Classes.objects.get(
            pk=request.data.pk, teacher=request.user)
        delete_class.delete()
        return Response({'status': "Deleting Sucsess"})
    except Classes.DoesNotExist:
        return Response(status=404)
