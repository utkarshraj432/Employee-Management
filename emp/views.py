from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp

# Create your views here.
def emp_home(request):

    emps=Emp.objects.all()
    
    return render(request,"emp/home.html",{'emps':emps})

def add_emp(request):
    if request.method=="POST":
        name=request.POST.get("name")
        emp_id=request.POST.get("emp_id")
        phone=request.POST.get("phone")
        department=request.POST.get("department")
        address=request.POST.get("address")
        working=request.POST.get("working")
        #validation


        #create model object and set the data 0
        e=Emp()
        e.name=name
        e.emp_id=emp_id
        e.phone=phone
        e.address=address
        e.department=department
        if working is None:
            e.working=False
        else:
            e.working=True


        e.save()



        print("Data is coming")
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/") 

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })

def do_update_emp(request,emp_id):
    if request.method=='POST':
        name=request.POST.get("name")
        emp_id_temp=request.POST.get("emp_id")
        phone=request.POST.get("phone")
        department=request.POST.get("department")
        address=request.POST.get("address")
        working=request.POST.get("working")

        e=Emp.objects.get(pk=emp_id)
        
        e.name=name
        e.emp_id=emp_id_temp
        e.phone=phone
        e.address=address
        e.department=department
        if working is None:
            e.working=False
        else:
            e.working=True

        e.save()
    return redirect("/emp/home")