from rest_framework import serializers # type: ignore
from .models import Book
from author.serializers import AuthorSerializator
from author.models import Author


class BookSerializator(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(),required=False)
    class Meta:
        model=Book
        fields=['title','description','count','author']

    # title = serializers.CharField(max_length=128, required=False)
    # description = serializers.CharField(max_length=128, required=False)
    # count = serializers.IntegerField(default=10, required=False)
    # author = serializers.PrimaryKeyRelatedField(
    #     queryset=Author.objects.all(),
    #     required=False
    # )    
