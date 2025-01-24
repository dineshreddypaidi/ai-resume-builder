from django.http import JsonResponse
from users import models as usermodels

from . import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib.auth import authenticate

class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = serializers.RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            
            return Response({
                "message": "User registered successfully.",
                'token': token.key,
                "user": {
                    "id" : user.id,
                    "username": user.username,
                    "email": user.email,
                    "name": user.name,
                    "contact_number": user.contact_number,
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_input = request.data.get('username')
        password = request.data.get('password')
        
        try:
            user_obj = usermodels.CustomUser.objects.filter(
                Q(email=user_input) |
                Q(username=user_input) |
                Q(phone_number=user_input)
            ).first()
        except usermodels.CustomUser.DoesNotExist:
            return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user = authenticate(username=user_obj.username, password=password)
    
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key
                },status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
class LogoutAPIView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)















































































def hello(request):
    d = {"hello" : "welcome"}
    return JsonResponse(d)