# Generated by Django 3.1.3 on 2020-11-22 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20201105_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='OS_UploadAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.CharField(max_length=30)),
                ('file', models.FileField(upload_to='student/uploadAssignment')),
                ('Student_name', models.CharField(max_length=30)),
            ],
        ),
    ]