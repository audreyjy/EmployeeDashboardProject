"""EmployeeDashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dashboardpages.views import TableauPageView
from dashboardpages.views import filterPageView
from dashboardpages.views import NotificationsPageView

urlpatterns = [
    path("", include("dashboardpages.urls")), 
    path('admin/', admin.site.urls),
    path("tableau/", TableauPageView, name="tableau"),
    path("filteredEmps/", filterPageView, name="filteredEmps"),
    path("notifications/", NotificationsPageView, name="notifications"),
]
