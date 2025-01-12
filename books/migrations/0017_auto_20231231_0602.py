# Generated by Django 3.2.19 on 2023-12-31 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20231230_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(max_length=1024, verbose_name='Сеціўная спасылка'),
        ),
        migrations.AlterField(
            model_name='narration',
            name='duration',
            field=models.DurationField(blank=True, null=True, verbose_name='Працягласць'),
        ),
    ]
