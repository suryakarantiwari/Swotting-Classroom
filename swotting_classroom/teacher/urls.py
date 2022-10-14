from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name="TeacherHome"),
    path("aboutus", views.aboutus, name="Aboutus"),
    path("contactus", views.contactus, name="Contactus"),
    path("delete",views.delete,name="delete"),
    path("edit",views.edit,name="Edit"),
    path("assignment",views.assignment,name="Assignment"),
    path("change_password", views.change_password, name="change_password"),
    path("assignment_view", views.assignment_view, name="assignment_view"),
    # path("contactus", views.contactus, name="Contactus"),
]