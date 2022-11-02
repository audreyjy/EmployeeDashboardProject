from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Job, Payment, Employee
def indexPageView(request) :
    job = Job.objects.all()
    context ={
        "job": job,
    }
    return render(request, 'dashboardpages/index.html', context)
# Create your views here.

def TableauPageView(request) :
    return render(request, 'dashboardpages/tableau.html')