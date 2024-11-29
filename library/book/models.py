from django.db import models
import author.models

# Create your models here.
class Book(models.Model):
    title=models.CharField(blank=True, max_length=128)
    description=models.TextField(blank=True, max_length=128)
    count=models.IntegerField(default=10)
    author = models.ForeignKey('author.Author', on_delete=models.CASCADE)
