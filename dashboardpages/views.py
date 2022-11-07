from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Job, Payment, Employee
def indexPageView(request) :
    job = Job.objects.all()

    context ={
        "job": job, 
    }

    return render(request, 'dashboardpages/index.html', context)


#view to display filtered request based on semester, year, and position 
def filterPageView(request) :
    eSemester = request.GET['semester_test']
    eYear = request.GET['year_test']
    ePosition = request.GET['position_type_test']

    #if all inputs are filled in
    if ((eSemester != "") & (eYear != "") & (ePosition != "")): 
        print("print first one")
        print(ePosition)
        data = (Job.objects.filter(semester=eSemester) & Job.objects.filter(year=eYear) & Job.objects.filter(position_type=ePosition))
    
    #if semester and year filled in 
    elif ((eSemester != "") & (eYear != "") & (ePosition == "")):
        print("print second one")
        data = (Job.objects.filter(semester=eSemester) & Job.objects.filter(year=eYear))
    
    #if semester and position_type filled in 
    elif ((eSemester != "") and (eYear == "") and (ePosition != "")):
        data = (Job.objects.filter(semester=eSemester) & Job.objects.filter(position_type=ePosition))

    #if year and position_type filled in 
    elif ((eSemester == "") and (eYear != "") and (ePosition != "")):
        data = (Job.objects.filter(year=eYear) & Job.objects.filter(position_type=ePosition))

    #if semester filled in
    elif ((eSemester != "") and (eYear == "") and (ePosition == "")):
        data = (Job.objects.filter(semester=eSemester))

    #if year filled in
    elif ((eSemester == "") and (eYear != "") and (ePosition == "")):
        data = (Job.objects.filter(year=eYear))

    #if position type filled in 
    elif ((eSemester == "") and (eYear == "") and (ePosition != "")):
        data = (Job.objects.filter(position_type=ePosition))

    else:
        data = (Job.objects.filter(semester=eSemester) & Job.objects.filter(year=eYear) & Job.objects.filter(position_type=ePosition))

    if data.count() > 0:
        context = {
            "job" : data
        }
        return render(request, 'dashboardpages/filteredEmployees.html', context)
    else:
        return HttpResponse("Not found")


def TableauPageView(request) :
    return render(request, 'dashboardpages/tableau.html')