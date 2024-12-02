from django.db import models
import book.models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50,blank=True)
    surname=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return f"{self.surname} {self.name}"
