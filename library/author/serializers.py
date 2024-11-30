from rest_framework import serializers
from .models import Author
from book.models import Book

class AuthorSerializator(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['name','surname']