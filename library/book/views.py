from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from rest_framework.response import Response
from .serializers import BookSerializator
from rest_framework import status
from django.shortcuts import get_object_or_404
from author.models import Author


# Create your views here.


class BookApiView(APIView):
    def get(self, request, id=None):
        if id:
            # book = Book.objects.filter(pk=id).all()
            book = get_object_or_404(Book, pk=id)
            if book:
                book_serializer = BookSerializator(book)
                return Response(book_serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND
            )
        else:
            books = Book.objects.all()
            if books:
                books_serializer = BookSerializator(books, many=True)
                return Response(books_serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"error": "Books not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        serializer = BookSerializator(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": "Book created succesfully"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id:
            # book = Book.objects.filter(pk=id).first()
            book = get_object_or_404(Book, pk=id)
            if book:
                book.delete()
                return Response(
                    {"succes": "Book deleted successfuly"}, status=status.HTTP_200_OK
                )
            return Response(
                {"error": "Books not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {"error": "id is required to delete book"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, id=None):
        if id:
            # book=Book.objects.filter(pk=id).first()
            book = get_object_or_404(Book, pk=id)
            if book:
                serializer = BookSerializator(book, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(
                {"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {"error": "id is required to update book"},
            status=status.HTTP_400_BAD_REQUEST,
        )
