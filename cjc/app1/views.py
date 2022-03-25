from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm


# Create your views here.


def uploadView(request):
    template_name = "app1/upload.html"
    form = EmployeeForm()
    context = {"form":form}

    if request.method=="POST":
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()


    return render(request,template_name,context)


def showView(request):
    template_name = "app1/show.html"
    obj = Employee.objects.all()
    context = {"data":obj}

    return render(request,template_name,context)
