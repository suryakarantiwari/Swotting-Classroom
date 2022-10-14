from django.shortcuts import render
from . models import Admins
from student . models import Student
from teacher . models import Teacher
from django.http import HttpResponse


param={}
def index(request):
    username = request.POST.get("exampleInputEmail1")
    password = request.POST.get("exampleInputPassword1")
    name = Admins.objects.filter(username=username, password=password)
    if len(name) == 0:
        return render(request, 'wronginput.html')
    else:
        param['student']=Student.objects.all()
        param['teacher']=Teacher.objects.all()
        # print(param['student'][5].delete())
        param['hod']=name[0]
        param['admins']=Admins.objects.all()
        return render(request,'HOD/Hod_home.html',param)

def aboutus(request):
    return render(request,"AboutUs.html")


def contactus(request):
    return render(request,"contactus.html")

def register_admin(request):
    name = request.POST.get("formGroupExampleInput1")
    phone = request.POST.get("formGroupExampleInput2")
    email = request.POST.get("colFormLabel")
    address = request.POST.get("exampleFormControlTextarea1")
    username = request.POST.get("formGroupExampleInput3")
    password = request.POST.get("inputPassword1")
    confirm_password = request.POST.get("inputPassword2")
    file = request.POST.get("exampleFormControlFile1")
    s = Admins(full_name=name,phone=phone,email=email,address=address,username=username,
               password=password,confirm_passward=confirm_password,photo=file)
    s.save()
    return render(request,'HOD/Hod_home.html',param)

def register_teacher(request):
    name = request.POST.get("formGroupExampleInput1")
    phone = request.POST.get("formGroupExampleInput2")
    email = request.POST.get("colFormLabel")
    address = request.POST.get("exampleFormControlTextarea1")
    subject = request.POST.get("formGroupExampleInput")
    username = request.POST.get("formGroupExampleInput3")
    password = request.POST.get("inputPassword1")
    confirm_password = request.POST.get("inputPassword2")
    file = request.POST.get("exampleFormControlFile1")
    s = Teacher(full_name=name,phone=phone,email=email,address=address,subject=subject, username=username,
                password=password,confirm_passward=confirm_password,photo=file)
    s.save()
    # param['teacher'] = Teacher.objects.all()
    # param['admins'] = Admins.objects.all()
    return render(request, 'HOD/Hod_home.html', param)

def register_student(request):
    name = request.POST.get("formGroupExampleInput1")
    email = request.POST.get("colFormLabel")
    phone = request.POST.get("formGroupExampleInput2")
    parent_no = request.POST.get("formGroupExampleInput3")
    address = request.POST.get("exampleFormControlTextarea1")
    username = request.POST.get("formGroupExampleInput4")
    password = request.POST.get("inputPassword1")
    confirm_password = request.POST.get("inputPassword2")
    year = request.POST.get("formGroupExampleInput5")
    section = request.POST.get("formGroupExampleInput6")
    semester = request.POST.get("formGroupExampleInput7")
    subject1 = request.POST.get("formGroupExampleInput8")
    subject2 = request.POST.get("formGroupExampleInput9")
    subject3 = request.POST.get("formGroupExampleInput10")
    subject4 = request.POST.get("formGroupExampleInput11")
    subject5 = request.POST.get("formGroupExampleInput12")
    file = request.POST.get("exampleFormControlFile1")
    s = Student(full_name=name,email=email,phone_no=phone,parent_phone_no=parent_no,address=address,username=username,
                password=password,confirm_password=confirm_password,year=year,section=section,semester=semester,
                subject1=subject1,subject2=subject2,subject3=subject3,subject4=subject4,subject5=subject5,photo=file)
    s.save()
    # param['student'] = Student.objects.all()
    # param['admins'] = Admins.objects.all()
    return render(request, 'HOD/Hod_home.html', param)

def change_password(request):
    current_password = request.POST.get("Password")
    password = request.POST.get("Password1")
    confirm_password = request.POST.get("Password2")
    original_password = request.POST.get("original_password")
    username = request.POST.get("username")
    if current_password == original_password:
        if password == confirm_password:
            temp = Admins.objects.get(password=original_password,username=username)
            temp.password = password
            temp.confirm_passward = password
            temp.save()
            return render(request,'HOD/Success_message.html',param)
        else:
            return render(request, 'HOD/unmatch_confirm.html', param)

    else:
        return render(request, 'HOD/unmatch_current.html', param)
