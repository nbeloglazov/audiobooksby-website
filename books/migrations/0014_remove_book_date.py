# Generated by Django 3.2.19 on 2023-11-16 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_remove_book_translators'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date',
        ),
    ]
