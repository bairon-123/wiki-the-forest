# Generated by Django 5.2 on 2025-04-21 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0012_animal_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='numero',
            field=models.IntegerField(),
        ),
    ]
