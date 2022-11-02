from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Job, Payment, Employee
def indexPageView(request) :
    ee = Employee.objects.all()
    job = Job.objects.all()
    # spec = Specialty.objects.all()
    context ={
        "ee": ee,
        "job": job,
        # "spec": spec
    }
    return render(request, 'dashboardpages/index.html', context)
# Create your views here.
