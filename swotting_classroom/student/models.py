from django.db import models

# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=10)
    parent_phone_no = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    year = models.CharField(max_length=10,default="")
    section = models.CharField(max_length=10,default="")
    semester = models.CharField(max_length=10,default="")
    subject1 = models.CharField(max_length=50)
    subject2 = models.CharField(max_length=50)
    subject3 = models.CharField(max_length=50)
    subject4 = models.CharField(max_length=50)
    subject5 = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="student/images", default="")


    def __str__(self):
        return self.full_name

class Os_UploadAssignment(models.Model):
    assignment = models.CharField(max_length=30)
    file = models.FileField(upload_to="student/uploadAssignment",default="")
    Student_name = models.CharField(max_length=30)

    def __str__(self):
        return self.assignment


class CN_UploadAssignment(models.Model):
    assignment = models.CharField(max_length=30)
    file = models.FileField(upload_to="student/uploadAssignment",default="")
    Student_name = models.CharField(max_length=30)

    def __str__(self):
        return self.assignment


class Project_UploadAssignment(models.Model):
    assignment = models.CharField(max_length=30)
    file = models.FileField(upload_to="student/uploadAssignment",default="")
    Student_name = models.CharField(max_length=30)

    def __str__(self):
        return self.assignment


class Java_UploadAssignment(models.Model):
    assignment = models.CharField(max_length=30)
    file = models.FileField(upload_to="student/uploadAssignment",default="")
    Student_name = models.CharField(max_length=30)

    def __str__(self):
        return self.assignment


class OOAD_UploadAssignment(models.Model):
    assignment = models.CharField(max_length=30)
    file = models.FileField(upload_to="student/uploadAssignment",default="")
    Student_name = models.CharField(max_length=30)

    def __str__(self):
        return self.assignment



