from django.db import models

# class HOD(models.Model):
#     full_name = models.CharField(max_length=50,null=False)
#     phone = models.CharField(max_length=10)
#     email = models.EmailField(max_length=50)
#     address = models.CharField(max_length=50)
#     username = models.CharField(max_length=20,primary_key=True)
#     password = models.CharField(max_length=20)
#     confirm_passward = models.CharField(max_length=20)
#     photo = models.ImageField(upload_to="hod/images", default="")
#
#
#     def __str__(self):
#         return self.full_name

class Admins(models.Model):
    full_name = models.CharField(max_length=50,null=False)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    confirm_passward = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="hod/images", default="")


    def __str__(self):
        return self.full_name