from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) :
    return render(request, 'dashboardpages/index.html')
# Create your views here.

def TableauPageView(request) :
    return render(request, 'dashboardpages/tableau.html')