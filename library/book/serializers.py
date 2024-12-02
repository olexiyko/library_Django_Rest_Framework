from rest_framework import serializers # type: ignore
from .models import Book
from author.serializers import AuthorSerializator
from author.models import Author


class BookSerializator(serializers.ModelSerializer):
    authors = AuthorSerializator(many=True, read_only=True) 
    author_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    ) 
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'count', 'authors', 'author_ids']

    def create(self, validated_data):
        author_ids = validated_data.pop('author_ids', [])
        book = Book.objects.create(**validated_data)

        if author_ids:
            existing_authors = Author.objects.filter(id__in=author_ids)
            existing_author_ids = existing_authors.values_list('id', flat=True)

            new_author_ids = set(author_ids) - set(existing_author_ids)
            for author_id in new_author_ids:
                Author.objects.create(id=author_id, name="Default Name", surname="Default Surname")

            authors = Author.objects.filter(id__in=author_ids)
            book.authors.set(authors)

        return book
