from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home", views.index, name="StudentHome"),
    path("aboutus", views.aboutus, name="Aboutus"),
    path("contactus", views.contactus, name="Contactus"),
    path("change_password", views.change_password, name="change_password"),
    path("assignment_view",views.assignment_view,name="Assignment_view"),
    path("UploadAssignment",views.UploadAssignment,name="UploadAssignment"),
    path("os_Assignment",views.os_Assignment,name="OS_Assignment"),
    path("OS_Quiz",views.OS_Quiz,name="OS_Quiz"),
    path("OS_SubjectInfo",views.OS_SubjectInfo,name="OS_subjectinfo"),
    path("project_SubjectInfo",views.project_SubjectInfo,name="project_SubjectInfo"),
    path("project_Assignment",views.project_Assignment,name="project_Assignment"),
    path("project_Quiz",views.project_Quiz,name="project_Quiz"),
    path("java_SubjectInfo",views.java_SubjectInfo,name="java_SubjectInfo"),
    path("java_Assignment",views.java_Assignment,name="java_Assignment"),
    path("java_Quiz",views.java_Quiz,name="java_Quiz"),
    path("OOAD_SubjectInfo",views.OOAD_SubjectInfo,name="OOAD_SubjectInfo"),
    path("OOAD_Assignment",views.OOAD_Assignment,name="OOAD_Assignment"),
    path("OOAD_Quiz",views.OOAD_Quiz,name="OOAD_Quiz"),
    path("CN_SubjectInfo",views.CN_SubjectInfo,name="CN_SubjectInfo"),
    path("CN_Assignment",views.CN_Assignment,name="CN_Assignment"),
    path("CN_Quiz",views.CN_Quiz,name="CN_Quiz"),
]
