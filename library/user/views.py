from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from .serializers import UserSerializator
from rest_framework import status

# Create your views here.
class UserAPIView(APIView):
    def get(self,request):
        users=User.objects.filter().all()
        if users:
            serialized_users=UserSerializator(users,many=True)
            return Response(serialized_users.data,status=status.HTTP_200_OK)
        else: 
            return Response({"error": "User not found"},status=status.HTTP_404_NOT_FOUND) 
        