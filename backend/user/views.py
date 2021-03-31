import json

from backend.user.serializers import UserSerializer, UserUpdateSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .utils import IsNotAuthenticated


class RegisterView(generics.CreateAPIView):
    """
    Creat new user
    """
    queryset = User.objects.all()
    permission_classes = (IsNotAuthenticated,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)


class UpdateView(generics.UpdateAPIView):
    """
    Creat new user
    """
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserUpdateSerializer

    def update(self, request, *args, **kwargs):

        serializer = self.serializer_class(
            instance=request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'success'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def uesr_view(request):
    return Response({
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "username": request.user.username,
        "email": request.user.email,
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'logout': 'success'})


@api_view(['POST'])
@permission_classes([IsNotAuthenticated])
def login_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    if username is None or password is None:
        return JsonResponse({
            "errors": {
                "__all__": "Please enter both username and password"
            }
        }, status=400)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "email": user.email,
        })
    return JsonResponse(
        {"detail": "Invalid credentials"},
        status=400,
    )
