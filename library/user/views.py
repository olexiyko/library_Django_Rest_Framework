from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser
from rest_framework.response import Response
from .serializers import UserSerializator
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.
class UserAPIView(APIView):
    def get(self, request, id=None):
        if id:
            # user=get_object_or_404(CustomUser,pk=id)
            user = CustomUser.objects.filter(pk=id, is_active=True).first()
            if user:
                serialized_user = UserSerializator(user)
                return Response(serialized_user.data, status=status.HTTP_200_OK)
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        else:
            users = CustomUser.objects.filter(is_active=True).all()
            if users:
                serialized_users = UserSerializator(users, many=True)
                return Response(serialized_users.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "Users not found"}, status=status.HTTP_404_NOT_FOUND
                )

    def post(self, request):
        serializer = UserSerializator(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data["password"])
            user.save()
            response_serializer = UserSerializator(user)
            return Response(response_serializer.data, status=status.status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id:
            user = get_object_or_404(CustomUser, pk=id)
            if user:
                user.is_active = False
                user.save()
                return Response(
                    {"success": "User was successfuly deleted"},
                    status=status.HTTP_204_NO_CONTENT,
                )
            return Response(
                {"error": "Users not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {"error": "id is required to delete user"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, id=None):
        if id:
            user = get_object_or_404(CustomUser, pk=id)
            if user:
                serializer = UserSerializator(user, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    user.save()
                    return Response(
                        {"success": "User updated successfuly"}, status=status.HTTP_200_OK
                    )
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
