from django.shortcuts import render
from user.models import Complaint
# Create your views here.
def home(request):
    return render(request,'home.html')
def dashbord(request):
    complaintdata=Complaint.objects.all()
    context={'complaintdata':complaintdata}
    return render(request,'dashbord.html',context)
    

