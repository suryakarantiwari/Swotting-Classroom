from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'AboutUs.html')

def contactus(request):
    return render(request,'contactus.html')