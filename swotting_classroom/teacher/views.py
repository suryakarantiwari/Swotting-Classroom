from django.shortcuts import render
from .models import Teacher
from .models import OS_Assignment
from .models import Project_Assignment
from .models import Java_Assignment
from .models import Ooad_Assignment
from .models import Cn_Assignment
from student . models import Student
from student . models import Os_UploadAssignment
from student . models import Project_UploadAssignment
from student . models import Java_UploadAssignment
from student . models import OOAD_UploadAssignment
from student . models import CN_UploadAssignment
from django.http import HttpResponse

param = {}
assingment_info = {}
def index(request):
    username = request.POST.get("exampleInputEmail1")
    password = request.POST.get("exampleInputPassword1")
    name = Teacher.objects.filter(username=username, password=password)
    student = Student.objects.all()
    if len(name) == 0:
        return render(request, 'wronginput.html')
    else:
        teacher = name[0]
        subject = student[0]
        param['teacher'] = teacher
        param['sub'] = subject
        if param['teacher'].subject == param['sub'].subject1:
            data = OS_Assignment.objects.all()
        elif param['teacher'].subject == param['sub'].subject2:
            data = Project_Assignment.objects.all()
        elif param['teacher'].subject == param['sub'].subject3:
            data = Java_Assignment.objects.all()
        elif param['teacher'].subject == param['sub'].subject4:
            data = Ooad_Assignment.objects.all()
        elif param['teacher'].subject == param['sub'].subject5:
            data = Cn_Assignment.objects.all()
        param['data'] = data
        return render(request, 'teacher/teacher_home.html', param)

def delete(request):
    name = request.POST.get("topic")
    if param['teacher'].subject == param['sub'].subject1:
        temp = OS_Assignment.objects.filter(assignment_name=name)
        data = OS_Assignment.objects.all()
        temp.delete()
    elif param['teacher'].subject == param['sub'].subject2:
        temp = Project_Assignment.objects.filter(assignment_name=name)
        data = Project_Assignment.objects.all()
        temp.delete()
    elif param['teacher'].subject == param['sub'].subject3:
        temp = Java_Assignment.objects.filter(assignment_name=name)
        data = Java_Assignment.objects.all()
        temp.delete()
    elif param['teacher'].subject == param['sub'].subject4:
        temp = Ooad_Assignment.objects.filter(assignment_name=name)
        data = Ooad_Assignment.objects.all()
        temp.delete()
    elif param['teacher'].subject == param['sub'].subject5:
        temp = Cn_Assignment.objects.filter(assignment_name=name)
        data = Cn_Assignment.objects.all()
        temp.delete()
    param['data'] = data
    return render(request,"teacher/teacher_home.html",param)

def edit(request):
    name = request.POST.get("AssignmentName")
    question = request.POST.get("question")
    file = request.FILES["AssignmentFile"]
    date = request.POST.get("Lastdate")
    if param['teacher'].subject == param['sub'].subject1:
        temp = OS_Assignment.objects.get(assignment_name=name)
        data = OS_Assignment.objects.all()
    elif param['teacher'].subject == param['sub'].subject2:
        temp = Project_Assignment.objects.get(assignment_name=name)
        data = Project_Assignment.objects.all()
    elif param['teacher'].subject == param['sub'].subject3:
        temp = Java_Assignment.objects.get(assignment_name=name)
        data = Java_Assignment.objects.all()
    elif param['teacher'].subject == param['sub'].subject4:
        temp = Ooad_Assignment.objects.get(assignment_name=name)
        data = Ooad_Assignment.objects.all()
    elif param['teacher'].subject == param['sub'].subject5:
        temp = Cn_Assignment.objects.get(assignment_name=name)
        data = Cn_Assignment.objects.all()
        temp.delete()
    temp.question = question
    temp.date = date
    temp.file = file
    temp.save()
    param['data'] = data
    return render(request,'teacher/teacher_home.html',param)

def aboutus(request):
    return render(request,"AboutUs.html")

def contactus(request):
    return render(request,"contactus.html")

def change_password(request):
    current_password = request.POST.get("password")
    password = request.POST.get("password1")
    confirm_password = request.POST.get("password2")
    original_password = request.POST.get("original_password")
    username = request.POST.get("username")
    if current_password == original_password:
        if password == confirm_password:
            temp = Teacher.objects.get(password=original_password,username=username)
            temp.password = password
            temp.confirm_passward = password
            temp.save()
            return render(request,'teacher/Success_message.html',param)
        else:
            return render(request, 'teacher/unmatch_confirm.html', param)
    else:
        return render(request, 'teacher/unmatch_current.html', param)

def assignment(request):
    name = request.POST.get("AssignmentName")
    question = request.POST.get("question")
    file = request.FILES['AssignmentFile']
    date = request.POST.get("Lastdate")
    if param['teacher'].subject == param['sub'].subject1:
        s = OS_Assignment(assignment_name=name,question=question,file=file,date=date)
        data = OS_Assignment.objects.all()
        s.save()
    elif param['teacher'].subject == param['sub'].subject2:
        s = Project_Assignment(assignment_name=name, question=question, file=file, date=date)
        data = Project_Assignment.objects.all()
        s.save()
    elif param['teacher'].subject == param['sub'].subject3:
        s = Java_Assignment(assignment_name=name, question=question, file=file, date=date)
        data = Java_Assignment.objects.all()
        s.save()
    elif param['teacher'].subject == param['sub'].subject4:
        s = Ooad_Assignment(assignment_name=name, question=question, file=file, date=date)
        data = Ooad_Assignment.objects.all()
        s.save()
    elif param['teacher'].subject == param['sub'].subject5:
        s = Cn_Assignment(assignment_name=name, question=question, file=file, date=date)
        data = Cn_Assignment.objects.all()
        s.save()
    temp = param['teacher']
    assignment_table={'data':data ,'teacher': temp}
    return render(request,"teacher/teacher_home.html",assignment_table)

def assignment_view(request):
    name = request.POST.get("assignment_name")
    count = len(param['data'])
    for i in range(count):
        if str(param['data'][i]) == str(name) :
            question = param['data'][i].question
            date = param['data'][i].date
            break
    file = request.POST.get("file")
    teacher_name = param['teacher'].full_name
    subject = param['teacher'].subject
    mail = param['teacher'].email
    assingment_info ={'name' : name , 'question' : question , 'file' : file , 'date' : date , 'teacher' : teacher_name , 'subject' : subject , 'mail' : mail}

    if param['teacher'].subject == param['sub'].subject1:
        data = Os_UploadAssignment.objects.all()
    elif param['teacher'].subject == param['sub'].subject2:
        data = Project_UploadAssignment.objects.all()
    elif param['teacher'].subject == param['sub'].subject3:
        data = Java_UploadAssignment.objects.all()
    elif param['teacher'].subject == param['sub'].subject4:
        data = OOAD_UploadAssignment.objects.all()
    elif param['teacher'].subject == param['sub'].subject5:
        data = CN_UploadAssignment.objects.all()
    assingment_info['data']=data
    if len(data) > 0:
        assingment_info['stu_file']=data[0].file
    return render(request,'teacher/Assignment_view.html',assingment_info)
