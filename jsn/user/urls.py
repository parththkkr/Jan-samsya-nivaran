"""jsn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from . import views
urlpatterns = [
   
    
    path('userhome',views.userhome),
    path('complaint',views.complaint),
    path('saveComplaint',views.saveComplaint),
    path('mydashbord',views.mydashbord),
    path('updatecomplaint/<int:complaint_id>',views.updatecomplaint),
    path('deletecomplaint/<int:complaint_id>',views.deletecomplaint),
    path('updateapplied',views.updateapplied),
    path('myaccount',views.myaccount),
    path('logout',views.logout),
    path('updateaccount',views.updateaccount),
    path('help',views.help)
   
    
]
