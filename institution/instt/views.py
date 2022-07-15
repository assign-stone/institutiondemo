from django import http
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
class Employee:
    def __init__(self,id,name,salary,phone,age):
        self.id=id
        self.name=name
        self.salary=salary
        self.phone=phone
        self.age=age
def openfactorialform(request): #to show form page
    return render(request,"form.html")
def calculatefactorial(request):
    num=int(request.GET['number'])
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return render(request,"form.html",{"result":fact})
def employeesdata(request):
    list=[
    Employee(1,"Avinash",80000,"5248637892",30),
    Employee(2,"Raj",14000,"2547896351",44),
    Employee(3,"Yash",100000,"3589652475",24),
    Employee(4,"Paridhi",20000,"5624395682",25),
    Employee(5,"Tapam",230000,"5684268924",35)
    ]
    return render(request,"employeedata.html",{"employee":list})
    