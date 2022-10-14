from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name="HODHome"),
    path("aboutus", views.aboutus, name="Aboutus"),
    path("contactus", views.contactus, name="Contactus"),
    path("register_admin",views.register_admin,name="register_admin"),
    path("register_teacher",views.register_teacher,name="register_teacher"),
    path("register_student",views.register_student,name="register_student"),
    path("change_password",views.change_password,name="change_password"),
]