from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from .serializers import UserSerializator
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
class UserAPIView(APIView):
    def get(self,request,id=None):
        if id:
            # user=get_object_or_404(User,pk=id)
            user=User.objects.filter(pk=id).first()
            if user:
                serialized_user=UserSerializator(user)
                return Response(serialized_user.data,status=status.HTTP_200_OK)
            return Response({"error": "User not found"},status=status.HTTP_404_NOT_FOUND)          
        else:
            users=User.objects.filter().all()
            if users:
                serialized_users=UserSerializator(users,many=True)
                return Response(serialized_users.data,status=status.HTTP_200_OK)
            else: 
                return Response({"error": "Users not found"},status=status.HTTP_404_NOT_FOUND) 
            