# Generated by Django 2.2 on 2020-03-22 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_add_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes'),
        ),
    ]
