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

def addPageViewGet(request):
    
    context ={
        'job' : Job.objects.all(),
        'emp' : Employee.objects.all(),
        'course' : Course.objects.all()
    }
    return render(request, 'dashboardpages/edit.html', context)


def AddPageViewPost(request) :

    if request.method == 'POST':
        new_job = Job()
        employee = Employee.objects.get(pk=request.POST.get('emp'))
        new_pay = Payment()
        course = Course.objects.get(course_code=request.POST.get('classcode'))
        print(request.POST.keys(), request.POST.get('grad'))
        new_job.employee = employee
        new_job.course = course
        new_pay.payrate = request.POST.get('payrate')
        new_pay.last_increase_date = request.POST.get('lastraise') if request.POST.get('lastraise') else None
        new_pay.save()

        new_job.payment = Payment.objects.get(pk=new_pay.id)

        new_job.semester = request.POST.get('semester')
        new_job.year = request.POST.get('year')
        new_job.position_type = request.POST.get('position')
        new_job.year_in_program = request.POST.get('program')
        new_job.pay_grad_tuition = request.POST.get('grad')
        new_job.hire_date = request.POST.get('hiredate')
        new_job.name_change_complete = request.POST.get('namechange')
        new_job.qualtrics = request.POST.get('qual')
        new_job.submitted = request.POST.get('submitted')
        new_job.submitted_date = request.POST.get('submitdate') if request.POST.get('submitdate') else None
        new_job.authorized = request.POST.get('auth')
        new_job.authorization_to_work_email_sent_date = request.POST.get('authdate') if request.POST.get('authdate') else None
        new_job.terminated = request.POST.get('terminated')
        new_job.termination_date = request.POST.get('termdate') if request.POST.get('termdate') else None
        new_job.notes = request.POST.get('note')
        new_job.expected_hours_per_week = request.POST.get('hours')
        new_job.payment.last_increase_date = request.POST.get('lastraise') if request.POST.get('lastraise') else None

        new_job.save()

        data = Job.objects.all
        context = {
            'job': data
        }

    return render(request, 'dashboardpages/index.html', context)

def EditPageView(request, j_id):
    job = Job.objects.get(pk=j_id)
    job.hire_date = job.hire_date.strftime('%Y-%m-%d') if job.hire_date else None
    job.authorization_to_work_email_sent_date = job.authorization_to_work_email_sent_date.strftime('%Y-%m-%d') if job.authorization_to_work_email_sent_date else None
    job.submitted_date = job.submitted_date.strftime('%Y-%m-%d') if job.submitted_date else None
    job.payment.last_increase_date = job.payment.last_increase_date.strftime('%Y-%m-%d') if job.payment.last_increase_date else None
    job.termination_date = job.termination_date.strftime('%Y-%m-%d') if job.termination_date else None
    print(type(job.payment.last_increase_date))
    context ={
        'job' : Job.objects.all(),
        'emp' : Employee.objects.all(),
        'course' : Course.objects.all(),
        'one' : job
    }

    return render(request, 'dashboardpages/edit.html', context)

def EditPageViewPost(request, j_id):
    old_job = Job.objects.get(pk=j_id)

    old_job.employee = Employee.objects.get(pk=request.POST.get("emp"))

    old_job.course = Course.objects.get(pk=request.POST.get("classcode"))

    old_job.payment.payrate = request.POST.get('payrate')
    old_job.payment.last_increase_date = request.POST.get('lastraise') if request.POST.get('lastraise') else None

    old_job.year = request.POST.get('year')
    old_job.semester = request.POST.get('semester')
    old_job.position_type = request.POST.get('position')
    old_job.year_in_program = request.POST.get('program')
    old_job.pay_grad_tuition = request.POST.get('grad')
    old_job.hire_date = request.POST.get('hiredate')
    old_job.name_change_complete = request.POST.get('namechange')
    old_job.qualtrics = request.POST.get('qual')
    old_job.submitted = request.POST.get('submitted')
    old_job.submitted_date = request.POST.get('submitdate') if request.POST.get('submitdate') else None
    old_job.authorized = request.POST.get('auth')
    old_job.authorization_to_work_email_sent_date = request.POST.get('authdate') if request.POST.get('authdate') else None
    old_job.terminated = request.POST.get('terminated')
    old_job.termination_date = request.POST.get('termdate') if request.POST.get('termdate') else None
    old_job.notes = request.POST.get('note')
    old_job.expected_hours_per_week = request.POST.get('hours')

    old_job.payment.save()
    old_job.save()


    data = Job.objects.all
    context = {
        'job': data
    }

    return render(request, 'dashboardpages/index.html', context)

def DelPageView(request, j_id):
    try:
        job = Job.objects.get(pk=j_id)
        pay = Payment.objects.get(pk=job.payment.id)

        job.delete()
        pay.delete()
    except:
        pass
    
    data = Job.objects.all
    context = {
        'job': data
    }
    return render(request, 'dashboardpages/index.html', context)

# Create your views here.


def TableauPageView(request) :
    return render(request, 'dashboardpages/tableau.html')

def NotificationsPageView(request) :
    job = Job.objects.all()
    context ={
        "job": job,
    }
    return render(request, 'dashboardpages/notifications.html', context)