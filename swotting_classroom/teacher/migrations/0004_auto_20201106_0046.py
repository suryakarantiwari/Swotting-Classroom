# Generated by Django 3.1.3 on 2020-11-05 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_auto_20201105_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_name', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=300)),
                ('file', models.FileField(upload_to='')),
                ('date', models.DateField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Assignment',
            new_name='OS_Assignment',
        ),
    ]