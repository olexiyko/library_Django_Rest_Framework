# Generated by Django 4.1 on 2024-12-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0004_remove_author_book_id'),
        ('book', '0002_remove_book_author_book_author_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_id',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='author.author'),
        ),
    ]
