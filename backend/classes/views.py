from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ClassesSerializers
from .models import Classes
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_class(request):
    serializer = ClassesSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_class(request):
    to_update = Classes.objects.get(
        pk=request.data.pk)  # TODO is creator is user
    serializer = ClassesSerializers(instance=to_update, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def class_list(request):
    classes = Classes.objects.all()  # TODO joined or created only
    serializer = ClassesSerializers(instance=classes, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_class(request):
    try:
        delete_class = Classes.objects.get(
            pk=request.data.pk)  # TODO if creator is user
        delete_class.delete()
        return Response("Deleting Sucsess")
    except Classes.DoesNotExist:
        return Response(status=404)
