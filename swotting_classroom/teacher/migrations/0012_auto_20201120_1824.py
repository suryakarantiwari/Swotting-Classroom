# Generated by Django 3.1.3 on 2020-11-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0011_auto_20201119_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='os_assignment',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
