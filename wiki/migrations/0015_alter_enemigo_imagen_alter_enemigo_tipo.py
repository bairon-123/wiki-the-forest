# Generated by Django 5.2 on 2025-04-22 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0014_enemigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enemigo',
            name='imagen',
            field=models.ImageField(default='wiki/imagenes/default.png', upload_to='enemigos/'),
        ),
        migrations.AlterField(
            model_name='enemigo',
            name='tipo',
            field=models.CharField(max_length=100),
        ),
    ]
