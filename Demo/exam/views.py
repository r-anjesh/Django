from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def about(request):

    a = "Anjesh"
    b = "Vanya"

    context = {
        "a":a,
        "b":b
    }
    template = loader.get_template('exam.html')

    res = template.render(context,request)
    return HttpResponse(res)
# Create your views here.
