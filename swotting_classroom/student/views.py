from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
from teacher . models import OS_Assignment
from teacher . models import Project_Assignment
from teacher . models import Java_Assignment
from teacher . models import Ooad_Assignment
from teacher . models import Cn_Assignment
from . models import Os_UploadAssignment
from . models import Project_UploadAssignment
from . models import Java_UploadAssignment
from . models import OOAD_UploadAssignment
from . models import CN_UploadAssignment

param = {}
assignment_info = {}
def index(request):
    username = request.POST.get("exampleInputEmail1")
    password = request.POST.get("exampleInputPassword1")
    name = Student.objects.filter(username=username,password=password)
    if len(name) == 0:
        return render(request,'wronginput.html')
    else:
        student = name[0]
        param['student'] = student
        return render(request,'student/student_home.html',param)

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
            temp = Student.objects.get(password=original_password,username=username)
            temp.password = password
            temp.confirm_passward = password
            temp.save()
            return render(request,'student/Success_message.html',param)
        else:
            return render(request, 'student/unmatch_confirm.html', param)
    else:
        return render(request, 'student/unmatch_current.html', param)

def OS_SubjectInfo(request):
    return render(request,"student/OS_subjectinfo.html",param)

def os_Assignment(request):
    data = OS_Assignment.objects.all()
    param['data'] = data
    return render(request,"student/OS_Assignment.html",param)

def OS_Quiz(request):
    return render(request,"student/OS_Quiz.html",param)

def project_SubjectInfo(request):
    return render(request,"student/project_SubjectInfo.html",param)

def project_Assignment(request):
    data = Project_Assignment.objects.all()
    param['data'] = data
    return render(request,"student/project_Assignment.html",param)

def project_Quiz(request):
    return render(request,"student/project_Quiz.html",param)

def java_SubjectInfo(request):
    return render(request,"student/java_SubjectInfo.html",param)

def java_Assignment(request):
    data = Java_Assignment.objects.all()
    param['data'] = data
    return render(request,"student/java_Assignment.html",param)

def java_Quiz(request):
    return render(request,"student/java_Quiz.html",param)

def OOAD_SubjectInfo(request):
    return render(request,"student/OOAD_SubjectInfo.html",param)

def OOAD_Assignment(request):
    data = Ooad_Assignment.objects.all()
    param['data'] = data
    return render(request,"student/OOAD_Assignment.html",param)

def OOAD_Quiz(request):
    return render(request,"student/OOAD_Quiz.html",param)

def CN_SubjectInfo(request):
    return render(request,"student/CN_SubjectInfo.html",param)

def CN_Assignment(request):
    data = Cn_Assignment.objects.all()
    param['data'] = data
    return render(request,"student/CN_Assignment.html",param)

def CN_Quiz(request):
    return render(request,"student/CN_Quiz.html",param)


def assignment_view(request):
    name = request.POST.get("assignment_name")
    file = request.POST.get("file")
    subject = request.POST.get("subject")
    count = len(param['data'])
    for i in range(count):
        if str(param['data'][i]) == str(name):
            question = param['data'][i].question
            date = param['data'][i].date
            break
    # assignment_info ={'name' : name , 'question' : question , 'file' : file , 'date' : date , 'subject' : subject}
    assignment_info['name']=name
    assignment_info['question']=question
    assignment_info['file']=file
    assignment_info['date']=date
    assignment_info['subject']=subject
    return render(request,'student/Assignment_view.html',assignment_info)

def UploadAssignment(request):
    file = request.FILES["AssignmentFile"]
    name = request.POST.get("name")
    subject = request.POST.get("subject")
    # print(subject)
    student_name = param['student']
    if subject == "OPERATING":
        temp = Os_UploadAssignment(assignment=name,file=file,Student_name=student_name)
        data = Os_UploadAssignment.objects.all()
        temp.save()
        # return HttpResponse("done")
    elif subject == "MINOR":
        temp = Project_UploadAssignment(assignment=name, file=file, Student_name=student_name)
        data = Project_UploadAssignment.objects.all()
        temp.save()
    elif subject == "JAVA":
        temp = Java_UploadAssignment(assignment=name,file=file,Student_name=student_name)
        data = Java_UploadAssignment.objects.all()
        temp.save()
    elif subject == "OOAD":
        temp = OOAD_UploadAssignment(assignment=name,file=file,Student_name=student_name)
        data = OOAD_UploadAssignment.objects.all()
        temp.save()
    elif subject == "COMPUTER":
        temp = CN_UploadAssignment(assignment=name,file=file,Student_name=student_name)
        data = CN_UploadAssignment.objects.all()
        temp.save()
    print(assignment_info)
    print(param)
    assignment_info['Uploaded']=file
    # assignment_info['data'] = data
    return render(request,'student/Assignment_view.html',assignment_info)
