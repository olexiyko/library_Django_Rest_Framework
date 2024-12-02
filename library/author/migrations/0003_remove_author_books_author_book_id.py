# Generated by Django 4.1 on 2024-12-02 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
        migrations.AddField(
            model_name='author',
            name='book_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]