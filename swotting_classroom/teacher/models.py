from django.db import models

class Teacher(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    subject = models.CharField(max_length=30)
    username = models.CharField(max_length=20 , primary_key=True)
    password = models.CharField(max_length=20)
    confirm_passward = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="teacher/images", default="")


    def __str__(self):
        return self.full_name

class OS_Assignment(models.Model):
    assignment_name = models.CharField(max_length=50)
    question = models.CharField(max_length=300)
    file = models.FileField(upload_to="teacher/Assignment_file")
    date = models.DateField()

    def __str__(self):
        return self.assignment_name

class Project_Assignment(models.Model):
    assignment_name = models.CharField(max_length=50)
    question = models.CharField(max_length=300)
    file = models.FileField(upload_to="teacher/Assignment_file")
    date = models.DateField()

    def __str__(self):
        return self.assignment_name

class Java_Assignment(models.Model):
    assignment_name = models.CharField(max_length=50)
    question = models.CharField(max_length=300)
    file = models.FileField(upload_to="teacher/Assignment_file")
    date = models.DateField()

    def __str__(self):
        return self.assignment_name

class Ooad_Assignment(models.Model):
    assignment_name = models.CharField(max_length=50)
    question = models.CharField(max_length=300)
    file = models.FileField(upload_to="teacher/Assignment_file")
    date = models.DateField()

    def __str__(self):
        return self.assignment_name

class Cn_Assignment(models.Model):
    assignment_name = models.CharField(max_length=50)
    question = models.CharField(max_length=300)
    file = models.FileField(upload_to="teacher/Assignment_file")
    date = models.DateField()

    def __str__(self):
        return self.assignment_name