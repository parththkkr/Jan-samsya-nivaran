from django.shortcuts import render,redirect
from .models import Complaint
from registration.models import Registration
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your views here.
def userhome(request):
    emailid=request.session['emailid']
    username=request.session['username']
    context={'emailid':emailid,'username':username}
    return render(request,'userhome.html',context)
def complaint(request):
    context={'action':'saveComplaint'}
    return render(request,'complaint.html',context)
def saveComplaint(request):
    
    if request.method == "POST":
        problem= request.POST.get('problem','')
        description=request.POST.get('desc','')
        image=request.FILES['image']
        #ig = FileSystemStorage()
        address=request.POST.get('address','')
        zip=request.POST.get('zip','')
        ward = request.POST.get('ward','')
        username=request.session['username']
        Complaints=Complaint(problem=problem,description=description,address=address,zip=zip,image=image,ward=ward,username=username)
        Complaints.save()    
        return redirect('/user/userhome')

def mydashbord(request):
    username=request.session['username']
    complaintdata=Complaint.objects.filter(username=username)
    context={'complaintdata':complaintdata}
    return render(request,'mydashbord.html',context)
        
def updatecomplaint(request,complaint_id):
    username=request.session['username']
    Complaints=Complaint.objects.get(complaint_id=complaint_id,username=username)
    request.session['complaint_id']=Complaints.complaint_id
    context={'problem':Complaints.problem,'desc':Complaints.description,'image':Complaints.image,'address':Complaints.address,'ward':Complaints.ward,'zip':Complaints.zip,'action':'/user/updateapplied'}
    return render(request,'complaint.html',context)

def updateapplied(request):
    if request.method=="POST":
        complaint_id=request.session['complaint_id']
        problem= request.POST.get('problem','')
        description=request.POST.get('desc','')
        image=request.FILES['image']
        #ig = FileSystemStorage()
        address=request.POST.get('address','')
        zip=request.POST.get('zip','')
        ward = request.POST.get('ward','')
        username=request.session['username']
        Complaints=Complaint.objects.filter(complaint_id=complaint_id).update(problem=problem,description=description,address=address,zip=zip,ward=ward)
        ComplaintImg=Complaint.objects.get(complaint_id=complaint_id)
        ComplaintImg.image=image
        ComplaintImg.save()    
        return render(request,'userhome.html')

def deletecomplaint(request,complaint_id):
    username=request.session['username']
    Complaint.objects.get(complaint_id=complaint_id,username=username).delete()
    return redirect('/user/userhome')

def myaccount(request):
    username=request.session['username']
    Registrations=Registration.objects.get(username=username)
    context={'firstname':Registrations.firstname,'lastname':Registrations.lastname,'emailid':Registrations.emailid,'city':Registrations.city,'zip':Registrations.zipcode,'state':Registrations.state,'username':Registrations.username,'displayusername':'none'}
    return render(request,'myaccount.html',context)

def updateaccount(request):
    
    username=request.session['username']
    Registrations=Registration.objects.get(username=username)
    username=Registrations.username
    emailid=Registrations.emailid
    if request.method == "POST":  

        updateusername=request.POST.get('username','')
        updatefirstname=request.POST.get('firstname','')
        updatelastname=request.POST.get('lastname','')
        updatecity=request.POST.get('city','')
        updatestate=request.POST.get('state','')
        updatezipcode=request.POST.get('zip','')
        if(updateusername==username):

            
            Registrations.firstname=updatefirstname
            Registrations.lastname=updatelastname
            Registrations.username= updateusername
            Registrations.city= updatecity
            Registrations.state= updatestate
            Registrations.zipcode= updatezipcode
            Registrations.save()
            
            
            
        elif(updateusername!=username):

            try:
                Registrations=Registration.objects.get(username=updateusername)
                context={'firstname':Registrations.firstname,'lastname':Registrations.lastname,'emailid':Registrations.emailid,'city':Registrations.city,'zip':Registrations.zipcode,'state':Registrations.state,'username':Registrations.username,'displayusername':''}
                return render(request,'myaccount.html',context)
            except:
         
                Registrations.firstname=updatefirstname
                Registrations.lastname=updatelastname
                Registrations.username= updateusername
                Registrations.city= updatecity
                Registrations.state= updatestate
                Registrations.zipcode= updatezipcode
                Registrations.save()
                if(Complaint.objects.filter(username=username).update(username=updateusername)):
                    pass
                else:
                    pass
                
                
                request.session['username']=updateusername
                context={'firstname':Registrations.firstname,'lastname':Registrations.lastname,'emailid':Registrations.emailid,'city':Registrations.city,'zip':Registrations.zipcode,'state':Registrations.state,'username':Registrations.username,'displayusername':'none'}
                return render(request,'myaccount.html',context)
    
            
                
                

    context={'firstname':Registrations.firstname,'lastname':Registrations.lastname,'emailid':Registrations.emailid,'city':Registrations.city,'zip':Registrations.zipcode,'state':Registrations.state,'username':Registrations.username,'displayusername':'none',}
    return render(request,'myaccount.html',context)

                   
def logout(request):
    del request.session['username']
    del request.session['emailid']
    return redirect('/home')

def help(request):
    return render(request,'help.html')