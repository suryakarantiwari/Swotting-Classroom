# Generated by Django 3.1.3 on 2020-11-22 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0012_auto_20201120_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cn_assignment',
            name='file',
            field=models.FileField(upload_to='teacher/Assignment_file'),
        ),
        migrations.AlterField(
            model_name='java_assignment',
            name='file',
            field=models.FileField(upload_to='teacher/Assignment_file'),
        ),
        migrations.AlterField(
            model_name='ooad_assignment',
            name='file',
            field=models.FileField(upload_to='teacher/Assignment_file'),
        ),
        migrations.AlterField(
            model_name='os_assignment',
            name='file',
            field=models.FileField(upload_to='teacher/Assignment_file'),
        ),
        migrations.AlterField(
            model_name='project_assignment',
            name='file',
            field=models.FileField(upload_to='teacher/Assignment_file'),
        ),
    ]
