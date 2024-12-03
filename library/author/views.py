from django.shortcuts import render
from rest_framework import status
from .serializers import *
from rest_framework.views import APIView
from .models import Author
from .serializers import AuthorSerializator
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


# Create your views here.
class AuthorApiView(APIView):
    def get(self, request, id=None):
        if id:
            author = get_object_or_404(Author, pk=id)
            if author:
                serializer = AuthorSerializator(author)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND
            )
        else:
            authors = Author.objects.all()
            if authors:
                serializer = AuthorSerializator(authors, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"error": "Authors not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        serializer = AuthorSerializator(data=request.data)
        if serializer.is_valid():
            author = serializer.save()
            deserializer = AuthorSerializator(author)
            return Response(
                {"new_author": deserializer.data, "status": "success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        if id:
            author = Author.objects.filter(pk=id).first()
            if author:
                serializer = AuthorSerializator(author, data=request.data)
                if serializer.is_valid():
                    updated_author = serializer.save()
                    deserializer = AuthorSerializator(updated_author)
                    return Response(
                        {
                            "updated_author": deserializer.data,
                            "data_to_update": serializer.validated_data,
                            "status": "success",
                        }
                    )
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(
                {"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {"error": "Id is required to update author"},
            status=status.HTTP_400_BAD_REQUEST,
        )
