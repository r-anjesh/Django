from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import EmployeeForm
from .models import employee


def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form':form})

def employee_list(request):
    employees = employee.objects.all()
    return render(request, 'employee_list.html', {'employees' : employees})

def home(request):
    template = loader.get_template('testapp.html')
    res = template.render()
    return HttpResponse(res)

def greetings(request):
    s = "<h1>Welcome Backend bro Let's have some fun..!<h1>"
    return HttpResponse(s)
# Create your views here.

def contact(request):
    text = "Anjesh Kumar"
    context = {
        'text':text
    }
    template = loader.get_template('contact.html')
    res = template.render(context, request)
    return HttpResponse(res)


