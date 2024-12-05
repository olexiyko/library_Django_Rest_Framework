from django.db import models
from book.models import Book
from author.models import Author

# Create your models here.

class Order(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(Author,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(null=True, blank=True)
    quantity=models.IntegerField(default=1)