# Generated by Django 3.2.19 on 2023-07-20 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_linktype_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='livelib_url',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='LiveLib URL'),
        ),
    ]