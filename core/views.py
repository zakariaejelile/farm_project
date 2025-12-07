from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import User
from farm.serializers import UserSerializer
from django.contrib.auth.hashers import make_password

class RegisterView(APIView):
    permission_classes = []

    def post(self, request):
        data = request.data
        if User.objects.filter(email=data.get('email')).exists():
            return Response({'error':'Email exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            password=make_password(data.get('password'))  # hash password
        )
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


