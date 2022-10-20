from http.client import HTTPResponse
from django.shortcuts import render
import datetime
from django.http import HttpResponse

def home(request):
    isActive=True
    if request.method=='POST':
          check=request.POST.get("check")
          print(check)
          if check is None: isActive=False
          else: isActive=True


    date=datetime.datetime.now()
    
    name="UTKARSH RAJ"
    list_of_programs=[
        'WAP to cheak even or odd',
        'WAP to cheak prime numers',
        'WAP to print all prime numers from 1 to 100',
        'WAP to print pascals triangle '
    ]
    student={
        'student_name':"Rahul",
        'student_college':"ZYZ",
        'student_city':'Patna'
    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student

    }
    #return HttpResponse("<h1>Hello this is index page</h1>")
    return render(request,"home.html",data)

def about(request):
    #return HttpResponse("<h1>This is about page</h1>")
    return render(request,"about.html",{})

def services(request):
    return render(request,"services.html",{})
    #return HttpResponse("<h1>This is services page</h1>")

def contact(request):
    return render(request,"contact.html",{})
    #return HttpResponse("<h1>This is contact page</h1>")
